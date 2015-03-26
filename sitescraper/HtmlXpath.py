import re
from collections import defaultdict


        
class HtmlXpath(object):
    """Encapsulate an xpath

    >>> x = HtmlXpath('/html/body/a[1]')
    >>> x[2]
    'a[1]'
    >>> x[2] = 'p[1]'
    >>> x.get()
    '/html/body/p[1]'
    >>> list(x)
    ['html', 'body', 'p[1]']
    """
    COLLAPSE_MODE, ABSTRACT_MODE = 0, 1
    sepRE = re.compile('/+')
    #___________________________________________________________________________

    def __init__(self, xpath):
        self.set(xpath)
    #___________________________________________________________________________

    def __len__(self):
        return len(self.sections())
    #___________________________________________________________________________

    def __getitem__(self, i):
        return self.sections()[i]
    #___________________________________________________________________________

    def __setitem__(self, i, v):
        xpathStr = str(self)
        starts, ends = [], []
        for j, match in enumerate(HtmlXpath.sepRE.finditer(xpathStr)):
            starts.append(match.end())
            if match.start() > 0:
                ends.append(match.start())
            if j > i: 
                break
        ends.append(len(xpathStr))
        self._xpathStr = xpathStr[:starts[i]] + v + xpathStr[ends[i]:]
        return self
    #___________________________________________________________________________

    def __iter__(self):
        return self.sections().__iter__()
    #___________________________________________________________________________

    def __str__(self):
        return self._xpathStr
    #___________________________________________________________________________

    def __cmp__(self, other):
        return cmp(str(self), str(other))
    #___________________________________________________________________________

    def __hash__(self):
        return hash(str(self.get()))
    #___________________________________________________________________________

    def copy(self):
        return HtmlXpath(self.get())
    #___________________________________________________________________________

    def get(self): 
        return str(self) if self._mode == HtmlXpath.COLLAPSE_MODE else [str(self)]
    #___________________________________________________________________________

    def set(self, xpath): 
        if isinstance(xpath, str):
            self._mode = HtmlXpath.COLLAPSE_MODE
            self._xpathStr = xpath
        elif isinstance(xpath, list):
            self._mode = HtmlXpath.ABSTRACT_MODE
            self._xpathStr = xpath[0]
        elif isinstance(xpath, HtmlXpath):
            self.set(xpath.get())
        else:
            raise Exception("Invalid type for HtmlXpath '%s'" % type(xpath))
    #___________________________________________________________________________

    """def mode(self):
        return self._mode"""
    def isabstract(self):
        return self._mode == HtmlXpath.ABSTRACT_MODE
    #___________________________________________________________________________
    
    def iscollapse(self):
        return self._mode == HtmlXpath.COLLAPSE_MODE
    #___________________________________________________________________________


    def sections(self):
        """Return sections of xpath

        >>> HtmlXpath('/a/b/c').sections()
        ['a', 'b', 'c']
        >>> HtmlXpath('/a[1]/b').sections()
        ['a[1]', 'b']
        """
        return HtmlXpath.sepRE.split(str(self))[1:]
    #___________________________________________________________________________

    def tags(self):
        """Return list of tags in xpath
        
        >>> HtmlXpath('/a/b[1]/c').tags()
        ['a', 'b', 'c']
        """
        removeIndex = lambda s: '[' in s and s[:s.index('[')] or s
        return [removeIndex(s) for s in self.sections()]
    #___________________________________________________________________________

    def walk(self):
        """Return list of sub xpaths

        >>> HtmlXpath('/a/b/c').walk()
        ['/a', '/a/b', '/a/b/c']
        >>> HtmlXpath('/a[1]/b').walk()
        ['/a[1]', '/a[1]/b']
        """
        xpaths = []
        for match in HtmlXpath.sepRE.finditer(str(self)):
            end = match.start()
            if end > 0:
                xpaths.append(str(self)[:end])
        xpaths.append(str(self))
        return xpaths
    #___________________________________________________________________________

    def normalize(self):
        """A normalized xpath has an index defined at each node. ElementTree treats indexless nodes as a regular expression.
        
        >>> HtmlXpath("/a[1]/b/c[@id='2']/d").normalize().get()
        "/a[1]/b[1]/c[@id='2']/d[1]"
        """
        for i, section in enumerate(self):
            if section != '*' and not section.endswith(']'):
                self[i] = section + '[1]'
        return self
    #___________________________________________________________________________

    def isNormalized(self):
        """
        >>> HtmlXpath('/a[1]/b[2]').isNormalized()
        True
        >>> HtmlXpath('/a[1]/b').isNormalized()
        False
        """
        return self.copy().normalize() == self
    #___________________________________________________________________________

    def diff(self, other):
        """Returns indices where xpaths differ.

        >>> HtmlXpath('/a/c/c').diff(HtmlXpath('/a/b/c'))
        [1]
        >>> HtmlXpath('/a/b/c').diff(HtmlXpath('/a/b/c/d/e'))
        [3, 4]
        """
        indices = []
        if self != other:
            for i in range(max(len(self), len(other))):
                if i >= len(self) or i >= len(other) or self[i] != other[i]:
                    indices.append(i)
        return tuple(indices)




class HtmlXpathSet(list):
    """Encapsulate a set of xpaths for the model
    
    [(xpath1, xpath2, ...),
     ([abstract1], [abstract2], ...)]
    """
    def __init__(self, model=[]):
        list.__init__(self)
        if model:
            for record in model:
                self.append(record)
    
    def __str__(self):
        return str([tuple([xpath.get() for xpath in record]) for record in self])
    
    def append(self, record):
        """Expects single xpath or tuple
        """
        if not isinstance(record, tuple):
            record = (record,)
        list.append(self, tuple([HtmlXpath(xpath) for xpath in record]))