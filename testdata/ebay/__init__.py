#!/usr/bin/python
# -*- coding: utf-8 -*-

data = [
    ('1.html', [
        ["LOT 2 Mary Kay TimeWise Targeted-Action Line Reducer", "NASCAR 2008 Ford Fusion Action COT 1/64th Scale Car", "Lot of Batman and Superman animated action figures."],
        ["$31.00", "$1.25", "$5.00"]
    ]),
    ('2.html', [
        ["NEW NINTENDO WII FIT GAME BALANCE BOARD +GAMES", "THE BEST AMOS 'N ANDY ANYWHERE! All 79 TV SHOWS. EXTRAS", "Icon-The Complete Miniseries-Swayze-NEW-FREE SHIPPING!!"],
        ["$100.00", "$39.95", "$7.98"]
    ]),
    ('3.html', [
        ["Sexy French Maid Adult Halloween Costume Mini dress", " Aussie Lingerie 2 Pr Adult Hot FishNet Sock White+Black", "Adult Mature Brass Corkscrew Bottle Opener New In Box"],
        ["$19.37", "$0.77", "$8.95"]
    ]),
    ('4.html', [
        ["FOR VERIZON ADVENTURE MOTOROLA V750 NEW COVER CASE+CLIP", "Leather Case Pouch for Verizon Motorola Adventure v750", "CAR CHARGER+CASE for VERIZON MOTOROLA V750 ADVENTURE"],
        ["$9.99", "$5.12", "$8.99"]
    ]),
    ('5.html', [
        ["Enlarge British Africa - South Africa #B1-4 MH-LH VF CV $48.25", "British Africa - South Africa #C5-6 MLH VF CV $36.00", "29.44cts 26x27mm PICTURE JASPER PEAR CAB AFRICA $NR!"],
        ["$12.15", "$9.15", "$0.99"]
    ]),
    ('6.html', [
        ["Breaking Ice -ANTHOLOGY OF AFRICAN AMERICAN FICTION", "Sweeter Than Honey M. Morrison african american fiction", "Can't Say No by Bette Ford african american fiction"],
        ["$1.99", "$7.99", "$2.99"]
    ]),
]


# ebay's formatting is inconsistent depending on whether the price is marked down
# consequently this model will get duplicate results for the prices
model = [
    ['/html/body/div[3]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[4]/div/div[3]/table/tr/td[5]'],
    ['/html/body/div[3]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[4]/div/div[3]/table/tr/td[2]/a'],
]
