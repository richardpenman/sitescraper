#!/usr/bin/python
# -*- coding: utf-8 -*-



data = [
    ('1.html', ["Wireless not finding any networks when other computers are able to - Tech Support Forum",
    ["""Hello again, network messiahs!

    So I just bought a new Sony Vaio laptop (Windows Vista) but it's unable to find my wireless router. The weird thing is however, the computer (running Windows XP) from which I am typing from right now is able to find the connection effortlessly.

    I have updated the wireless adapter to the latest version, ensured that the 'wireless' light is on (I have tried it 'off', too), made the routers connection *completely* unsecured (public... only temporarily until things are working), changed workgroup name, computer name... everything I can think of!

    Is it time I took my laptop back to the store to get it checked, or is there something else I can try?

    If there's any information I have neglected to provide, please let me know.

    Thanks computer gods!
    ~Luke""",
    """Turn off your firewall temporarily and see if that's the problem.

    Check Device Manager and make certain that you don't have a hardware problem.

    Check "Services" in Administrative Tools and make certain Windows Zero Configuration Service is running normally, or, if Vaios have their own configuration service, make certain it is running normally. -Note: Some premanufactured computers have their own configuration software for wireless connections, and I've found they go bad and it's very difficult to figure out why. It's easiest usually to just reinstall the software sometimes.

    -Also, there are a bunch of other Services that are necessary to connect wirelessly, and if any of them are not running, you won't connect. Have you (like me) gone through and turned off "unnecessary" services in order to speed up the computer ? I do this all the time, and sometimes turn off something critical.

    Check Networking and make certain your adapter appears and is not disabled or something.

    Is the Vaio new (and un-messed with) ? Or old, used and or possibly "messed-with". Did it EVER connect wirelessly ? If so, did something happen just before it went bad ? If so, what was it ?""",
    """Thanks for the quick and detailed response! You guys never fail to amaze me with how quick and useful the responses generally are.

    The laptop has only one Firewall which I know of and that's the 'Windows Firewall' suite that comes with Windows, and I did disable the firewall temporarily and attempt to search for nearby networks-- sadly, to no effect.

    Looking into the services menu, I see that the Windows Zero Configuration Service does not at all appear on the list. The Sony laptop does indeed come with its own configuration service, but the only options appear to be whether or not the wireless button should toggle a combination of Bluetooth and wireless. (Screenshot attached)

    Also in the attached screenshot appears to be a 'System Information' warning message which is making little sense to me because I remember at one point I used to have the option (which was un-selectable) to activate a 2.4ghz signal (5.0 however is the only available choice now)

    Regarding disabling other services, I have not tampered with them at all (unless new ones were added along with software I have installed on my laptop). I should note however that my current internet connection is a 'Mobile bandwidth' connection with a USB dongle and a software suite which manages connection.

    Could this be a problem? Is it worth attempting to uninstall the mobile bandwidth suite to see if wifi detects any networks?

    To check to see if my adapters are functioning correctly, I assume you mean to check the Device Manager to ensure the devices are enabled and not malfunctioning, to which I can only sadly report that they are (working correctly).

    Finally, the Vaio is brand new. I've only had it for a couple of months but am now switching my home internet connection to wireless, hence why this wasn't arranged sooner.

    Thanks again for the quick and helpful reply,
    ~Luke""",
    """Update: un-installing the Mobile broadband drivers and software did not help detect other networks, and installing the mobile broadband suite on my other computer has not compromised it's ability to locate networks at all, which has confused me even further

    ~Luke""",
    """Bumping... still looking for an answer. Thanks everyone!""",
    """Did you try reloading the wireless drivers for that machine? If you check the properties of the wireless adapter in Device Manager, are there any hints there as to why 2.4ghz capability disappeared?""",
    """Hi John.

    Thanks for your reply! Yes, the wireless drivers are all the latest versions from the manufacturers website, and the driver model was confirmed by a Sony driver diagnostic analysis tool.

    The 2.4ghz capability disappeared for an unknown reason, and since this has occurred roughly a month ago now, it is difficult to retrace any steps which may have caused the capability to disappear.

    Thanks again!
    ~Luke""",
    """I'm wondering if something is set in Device Manager to restrict 802.11g capability. Another cause may be the adapter has malfunctioned.""",
    """Hi John.

    This is new... one of my network adapters are reporting a problem, but I have no idea what it is...

    Next steps?

    Screenshot supplied.

    Thanks again!

    ~Luke""",
    """Hmm, that looks like Vista. Is that Vista ? Or an XP add-on?

    If so, that is a possible cause to keep in mind.

    First I'd uninstall the device, and let XP (?) find it again and reinstall the driver. That might fix it. Otherwise, you are going to have to figure out what it is and where to find the driver and install it manually.""",
    """Pardon the confusion. The operating system is indeed Vista. I have multiple computers, even though my 'main' computer uses XP. The laptop is not in my possession at the moment, but when it comes back to me I will try what you suggested and let you know how it turned out.

    Thanks again for your help!

    ~Luke""",
    """There is a school of thought that says that isn't a real issue. I've seen people run with that error, but many others see it and it stops them cold.

I'd first do this.


Disable the IP Helper service:

1. Hold the Windows key and type R, enter "services.msc" (without the quotes) and press Enter
2. Scroll down to the IP Helper service, right click on it and select Properties
3. In the dropdown box that says "Automatic" or "Manual", set it to Disabled and then click on "Apply"
4. Then click on "Stop" to stop the service from running in the current session
5. Click OK to exit the dialog



Disable IPv6:

1. Hold the Windows key and type R, enter "ncpa.cpl" (without the quotes) and press Enter
2. Right click on each network connection and select "Properties"
3. Remove the checkmark from the box next to "Internet Protocol Version 6 (TCP/IPv6)
4. Click OK to exit the dialog

NOTE: You should do this for each network connection.



Disable the DHCP Broadcast Flag:

Link: http://support.microsoft.com/default.aspx/kb/928233

   1. Hold the Windows key and type R, enter regedit and press Enter.
   2. Locate and then click the following registry subkey:
   3. HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{GUID}
   4. In this registry path, click the (GUID) subkey to be updated.
   5. If the key DhcpConnForceBroadcastFlag does not exist, use the Edit menu, point to New, and then click DWORD (32-bit) Value. In the New Value #1 box, type DhcpConnForceBroadcastFlag, and then press ENTER. If the key exists, skip this step.
   6. Right-click DhcpConnForceBroadcastFlag, and then click Modify.
   7. In the Value data box, type 0, and then click OK.
   8. Close Registry Editor.

NOTE: You should do this for each and every GUID subkey.
NOTE2: (GUID) is a mnemonic for the individual subkeys, the actual text "GUID" does not appear.




The only program I'm aware of that currently relies on IPv6 is the new Windows Meeting Space. The first 2 changes will cause that program not to work - but will leave all of your normal (IPv4) connections unaffected. If it causes problems that you can't overcome, simply revert back to the original settings.




Next, I'd uninstall the NIC drivers totally, reboot and install them again."""]
    ]),
    ('2.html', ["Keep Losing Internet Connection - Tech Support Forum",
    ["""Recently, I have been getting problems connecting my computer to the internet through my router. Sometimes, when I boot up the computer, there is no internet connection available. I would have to reboot my modem, router, and/or computer, and sometimes more than once, for it to work again. Even after I have got internet working again, it it would randomly cut off again after a period of time, where I would have to reboot the devices again, and repeat the cycle.

I have the computer connected directly to the router using an ethernet cable. My laptop, which connects wirelessly, picks up the internet connection perfectly, even while my computer is having problems. This leads me to believe it is possibly a configuration problem on the computer end. Does anyone have any ideas of what this problem could be?

BTW, my internet connection is a cable connection, and I'm using a Netgear WGT634U with the latest firmware, if that helps. I also am not using any firewalls, and only using antivirus and antimalware software.

Thanks""",
    """Forgot to mention that while I'm having problems connecting to the internet, I also have problems connecting to my router. These problems go away while the internet is working.""",
    """Since the laptop doesn't have an issue, I'd be starting at the wired connection.

Try a different port on the router, and a different cable to start.

Next, when you are experiencing the issue, please do the following steps.

Hold the Windows key and press R, then type devmgmt.msc

Please respond to all the following steps.

   1. Under Network adapters, please tell me all the devices listed.
   2. Are there any devices under Network adapters that have a red x displayed?
   3. Also, are there any devices anywhere in the Device Manager display with yellow ? or ! displayed?



I'd also like to see this.

Hold the Windows key and press R, then type CMD to open a command prompt:

In the command prompt window that opens, type type the following command:

Note that there is a space before the /ALL, but there is NOT a space after the / in the following command.

IPCONFIG /ALL

Right click in the command window and choose Select All, then hit Enter to copy the contents to the clipboard.
Paste the results in a message here.

If you are on a machine with no network connection, use a floppy, USB disk, or a CD-RW disk to transfer a text file with the information to allow pasting it here.""",
    """In the Device Manager, there is a red cross next to the inbuilt wireless adapter, which I disabled after the problem started to see whether that was causing it in some way. Apart from that though, everything else is good.

The IP configuration when all is working well is as follows, if it's of any use. Haven't had a problem for a while.

Windows IP Configuration

Host Name . . . . . . . . . . . . : 22ndstre-552b9b
Primary Dns Suffix . . . . . . . :
Node Type . . . . . . . . . . . . : Hybrid
IP Routing Enabled. . . . . . . . : No
WINS Proxy Enabled. . . . . . . . : No

Ethernet adapter Local Area Connection:

Connection-specific DNS Suffix . :
Description . . . . . . . . . . . : Marvell Yukon 88E8001/8003/8010 PCI
Gigabit Ethernet Controller
Physical Address. . . . . . . . . : 00-1A-92-21-D6-3B
Dhcp Enabled. . . . . . . . . . . : No
IP Address. . . . . . . . . . . . : 192.168.0.23
Subnet Mask . . . . . . . . . . . : 255.255.255.0
Default Gateway . . . . . . . . . : 192.168.0.1

Ethernet adapter Local Area Connection 2:

Connection-specific DNS Suffix . :
Description . . . . . . . . . . . : Marvell Yukon 88E8056 PCI-E Gigabit
Ethernet Controller
Physical Address. . . . . . . . . : 00-1A-92-21-E3-E2
Dhcp Enabled. . . . . . . . . . . : Yes
Autoconfiguration Enabled . . . . : Yes
IP Address. . . . . . . . . . . . : 192.168.1.2
Subnet Mask . . . . . . . . . . . : 255.255.255.0
Default Gateway . . . . . . . . . : 192.168.1.1
DHCP Server . . . . . . . . . . . : 192.168.1.1
DNS Servers . . . . . . . . . . . : 192.168.1.1
Primary WINS Server . . . . . . . : 192.168.1.1
Lease Obtained. . . . . . . . . . : 13 December 2008 21:54:27
Lease Expires . . . . . . . . . . : 20 December 2008 21:54:27""",
    """And here it is while I'm having the problem.. and it's identical:

Windows IP Configuration

Host Name . . . . . . . . . . . . : 22ndstre-552b9b
Primary Dns Suffix . . . . . . . :
Node Type . . . . . . . . . . . . : Hybrid
IP Routing Enabled. . . . . . . . : No
WINS Proxy Enabled. . . . . . . . : No

Ethernet adapter Local Area Connection:

Connection-specific DNS Suffix . :
Description . . . . . . . . . . . : Marvell Yukon 88E8001/8003/8010 PCI
Gigabit Ethernet Controller
Physical Address. . . . . . . . . : 00-1A-92-21-D6-3B
Dhcp Enabled. . . . . . . . . . . : No
IP Address. . . . . . . . . . . . : 192.168.0.23
Subnet Mask . . . . . . . . . . . : 255.255.255.0
Default Gateway . . . . . . . . . : 192.168.0.1

Ethernet adapter Local Area Connection 2:

Connection-specific DNS Suffix . :
Description . . . . . . . . . . . : Marvell Yukon 88E8056 PCI-E Gigabit
Ethernet Controller
Physical Address. . . . . . . . . : 00-1A-92-21-E3-E2
Dhcp Enabled. . . . . . . . . . . : Yes
Autoconfiguration Enabled . . . . : Yes
IP Address. . . . . . . . . . . . : 192.168.1.2
Subnet Mask . . . . . . . . . . . : 255.255.255.0
Default Gateway . . . . . . . . . : 192.168.1.1
DHCP Server . . . . . . . . . . . : 192.168.1.1
DNS Servers . . . . . . . . . . . : 192.168.1.1
Primary WINS Server . . . . . . . : 192.168.1.1
Lease Obtained. . . . . . . . . . : 14 December 2008 14:39:27
Lease Expires . . . . . . . . . . : 21 December 2008 14:39:27""",
    """When it fails, please do this.

Try these simple tests.

Hold the Windows key and press R, then type CMD (COMMAND for W98/WME) to open a command prompt:

In the command prompt window that opens, type type the following commands one at a time, followed by the Enter key:

IPCONFIG /ALL

PING <computer_IP_address>

PING <default_gateway_address>

PING <dns_servers>

PING 206.190.60.37

PING yahoo.com

Right click in the command window and choose Select All, then hit Enter to copy the contents to the clipboard.
Paste the results in a message here.

<computer_IP_address> - The IP Address of your computer, obtained from the IPCONFIG command above.

<default_gateway_address> - The IP address of the Default Gateway, obtained from the IPCONFIG command above.

<dns_servers> - The IP address of the first (or only) address for DNS Servers, obtained from the IPCONFIG command above.

If you are on a machine with no network connection, use a floppy, USB disk, or a CD-RW disk to transfer a text file with the information to allow pasting it here.""", 
    """C:\Documents and Settings\Owner>ping 86.18.185.121

Pinging 86.18.185.121 with 32 bytes of data:

Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 86.18.185.121:
Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),

C:\Documents and Settings\Owner>ping 192.168.1.1 (Note: This is the IP Address for both the Default Gateway and the DNS Servers)

Pinging 192.168.1.1 with 32 bytes of data:

Reply from 192.168.1.1: bytes=32 time<1ms TTL=64
Reply from 192.168.1.1: bytes=32 time<1ms TTL=64
Reply from 192.168.1.1: bytes=32 time<1ms TTL=64
Reply from 192.168.1.1: bytes=32 time<1ms TTL=64

Ping statistics for 192.168.1.1:
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
Minimum = 0ms, Maximum = 0ms, Average = 0ms

C:\Documents and Settings\Owner>ping 206.190.60.37

Pinging 206.190.60.37 with 32 bytes of data:

Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 206.190.60.37:
Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),

C:\Documents and Settings\Owner>ping yahoo.com

Pinging yahoo.com [206.190.60.37] with 32 bytes of data:

Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 206.190.60.37:
Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),""",
    """Where did you get the IP address of 86.18.185.121?

TCP/IP stack repair options for use with Windows XP with SP2/SP3.

Start, Run, CMD to open a command prompt:

In the command prompt window that opens, type type the following commands:

Note: Type only the text in bold for the following commands.

Reset TCP/IP stack to installation defaults, type: netsh int ip reset reset.log

Reset WINSOCK entries to installation defaults, type: netsh winsock reset catalog

Reboot the machine.""",
    """That would be my IP Address, which I got from http://whatismyip.com/

I tried those steps and rebooted, but am still having the same problems. The connection now keeps disconnecting around every 25-30 minutes for a period of around 15-20 minutes, after which it automatically reconnects. I don't have to reboot the router to get it to work.""",
    """This is only this computer, and other computers on the same router work fine?

Have you tried a different cable and a different port on the router?""",
    """Finally. Looks like it's working now. I switched the port on the router and rebooted. At first, there was no internet connection. Then I actually diabled the internet connection on the computer, and then reenabled. It then started working and without dropouts (so far, been like 4 hours).

Thanks John for all your help.""",
    """Hopefully, it was as simple as that."""]
    ]),
    ('3.html', ["[SOLVED] Major Internet Connection Issue - Tech Support Forum",
    ["""THE PREAMBLE
---------------
I feel so guilty posting such a potentially trivial problem here, but I've had a look around, and I haven't seen anything that might help me in my situation... and frankly, I don't know enough about this voodoo stuff to risk prodding about where I'm not wanted.
So, any help would be much appreciated!

THE BACKGROUND
------------------
I bought a new machine. An Acer Aspire X3200.. a pretty little thing, with 4GB RAM, a quad core Phenom processor. It also came with Vista pre-installed. At this point I don't want to get into the whole Vista vs XP debate... suffice it to say that I wanted XP on it.
Turns out that it wasn't as simple as putting the CD in the drive and asking it to do downgradey magic.

Ultimately, I made a new copy of XP, and stuffed some motherboard nvidia drivers on there also, which got around the BSOD issue, and subsequent to this, I've set it up nicely, and have installed appropriate gfx and sound drivers.

It's worth nothing at this point that no software/CDs were provided in the box.

THE PROBLEM
--------------
I now have this new shiny machine with no ability to connect to the internet. It tells me there is (virtually) no connection.

My network adaptor, which is an nvidia 10/100 thingy says it's working ok in Device Manager.

THE INFORMATION
-------------------

I'm using Windows XP 64.


Windows IP Configuration

Host Name . . . . . . . . . . . . : Omega
Primary Dns Suffix . . . . . . . :
Node Type . . . . . . . . . . . . : Unknown
IP Routing Enabled. . . . . . . . : No
WINS Proxy Enabled. . . . . . . . : No

Ethernet adapter Local Area Connection 2:

Connection-specific DNS Suffix . :
Description . . . . . . . . . . . : NVIDIA nForce 10/100/1000 Mbps Ethernet
Physical Address. . . . . . . . . : 00-1D-72-A9-7D-AC
DHCP Enabled. . . . . . . . . . . : Yes
Autoconfiguration Enabled . . . . : Yes
Autoconfiguration IP Address. . . : 169.254.138.235
Subnet Mask . . . . . . . . . . . : 255.255.0.0
Default Gateway . . . . . . . . . :

--------------------------------------------------------

I can't ping any domain names, IP addresses, etc.
I tried a "netsh winsock reset" without any noticeable change.

When trying to iipconfig /renew, I get;

Windows IP Configuration

An error occurred while renewing interface Local Area Connection 2 : unable to contact your DHCP server. Request has timed out.

---------------------------------------------------------

My laptop, which I'm currently using, has no such issues. I'm using the same cable modem and connections, so it's not a related hardware issue.


THE PRESTIGE
--------------

No prestige here... just begging... please please please please help get my new toy working! Thank you! :)
x""",
    """Must be a IP / DNS issue...
What are your DNS IP nos ? are they the same as your laptop's ?
You need to contact your ISP and ask them the IP addresses to use along with the preferred and alternate DNS server IP nos, if they do no provide them automatically.
Post a HijackThis report over here , pls check
http://www.techsupportforum.com/secu...oval-help.html
for instructions on using it.""",
    """TCP/IP stack repair options for use with Windows Vista.

Start, Programs\Accessories and right click on Command Prompt, select "Run as Administrator" to open a command prompt.

In the command prompt window that opens, type type the following commands:

Reset WINSOCK entries to installation defaults: netsh winsock reset catalog

Reset IPv4 TCP/IP stack to installation defaults. netsh int ipv4 reset reset.log

Reset IPv6 TCP/IP stack to installation defaults. netsh int ipv6 reset reset.log

Reboot the machine.



Check your Services are Started on all PCs:

    * COM+ Event System (for WZC issues)
    * Computer Browser
    * DHCP Client
    * DNS Client
    * Network Connections
    * Network Location Awareness
    * Remote Procedure Call (RPC)
    * Server
    * TCP/IP Netbios helper
    * Workstation


Note: You can check the services in Control Panel, Administrative Tools, Services.

All of these services should be started, and their startup type should be automatic (or perhaps manual).

If a service is not running, open it's properties and check the dependencies. Check each of the dependencies and see which one is preventing the service from running. Checking the event log is also a good idea here, there may be clues to what is failing.""",
    """Thank you all for the help and advice.

As it turns out, it just needed the modem to be reset.
I guess because the existing laptop already had whatever configuration it needed, that's the reason it had no problems, but the new machine did.

I'm posting from my new machine now! Woohoo!

Thanks again... :)

x""",
    """
Hi Grrr Power,
I saw your previous thread:
[SOLVED] Aspire x3200
and I am glad to hear you have your issues resolved.
Enjoy your "new" XP machine.
Thanks,
Bill"""]
    ]),
    ('4.html',
    ["Limited or No Connectivity - Tech Support Forum",
    ["""It's driving me insane, I've searched all over the net, tried every troubleshooting thing I've found and all to no avail.

I have two computers, an HP desktop and a Toshiba laptop. Both with Windows XP SP2. I'm using a Linksys Wireless G UBS adapter with the laptop. And a SpeedStream homenetworking modem from Bell Aliant

It will connect with no encryption.
Both IP's are in the trusted zone of Norton on both computers.
The workgroups are the same
They can ping each other and the router but not themselves

uh that's all I can think of that I've tried, I've probably done more. Anyway, if anyone has any help I'd be forever grateful.""",
    """This sounds like a classic Norton mis-configuration issue.

Did you try totally disabling Norton to see if they connect?""",
    """I think I've realized the problem, whenever I turn off my laptop and then turn it back on the wireless adapter changes the IP address (or maybe the router) anyway I'm getting in contant with my ISP for the DNS servers so I can see if setting up a static IP will work""",
    """I doubt your ISP will sort out local networking issues.""",
    """yeah your right, no help there.

So I disabled the firewall and the computers were able to ping themselves but even with the firewalls down I'm still getting the limited to no connectivity when I try to encrypt the network. I'm also not able to file or printer share.""",
    """If you can connect with encryption disabled, but can't connect with it enabled, we're closing in.

If you're using WEP, use ONLY the HEX key option and not the ASCII passphrase option."""]
    ]),
    ('5.html', ["Wireless, Laptop Help. - Tech Support Forum",
    ["""So here is my problem, I had to reboot my laptop beacuse It was at loading your personal details for 30 mins, I restarted 3-4 times so I rebooted. Wireless Internet was working before that when I rebooted but now it doesn't work obviously beacsue I rebooted, Router and cables are in place but I can't find find the Icon on which I can search for Internet connections in area.

Most likely problem is that I don't have wireless card Installed on this computer Which I am using, And if i also need it on my laptop?

So I installed the wireless card on this computer, I went to device managers to check and it isn't there? if there is a link you know with a wireless card drive for windows XP please post it here ^.^

I need to find another way to connect to Internet through laptop, using wireless.

I am using a 3com router, I have follwed some instructions using USB didn't work though. Please help me out. If you need any more details on my problem just post it.

Help would be greatly appreciated.""",
    """Bump.""",
    """Please supply the following info, exact make and models of the equipment please.

Name of your ISP (Internet Service Provider).
Make and exact model of the broadband modem.
Make and exact model and hardware version of the router (if a separate unit).
Model numbers can usually be obtained from the label on the device.
Connection type, wired or wireless.
If wireless, encryption used, (none, WEP, WPA, or WPA2)
Version and patch level of Windows on all affected machines, i.e. XP (Home or Pro), SP1-SP2-SP3, Vista (Home, Business, Ultimate), etc.
The Internet Browser in use, IE, Firefox, Opera, etc.




Please give an exact description of your problem symptoms, including the exact text of any error messages.


    * If you're using a wireless connection, have you tried a direct connection with a cable to see if that changes the symptoms?
    * For wireless issues, have you disabled all encryption on the router to see if you can connect that way?
    * Have you connected directly to the broadband modem to see if this is a router or modem/ISP issue?
    * If there are other computers on the same network, are they experiencing the same issue, or do they function normally?





On any affected computer, I'd also like to see this:

Hold the Windows key and press R, then type CMD (COMMAND for W98/WME) to open a command prompt:

Type the following commands on separate lines, following each one with the Enter key:

PING 206.190.60.37

PING yahoo.com

NBTSTAT -n

IPCONFIG /ALL

Right click in the command window and choose Select All, then hit Enter.
Paste the results in a message here.

If you are on a machine with no network connection, use a floppy, USB disk, or a CD-RW disk to transfer a text file with the information to allow pasting it here.""",
    """Edit: Its fine now, fixed the problem. I had to install the wireless driver on to the laptop, thanks for the help anyway. Just one more request please how do I block websites from popping up.""",
    """I'm not sure I understand the question about websites "popping up". How about some specifics?"""]
    ]),
    ('6.html', ["Computer Crashes whenever I'm connected to my wireless network! HELP! - Tech Support Forum",
    ["""I'm running Windows XP and connecting to our wireless router via a USB Stick. The problem is everytime I connect to the network and/or go online my computer freezes and I have to reset the comp, it may last for an hour before it happens, or sometimes even only 30 seconds. If I disable the network connection it's fine and never crashes, only when I'm connected.
I tried wiping my hard drive and doing a fresh install and it hasnt cured it. Any ideas? It only happens to my computer too , there are 3 on the network, one connected directly to the router upstairs and a laptop via a WiFi Card.
Help me techsupport forum...you're my only hope.""",
    """I'd consider the drivers for the wireless USB adapter. If updating the drives doesn't help, perhaps it's time to pick up a different adapter. I'd recommend a PCI or PCMCIA model, I find them a bit more stable than USB models.""",
    """Hi. I have a IBM thinkpad t30 with windows xp (with SP2). We just got Verizon FIOS toda installed at my house. My desktop is connected to the wireless router (actiontec MI424WR) by an ethernet cord. I haven't successfully connected to the internet via wireless by secure network on our router. My roommate has.
I have a Belkin Wireless Notebook Card (it says "802.11g 2.4 Ghz" on the card, and its model F5D7010). I haven't had any trouble connecting using this card (it goes into a PCMIA slot on the leftside of the laptop) at places like panera or the wirless at my dad's house.
When I try to connect to the secure wireless network,
a dialog box will pop up saying "Please wait wile Windows connects to "XXXXX" network" with a little green bar moving from left to right as its working saying "Detecting network type..." then the computer freezes, I can't reboot it via ctrl-alt-delete or move the cursor. So I have to hold down the power button to manually turn it off.
Already had the verizon tech support people remotely try stuff on my computer with the computer hooked up to the router via an ethernet cord. He suggested uninstalling and/or reinstalling the ethernet card. I've done that, same result as above. he also suggested getting a new notebook/network card. Since this thing has worked fine up until now, I'm open to trying anything before I get a new one. Can someone please help?
Thanks""",
    """I have the exact same problem as the user who posted this thread. The only difference is that I am using a PCI adapter (a netgear one).

I have reformatted my hard drive, and reinstalled the router and everything. I also upgraded to the latest firmware, but the problem continues to occur and my computer will freeze at random times ONLY when it is connected to the internet.

I noticed u suggested to buy a new adapter, but I just wanna know if there is anything else I could possibly try to fix this problem?

-Thank you very much""",
    """I also am having the same problem. I have updated to all new drivers and still get the BSOD whenever the network is turned on. Could a usb link be the problem? My computer has never experienced this before, I have always had a good wireless reception but never used a usb link.""",
    """All of you folks need to post your own individual threads with complete details of the issue if you want help. Tagging onto another post is NOT the way to get help.

I'm closing this thread."""]
    ]),
]


model = [
    '/html/head/title',
    ['/html/body/div/div[2]/div/div/div/div/table/tr[2]/td[2]/div[2]']
]
