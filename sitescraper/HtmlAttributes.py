import re
from collections import defaultdict
from common import flatten



class HtmlAttributes:
    """Extract attributes from XML tree and store them reverse indexed by attribute

    >>> from HtmlDoc import HtmlDoc
    >>> from HtmlXpath import HtmlXpath
    >>> d1 = HtmlDoc('../testdata/yahoo_search/1.html', [])
    >>> d2 = HtmlDoc('../testdata/yahoo_search/2.html', [])
    >>> d3 = HtmlDoc('../testdata/yahoo_search/3.html', [])
    >>> a = HtmlAttributes([d1, d2, d2])
    >>> xpath = '/html/body/div/div[2]/div[2]/div[2]/div/div[3]/ol/li/div/div[2]'
    >>> e1 = d1.tree().xpath(xpath)[0]
    >>> a.extractAttribs(e1)
    [('class', 'abstr')]
    >>> attribs = a.uniqueAttribs(HtmlXpath(xpath))
    >>> attribs
    [[('lang', 'en')], [('id', 'ysch')], [('id', 'doc')], [('id', 'bd')], [('id', 'results')], [('id', 'left')], [('id', 'main')], [('id', 'web')], [('start', '1')], [], [('class', 'res')], [('class', 'abstr')]]
    >>> a.addAttribs(HtmlXpath(xpath), attribs).get()
    "/html[@lang='en']/body[@id='ysch']/div[@id='doc']/div[@id='bd']/div[@id='results']/div[@id='left']/div[@id='main']/div[@id='web']/ol[@start='1']/li/div[@class='res']/div[@class='abstr']"

    >> tree = lxmlHtml.fromstring("<html><body node='0'><c class='1' node='1'>C<d class='2'></d></c><c class='1' node='2'>D</c></body</html>").getroottree()
    >> a = HtmlAttributes(tree)
    >> extractXpaths(tree)
    {'C': ['/html[1]/body[1]/c[1]'], 'D': ['/html[1]/body[1]/c[2]']}
    >> a.extractAttribs(['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    {('node', '0'): ['/html[1]/body[1]'], ('node', '2'): ['/html[1]/body[1]/c[2]'], ('node', '1'): ['/html[1]/body[1]/c[1]'], ('class', '1'): ['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]']}
    >> attribs = a.commonAttribs(['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    >> attribs
    [('/html[1]/body[1]', ('node', '0')), ('/html[1]/body[1]/c[2]', ('class', '1'))]
    >> a.addCommonAttribs(attribs, ['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    ["/html[1]/body[1][@node='0']/c[1][@class='1']", "/html[1]/body[1][@node='0']/c[2][@class='1']"]
    """
    #___________________________________________________________________________

    def __init__(self, docs):
        self._docs = docs
    #___________________________________________________________________________

    def docs(self):
        return self._docs
    #___________________________________________________________________________

    def uniqueAttribs(self, xpath):
        """Return a list of attributes that uniquely distinguish the element at each segment"""
        acceptedAttribs = []
        # select examples which contain the relevant xpath
        docs = [doc for doc in self.docs() if doc.tree().xpath(str(xpath))]
        for i, section in enumerate(xpath.walk()):
            sectionElements = flatten([doc.tree().xpath(section) for doc in docs])
            try:
                siblingElements = flatten([[s for s in e.itersiblings() if s.tag == e.tag] for e in sectionElements])
            except AttributeError:
                pass
            else:
                siblingAttribs = flatten([self.extractAttribs(e) for e in siblingElements])
                proposedAttribs = self.commonAttribs(sectionElements)
                acceptedAttribs.append([a for a in proposedAttribs if a not in siblingAttribs])
        return acceptedAttribs
    #___________________________________________________________________________

    def extractAttribs(self, element):
        """Return a list of attributes for the element"""
        attribs = []
        #print element.attrib.items()
        for attrName, attrValue in element.attrib.items():
            # punctuation such as '/' and ':' can confuse xpath, so ignore attributes with these characters
            if not self.anyIn('/: ', attrValue + attrName): # why space XXX
                attribs.append((attrName, attrValue.replace(',', '"')))
        return attribs
    #___________________________________________________________________________

    def commonAttribs(self, elements):
        """Return a list of common attributes among a group of elements"""
        common = defaultdict(int)
        for e in elements:
            for attrib in self.extractAttribs(e):
                common[attrib] += 1
        return [attrib for (attrib, count) in common.items() if count == len(elements)]
    #___________________________________________________________________________

    def addAttribs(self, xpath, allAttribs):
        """Add attributes to xpath"""
        sections = []
        for i, (section, attribs) in enumerate(zip(xpath, allAttribs)):
            if attribs:
                section = re.sub('\[\d+\]', '', section)
            for attrib in attribs:
                if isinstance(attrib, int):
                    section += '[%d]' % attrib
                else:
                    section += "[@%s='%s']" % attrib
            xpath[i] = section
        return xpath
    #___________________________________________________________________________

    def removeAttribs(self, xpath):
        """
        >>> from HtmlXpath import HtmlXpath
        >>> HtmlAttributes([]).removeAttribs(HtmlXpath("/a[1]/b[@class='abc']/c")).get()
        '/a[1]/b/c'
        """
        attribRE = re.compile('\[@.*?\]')
        for i, section in enumerate(xpath):
            xpath[i] = re.sub(attribRE, '', xpath[i])
        return xpath
    #___________________________________________________________________________

    def anyIn(self, l1, l2):
        """Return values in l1 that exist in l2

        >>> HtmlAttributes([]).anyIn([1,2], [2,3])
        2
        >>> HtmlAttributes([]).anyIn([1,2], [3])
        
        """
        for v1 in l1:
            if v1 in l2:
                return v1
        return None
    #___________________________________________________________________________

    def allIn(self, l1, l2):
        """Return true if all of first list is in second list

        >>> HtmlAttributes([]).allIn([1,2], [2,3])
        False
        >>> HtmlAttributes([]).allIn([1,2], [1,2])
        True
        """
        for v1 in l1:
            if v1 not in l2:
                return False
        return True
    #___________________________________________________________________________
