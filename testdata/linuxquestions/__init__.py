#!/usr/bin/python
# -*- coding: utf-8 -*-


data = [
    ('1.html', ['gstreamer/amarok',
    """i just installed amarok and whenever i start it it says please select gstreamer output plugin but gstreamer is not an option for output plugings for me, but i do have gstreamer installed.""",
    ["""
    Quote:
    Originally posted by doralsoral
    i just installed amarok and whenever i start it it says please select gstreamer output plugin but gstreamer is not an option for output plugings for me, but i do have gstreamer installed.
    You may have to install gstreamer plugins. I would just ditch gstreamer for xine. Amarok can use the xine engine and thus play more media types.
    """,
    """gstreamer-plugins are already installed.""",
    """
    Quote:
    Originally posted by doralsoral
    gstreamer-plugins are already installed.
    So did you try using xine as the output plugin? Some distros have extra gstreamer plugins (not packaged with gstreamer-plugins), so also take a look into that.""",
    """Which version of gstreamer are you using? I think I ran into a similar problem and ended up downgrading to version 0.8.6 you might try that."""],
    ["doralsoral", "reddazz", "doralsoral", "reddazz", "Backstander"],
    ["10-30-2005, 02:12 PM", "10-30-2005, 03:09 PM", "10-30-2005, 03:48 PM", "10-30-2005, 09:39 PM"],
]),
    ('2.html', ['webmin/apache',
    """i have a problem...im on slackware 9 using webmin 1.100...but heres the problem..im trying to setup a virtual server so when sombody browses my site...example: something.mydomain.com it takes them to whatever i got the document root set to..but i cant get rid of the default for sum reason...if anybody can tell me how to get rid of the default virtual server i would really appreciate it...the default looks like this..therefore any address i put on my box...it auto takes em to the default virtual server which i dont want...

    Address Any
    Port Any
    Server Name myservername
    Document Root /home/artistik/public_html/

    i need to find a way to delete this offa webmin but it wont let me...""",
    ["""
    Quote:
    Originally posted by artistik
    i need to find a way to delete this offa webmin but it wont let me...
    What you should do if you're unhappy with what webmin does, is edit your /etc/apache/httpd.conf by hand, remove these entries, and put in your documentroot or whatever as you want.""",
    """well i did do that...i want so when ppl browse my web adress it takes em to what the document root says....but when i setup a virual server ie: something.mydomain.com and i got that set to a diff documentroot it still goes to the main document root...because webmin has the default virtual server set to any address...and i cant find a way to delete the default server on webmin =p"""],
    ["artistik", "andrewlkho", "artistik", "andrewlkho"],
    ["08-17-2003, 07:07 PM", "08-17-2003, 11:58 PM", "08-18-2003, 01:35 PM"],
]),
    ('3.html', ['mutt/fetchmail',
    """Hi,
    I've been trying to use my gmail from CLI.
    Here's my .fetchmailrc

    Code:

    poll pop.gmail.com with proto POP3 and options no dns
    user 'username@gmail.com' is 'username' here options ssl

    Obviously username is replaced with the real one. Also, POP is enabled in my gmail settings (I've been using thunderbird for a while)


    Here's my .muttrc
    Code:

    set pop_user="username@gmail.com"

    # My email account password
    set pop_pass="my password"

    # Too many email headers make reading a message difficult
    ignore *
    unignore From: To: Cc: Subject: Date: #Only these are shown in the header

    #To ensure that mutt does not put
    #'username@localhost.localdomain in From
    set from="username@gmail.com"
    set use_from=yes
    set envelope_from="yes"

    #The text editor I want to use to write emails
    #The default is emacs
    set editor="emacs -nw"


    the output of fetchmail -vk

    Code:

    sycamorex@debian205:~$ fetchmail -vk
    Enter password for username@gmail.com@pop.gmail.com: 
    fetchmail: 6.3.8 querying pop.gmail.com (protocol POP3) at Sun 23 Dec 2007 14:42:05 GMT: poll started
    Trying to connect to 66.2bla...bla..bla09/995...connected.
    fetchmail: Issuer Organisation: Equifax
    fetchmail: Unknown Issuer CommonName
    fetchmail: Server CommonName: pop.gmail.com
    fetchmail: pop.gmail.com key fingerprint: 44:A8:E9:2C:FB.....bla bla..blaB2:9E:F1:A9
    fetchmail: Server certificate verification error: unable to get local issuer certificate
    fetchmail: Server certificate verification error: certificate not trusted
    fetchmail: Server certificate verification error: unable to verify the first certificate
    fetchmail: POP3< +OK Gpop ready for requests from 83.4.bla... bla..blao24pf3879126ugd.0
    fetchmail: POP3> CAPA
    fetchmail: POP3< +OK Capability list follows
    fetchmail: POP3< USER
    fetchmail: POP3< RESP-CODES
    fetchmail: POP3< EXPIRE 0
    fetchmail: POP3< LOGIN-DELAY 300
    fetchmail: POP3< X-GOOGLE-VERHOEVEN
    fetchmail: POP3< UIDL
    fetchmail: POP3< .
    fetchmail: POP3> USER username@gmail.com
    fetchmail: POP3< +OK send PASS
    fetchmail: POP3> PASS *
    fetchmail: POP3< +OK Welcome.
    fetchmail: POP3> STAT
    fetchmail: POP3< +OK 0 0
    fetchmail: No mail for hemarcin@gmail.com at pop.gmail.com
    fetchmail: POP3> QUIT
    fetchmail: POP3< +OK Farewell.
    fetchmail: 6.3.8 querying pop.gmail.com (protocol POP3) at Sun 23 Dec 2007 14:42:07 GMT: poll completed
    fetchmail: normal termination, status 1

    when I open mutt and want to write an email - it says that email has been sent but then when I want to check it on my other email account nothing has been delivered.

    can you give me any hint. I'm working with mutt, fetchmail for the first time.

    thanks
    """,
    ["""Well, that's because you maybe just configured GETTING your mail, but not SENDING your mail?

    POP and fetchmail are about getting your mail from your POP/IMAP-account.

    Mutt is just your tool to compose the mail (your mail user agent) - now you need something to get it out there.

    In your case of using gmail it possibly involves relaying over gmail - which is possible.

    I use msmtp to send mail out after composing it in mutt. Msmtp is small and very simple - I don't need an entire sendmail on my notebook just to send out 50 mails a day.

    From within mutt, this would be something like this in your muttrc:

    set sendmail="/usr/local/bin/msmtp"

    And my msmtprc says for gmail-relaying something like this:

    account default
    host smtp.gmail.com
    port 587
    user YOU@gmail.com
    password PASSWORD
    protocol smtp
    tls_starttls on
    logfile /home/MYHOME/.msmtp.log

    This is totally independent from your POP-fetchmail-setting.""",
    """thanks, makes sense

    However, what I get in Mutt when I try to send an email is:

    Quote:
    msmtp: envelope from address YOU@gmail.com not accepted by the server
    msmtp: server message: 530 5.7.0 Must issue a STARTTLS command first k5sm707424nfh.18
    msmtp: could not send mail (account default from /home/sycamorex/.msmtprc)
    Quote:
    Error sending message, child exited 65 (Data format error.).
    and the log entry from .msmtp.log

    Quote:
    Dec 23 16:10:12 host=smtp.gmail.com tls=off auth=off from=YOU@gmail.com recipients=SOMEBODY@gmail.com smtpstatus=530 smtpmsg='530 5.7.0 Must issue a STARTTLS command first k5sm707424nfh.18' errormsg='envelope from address YOU@gmail.com not accepted by the server' exitcode=EX_DATAERR
    my .msmtprc

    Quote:
    account default
    host smtp.gmail.com
    port 587
    user YOU@gmail.com
    password blablabal
    protocol smtp
    tls_starttls on
    logfile /home/sycamorex/Mail/.msmtp.log
    thanks"""],
    ["sycamorex", "Su-Shee", "sycamorex", "andrew.46"],
    ["12-23-2007, 08:50 AM", "12-23-2007, 09:32 AM", "12-23-2007, 10:13 AM", "12-27-2007, 05:08 AM"],
]),
    ('4.html', ['XGL / Compiz',
    """Hi. I use fluxbox as my window manager under Ubuntu, and recently I have been hearing a lot about XGL and Compiz. I know Compiz is a window manager, so I can't get the neat effects with fluxbox. I was wondering, however, if Compiz can run stand alone, without having to load a window environment. Is this possible? If so, how would I go about doing this? Thanks.""",
    ["""You run xgl and compiz with gnome or kde.""",
    """So there is no ability to run compiz in stand-alone? Are there any other xgl window managers that support this that you know of?""",
    """Hi, After posting this I did some more research, and it turns out that you need a 'Desktop Environment', rather than a 'window manager' in order to use it. You can use KDE, Gnome, or XFCE since they are Desktop Environments. You can't use it with fluxbox or other plain window managers.""",
    """
    Quote:
    Originally Posted by Blazeix
    Hi, After posting this I did some more research, and it turns out that you need a 'Desktop Environment', rather than a 'window manager' in order to use it. You can use KDE, Gnome, or XFCE since they are Desktop Environments. You can't use it with fluxbox or other plain window managers.
    What is you are using gdm (or kdm i guess) with fluxbox on top of it?"""],
    ["Blazeix", "Caeda", "shamgar03", "Blazeix", "rjerina"],
    ["08-23-2006, 11:00 AM", "08-28-2006, 09:14 PM", "11-01-2006, 11:11 PM", "11-01-2006, 11:32 PM"],
]),
    ('5.html', ['Andrew - Australia',
    """Just wondering the topic of enson vs Cpanel, can someone clear up which one is better and the major differences please?""",
    ["""
    Quote:
    Originally posted by clacy
    Just wondering the topic of enson vs Cpanel, can someone clear up which one is better and the major differences please?
    Okay first of all, what does your Title of this thread have to do with your question?

    And secondly, this question is not a question in regards to this site itself, which the forum you placed it in was made for. I've requested to have this thread moved to a more appropiate forum and I'd like to ask you make better thread titles in the future.""",
    """Moved: This thread is more suitable in Linux - Software and has been moved accordingly to help your thread/question get the exposure it deserves.

    --jeremy"""],
    ["clacy", "trickykid", "jeremy"],
    ["06-24-2005, 09:32 AM", "06-24-2005, 09:35 AM", "06-24-2005, 09:44 AM"],
]),
    ('6.html', ['Dreamweaver Mock?',
    """Is there any software on linux that can kind of mock or be better than Macromedia's Dreamweaver, I want to be able to do a website with the capability of changing form design view to code view and for it to do the html for you because that is just a waist of time. If anyone knows something similar please tell me. Thanks.

    -luis""",
    ["""have you given bluefish a try?""",
    """is there any others?""",
    """Originally posted by lramos85
    is there any others?
    There is also Quanta and Screem that I know of but nothing in comparison as these are really true WYSIWYG editors. Your not going to have the "view page" type function with these.

    It is possible to just load Dreamweaver using wine.

    www.frankscorner.org"""],
    ["lramos85", "timdsmith", "lramos85", "trickykid"],
    ["12-11-2003, 06:56 PM", "12-11-2003, 07:08 PM", "01-05-2004, 06:34 PM"],
]),
]
   

model = [
    '/html/body/div/div/div/table/tr/td/table/tr/td/table/tr[2]/td/strong',
    '/html/body/div/div/div/table/tr/td/div[2]/div/div/div/div/div/table/tr[2]/td[2]/div[3]',
    ['/html/body/div/div/div/table/tr/td/div[2]/div/div[position()>1]/div/div/div/table/tr[2]/td[2]/div'],
    ['/html/body/div[1]/div/div/table/tr[1]/td[1]/div/div/div/div/div/div[1]/table/tr/td[1]/div[1]/a[1]'],
    ['/html/body/div[1]/div/div/table/tr[1]/td[1]/div/div/div/div/div/div[1]/table/tr[1]/td[1]'],
]