#!/usr/bin/python
# -*- coding: utf-8 -*-


# doesn't fit model: http://forums.cnet.com/5208-7589_102-0.html?forumID=62&threadID=319574
data = [
    ('1.html', ['Router/Switch help - CNET Networking & wireless Forums',
    ["Router/Switch help",
    "(NT) Switch will be fine and no."],
    ["""We've got a Cisco WRT310N router hooked up to the modem in one room and all 4 ports are in use. I want to get a switch so I can connect my PC, a laptop, and a video game console in another area of the house. Is there any specific switch I should get or will any brand/model do?
    Also, will using a switch slow down the internet connection to the PC at all?"""],
    ]),
    ('2.html', ['File Sharing - CNET Networking & wireless Forums',
    [
    "File Sharing",
    "Which OS, Home or Pro?",
    "Both PCs are connected, but not seen on the Explorer ",
    "Can you make sure that file and print sharing are enabled ",
    "Firewall is not reason",
    "Not that it would make much difference but ",
    "What I do . . . ",
    "Computer NOT found in My Network Places ",
    "Read your posts twice. ",
    "Read it all again. ",
    ],
    [
    """
    Hello,
    I want to share files on 2 PCs: a desktop and a laptop.
    I have got a router.
    Both PCs are connected to the internet.
    Both PCs have the same workgroup name: mshome.
    The desktop name is Desktop-PC.
    The laptop name is Laptop-PC.
    Both PCs have shared folders called: Shared Documents.
    The service Server is enabled on both PCs.
    When I right click "My Computer">Map Network Drive, I do not see any workgroup and no shared workgroup folder.
    How and where do I find the laptop Laptop-PC in the desktop Desktop-PC folders tree in the Explorer?
    I tried to search computer Laptop-PC, but found nothing.
    What do I miss?
    Thank you,
    Gila.
    """,
    """
    Have you created the share? Without having a shared drive, folder or other device, there's nothing to show when browsing the network. What you might try first is to see if you can "ping" one PC from the other. You only need to know it's IP address which you can find from Start/Run and typing "command" (without quotes) in the box. It will bring up a command window where you type "ping <IP address of other PC>" (again, no quotes). An example might be

    ping 192.168.100.2

    You should get 4 return lines. If you get a reply showing packets sent/received with none lost, you are connected. If you get a timeout or destination unreachable message, you're not connected. Let's see where you stand in that department first.
    """,
    """
    Hello Steven,
    Thank you.
    My OS is Windows XP Home.
    Desktop-PC IP Address is: 10.0.0.1
    Laptop-PC IP Address is: 10.0.0.2
    Run > ping 10.0.0.2 on Desktop-PC OK
    Run > ping 10.0.0.1 on Laptop-PC OK
    Both PCs are connected and recognize each other.
    No packets lost.
    On Desktop-PC: Workstation Service Started
    On Laptop-PC: Server Service Started
    My firewall is ZoneAlarm. Both IPs are in the trusted zone.
    I still can not see the other PC in the folder "My Network Places".
    Are there any services that must be started for file sharing?
    Thank you again,
    Gila.
    """,
    """and that the Windows firewall has the local area network listed as an exception? As a test, you can always temporarily disable a firewall to see if it's what's blocking you. I'm also a wondering why those IP addresses were chosen. Did you set these statically or are they coming from your router? Not that it should matter but you might want to change to the standard MS convention of 192.168.X.X and see if that helps.""",
    """I shut the firewall on both PCs but it did not help.
    My router identification is 10.0.0.138. I assume those IP addresses were chosen by the router.
    The router is ASUS. Wireless is disabled (Safety reason).
    How can I change to the standard MS convention of 192.168.X.X to see if that helps? I do not know how it is done.
    What should be the exact IP (without X.X)?""",
    """you'd do this by going to your router's web interface and changing it's IP address to something like 192.168.1.1. After that, you'd select the range of IP addresses your router could hand out. I like to reserve some for static use and usually let the router handle the rest. An example might be that you'd then let the router handle addresses from 192.168.1.100 and up. You'd need to restart the router and shut down your browser. Your PC is going to loose it's connection but should get it back when a new IP address is assigned. In some cases it's easier to just shut down and restart whatever is on the network. Where I've seen the MS convention used is in the original ICS feature with Win 98. The PC sharing the connection needed to be at address 192.168.0.1. There are different classes of address ranges and some are reserved. I don't know much about that.""",
    """is use Explorer. Click the + sign next to My Network Places and expand it. You'll find the computer there.

    Unless you are running a firewall. If so you'll need to allow access through the firewall.""",
    """Hello Coryphaeus,
    Thank you.
    My firewall is ZoneAlarm. Both IPs are in the trusted zone.
    I still can not see the other PC in the folder "My Network Places".
    Thank you again,
    Gila.""",
    """And missed the OS in use. So for Vista to XP networking you install the LLTD. (see google or this forum's sticky.)

    You didn't tell much about the router. It can have a firewall or "AP ISOLATION."
    Bob""",
    """Details are still sketchy. Firewalls even when disabled (Zonealarm, others) still work so I've taken to uninstalling them when I hit that issue.

    The Asus router is noted but I can't find the model number. What you need to understand is that the details is where the problem is. Be sure to have a nice post with all of them.
    Bob"""
    ],
    ]),
    ('3.html', ["School Network Question - CNET Networking & wireless Forums",
    ["School Network Question",
    "Home quality router in a school "],
    ["""Hello Folks,

    I have a question, hope you guys got some thoughts.

    I run a small international school network (about 70 users) and I just bought a Linksys WRT350N Gigabit router for the campus. I am finding that this is failing almost every 24 hours. I have updated the firmware to the newest possible. I am basically wondering, is it possible that since this is a home router, it just cannot handle this much traffic? The school has no problem dropping some money on a business class router. I just don't know if that is possible.

    Secondly, I heard somewhere that it is better to separate out the wireless function? So use a wired router, then just have access points, so that the router can just worry about routing.

    Third, I have thought about running a PC as a router in lieu of a expensive router. How hard is it to install/configure? Is it even worth it?

    Thanks for your time,

    Tark""",
    """For a school, I'd go with something better and even consider a router with a managed firewall. I offer some support to a small K-8 school. Their router is from Sonicwall and is managed remotely. It can block specific types of traffic, sites, etc. You'll want that capability. As for wireless, we added that separately. How we did ours was to purchase a number of APs with PoE capability, purchase a separate PoE switch and connect the access points through that. The PoE switch uplinks to a port on the router. The switch is also managed but quite simply. Doing this allowed me to connect that switch to an AC switching panel that allows the entire wireless network to be turned on and off separately. It's generally only turned on during school hours or for special use. This limits the time it's vulnerable to attack as the rest of the network is left on 24/7 for remote administration purposes and staff access to the school's NAS storage drive from their homes."""]
    ]),
    ('4.html', ["Internet disconnecting and connecting randomly - CNET Networking & wireless Forums",
    ["Internet disconnecting and connecting randomly ",
    "My first question.",
    "I would think so, matches ",
    "Now change the RF Channel. ",
    "Im sorry, confused",
    "The channel of your router's wifi. ",
    "If this helps ",
    "If 6 drops we try "],
    ["""Randomly my wireless internet will disconnect and reconnect a few seconds later. It'll say I have excellent connection but ignore that and disconnect makign everything im connected to refresh and all that annoying stuff.

    Other times my wireless connection will get the yellow yield sign and stay disconnected and when i repair itll connect before it finishes making it unable for me to figure out why its doing this.

    I was curious if any of you guys know how i can solve this.

    Thanks


    I have a Linksys WRT54G router and Cable high speed internet.""",
    """Is it set up per our forum sticky?

    (That's the top post stuck at the top of this forum.)""",
    """Yea set up like this (plus ive had this router for about 4-5 years and its been doing this alot in the past year)

    Wall >> Cable Modem >> Ethernet Cable >> Router >> Wireless Laptop (up a floor but happens to another wireless laptop around the same area of the router)

    If thats what you meant, ill keep looking through the sticky though.

    I also have been in my router admin options.""",
    """And share the rest of the details so members can check your work.""",
    """Im sorry, what do you mean by RF? I appreciate the help and sorry for lack of terms but could you give me an example?""",
    """It's in the router manual. Provide a link to the PDF so I can point out the page number.

    -> Remember I'm taking your word that this router is set per our forum sticky. It would be a shame to have this many posts and find out you set it to WEP protection.""",
    """I am on channel 6 of my router, but i have realized reading the first post in the sticky, i do not have a security set up. So neither WEP nor WPA..

    Sorry again I am not as knowledgeable on this topic, so if I should have it set to a certain WPA let me know. I will start to mess around with that.""",
    """1 then 11. The reason for the forum sticky is so that we don't have to cover the same issues with each new post. We use that first.
    Bob"""]
    ]),
    ('5.html', ["Looking for 2 Arcnet cards (Reconditioning or Refurbished) - CNET Networking & wireless Forums",
    ["Looking for 2 Arcnet cards (Reconditioning or Refurbished) ",
    "Try Ebay, Craigslist and such. ",
    "Arcnet Products ",
    "Call for your Address and Phone Number "],
    ["""Guys, if you have the info where can i get the following networking cards:
    Manufacturer : CNET Technology Inc,
    Model : CN190SBT
    NIC Type : ARCNET
    Transfer Rate: 2.5 Mbps
    Data Bus : 8 or 16 bit ISA
    Topology : Star / Linear Bus
    Wiring Type : Unshielded Twisted Pair RG62 A/U93 ohm Coaxial
    Boot ROM : Available
    Qty.Required : 2 pcs.
    The cards are obsolete, and I accept the reconditioning or refurbished ones as long they are still functioning.
    Please do not hesitate to share your knowledge.

    Sincerely,

    David Marihot""",
    """But CNET Forums has no association with that Cnet hardware company. Just so you know.""",
    """we have different ISA 8- and 16-bit new and refurbished Arcnet adapters and Hubs in stock.""",
    """Dear Sir,
    I am pleased to find out that you have the cards that we are looking for. Please kindly contact us in the below correspondence address:
    Mr.Devid Marihot
    PT Jupan Jaya Sejahtera
    Bambu I No.80
    Jakarta-Indonesia 11480
    Fax/Phone: +62-21-5847145
    Mobile: +62-0817797585

    We are looking forward to your respond.

    Regards,

    Devid Marihot"""]
    ]),
    ('6.html', ["D-Link DI-524 Problem - CNET Networking & wireless Forums",
    ["D-Link DI-524 Problem ",
    "When you connect cable modems to the PC.",
    "Done that ",
    "Sorry",
    "Router issue "],
    ["""Hey guys,

    Well, i was just happily browsing the web, when i decided i should reboot my internet modem, and my wireless router, just to refresh things up. After i rebooted my router, the status led light, just keeps flashing on and off, on and off. Every other light is ok, like the WAN and WLAN led lights, which are continuously on, but the status led light is off and on, off and on. This is a problem because i can't connect to the internet through my router anymore. I'm writing this by connecting my modem directly to my pc, but does anyone know the problem to my router?

    I didn't download any new firmware for it. It just happened all of a sudden.

    I just noticed that i got capped with my ISP at around the same time as the router wouldn't work..

    When i go through everything with the router, i can access the 192.168.0.1 page, and update stuff through there. But i can't access anything on the internet.

    I didn't update any firmware, it just happened when i rebooted my router. Every light is solid, except for the status light, which keeps flashing.

    Cheers, guys!""",
    """When you need to move it back to the router you need to power off the modem, move the ethernet cable, then power up the modem. I'll stop here.
    Bob""",
    """I did that, but still same problem. I can connect to D-Links configuration page (192.168.0.1), but i can't connect to the internet.""",
    """Looking at your post I can't tell how you configured the router. This is something you'll have to share if you want others to check your work.""",
    """If you reset modem and did a physical reset of the router and you still have a problem, reinstall the router software."""]
    ])
]


model = [
    '/html/head/title',    
    ['/html/body/div/div/div[2]/div/div/div/div/div/div[2]/div/div[5]/div/div/h3'],
    ['/html/body/div/div/div[2]/div/div/div/div/div/div[2]/div/div[5]/div/div/p'],
]
