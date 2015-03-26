from collections import defaultdict

from HtmlDoc import HtmlDoc
from HtmlXpath import HtmlXpath, HtmlXpathSet
from HtmlAttributes import HtmlAttributes
from common import normalizeStr, unique, pretty, flatten, extractInt



class HtmlModel:
    """Generates a model to extract the desired information in a webpage
    """

    def __init__(self, docs, attributes=True, debug=False):
        """
        'docs' are the HTML webpages to model
        'attributes' are whether to replace the xpath indices with attributes
        'debug' is whether to print internal information of the model generation
        """
        self._docs = docs
        self._attributes = attributes
        self._debug = debug
    #___________________________________________________________________________

    def train(self):
        """Train the model using the known output for the given urls
        """
        # rate xpaths by the similarity of their content with the output
        model = HtmlXpathSet()
        i = 0
        while i < len(self._docs[0].outputs()):
            isGroup = False
            xpaths = []
            if self._debug:
                print self._docs[0].outputs()[i]
            for doc in self._docs:
                if i < len(doc.outputs()):
                    outputs = doc.outputs()[i]
                    if isinstance(outputs, list):
                        isGroup = True
                    else:
                        outputs = [outputs]
                    for output in outputs:
                        outputScores = defaultdict(int)
                        for xpath, score in doc.matchXpaths(normalizeStr(output)):
                            outputScores[xpath] += score

                        # select best xpath match for each output
                        bestScore = min([score for (xpath, score) in outputScores.items()])
                        if bestScore > 0: 
                            print "Warning: could not find '%s' (score=%d)" % (output, score)
                        xpaths.extend([xpath for (xpath, score) in outputScores.items() if score == bestScore])
                        if self._debug:
                            print pretty([(self._docs.index(doc), xpath, score) for (xpath, score) in outputScores.items() if score == bestScore])
            if xpaths:
                if isGroup:
                    model.append(self.abstractXpaths(xpaths))
                else:
                    model.append(tuple(self.rankXpaths(xpaths)))
                if self._debug:
                    print 'Best:\n%s\n' % model[-1]
            i += 1

        if self._attributes:
            self.addAttributes(model)
        return model
    #___________________________________________________________________________

    def addAttributes(self, model):
        """Replace xpath indices with attributes where possible
        """
        A = HtmlAttributes(self._docs)
        for record in model:
            for xpath in record:
                A.addAttribs(xpath, A.uniqueAttribs(xpath)) # XXX adds?
    #___________________________________________________________________________

    def abstractXpaths(self, xpaths):
        """Find a single xpath to represent this group of xpaths by replacing similar xpaths with a regular expression

        >>> doc = HtmlDoc('../testdata/yahoo_search/1.html', [])
        >>> xpathsGroup = [\
            [HtmlXpath('/html[1]/body[1]/table[1]/tr[1]/td[1]'), HtmlXpath('/html[1]/body[1]/table[1]/tr[1]')],\
            [HtmlXpath('/html[1]/body[1]/table[1]/tr[2]/td[1]'), HtmlXpath('/html[1]/body[1]/table[1]/tr[2]')],\
            [HtmlXpath('/html[1]/body[1]/table[1]/tr[3]'),],\
            [HtmlXpath('/html[1]/body[1]/a[1]')],\
        ]
        >>> [xpath.get() for xpath in HtmlModel([doc]).refineXpaths(xpathsGroup)]
        ['/html[1]/body[1]/a[1]', '/html[1]/body[1]/table[1]/tr']
        """
        popularity = defaultdict(list)
        for xpath1 in xpaths:
            for xpath2 in xpaths:
                if len(xpath1) == len(xpath2) and xpath1 != xpath2:
                    diff = xpath1.diff(xpath2)
                    abstractXpath = HtmlXpath([str(xpath1)])
                    indices = []
                    for partition in diff:
                        tag = xpath1.tags()[partition]
                        if tag != xpath2.tags()[partition]:
                            # have different tags so can't abstract
                            indices = []
                            break
                        abstractXpath[partition] = tag
                        indices.append(extractInt(xpath1[partition]))
                    popularity[(abstractXpath, diff)].append(indices)
                    #if self._debug:
                    #    print 'Abstracted: %s' % abstractXpath

        # find the most popular regular expression
        abstractXpath, diff = sorted([(len(v), k) for (k, v) in popularity.items()])[-1][1]
        # restrict xpath regular expressions to lowest index encountered
        minIndices = [min(indices) for indices in zip(*popularity[(abstractXpath, diff)])]
        for partition, minIndex in zip(diff, minIndices):
            #minIndex = min([indices[i] for indices in popularity[(abstractXpath, diff)]])
            #minIndex = min(indices)
            if minIndex > 1:
                abstractXpath[partition] += '[position()>%d]' % (minIndex - 1)
        # test abstraction
        """print 'Test abstraction: ' + str(abstractXpath)
        tmp = [str(xpath) for xpath in xpaths]
        print tmp
        total = count = 0
        for doc in self._docs:
            es = []
            for xpath in xpaths:
                es.extend(doc.tree().xpath(str(xpath)))
            for e in doc.tree().xpath(str(abstractXpath)):
                print e.getroottree().getpath(e), e in es
                total += 1
                if e in es: count += 1
        print '%d/%d\n' % (count, total)"""
        return abstractXpath
    #___________________________________________________________________________

    def rankXpaths(self, xpaths):
        """Xpaths are ranked by most common, length, then alphabetical"""
        def cmp(xpath1, xpath2):
            if xpaths.count(xpath1) != xpaths.count(xpath2):
                return xpaths.count(xpath2) - xpaths.count(xpath1)
            if len(str(xpath1)) != len(str(xpath2)):
                return len(str(xpath2)) - len(str(xpath1))
            else:
                return -1 if str(xpath1) < str(xpath2) else 1
        return unique(sorted(xpaths, cmp=cmp))#[0]
