# the available test cases
__all__ = [
    #'amazon',
    #'asx', 
    #'bbc_news',
    #'bom',
    #'checkdns',
    #'cnet',
    #'google_finance',
    #'google_search',
    #'imdb',
    #'linuxquestions',
    #'msn_search',
    #'msn_weather',
    #'rottentomatoes',
    #'slashdot',
    #'stackoverflow',
    #'techsupportforums',
    #'theage',
    #'theonion',
    #'theaustralian',
    'ubuntuforums',
    #'yahoo_weather',
    #'yahoo_finance',    
]
[
    'ebay', # scrape works, but not when try..?
    'yahoo_search', # extra div in scraped
]


for module in __all__:
    exec 'import ' + module
