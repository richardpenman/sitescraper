#!/usr/bin/python
# -*- coding: utf-8 -*-


data = [
    ('1.html', ['DragonflyBSD',
    ["""Just wondering has anyone extensively used it before? Haven't read much about it since it seems to fly under the radar a lot but I'm quite interested in trying it, that and MidnightBSD. It uses pkgsrc so that's a plus for me, but I was just interested if there was someone, anyone who knows anything about it as I really can't seem to find much info on it other than the usual it split from FreeBSD became a fork etc etc""",
    """It's a great project that is definitely going places. Their pkgsrc implementation is a bit screwy, but it's still a fun project to play with. It isn't as stable [yet] as Net, Open, or FreeBSD.""",
    """Grab the LiveDVD they just announced and give it a whirl.
http://distrowatch.com/?newsid=05066""",
    """
Quote:
Originally Posted by Antman View Post
Grab the LiveDVD they just announced and give it a whirl.
http://distrowatch.com/?newsid=05066
That was exactly what I saw which prompted my curiosity . What the heck I'll try it out, downloading now...""",
    """Necromany :
Anyways I finally bothered to installed DragonflyBSD instead of just trying out the liveDVD and it was really cool. Probably what's most interesting is the HAMMER filesystem which I think has a ton of potential. For those who don't know what it is http://www.dragonflybsd.org/hammer/hammer.pdf kinda long and probably dry and boring to most people but oh well . Anyways was just wondering if anybody else has tried DragonflyBSD recently along with the HAMMER filesystem and what their thoughts were about it.""",
    """HAMMER is amazing. It's really made for systems with massive hard drives, but it's still cool.""",
    """From now on I think I'm just going to change the title of all my BSD related threads to "cardinals_fan what's your opinion on <insert BSD topic>""",
    """HAMMER is fascinating.
Check out this article comparing it with Sun's ZFS.
Follow it up with some small corrections made by DragonFlyBSD's Matt Dillon."""],
    ["C!oud", "cardinals_fan", "Antman", "C!oud", "C!oud", "cardinals_fan"],
    ["September 2nd, 2008", "September 3rd, 2008", "September 3rd, 2008", "September 3rd, 2008", "December 11th, 2008", "December 11th, 2008", "December 11th, 2008", "December 12th, 2008"],
    ]),
    ('2.html', ['[SOLVED] unable to browse windows shares',
    ["""I have several windows shares setup on my XP computer. I am able to connect to all of them except for one using nautilus' browse network option. I will post the specifics and answer any questions of the issue once i get home. I just thought it was strange that I am able to connect to a browse 2 other shared directories on the same computer.""",
    """im sure you've done this, but on the one you cant see, have you allowed all other computers to see it, as far as windows firewall or router is concerned?""",
    """Yes I have they are all setup the same. I have set my windows firewall to allow access to my 3 shared folders across the network. The only thing i can see being an issue is that the share is in My Documents under my another user's profile but I have admin access to the computer. It is making me pull my hair out right now.""",
    """can you connect using the IP address and share name of the windows computer?

ie smb://192.168.x.x/sharename""",
    """Hi BDN

I think I might see your problem, then again maybe not.

Having it under another user name is not the problem, but do you have it under the SAME GROUP NAME?????

Even if you don't, it should be visible under Windows Network!

One other thing Places/Network does NOT always work right in Ubuntu. Sometimes you have to go up to GO/Location and type in the IP number of the machine for it to show all the shares.

However, since you said other shares on that same machine are showing up, I would go back to the Windows machine and double check everything again. I've shared folders nested some 8 levels deep stored in documents and settings/my documents with no problem. Even password protected and hidden folders to at one time.

On trick you may try is to UNSHARE the folder and then SHARE it again. I've had to do that many times as they somehow just got lost in the shuffle.

Good Luck

TTUL
Gary""",
    """I don't think you guys understand. I can see the folder but when i try and open it I get an error something like it is not accessible. I will post the exact error when i get home. So it will not let me browse into the folder and see the contents. but it is displayed. I have 2 other shares on the same computer and they work fine.

I have tried unsharing and resharing the folder on the windows PC and still get the same results. I don't understand what is wrong with that folder. I copied all the data to a backup drive and created a new share and that works. I still want to fix this issue since i will only update the data on the backup drive every once in a while.

halitech, I will try connecting to the IP address and share name and see if that enables me to access the folder.""",
    """As a test only make sure that the "Everyone" group has full permissions. Then try to access the folder, if this works you will need to make sure that your group settings are correct.""",
    """The exact error that i get is: "Unable to mount location. Failed to mount windows share.""",
    """Thank you so much. This worked perfectly, I don't know why i did not see this before. "Everyone" wasn't listed and it was for the other shares that I had setup.

Quote:
Originally Posted by foofighterjim View Post
As a test only make sure that the "Everyone" group has full permissions. Then try to access the folder, if this works you will need to make sure that your group settings are correct."""],
    ["BDNiner", "taseedorf", "BDNiner", "halitech", "Kellemora", "BDNiner", "foofighterjim", "BDNiner", "BDNiner"],
    ["December 9th, 2008", "December 10th, 2008", "December 11th, 2008", "December 11th, 2008", "December 11th, 2008", "December 12th, 2008"],
    ]),
    ('3.html', ['Request for Pear-ody theme', 
    ["""Hello,

I am hoping that someone has the pear-ody theme and would be able to send it to me.

The links no longer work on the themes page nor does google provide a working link.

My system crashed and I though I had a copy of he archive but I did not.

So if anyone has a copy I would love to get it again, all other themes cut of the fonts and look horrible.

Thanks""",
    """I have it. PM me and I'll send it to you on Tues or Wed. (I have the HD widescreen one, hopefully that is the one you need)

I'm not sure what files are needed, it's been almost a year since I installed it. I don't remember it being that hard to install though.

I haven't gotten around to fixing the MythVideo part yet. Maybe I'll try to get that done soon. I want to have it display the movie posters and have a blue box around the one that is selected. They should have made it just like the View Recordings page is like with the list up top and the movie poster and info on the bottom, but I'll have to have a lot of free time before I can look into changing that.



I need to think about backing up my system it looks like.
""",
    """Thanks. That is exactly the one that I was looking for. I have PM'ed you. Thanks a tonne.

Yeah backing up a system is good. I backup everything but never thought of the theme.""",
    """http://rapidshare.de/files/41117495/...-Wide.zip.html

Sorry it took so long, the computers were conspiring against me. Actually I can't remember how to make zip files in Linux and my internet connection isn't the most reliable.

If other people haven't tried this theme, I would recommend it. I've been using it for the past 10 months, and except for a few things I still need to correct in MythVideo, it looks really good.

I'll try and fix MythVideo this weekend and upload a new file.""",
    """Awesome! Looking great again. Thanks a tonne.

Kyfehr"""],
    ["kyfehr", "Caps18", "kyfehr", "Caps18", "kyfehr", "Caps18", "petit_prince"],
    ["December 7th, 2008", "December 8th, 2008", "December 8th, 2008", "December 12th, 2008", "December 12th, 2008", "December 15th, 2008", "January 25th, 2009"],
    ]),
    ('4.html', ['Newbie needs network help!!!',
    ["""Hey guys
I am a total newbie not long had 'intrepid' working and I am trying to linkup my laptop (XP) to share files and an internet connection.

i.s.p. is virgin cable

I have a wired router

two network ports....one that the internet goes into.

the ways I think it works is:-

cable from unused network port into router, then from router to lap top?

or should it be virgin modem to router then router to desktop and laptop?

From there I have no idea how to configure it all!

any advice or tutorials anybody knows of would be a great help

Thanks
lewbram is offline      Reply With Quote""",
    """The sharing of file with XP you will need to install samba,
Your router should provide the internet connection to your xp and linux boxes should get the IP address from there""",
    """Sounds like you need to change the IP address of your second router.

Not familiar with the Virgin cable setup but does the PC work connected directly to the virgin box ? If yes, then you should cable from the virgin box to your router then two cables from the new router to each pc.

Before you hook up the virgin to router connection connect your pc to the new router, power on and browse to http://192.168.1.1 Hopefully there should be a config page to change the address of the new router. Change it to something like 192.168.2.1 and save. For ease, power everything down, connect virgin to new router, restart everything and you should be good to go.

If not, then post more details about your hardware.""",
    """Thanks guys I have an exam now, will give it a go and get back to you tonight.

Thanks again""",
    """Hey I have tried this but nothing happens when i browse
http://192.168.1.1

The current situation is

desktop (ubuntu)
laptop (XP)

internet going into router, from router toboth desktop and laptop

can anybody help?

Thanks""",  
    """Hi Lew

The IP to get into your router might be different than what was given to try. It was just a common one used on many brands.

Ok, from your Virgin Cable the wire that comes into the house should be connected to your Modem.

Without using the Router, connect one of your PC's to the Modem to see if your Account is activated. If not, you will have to call your cable company to have then turn you on as a subscriber.

Once you KNOW the internet is active and working, THEN place the Router between the Modem and your computer. Most Routers are already defaulted to the proper settings and pass set-up through to your Network configuration when started.

Once you have one computer going, just plugging in the second computer to your router should get that one going also. Internet Networking comes set up already in Ubuntu.

If all else fails, place your LIVE CD with Ubuntu on it in your CD player and reboot the computer and run it from the LIVE CD, it should Automatically connect to the internet.

You can go into your System/Administration/Network and write down the numbers you see listed under DNS.

Then remove the CD and reboot.
Go back to System/Administration/Network and check what it shows there, if different you will have to change it to what is correct. It shouldn't be different though!

If it is come back and someone will ask for you to paste a couple of printouts.

TTUL
Gary"""],
    ["lewbram", "ibizatunes", "ianhaycox", "lewbram", "lewbram", "Kellemora", "lewbram"],
    ["December 12th, 2008", "December 12th, 2008", "December 13th, 2008"],
    ]),
    ('5.html', ["Couldn't a time-based login prevent brute force attacks?",
    ["""I've often read that strong passwords are good. I understand that weak ones (dictionary phrases) are easy to crack.

Please keep in mind that I don't know that much about technical details of things. I am not a programmer. So in your explanations and corrections, talk to me as if I'm a moron.

How difficult would it be to make logins time-based?

In other words, for a remote login, making it so that after the first and second failed attempts to log in to a particular account, you'd have to wait 5 seconds to log in for that particular account, and then after the third failed attempt, you'd have to wait an extra 10 seconds and so on. If there were ten failed attempts coming from the same source, that source would no longer be able to log in for the next 24 hours, and even if that source tried to log in with a correct username and password, it would be denied.

Is this not implemented because it would be difficult to identify a source? Even so, forcing at least a 5-second delay would significantly increase the time it would take for an automated program to go through every single possible dictionary word.

I think I've seen time-based logins before (I forget in what context). Why aren't they more common? And why wouldn't they then make dictionary-word passwords more secure than they currently are?""",
    """At my highschool, if you put in the wrong password 5 times it blocks your account. I would assume most systems would have something like that.""",
    """I don't know how hard that would be to implement (I'm not a programmer myself). But, it surprises me that something like that isn't already implemented. It's an extremely good idea.

My friend's iPhone had a feature like that. If you locked the screen with a 4-digit PIN and then got the PIN incorrect around 3 times or so, it wouldn't let you unlock for about 5 minutes. Then if you got it incorrect again, it would be locked for 15 minutes. Incorrect after that, then it would be around 30 minutes, then an hour. Turning it off and on again didn't remove the penalty. It was pretty frustrating to my friend to not be able to use the phone for 15 minutes but it's a good security measure.

The thought that if you couldn't login for 24 hours, even with the correct username and password is also something I like because if someone guessed the correct password, they may not know that it would work.

I hope someone gets a chance to implement this, if it isn't already available yet.""",
    """Well, yes, it would work, but not if they boot a livecd.

Edit: Kind of like how the club thing works for cars, so long as the guy trying to steal the car doesn't have a spare wheel to put on."""],
    ["aysiu", "DOS4dinner", "thegreatbitbucket", "bobbob1016", "will1911a1", "aysiu", "binbash", "Jammanuser", "happysmileman"],
    ["December 12th, 2008", "December 12th, 2008"],
    ]),
    ('6.html', ['where to find online interpreters',
    ["""Hello!

I have head that there are some sites on the web that you can use to program in python (or java), as if it were a installed interpreter!

does anybody know where i can find one of these sites? thank you!""",
    """Python: http://try-python.mired.org/""",
    """thank you very much!]

yay! now i can learn python while at school!""",
    """
Quote:
Originally Posted by hyperhopper View Post
yay! now i can learn python while at school!
If your school has Windows boxes you can use, you can put Portable Python on a USB flash drive.""",
    """ummmm just to let ya know, my schools windows computers have a STRONG security system.

only authorized programs are allowed to be executed, NOTEPAD.exe is unusable, along with the default calculator and ANY program that I were to install myself. the command prompt is disabled.

EDIT: just tried the online interpreter at school, and it didnt work, (the only browser allowed is IE and it seems to be blocking the script)


the school encourages me to try to break this protection, (they made me the dedicated System operator becuase i have found 3 MAJOR flaws in the system before)

so any way to do this would be appreciated!""",
    """
Quote:
Originally Posted by hyperhopper View Post
only authorized programs are allowed to be executed, NOTEPAD.exe is unusable, along with the default calculator and ANY program that I were to install myself. the command prompt is disabled.
Sounds like overkill to me. Can you boot from CD or USB?""",
    """
Quote:
Originally Posted by mdebusk View Post
Sounds like overkill to me. Can you boot from CD or USB?
thats where the school draws my line.

im free INSIDE windows, but if they see bios or grub, i get an afterschool detention

so the answer is no......


(its overkill because i got the SYS admin yelled at when i found the medical records. heeheheh)"""],
    ["hyperhopper", "rjack", "hyperhopper", "mdebusk"],
    ["December 11th, 2008", "December 12th, 2008", "December 13th, 2008"],
    ]),
]


model = [
    '/html/body/div/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table/tr[2]/td[2]/div/strong[1]',
    ['/html/body/div/div[3]/div/div/div/div/div/div/div/div/table/tr[2]/td[2]/div[2]'],
    ['/html/body/div/div[3]/div/div/div/div/div/div/div/div/table/tr[2]/td[1]/div[1]/a[1]'],
    ['/html/body/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tr[1]/td[1]'],
]
