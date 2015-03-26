#!/usr/bin/python
# -*- coding: utf-8 -*-


    
data = [
    ('1.html', [["Action: The Complete Series", "Next", "Action!: Nothing Happens Until Something Moves"], ["$14.49", "$13.99", "$16.47"]]),
    ('2.html', [["It Doesn't Get Dark Until Midnight", "Hatchet", "Alexander: Hall of the Gods"], ["$14.95", "$6.99", "$12.92"]]),
    ('3.html', [["Girl Next Door", "Lie With Me", "Shortbus (Unrated Edition)"], ["$1.99", "$7.99", "$24.99"]]),
]

model = [
    ["/html[1]/body[1]/div[@id='searchTemplate']/div[@id='rightResults']/div[@id='Results']/div[@class='listView']/div/div[@class='productData']/div[@class='productTitle']/a[1]"],
    ["/html[1]/body[1]/div[@id='searchTemplate']/div[@id='rightResults']/div[@id='Results']/div[@class='listView']/div/div[@class='productData']/div[2]/span[1]"]
]
