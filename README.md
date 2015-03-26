# Overview #
SiteScraper extracts the data you want from webpages. No programming or HTML knowledge is required. 

For an in depth analysis of how it works have a browse of [this unpublished paper](http://sitescraper.googlecode.com/files/sitescraper.pdf).

## Example ##
Here is a simple example to show how SiteScraper works:


```
#!python

>>> from sitescraper import sitescraper
>>> ss = sitescraper()
>>> url = 'http://www.amazon.com/s/ref=nb_ss_gw?url=search-alias%3Daps&field-keywords=python&x=0&y=0'
>>> data = ["Amazon.com: python", ["Learning Python, 3rd Edition", 
     "Programming in Python 3: A Complete Introduction to the Python Language (Developer's Library)", 
     "Python in a Nutshell, Second Edition (In a Nutshell (O'Reilly))"]]
>>> ss.add(url, data)
>>> # we can add multiple example cases, but this is a simple example so 1 will do (I generally use 3)
>>> # ss.add(url2, data2) 
>>> ss.scrape('http://www.amazon.com/s/ref=nb_ss_gw?url=search-alias%3Daps&field-keywords=linux&x=0&y=0')
["Amazon.com: linux", ["A Practical Guide to Linux(R) Commands, Editors, and Shell Programming", 
"Linux Pocket Guide", 
"Linux in a Nutshell (In a Nutshell (O'Reilly))", 
'Practical Guide to Ubuntu Linux (Versions 8.10 and 8.04), A (2nd Edition)', 
'Linux Bible, 2008 Edition: Boot up to Ubuntu, Fedora, KNOPPIX, Debian, openSUSE, and 11 Other Distributions']]

```

## Explanation ##
As you may have figured out, this example extracts the book titles from an Amazon search. All SiteScraper requires is the titles from one example search and then it can build a model to extract the titles from future Amazon searches.

(To run this example first update the titles to what Amazon now returns and for more robust results provide a number of example cases.) 


## Model format ##
Internally SiteScraper models the data in a webpage using [Xpaths](http://www.w3.org/TR/xpath). 
Here is an example Xpath:


```
#!css

/html[1]/body[1]/div[position()>1]/ul[@class='big']/li

```

This Xpath will match all list elements within an unordered list of class 'big' within the second and following divs (index starts from 0) within the body of the HTML document.


# Install #

SiteScraper is written in pure [Python](http://www.python.org/) but depends on version 2 of [lxml](http://codespeak.net/lxml/) (for the HTML module). 
Currently many Linux repositories provide the old version 1, which means you may need to [build from source](http://codespeak.net/lxml/build.html). For example Ubuntu up to version 8.04 used version 1 but 8.10 onwards uses version 2.
This dependency is a pain but it is a [very](http://blog.ianbicking.org/2008/12/10/lxml-an-underappreciated-web-scraping-library/) [useful](http://blog.ianbicking.org/2008/03/30/python-html-parser-performance/) library. 

A zip file is available for download but this is usually out of date. Better to checkout the [SVN repository](http://code.google.com/p/sitescraper/source/checkout).


# Future goals #
Some goals for the future:

* Remove lxml dependency so that SiteScraper is pure Python and can work on Google App Engine. This would be possible by replacing lxml with a pure Python parser like [html5lib](http://code.google.com/p/html5lib/). Alternatively I could integrate work from [this project](http://code.google.com/p/webscraping/source/browse/xpath.py), which uses XPath on unstructured HTML without the need for a parser.
* Instead of absolute XPath's from the root of the document generate relative XPath's around a tag with an ID (eg: //div[@id="abc"]../table/tr/td). Such XPaths are more stable.
* Better handling of unicode characters. Currently SiteScraper skips any characters it can't decode.
* Refactor the XPath module, which is somewhat messy now.
* Firebug always includes _tbody_ in the XPath whether the tag exists in the HTML or not. Allow this.


# Regression tests #

Included with SiteScraper are a set of [test cases](http://en.wikipedia.org/wiki/Regression_testing regression) ([in testdata/](http://code.google.com/p/sitescraper/source/browse/#svn/trunk/testdata)) that successfully extract data from stock sites, news sites, weather sites, web forums, and search engines. 

Each regression test has:
* a few example webpages from a website
* the desired data from each webpage
* and a list of the xpaths that will locate the desired data
See [here](http://code.google.com/p/sitescraper/source/browse/trunk/testdata/amazon/__init__.py) for an example.
The script [test.py](http://code.google.com/p/sitescraper/source/browse/trunk/test.py) runs the regression tests and reports which tests fail.

# License #

SiteScraper is licensed under the [LGPL license](http://www.gnu.org/licenses/lgpl.html), which means you are free to use it in any project (including commercial) but must publish modifications you make to SiteScraper.

# Contact #

You can ask questions or tell me how you have used SiteScraper by emailing me at richard@[webscraping.com](http://webscraping.com).
I am particularly interested to hear from you if you have a webpage that fails and ideas how to improve SiteScraper to scrape it correctly.