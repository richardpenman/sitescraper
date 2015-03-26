#!/usr/bin/python
# -*- coding: utf-8 -*-

data = [
    ('1.html', ["What is the most succinct way that you would define the key roles within software development?",
["""


I am looking for a plain English explanation of what skills and qualities define each major role within software development (for example, what differentiates between the Junior Developer, Developer and Senior Developer), as well as descriptions that highlight the nuances between various roles that to the 'business' appear to be similar (for example, Technical Architect vs Software Architect vs Solution Architect vs Network Architect vs Lead Architect).

The answer would ideally highlight the most common roles that exist in software development teams as well as provide a definition that allows people to recognise their role and see what they would need to work on to progress with their chosen career path.

""",
"""
I would break down the question by skill Sets.

    *

          Program Manager. This is the person with oversight to the program. What are the analysts, architects, and developers doing. A really good program manager takes care of all of the excess, so that the computer people can do their computer things. The good program managers that I work with spend a lot of time taking care of all of those tedious emails and phone calls so that developers don't have to worry about that interference.
              *

                    Business Analyst. This person is a hybrid, someone who has a fundamental understanding of programming (doesn't have to be an expert) and can really understand people and their problems. Has the ability to translate a real-world problem into a programmable solution. This can be one of the most difficult skills to find, since you need someone who can (a) talk to the customer in their language without (b) becoming a salesman. A good business analyst can solve problems by determining the workflow of an application, understands edge cases, and can design a functional requirements document that software architects will understand.
                        *

                              Software Architect. This person designs the program, specifically the library and class diagram requirements. What does the program actually do? In interface-based programming, this is the person designing the public interfaces that objects expose. The design of the class libraries from the software architect may not be method/property complete (some methods may be missing) but it should be functionally complete.
                                  *

                                        Developer/Programmer. Fills in the gaps left by the software architect. If the architect is the framer, then it is the developer who adds the wiring, plumbing, and drywall. A developer is not necessarily lower level. Just because an architect says, "We need a method to perform function 'X'", it does necessarily mean that performing function 'X' is easy.
                                            *

                                                  Most business programs will be about data, and if yours involves a server, then you'll want a database architect. The DBA does more that just create the table. A good DBA knows all of the little intricacies (like the differences between clustered or nonclustered indexes, and such minutiae) that make a program go from working to working fast.

                                                  Software design is not always top-to-bottom. At the interviews I been in, the paths seems to be very linear. Developer, then architect, then analyst, then program manager. But I really like being an architect. Even though the Analysts get paid more (and the Program Managers get paid more still), I don't think that I would like those positions. At my company, they aren't coders any longer. Analysts do participate in GUI/Web design, though, since that can have a direct effect on the the workflow and business requirements. But they don't write the "guts".

                                                  Hope this helps.

""",
"""
Junior Developer - can write code given low level design, can debug his/her own work. Senior Developer - can write code given low level design, understands high level design, can do code review, can troubleshoot issues that junior developers are facing, has more experience

Team Lead - is good at understanding functional requirements, is good at understanding high level design, is good and creating low level design, is good at tracking work progress, is good at assigning tasks, is good and seeing the broad picture, is good at client handling

These were my quick outputs. Will need to add more to these.

""",
"""
Let's first define software development as going through the life cycle of requirements gathering, design and analysis, implementation, testing, deployment and maintenance so here is an elaboration on each:

Requirements gathering - This is where the "what" part of the software is determined as in finding out what is needed. Usually this involves talking to non-technical people and converting their requests into technical documentation known as a specification or spec. Business analysts are usually the role that handles this aspect of a project.

Design and analysis - This is where a plan is put forth as to what to do. Architects, business analysts and developers can all be involved here as this is where that specification is refined enough to be put into actual software.

Implementation - This is where the developers write the code to produce the requested software.

Testing - This is where what was done is verified to see that it was in fact done.

Deployment and maintenance - This is where the software is pushed out into the wild in a sense. Systems administrators are typically responsible for keeping an eye on the servers in the case of a web roll out though in other cases there may be techincal support people that get to see the software to handle any incoming calls.

Those are the major parts as I know them with a project manager to keep an eye on the project, a team lead which is usually one of the developers to be the person that any technical squabble can be resolved such as developers putting the finger at each other when there is a bug when their code is integrated, and sometimes someone from the business that is requesting the work may also play a role.

Junior/Intermediate/Senior - These will vary considerably as a Senior .Net developer may not have decades of experience that a COBOL or assembler programmer may have.

Architects are sometimes used though at my last job there wasn't such a position, just developers that took requirements from the CTO or CEO and wrote the software and had a tester who also deployed it.

Another point is to be aware of different methodologies that exist in software development like the traditional Waterfall where things are done one stage at a time and in order with no backtracking over several months, that is what is requested initially is what gets done without any changes or updated, compared to Agile where the requirements may change weekly and this is accomodated.

Application / Systems / Web - these are usually nearly the same thing these days as my last title was Senior Application Developer and the company was an Application Service Provider though more typically I say that I am a Web Developer. Systems tends to refer to working with an Operating System or something close to the O/S like configuring IIS or MS-SQL Servers for performance.

Administrators are those that run things and this could be networks, systems or databases. If you have other jargon in mind I think that should be viewed as a separate question as this answer is pretty long already I think.

JB
"""]
]),
    ('2.html', ["Can I get more than 1000 records from a DirectorySearcher in Asp.Net?",
["""

I just noticed that the return list for results is limited to 1000. I have more than 1000 groups in my domain (HUGE domain). How can I get more than 1000 records? Can I start at a later record? Can I cut it up into multiple searches?

Here is my query:

DirectoryEntry dirEnt = new DirectoryEntry("LDAP://dhuba1kwtn004");
string[] loadProps = new string[] { "cn", "samaccountname", "name", "distinguishedname" };
DirectorySearcher srch = new DirectorySearcher(dirEnt, "(objectClass=Group)", loadProps);
var results = srch.FindAll();

I have tried to set srch.SizeLimit = 2000; but that doesn't seem to work. Any ideas?

""",
"""You need to set DirectorySearcher.PageSize to a non-zero value to get all results.

BTW you should also dispose DirectorySearcher when you're finished with it

using(DirectorySearcher srch = new DirectorySearcher(dirEnt, "(objectClass=Group)", loadProps))
{
    srch.PageSize = 1000;
        var results = srch.FindAll();
        }

        The API documentation isn't very clear, but essentially:

            *

                  when you do a paged search, the SizeLimit is ignored, and all matching results are returned as you iterate through the results returned by FindAll. Results will be retrieved from the server a page at a time. I chose the value of 1000 above, but you can use a smaller value if preferred. The tradeoff is: using a small PageSize will return each page of results faster, but will require more frequent calls to the server when iterating over a large number of results.
                      *

                            by default the search isn't paged (PageSize = 0). In this case up to SizeLimit results is returned.

                            As Biri pointed out, it's important to dispose the SearchResultCollection returned by FindAll, otherwise you may have a memory leak as described in the Remarks section of the MSDN documentation for DirectorySearcher.FindAll: http://msdn.microsoft.com/en-us/library/system.directoryservices.directorysearcher.findall.aspx

                            One way to help avoid this in .NET 2.0 or later is to write a wrapper method that automatically disposes the SearchResultCollection. This might look something like the following (or could be an extension method in .NET 3.5):

                            public IEnumerable<SearchResult> SafeFindAll(DirectorySearcher searcher)
                            {
                                using(SearchResultCollection results = searcher.FindAll())
                                    {
                                            foreach (SearchResult result in searchResults)
                                                    {
                                                                yield return result;        
                                                                        } // SearchResultCollection will be disposed here
                                                                            }
                                                                            }

                                                                            You could then use this as follows:

                                                                            using(DirectorySearcher srch = new DirectorySearcher(dirEnt, "(objectClass=Group)", loadProps))
                                                                            {
                                                                                srch.PageSize = 1000;
                                                                                    var results = SafeFindAll(srch);

""",
"""@naspinski: I also replied on your comment on your previous post.

Not only dispose DirectorySearcher, but also dispose the SearchResultCollection as well. It is using some unmanaged resources.
"""]
]),
    ('3.html', ["What is the best way to check the strength of a password?",
["""

What is the best way of ensuring that a user supplied password is a strong password in a registration or change password form?

EDIT: one idea I had (in python)

def validate_password(passwd):
    conditions_met = 0
        conditions_total = 3
            if len(passwd) >= 6: 
                    if passwd.lower() != passwd: conditions_met += 1
                            if len([x for x in passwd if x.isdigit()]) > 0: conditions_met += 1
                                    if len([x for x in passwd if not x.isalnum()]) > 0: conditions_met += 1
                                        result = False
                                            print conditions_met
                                                if conditions_met >= 2: result = True
                                                    return result


""",
"""Depending on the language, I usually use regular expressions to check if it has:

    * At least one uppercase and one lowercase letter
        * At least one number
            * At least one special character
                * A length of at least six characters

                You can require all of the above, or use a strength meter type of script. For my strength meter, if the password has the right length, it is evaluated as follows:

                    * One condition met: weak password
                        * Two conditions met: medium password
                            * All conditions met: strong password

                            You can adjust the above to meet your needs.

""",
"""
http://webtecker.com/2008/03/26/collection-of-password-strength-scripts/
""",
"""
The two simplest metrics to check for are:

   1. Length. I'd say 8 characters as a minimum.
      2. Number of different character classes the password contains. These are usually, lowercase letters, uppercase letters, numbers and punctuation and other symbols. A strong password will contain characters from at least three of these classes; if you force a number or other non-alphabetic character you significantly reduce the effectiveness of dictionary attacks.
""",
"""
I like using Microsoft's password checker
""",
"""
If you have the time, run a password cracker against it.
"""]
]),
    ('4.html', ["Application Level Replication Technologies",
["""

I am building out a solution that will be deployed in multiple data centers in multiple regions around the world, with each data center having a replicated copy of data actively updated in each region. I will have a combination of multiple databases and file systems in each data center, the state of which must be kept consistent (within a data center). These multiple repositories will be fronted by a SOA service tier.

I can tolerate some latency in the replication, and need to allow for regions to be off-line, and then catch up later.

Given the multiple back end repositories of data, I can't easily rely on independent replication solutions for each one to maintain a consistent state. I am thus lead to implementing replication at the application layer -- by replicating the SOA requests in some manner. I'll need to make sure that replication loops don't occur, and that last writer conditions are sorted out correctly.

In your experience, what is the best pattern for solving this problem, and are there good products (free or otherwise) that should be investigated?

""",
"""Lotus/ Domino is your answer. I've been working with it for ten years and its exactly what you need. It may not be trendy (a perception that I would challenge) but its powerful, adaptable and very secure, The latest version R8 is the best yet.
""",
"""You dont give enough specifics to be certain of your needs but I think you should check out SQL Server Merge replication. It allows for asynchronous replication of multiple databases with full conflict resolution. You will need to designate a Global master and all the other databases will replicate to that one, but all the database instances are fully functional (read/write) and so you can schedule replication at whatever intervals suit you. If any region goes offline they can catch up later with no issues - if the master goes offline everyone will work independantly until replication can resume.

I would be interested to know of other solutions this flexible (apart from Lotus Notes/Domino of course which is not very trendy these days).

"""]
]),
    ('5.html', ["What is your bug/task tracking tool (FAQ)",
["""

This is a placeholder to bug/task tracking system overview.

What i want to do here is :
1) List all tools used in the industry.(please provide a link to the tool discussed).
2) Gather ppl opinion on each tool.(Please back up your opinion with facts i.e provide advantages and disadvantages).

Cross-links to another posts:
What is your tool for version control (FAQ)
Free/Cheap Task/Bug Management software
What bug tracking software do you use?

Please put each tool in separate answer and please make it community owned wiki to give an option to add/edit to as many ppl as possible.

""",
"""Trac (http://trac.edgewall.org/)

It's sleek, fast, free and has subversion integration.

""",
"""FogBugz

I'm not just sucking up to Joel, it realy does rock.

"""]
]),
    ('6.html', ["Automatically select all text on focus in WinForms TextBox",
["""

When a C# WinForms text box receives focus, I want to select all the text in the textbox.

To see what I mean, click in your web browser's address bar. See how all text was selected? I want to do that.

FASTEST GUN ALERT: please read the following before answering! Thanks guys. :-)

    Calling .SelectAll() during the .Enter or .GotFocus events won't work because if the user clicked the textbox, the caret will be placed where he clicked, thus deselecting all text.

        Also, calling .SelectAll() during the .Click event won't work because the user won't be able to select any text with the mouse; the .SelectAll() call will keep overwriting the user's text selection. )


""",
"""Click event of textbox? Or even MouseCaptureChanged event works for me. - OK. doesn't work.

So you have to do 2 things:

private bool f = false;

private void textBox_MouseClick(object sender, MouseEventArgs e)
{ 
  if (this.f) { this.textBox.SelectAll(); }
    this.f = false;
    }

    private void textBox_Enter(object sender, EventArgs e)
    {
      this.f = true;
        this.textBox.SelectAll();
        }
        private void textBox_MouseMove(object sender, MouseEventArgs e) // idea from the other answer
        {
          this.f = false; 
          }

          Works for tabbing (through textBoxes to the one) as well - call SelectAll() in Enter just in case...

""",
"""If you overload the Click event you can use .SelectAll() and all text will be selected.
"""]
]),
]


model = [
    '/html/body/div/div[2]/div/h2/a',
    ["/html[1]/body[1]/div[@class='container']/div[@id='content']/div[@id='mainbar']/div[@id='answers']/div[position()>1]/table[1]/tr[1]/td[2]/div[@class='post-text']"]
]
