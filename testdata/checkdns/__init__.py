#!/usr/bin/python
# -*- coding: utf-8 -*-



data = [
    ('1.html', ['Automatically clearing "Preferred Networks" list',
    ["""
    Automatically clearing "Preferred Networks" list

    Postby Jack B. Pollack on Sat Oct 06, 2007 2:05 am
    I am looking for a way through a batch file, reg file, etc. to clear the
    "Preferred Networks" list in Win XP.

    I found references to the SSID's in 2 registry keys:

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\EAPOL\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WZCSVC\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}

    Even after deleting these keys (and rebooting) the "Preferred Networks" list
    is not clear.

    Anyone have any idea where the remaining settings are stored and how to
    clear the list automatically?

    Thanks
    """,
    """Just a thought -
    Before deleting these keys, make sure that wzcsvc is stopped.
    Do you have SP2 with the latest wireless updates (WPA2) ?

    --PA



    "Jack B. Pollack" <N@NE.nothing> wrote in message news:%23IJjZ17BIHA.484@TK2MSFTNGP06.phx.gbl...
    [quote]I am looking for a way through a batch file, reg file, etc. to clear the
    "Preferred Networks" list in Win XP.

    I found references to the SSID's in 2 registry keys:

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\EAPOL\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WZCSVC\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}

    Even after deleting these keys (and rebooting) the "Preferred Networks" list
    is not clear.

    Anyone have any idea where the remaining settings are stored and how to
    clear the list automatically?

    Thanks


    [/quote]""",
    """Jack,

    Why don't you force your machine to use the one you want.

    If you're using wireless then you could be picking up your neighbours wireless network

    -- 
    Newbie Coder
    (It's just a name)

    "Jack B. Pollack" <N@NE.nothing> wrote in message
    news:%23IJjZ17BIHA.484@TK2MSFTNGP06.phx.gbl...
    [quote]I am looking for a way through a batch file, reg file, etc. to clear the
    "Preferred Networks" list in Win XP.

    I found references to the SSID's in 2 registry keys:

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\EAPOL\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WZCSVC\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}

    Even after deleting these keys (and rebooting) the "Preferred Networks" list
    is not clear.

    Anyone have any idea where the remaining settings are stored and how to
    clear the list automatically?

    Thanks


    [/quote]""",
    """I have users that travel and connect at hotels, etc. The Preferred network
    list sometimes contains 100's of entries with the "real' networks at the
    bottom and networks that will never be used again at the top.

    Looking for a quick way to clear the list and maybe populate it with just
    the real networks



    "Newbie Coder" <newbiecoder@spammeplease.com> wrote in message
    news:ORmbRyKCIHA.4176@TK2MSFTNGP06.phx.gbl...
    [quote]Jack,

    Why don't you force your machine to use the one you want.

    If you're using wireless then you could be picking up your neighbours
    wireless network

    --
    Newbie Coder
    (It's just a name)

    "Jack B. Pollack" <N@NE.nothing> wrote in message
    news:%23IJjZ17BIHA.484@TK2MSFTNGP06.phx.gbl...
    I am looking for a way through a batch file, reg file, etc. to clear the
    "Preferred Networks" list in Win XP.

    I found references to the SSID's in 2 registry keys:


    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\EAPOL\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}


    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WZCSVC\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}

    Even after deleting these keys (and rebooting) the "Preferred Networks"
    list
    is not clear.

    Anyone have any idea where the remaining settings are stored and how to
    clear the list automatically?

    Thanks



    [/quote]""",
    """Stopping the serviced WORKED. Thanks

    "Pavel A." <pavel_a@NOwritemeNO.com> wrote in message
    news:#LxHaVCCIHA.5044@TK2MSFTNGP03.phx.gbl...
    [quote]Just a thought -
    Before deleting these keys, make sure that wzcsvc is stopped.
    Do you have SP2 with the latest wireless updates (WPA2) ?

    --PA



    "Jack B. Pollack" <N@NE.nothing> wrote in message
    news:%23IJjZ17BIHA.484@TK2MSFTNGP06.phx.gbl...
    I am looking for a way through a batch file, reg file, etc. to clear the
    "Preferred Networks" list in Win XP.

    I found references to the SSID's in 2 registry keys:


    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\EAPOL\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}


    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WZCSVC\Parameters\Interfaces\{93BA05F9
    -E76A-4F5F-A0B5-A2D700210346}

    Even after deleting these keys (and rebooting) the "Preferred Networks"
    list
    is not clear.

    Anyone have any idea where the remaining settings are stored and how to
    clear the list automatically?

    Thanks




    [/quote]""",
    ]]),
    ('2.html', ["Wireless connection speed decreases strangely", 
    ["""My wireless connection decreases from 56mbps to 1.0mbps for no reason after
    half-hour. I'm using linksys router and tried power cycling the router but to
    no avail. The only way I can do is to repair the connection and it returns to
    maximum speed.""",
    """On Tue, 25 Sep 2007 09:50:01 -0700, drago98 <drago98@discussions.microsoft.com>
    wrote:

    [quote]My wireless connection decreases from 56mbps to 1.0mbps for no reason after
    half-hour. I'm using linksys router and tried power cycling the router but to
    no avail. The only way I can do is to repair the connection and it returns to
    maximum speed.
    [/quote]
    Have you tried testing actual throughput periodically, as in when you first
    start out (max connection speed), then again when you are at min connection
    speed. If you have noise (analog interference) or neighbours (digital
    interference), you'll not be getting max throughput, regardless of connection
    speed.

    Some WiFi drivers may start your connection out at maximum expected speed, and
    gradually decrease, looking for a stable connection. Depending upon the
    interference that you may be getting, this could give you a steadily decreasing
    connection rate. Do a WiFi environment analysis, and watch your metrics and
    your neighbours.
    <http://nitecruzr.blogspot.com/2006/06/analyse-your-wifi-environment.html>
    http://nitecruzr.blogspot.com/2006/06/a ... nment.html

    -- 
    Cheers,
    Chuck, MS-MVP 2005-2007 [Windows - Networking]
    http://nitecruzr.blogspot.com/
    Paranoia is not a problem, when it's a normal response from experience.
    My email is AT DOT
    actual address pchuck mvps org.""",
    """However, my other laptop using the same wireless router is running at full
    speed. So there isn't any interference. Both laptops are using the same
    settings.

    "Chuck [MVP]" wrote:

    [quote]On Tue, 25 Sep 2007 09:50:01 -0700, drago98 <drago98@discussions.microsoft.com
    wrote:

    My wireless connection decreases from 56mbps to 1.0mbps for no reason after
    half-hour. I'm using linksys router and tried power cycling the router but to
    no avail. The only way I can do is to repair the connection and it returns to
    maximum speed.

    Have you tried testing actual throughput periodically, as in when you first
    start out (max connection speed), then again when you are at min connection
    speed. If you have noise (analog interference) or neighbours (digital
    interference), you'll not be getting max throughput, regardless of connection
    speed.

    Some WiFi drivers may start your connection out at maximum expected speed, and
    gradually decrease, looking for a stable connection. Depending upon the
    interference that you may be getting, this could give you a steadily decreasing
    connection rate. Do a WiFi environment analysis, and watch your metrics and
    your neighbours.
    http://nitecruzr.blogspot.com/2006/06/a ... nment.html
    http://nitecruzr.blogspot.com/2006/06/a ... nment.html

    --
    Cheers,
    Chuck, MS-MVP 2005-2007 [Windows - Networking]
    http://nitecruzr.blogspot.com/
    Paranoia is not a problem, when it's a normal response from experience.
    My email is AT DOT
    actual address pchuck mvps org.
    [/quote]""",
    """what operating system? what NIC and what driver?
    which Linksys router model number and hardware rev and what firmware
    version?

    On Tue, 25 Sep 2007 09:50:01 -0700, drago98
    <drago98@discussions.microsoft.com> wrote:

    [quote]My wireless connection decreases from 56mbps to 1.0mbps for no reason after
    half-hour. I'm using linksys router and tried power cycling the router but to
    no avail. The only way I can do is to repair the connection and it returns to
    maximum speed.
    --[/quote]

    Barb Bowman
    MS Windows-MVP
    http://www.microsoft.com/windowsxp/expe ... owman.mspx
    http://blogs.digitalmediaphile.com/barb/""",
    """On Wed, 3 Oct 2007 03:03:03 -0700, drago98 <drago98@discussions.microsoft.com>
    wrote:

    [quote]"Chuck [MVP]" wrote:

    On Tue, 25 Sep 2007 09:50:01 -0700, drago98 <drago98@discussions.microsoft.com
    wrote:

    My wireless connection decreases from 56mbps to 1.0mbps for no reason after
    half-hour. I'm using linksys router and tried power cycling the router but to
    no avail. The only way I can do is to repair the connection and it returns to
    maximum speed.

    Have you tried testing actual throughput periodically, as in when you first
    start out (max connection speed), then again when you are at min connection
    speed. If you have noise (analog interference) or neighbours (digital
    interference), you'll not be getting max throughput, regardless of connection
    speed.

    Some WiFi drivers may start your connection out at maximum expected speed, and
    gradually decrease, looking for a stable connection. Depending upon the
    interference that you may be getting, this could give you a steadily decreasing
    connection rate. Do a WiFi environment analysis, and watch your metrics and
    your neighbours.
    http://nitecruzr.blogspot.com/2006/06/a ... nment.html
    http://nitecruzr.blogspot.com/2006/06/a ... nment.html

    However, my other laptop using the same wireless router is running at full
    speed. So there isn't any interference. Both laptops are using the same
    settings.
    [/quote]
    Interesting and useful details. What other details have you not disclosed?
    <http://nitecruzr.blogspot.com/2005/06/background-information-useful-in.html>
    http://nitecruzr.blogspot.com/2005/06/b ... ul-in.html

    -- 
    Cheers,
    Chuck, MS-MVP 2005-2007 [Windows - Networking]
    http://nitecruzr.blogspot.com/
    Paranoia is not a problem, when it's a normal response from experience.
    My email is AT DOT
    actual address pchuck mvps org.""",
    """
    "Chuck [MVP]" <none@example.net> wrote in message news:3l87g355hcs5c6qrc76oeh22q5aec55qen@4ax.com...

    [quote]Interesting and useful details. What other details have you not disclosed?
    [/quote]
    Models of wireless adapters on both machines.
    Band and channel set on the router.

    Regards,
    --PA""",
    ]]),
    ('3.html', ["Connecting Wireless Network from Building to Building",
    ["""We have a requirement to connect a number of notebooks in a building to a
    ship - wirelessly.

    The current proposal is to have a wireless bridge on the ship, bridging to a
    bridge on the ground. This bridge on the ground is then connected to an
    access point by cable and the notebooks connect to the access point.

    The access point maybe required to be a distance from the bridge due to the
    structure of the buildings - so that the access point can definately connect
    to the notebooks.

    I am not sure this is the best way. I don't want to run a cable from the
    bridge to the access point. I looked before at a repeater inline - with only
    using access points - but the signal was slightly un-reliable and we cannot
    afford this network connection to be unreliable.

    Any thoughts appreciated.""",
    """You need to be a lot more specific about distance, obstacles between
    the ship and the building and define the actual number of
    simultaneous wireless users.

    On Fri, 5 Oct 2007 09:52:01 +0100, "Jim" <jim@nomail.com> wrote:

    [quote]We have a requirement to connect a number of notebooks in a building to a
    ship - wirelessly.

    The current proposal is to have a wireless bridge on the ship, bridging to a
    bridge on the ground. This bridge on the ground is then connected to an
    access point by cable and the notebooks connect to the access point.

    The access point maybe required to be a distance from the bridge due to the
    structure of the buildings - so that the access point can definately connect
    to the notebooks.

    I am not sure this is the best way. I don't want to run a cable from the
    bridge to the access point. I looked before at a repeater inline - with only
    using access points - but the signal was slightly un-reliable and we cannot
    afford this network connection to be unreliable.

    Any thoughts appreciated.

    --[/quote]

    Barb Bowman
    MS Windows-MVP
    http://www.microsoft.com/windowsxp/expe ... owman.mspx
    http://blogs.digitalmediaphile.com/barb/""",
    """Can't be that specific as it is not going to be tied to one building.

    The laptops (six devices) will be anything up to 150 metres from the ship,
    with various obsticles inbetween eg walls, metal doors etc.

    That's why I am asking about repeaters etc.


    "Barb Bowman" <barb@nospam.com> wrote in message
    news:pv3cg39geld1vh17jducn12eeqm8v2md71@4ax.com...
    [quote]You need to be a lot more specific about distance, obstacles between
    the ship and the building and define the actual number of
    simultaneous wireless users.

    On Fri, 5 Oct 2007 09:52:01 +0100, "Jim" <jim@nomail.com> wrote:

    We have a requirement to connect a number of notebooks in a building to a
    ship - wirelessly.

    The current proposal is to have a wireless bridge on the ship, bridging to
    a
    bridge on the ground. This bridge on the ground is then connected to an
    access point by cable and the notebooks connect to the access point.

    The access point maybe required to be a distance from the bridge due to
    the
    structure of the buildings - so that the access point can definately
    connect
    to the notebooks.

    I am not sure this is the best way. I don't want to run a cable from the
    bridge to the access point. I looked before at a repeater inline - with
    only
    using access points - but the signal was slightly un-reliable and we
    cannot
    afford this network connection to be unreliable.

    Any thoughts appreciated.

    --

    Barb Bowman
    MS Windows-MVP
    http://www.microsoft.com/windowsxp/expe ... owman.mspx
    http://blogs.digitalmediaphile.com/barb/[/quote]""",
    """Hi
    Technically you do it as describe in this page.
    Wireless Bridging - http://www.ezlan.net/bridging.html
    Would it work?
    It depends on the environment and the capacity to install multiple
    Bridges/Repeaters.
    Jack (MVP-Networking).

    "Jim" <jim@nomail.com> wrote in message
    news:XfWdnZTlkIVTjpvanZ2dneKdnZydnZ2d@pipex.net...
    [quote]Can't be that specific as it is not going to be tied to one building.

    The laptops (six devices) will be anything up to 150 metres from the ship,
    with various obsticles inbetween eg walls, metal doors etc.

    That's why I am asking about repeaters etc.


    "Barb Bowman" <barb@nospam.com> wrote in message
    news:pv3cg39geld1vh17jducn12eeqm8v2md71@4ax.com...
    You need to be a lot more specific about distance, obstacles between
    the ship and the building and define the actual number of
    simultaneous wireless users.

    On Fri, 5 Oct 2007 09:52:01 +0100, "Jim" <jim@nomail.com> wrote:

    We have a requirement to connect a number of notebooks in a building to a
    ship - wirelessly.

    The current proposal is to have a wireless bridge on the ship, bridging
    to a
    bridge on the ground. This bridge on the ground is then connected to an
    access point by cable and the notebooks connect to the access point.

    The access point maybe required to be a distance from the bridge due to
    the
    structure of the buildings - so that the access point can definately
    connect
    to the notebooks.

    I am not sure this is the best way. I don't want to run a cable from the
    bridge to the access point. I looked before at a repeater inline - with
    only
    using access points - but the signal was slightly un-reliable and we
    cannot
    afford this network connection to be unreliable.

    Any thoughts appreciated.

    --

    Barb Bowman
    MS Windows-MVP
    http://www.microsoft.com/windowsxp/expe ... owman.mspx
    http://blogs.digitalmediaphile.com/barb/

    [/quote]""",
    """We are did the same in our outdoor wireless using Cisco 1310 bridge. Based
    on our experience, you must have very clean distance between bridge and
    bridge/repeater/AP. More repeaters, the single will be weaker and
    un-reliable.

    -- 
    Bob Lin, MS-MVP, MCSE & CNE
    Networking, Internet, Routing, VPN Troubleshooting on
    http://www.ChicagoTech.net
    How to Setup Windows, Network, VPN & Remote Access on
    http://www.HowToNetworking.com


    "Jim" <jim@nomail.com> wrote in message
    news:XfWdnZTlkIVTjpvanZ2dneKdnZydnZ2d@pipex.net...
    [quote]Can't be that specific as it is not going to be tied to one building.

    The laptops (six devices) will be anything up to 150 metres from the ship,
    with various obsticles inbetween eg walls, metal doors etc.

    That's why I am asking about repeaters etc.


    "Barb Bowman" <barb@nospam.com> wrote in message
    news:pv3cg39geld1vh17jducn12eeqm8v2md71@4ax.com...
    You need to be a lot more specific about distance, obstacles between
    the ship and the building and define the actual number of
    simultaneous wireless users.

    On Fri, 5 Oct 2007 09:52:01 +0100, "Jim" <jim@nomail.com> wrote:

    We have a requirement to connect a number of notebooks in a building to a
    ship - wirelessly.

    The current proposal is to have a wireless bridge on the ship, bridging
    to a
    bridge on the ground. This bridge on the ground is then connected to an
    access point by cable and the notebooks connect to the access point.

    The access point maybe required to be a distance from the bridge due to
    the
    structure of the buildings - so that the access point can definately
    connect
    to the notebooks.

    I am not sure this is the best way. I don't want to run a cable from the
    bridge to the access point. I looked before at a repeater inline - with
    only
    using access points - but the signal was slightly un-reliable and we
    cannot
    afford this network connection to be unreliable.

    Any thoughts appreciated.

    --

    Barb Bowman
    MS Windows-MVP
    http://www.microsoft.com/windowsxp/expe ... owman.mspx
    http://blogs.digitalmediaphile.com/barb/

    [/quote]""",
    """You might need wired access points for roaming and/or wireless
    repeaters coupled with one or more devices on the ship (you didn't
    say how big the ship is). Or even a combination of everything,
    depending on topology. Special antennae might help as well. If you
    have the capability to hardwire some access points at the edges of
    buildings, that would help, especially with walls and metal doors in
    the line of sight.

    On Fri, 5 Oct 2007 11:36:53 +0100, "Jim" <jim@nomail.com> wrote:

    [quote]Can't be that specific as it is not going to be tied to one building.

    The laptops (six devices) will be anything up to 150 metres from the ship,
    with various obsticles inbetween eg walls, metal doors etc.

    That's why I am asking about repeaters etc.


    "Barb Bowman" <barb@nospam.com> wrote in message
    news:pv3cg39geld1vh17jducn12eeqm8v2md71@4ax.com...
    You need to be a lot more specific about distance, obstacles between
    the ship and the building and define the actual number of
    simultaneous wireless users.

    On Fri, 5 Oct 2007 09:52:01 +0100, "Jim" <jim@nomail.com> wrote:

    We have a requirement to connect a number of notebooks in a building to a
    ship - wirelessly.

    The current proposal is to have a wireless bridge on the ship, bridging to
    a
    bridge on the ground. This bridge on the ground is then connected to an
    access point by cable and the notebooks connect to the access point.

    The access point maybe required to be a distance from the bridge due to
    the
    structure of the buildings - so that the access point can definately
    connect
    to the notebooks.

    I am not sure this is the best way. I don't want to run a cable from the
    bridge to the access point. I looked before at a repeater inline - with
    only
    using access points - but the signal was slightly un-reliable and we
    cannot
    afford this network connection to be unreliable.

    Any thoughts appreciated.

    --

    Barb Bowman
    MS Windows-MVP
    http://www.microsoft.com/windowsxp/expe ... owman.mspx
    http://blogs.digitalmediaphile.com/barb/

    --[/quote]

    Barb Bowman
    MS Windows-MVP
    http://www.microsoft.com/windowsxp/expe ... owman.mspx
    http://blogs.digitalmediaphile.com/barb/""",
    ]]),
    ('4.html', ["Automatically assign SSID, Authentication and Network Key",
    ["""My brain is mush from trying to find an answer to this issue, but I'm hoping
    that someone here in the community has been driven as nuts as I and still
    forged forward and found the answer.

    I am creating a slipstreamed installation CD for our work laptops that would
    allow Windows XP Pro SP2 to be installed without user intervention. We have a
    wireless network that I would like to connect to without them having to enter
    the SSID, Encryption method or Network Key. Windows Connect Now allows one to
    save the settings to an XML file on a USB drive, but this method still
    requires the user to 'choose' to connect to the network. This is unacceptable
    in my work environment. Has anyone discovered a method of programmatically
    assigning an SSID, Encryption method and Network Key to a wireless network
    during installation of Windows XP SP2? I've googled all over the Internet and
    come up against a blank wall.""",
    """I'm not a developer so I can't confirm if this will give you everything you
    need, but go here:

    http://www.microsoft.com/technet/networ ... fifaq.mspx

    And look at the second question under "Wireless Auto Configuration."


    -- 
    Steve Riley
    steve.riley@microsoft.com
    http://blogs.technet.com/steriley
    http://www.protectyourwindowsnetwork.com


    "Bruce W. Darby" <BruceWDarby@discussions.microsoft.com> wrote in message
    news:3456150D-7202-4C99-9A41-606F2C204648@microsoft.com...
    [quote]My brain is mush from trying to find an answer to this issue, but I'm
    hoping
    that someone here in the community has been driven as nuts as I and still
    forged forward and found the answer.

    I am creating a slipstreamed installation CD for our work laptops that
    would
    allow Windows XP Pro SP2 to be installed without user intervention. We
    have a
    wireless network that I would like to connect to without them having to
    enter
    the SSID, Encryption method or Network Key. Windows Connect Now allows one
    to
    save the settings to an XML file on a USB drive, but this method still
    requires the user to 'choose' to connect to the network. This is
    unacceptable
    in my work environment. Has anyone discovered a method of programmatically
    assigning an SSID, Encryption method and Network Key to a wireless network
    during installation of Windows XP SP2? I've googled all over the Internet
    and
    come up against a blank wall.[/quote]""",
    """Steve Riley [MSFT]" wrote:

    [quote]I'm not a developer so I can't confirm if this will give you everything you
    need, but go here:
    [/quote]
    Steve,

    While I hadn't seen the faq page, the information it linked to I have and it
    won't help me because, as you, I am not a developer. :) But there was a link
    on one of the pages I followed that looks extremely promising. I'll need to
    get it to one of our dev's to see if they can work out a method whereby we
    can get the job done. Thanks much for the lead!""",
    """Bruce,

    For managed environments, it is better that all laptops be equipped with
    same wireless device & driver that supports managed setup.
    For one, PROset software for Centrino wi-fi adapters can do what you need -
    a proven, real life solution, free of any Windows domain or group policy complications.
    Other vendors may have similar solutions.
    The worst thing is if you let all users install their random mix of adapters and software.

    Regards,
    --PA


    "Bruce W. Darby" <BruceWDarby@discussions.microsoft.com> wrote in message
    news:6E667B50-B80B-4D1E-A20F-A4271BF5F8AC@microsoft.com...
    [quote]

    "Steve Riley [MSFT]" wrote:

    I'm not a developer so I can't confirm if this will give you everything you
    need, but go here:

    Steve,

    While I hadn't seen the faq page, the information it linked to I have and it
    won't help me because, as you, I am not a developer. :) But there was a link
    on one of the pages I followed that looks extremely promising. I'll need to
    get it to one of our dev's to see if they can work out a method whereby we
    can get the job done. Thanks much for the lead![/quote]""",
    ]]),
    ('5.html', ["US Robotics Routers?",
    ["""Anyone have any experience with these in a home network environment?

    Supposedly they will allow a mixed environment of some "B" and some "G"
    devices to operate at their designed speed instead of dropping back the
    entire network to the "B" capability.""",
    """Hi
    I do not know in specific about the USR. Newer Wireless Router do not revert
    entirely to 802.11b, there are differences in how much "Hit" the 802.11g
    takes in presence of 802.11b, but there is always a "Hit".
    Client 802.11g cards are so inexpensive these day that there is No reason to
    compromise on buying mediocre Wireless devices.
    In addition usage of 802.11b usually reduces the security configuration to
    WEP, which is currently Highly insecure.
    Jack (MVP-Networking).

    "Pegleg" <Pegleg@usnavyret.mil> wrote in message
    news:1pcqf3djt38u5ip8rj1t43k7hfh4qgkk6v@4ax.com...
    [quote]Anyone have any experience with these in a home network environment?

    Supposedly they will allow a mixed environment of some "B" and some "G"
    devices to operate at their designed speed instead of dropping back the
    entire network to the "B" capability.[/quote]""",
    """In wireless technology only one host can communicate with a WAP at a time.
    They have to take turns. So when it is "B's" turn to communicate it sends
    the packet,..because B is slower it takes more time for the Packet to
    complete the trip which causes the other to have to waite,...hence it slows
    down the WAP.

    The only thing I can think of is if the WAP has dual radios and uses two
    different channels so the B's can work over a different channel than the G's
    which might allow them to transceive at the same time or near the same time.
    You may still take some hit in performance.

    I don't know anything about the USRs but that is about the only thing I can
    think of that they might be doing,..and it is just a guess.

    -- 
    Phillip Windell
    http://www.wandtv.com

    The views expressed, are my own and not those of my employer, or Microsoft,
    or anyone else associated with me, including my cats.
    -----------------------------------------------------

    "Pegleg" <Pegleg@usnavyret.mil> wrote in message
    news:1pcqf3djt38u5ip8rj1t43k7hfh4qgkk6v@4ax.com...
    [quote]Anyone have any experience with these in a home network environment?

    Supposedly they will allow a mixed environment of some "B" and some "G"
    devices to operate at their designed speed instead of dropping back the
    entire network to the "B" capability.[/quote]""",
    """On Fri, 28 Sep 2007 14:07:01 -0400, "Jack \(MVP-Networking\)."
    <jack@discussiongroup.com> wrote:

    [quote]Client 802.11g cards are so inexpensive these day that there is No reason to
    compromise on buying mediocre Wireless devices.
    [/quote]
    I realize that however I use a PDA wirelessly that is only capable of
    ..11b. Both laptops we use are .11g. I have done some "unscientific"
    observations by watching the speed indicated on the laptops both before
    and after I get on the wireless network with my PDA and see no change.

    Of course I have no idea as to how accurate the speed indicator is in
    the XP(Home) system. With a .11g router I see anywhere from 18 Mbps to
    54 Mbps on the laptops depending on where I am in the house. Signing in
    with the .11b PDA seems to result in no changes.""",
    ]]),
    ('6.html', ["Disallow a wireless network",
    ["""Is there a way to disallow a wireless network connection? We've got a case
    where we have two wireless networks on campus - one is using WPA2 and we and
    the notebooks are setup to automatically connect - we aren't broadcasting the
    SSID. However - there is also an unsecured public wireless and the notebooks
    are connecting to that first and they never authenticate then against the
    other. If you reboot, and login again, then you can see the private network,
    disconnect the public and connect to the private, but needless to say this
    isn't a good option for the students. I'd like to set the notebooks to NEVER
    connect to the public wireless. is this possible? The notebooks are running
    XP w/sp2.""",
    """VickyS wrote:
    [quote]Is there a way to disallow a wireless network connection? We've got a case
    where we have two wireless networks on campus - one is using WPA2 and we and
    the notebooks are setup to automatically connect - we aren't broadcasting the
    SSID. However - there is also an unsecured public wireless and the notebooks
    are connecting to that first and they never authenticate then against the
    other. If you reboot, and login again, then you can see the private network,
    disconnect the public and connect to the private, but needless to say this
    isn't a good option for the students. I'd like to set the notebooks to NEVER
    connect to the public wireless. is this possible? The notebooks are running
    XP w/sp2.
    [/quote]
    Make sure that the "Automatically connect to non-preferred networks" box
    is not checked (from the "advanced" button -- not "advanced" tab -- of
    the "wireless network" tab of wireless network connection properties
    dialog). This is the default setting, and you are probably running into
    the problem that if a user EVER connects to this public network, Windows
    automatically adds it to the top of the list of preferred networks.

    Alternatively (I think this will work), configure the SSID of the public
    network with an encryption key. Because the network itself is
    unsecured, the configuration will not match and the users will therefore
    not connect to the public network. WZC should then find the
    non-broadcast secured network and connect to that.

    -- 
    Lem MS MVP -- Networking

    To the moon and back with 64 Kbits of RAM and 512 Kbits of ROM.
    http://en.wikipedia.org/wiki/Apollo_Guidance_Computer""",
    """Automatically connect to non-preferred is not checked and it is set to
    connect to access point (infrastructure) networks only, but I'll give your
    idea w/the SSIS a try.

    "Lem" wrote:

    [quote]VickyS wrote:
    Is there a way to disallow a wireless network connection? We've got a case
    where we have two wireless networks on campus - one is using WPA2 and we and
    the notebooks are setup to automatically connect - we aren't broadcasting the
    SSID. However - there is also an unsecured public wireless and the notebooks
    are connecting to that first and they never authenticate then against the
    other. If you reboot, and login again, then you can see the private network,
    disconnect the public and connect to the private, but needless to say this
    isn't a good option for the students. I'd like to set the notebooks to NEVER
    connect to the public wireless. is this possible? The notebooks are running
    XP w/sp2.

    Make sure that the "Automatically connect to non-preferred networks" box
    is not checked (from the "advanced" button -- not "advanced" tab -- of
    the "wireless network" tab of wireless network connection properties
    dialog). This is the default setting, and you are probably running into
    the problem that if a user EVER connects to this public network, Windows
    automatically adds it to the top of the list of preferred networks.

    Alternatively (I think this will work), configure the SSID of the public
    network with an encryption key. Because the network itself is
    unsecured, the configuration will not match and the users will therefore
    not connect to the public network. WZC should then find the
    non-broadcast secured network and connect to that.

    --
    Lem MS MVP -- Networking

    To the moon and back with 64 Kbits of RAM and 512 Kbits of ROM.
    http://en.wikipedia.org/wiki/Apollo_Guidance_Computer
    [/quote]""",
    """I'd encourage you to re-enable SSID broadcast of the WPA2 network. SSIDs
    aren't passwords, they're network names--so don't try to keep them secret.
    The XP client doesn't really like hidden SSIDs.

    http://www.microsoft.com/technet/techne ... fault.aspx
    describes why hiding an SSID does not make that network any more secure.

    http://technet.microsoft.com/en-us/libr ... 26942.aspx describes the
    general behavior of the XP and Vista clients.

    http://support.microsoft.com/kb/907405/ describes a hotfix you can get to
    work around a specific situation regarding reconnecting after manually
    disconnecting. But you're better off re-enabling SSID broadcast.

    -- 
    Steve Riley
    steve.riley@microsoft.com
    http://blogs.technet.com/steriley
    http://www.protectyourwindowsnetwork.com


    "VickyS" <VickyS@discussions.microsoft.com> wrote in message
    news:F919FDFC-7CC2-4785-AD1E-DDD859E79181@microsoft.com...
    [quote]Automatically connect to non-preferred is not checked and it is set to
    connect to access point (infrastructure) networks only, but I'll give your
    idea w/the SSIS a try.

    "Lem" wrote:

    VickyS wrote:
    Is there a way to disallow a wireless network connection? We've got a
    case
    where we have two wireless networks on campus - one is using WPA2 and
    we and
    the notebooks are setup to automatically connect - we aren't
    broadcasting the
    SSID. However - there is also an unsecured public wireless and the
    notebooks
    are connecting to that first and they never authenticate then against
    the
    other. If you reboot, and login again, then you can see the private
    network,
    disconnect the public and connect to the private, but needless to say
    this
    isn't a good option for the students. I'd like to set the notebooks to
    NEVER
    connect to the public wireless. is this possible? The notebooks are
    running
    XP w/sp2.

    Make sure that the "Automatically connect to non-preferred networks" box
    is not checked (from the "advanced" button -- not "advanced" tab -- of
    the "wireless network" tab of wireless network connection properties
    dialog). This is the default setting, and you are probably running into
    the problem that if a user EVER connects to this public network, Windows
    automatically adds it to the top of the list of preferred networks.

    Alternatively (I think this will work), configure the SSID of the public
    network with an encryption key. Because the network itself is
    unsecured, the configuration will not match and the users will therefore
    not connect to the public network. WZC should then find the
    non-broadcast secured network and connect to that.

    --
    Lem MS MVP -- Networking

    To the moon and back with 64 Kbits of RAM and 512 Kbits of ROM.
    http://en.wikipedia.org/wiki/Apollo_Guidance_Computer
    [/quote]""",
    """Hi
    By Not broadcasting the SSID you actually create a preference to the Network
    that does broadcast the SSID.
    Jack (MVP-Networking).

    "VickyS" <VickyS@discussions.microsoft.com> wrote in message
    news:F919FDFC-7CC2-4785-AD1E-DDD859E79181@microsoft.com...
    [quote]Automatically connect to non-preferred is not checked and it is set to
    connect to access point (infrastructure) networks only, but I'll give your
    idea w/the SSIS a try.

    "Lem" wrote:

    VickyS wrote:
    Is there a way to disallow a wireless network connection? We've got a
    case
    where we have two wireless networks on campus - one is using WPA2 and
    we and
    the notebooks are setup to automatically connect - we aren't
    broadcasting the
    SSID. However - there is also an unsecured public wireless and the
    notebooks
    are connecting to that first and they never authenticate then against
    the
    other. If you reboot, and login again, then you can see the private
    network,
    disconnect the public and connect to the private, but needless to say
    this
    isn't a good option for the students. I'd like to set the notebooks to
    NEVER
    connect to the public wireless. is this possible? The notebooks are
    running
    XP w/sp2.

    Make sure that the "Automatically connect to non-preferred networks" box
    is not checked (from the "advanced" button -- not "advanced" tab -- of
    the "wireless network" tab of wireless network connection properties
    dialog). This is the default setting, and you are probably running into
    the problem that if a user EVER connects to this public network, Windows
    automatically adds it to the top of the list of preferred networks.

    Alternatively (I think this will work), configure the SSID of the public
    network with an encryption key. Because the network itself is
    unsecured, the configuration will not match and the users will therefore
    not connect to the public network. WZC should then find the
    non-broadcast secured network and connect to that.

    --
    Lem MS MVP -- Networking

    To the moon and back with 64 Kbits of RAM and 512 Kbits of ROM.
    http://en.wikipedia.org/wiki/Apollo_Guidance_Computer
    [/quote]""",
    ]]),
]


model = [
    '/html/body/div/div[2]/h2/a',
    ['/html/body/div/div[2]/div[position()>2]/div/div/div'],
]
