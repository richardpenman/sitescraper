# Common functions used by multiple classes

import re
import string


#_______________________________________________________________________________

def unique(items):
    """Return unique elements of list

    >>> unique([1, 2, 3, 2, 2, 4])
    [1, 2, 3, 4]
    """
    found = set()
    keep = []
    for item in items:
        if item not in found:
            found.add(item)
            keep.append(item)
    return keep
#_______________________________________________________________________________

def flatten(l):
    """Expand all sublists into a single list

    >>> flatten([1, [2, 3, 4], 5])
    [1, 2, 3, 4, 5]
    """
    if isinstance(l,list):
        return sum(map(flatten, l),[])
    else:
        return [l]
#_______________________________________________________________________________

def extractInt(s):
    """Extract integer from string

    >>> extractInt('hello 99!')
    99
    """
    return int('0' + ''.join(c for c in s if c in string.digits))
#_______________________________________________________________________________

def normalizeStr(s):
    """Remove characters that make string comparison difficult from copied text"""
    #s = s.decode('utf-8')
    return re.sub('\s+', ' ', re.sub('[\n\r\t]', '', s)).strip()
#_______________________________________________________________________________

def pretty(var, depth=0):
    """
    >>> pretty([1, 2, 3])
    '1\\n2\\n3'
    >>> pretty({'a': 1, 'b': 2, 'c': 3})
    'a: 1\\nc: 3\\nb: 2'
    """
    if type(var) == type([]):
        return '\n'.join(depth*' ' + pretty(item, depth+1) for item in var)
    elif type(var) == type(()):
        return ', '.join(pretty(item, depth+1) for item in var)
    elif type(var) == type({}):
        return '\n'.join(depth*' ' + '%s: %s' % (pretty(k, depth+1), pretty(v, depth+1)) for (k, v) in var.items())
    else:
        return str(var)
#_______________________________________________________________________________
