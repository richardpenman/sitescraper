from HtmlModel import HtmlModel
from HtmlDoc import HtmlDoc
from HtmlXpath import HtmlXpath, HtmlXpathSet



class sitescraper:
    """This class is the interface to SiteScraper.
    
    It maintains the state of the model and training data, which it passes through to the backend classes."""
    #___________________________________________________________________________

    def __init__(self, model=None, debug=False):
        self.clear()
        self._model = HtmlXpathSet(model)
        self._debug = debug
    #___________________________________________________________________________

    def __len__(self):
        return len(self._examples)
    #___________________________________________________________________________

    def clear(self):
        self._docs = []
        self._previousInput = None
        self._previousDoc = None
        self._examples = []
        self._model = HtmlXpathSet()
    #___________________________________________________________________________
    
    def model(self): 
        if self._examples:
            self.train() # new examples to train
        return self._model
    #___________________________________________________________________________
    
    def add(self, input, outputs):
        """Add this training data"""
        self._examples.append((input, outputs))
    #___________________________________________________________________________

    def scrape(self, input, html=False):
        """Scrape data from this input using model from current training data
        The html flag determines whether to extract the raw HTML instead of parsed text"""
        if not self.model():
            raise SiteScraperError('Error: can not scrape because model is not trained')

        if self._previousInput == input:
            doc = self._previousDoc    
        else:
            self._previousDoc = doc = HtmlDoc(input, outputs=[], xpaths=[])            
            self._previousInput = input
        if doc.tree().getroot() is None:
            raise SiteScraperError('Error: %s has no root node' % input)

        outputFn = doc.getElementHTML if html else doc.getElementText
        results = []
        for record in self._model:
            for xpath in record:
                # XXX restrict grouping to xpath class...somehow
                #print type(xpath), str(xpath)
                result = [(e if isinstance(e, str) else outputFn(e)) for e in doc.tree().xpath(str(xpath))]
                if xpath.iscollapse():
                    if result:
                        result = ' '.join(result).strip()
                    else:
                        result = None # distinguish empty match from no match
                if result:
                    break
            results.append(result)
        return results
    #___________________________________________________________________________

    def train(self):
        """Train model from given examples"""
        for input, outputs in self._examples:
            self._docs.append(HtmlDoc(input, outputs=outputs))
        self._examples = []
        # train the model
        self._model = HtmlModel(self._docs, attributes=True, debug=self._debug).train()
    #___________________________________________________________________________



class SiteScraperError(Exception):
    pass
