#Deliverable 1 - Feasibility Study and Project Plan
#####Senior Project CIS 4911
#####SaaS Integration Library
#####Adam Merille
#####Professor Masoud Sadjadi




######Copyright :copyright: SaaS Integration Library Team 

-------

##Abstract
The following feasibility study and project plan is an outline for what the intention of this project is. The feasibility study walks through the possible solutions, judging criteria, and decisions on which solutions seem a best fit. The project plan points out who will be doing what for the project, as well as a timeline, and any requirements in order to develop the project.

-------

##Table of Contents
1. [Introduction](#1-introduction)

  1.1 [Problem Definition](#11-problem-definition)

  1.2 [Background](#12-background)

  1.3 [Definition, Acronyms, and Abbreviations](#13-definition-acronyms-and-abbreviations)

  1.4 [Overview of Document](#14-overview-of-document)

2. [Feasibility Study](#2-feasibility-study)

  2.1 [Description of Current System](#21-description-of-current-system)

  2.2 [Purpose of New System](#22-purpose-of-new-system)

  2.3 [High-Level User Requirements](#23-high-level-user-requirements)

  2.4 [Alternative Solutions](#24-alternative-solutions)

    2.4.1 [Description of Alternatives](#241-desription-of-alternatives)

    2.4.2 [Selection Criteria](#242-selection-criteria)

    2.4.3 [Analysis of Alternatives](#243-analysis-of-alternatives)

  2.5 [Recommendations](#25-recommendations)

3. [Project Plan](#3-project-plan)

  3.1 [Project Organization](#31-project-organization)

    3.1.1 [Project Personnel Organization](#311-project-personnel-organization)

    3.1.2 [Hardware and Software Resources](#312-hardware-and-software-resources)

  3.2 [Identification of Tasks, Milestones, and Deliverables](#32-identification-of-tasks-milestones-and-deliverables)

4. [Appendix](#4-appendix)

  4.1 [Appendix A - Project Schedule](#41-appendix-a---project-schedule)

  4.2 [Appendix B - Feasibility Matrix](#42-appendix-b---feasibility-matrix)

  4.3 [Appendix C - Cost Matrix](#43-appendix-c---cost-matrix)

  4.4 [Appendix D - Diary of Meetings](#44-appendix-d---diary-of-meetings)

5. [References](#5-references)


-------

##1. Introduction

###1.1 Problem Definition

The software company Brighgauge would like a platform to test certain datasources. Namely they want the data to come back in a formatted way which would enable them to dive into the details and decide the viability of including that datasource on their platform.

###1.2 Background

Brightgauge is a company that builds business intelligence solutions for IT Service Providers and Managed Service Providers. Essentially they enable data sources to be linked to a dashboard which allows the users to then create visualization of of that data that can be updated in real time. The Software-as-a-Service Integration Library (SaaS Integegration Library) is an exploratory tool for them to see how they might integrate new datasources as well as test possible new features of data display visualizations.

###1.3 Definition, Acronyms, and Abbreviations
    
**SaaS**: Software-as-a-Service is defined as a software licensing model that is subscription based. It enables a user to have access to some business application that they can use for their own unique purposes.

###1.4 Overview of Document

This document gives a big picture view of the viability and purpose of the system as well as the plan to complete the project. The following section discusses the feasibility of the project, including user requirements and alernative solutions. After that, in section 3, the project organization is discussed in terms of a timeline and deliverables to be accomplished.

######[top](#deliverable-1---feasibility-study-and-project-plan)
-------

##2. Feasibility Study

###2.1 Description of Current System

As of right now there is now current system in place for this project. This is version zero and so is a foray into the possibility of this testing ground and the features it might contain. 

###2.2 Purpose of New System

This new system will allow the company, Brightgauge, to judge whether a data source that might be used by their clients, or future clients, is a viable addition to their product. The big picture is to see what data can be retrieved and if that data would enable the clients to make better decisions or to see how they stand in the current environment.

###2.3 High-Level User Requirements

* The system shall enable a user to add a datasource, namely via Trello.
* The system shall allow the user to add multiple accounts from the same resource.
* The system shall make a calls to get labels, get cards, get lists, get boards, and get members from Trello.
* The system shall clean the data before displaying the results in a table format.
* The system shall allow for specific filtering with the get cards request into getting the users cards, cards due in 7 days, and cards past due.
* The system shall secure the credential information in a storage format that requires password protection.

###2.4 Alternative Solutions

####2.4.1 Description of Alternatives

Alternatives for website construction:

  1. Java
  2. PHP
  3. Python

Alternatives for databases:

  1. PostgreSQL
  2. MySQL
  3. SQLite

####2.4.2 Selection Criteria
The web construction alternatives will be judged according to:

* Speed to get going
  * How long does it take to get website up and running?
  * How many different resources are needed to get it up and running?
  * Is the process straighforward?

* Teammate knowledge 
  * How much of the language does the team know?
  * Does that knowledge extend to using the language for web application creation?
  * How long would it take to get up to speed?

* Frameworks 
  * Does the language have frameworks that will help speed the process up?
  * Does the language have libraries that make the process easier?
  * How difficult is it take to use the framework?
  
* Resources
  * How many avenues to get help does this language offer?
  * Does the language have good documentation references?
  * Can we leverage other people's knowledge of the language?

The database altervatives will be judged according to:

* Security 
  * Is there a secure way to access the data?
  * Does the data storage allow for hashing?
  * Does the data storage come with security installed or are there third party alternatives?

* Reliability 
  * Is it easy to retrieve and store the data?
  * Is it easy to create redundancy with this data storage?
  * Does the data storage have a low mean time to failure?
  
* Integrationalability 
  * Will the data storage work with any of the languages out of the box?
  * How much work is needed to access the data storage within the lanaguage?
  * Is there a trade off for ease of use vs functionality?
  
* Resources 
  * How many avenues to get help/learn does the data storage offer?
  * Does the data storage mechanism have good documentation?
  * Have we used or know anyone who has used the data storage mechanism?

####2.4.3 Analysis of Alternatives
Refer to [Appendix B](#42-appendix-b---feasibility-matrix) for the feasibility matrix which contains scoring.

**Website Construction Analysis:**

* Java

Pros | Cons
-----|-----
Lots of experience | Little experience with Java websites
Lots of resouces | Will probably have to build certain things
Highly scalable for web | 

* PHP

Pros | Cons
-----|-----
Probably tons of examples | Very little experience
Lots of resources | Extremely verbose
 | Slightly steeper learning curve

* Python

Pros | Cons
-----|-----
Experience with language | Little experience building website with Python
Django gets going fast | Generally considered not highly scalable
Shallow learning curve | 
Easy to follow tutorials |

**Database Analysis:**

* PostgreSQL

Pros | Cons
-----|-----
Strong Community | Performance can be slow
Lots of third-party support | Not as popular 
Stored procedures extensible |

* MySQL

Pros | Cons
-----|-----
Many third party tools | Reliability issues
Many Features | Integration with some languages might be difficult
High security |
Scalable |
Fast |

* SQLite

Pros | Cons
-----|-----
File based | Limited abilities
Easy to develop with | No user management
Comes preloaded with Django |

###2.5 Recommendations

Based on the above analysis and through discussion with members of Brightgauge there is a certain path that is being recommended. For the web application construction the choice is Python using the Django framework. For the database, PostgreSQL would like to be used but SQLite will be utilized for this first version.

Python with Django has been chosen due to its ease of use, team familiarity, and shallow learning curve. It will enable the project to move forward quickly without getting stuck on the details of the website. 

SQLite was mainly chosen because it comes built into Django. Support for PostgreSQL is available for Django but requires some set up. The way Django works changing the database later on will not affect the current code as writing and reading are handled by the framework rather than by the programmer through his/her development code.



######[top](#deliverable-1---feasibility-study-and-project-plan)
-------

##3. Project Plan

###3.1 Project Organization

####3.1.1 Project Personnel Organization

Adam Merille will be responsible for everything for this first version. He will be writing all the documentation, creating all the diagrams and charts, setting up and creating the Django project and web app. He will also be writing the code for the api calls on the backend. He will be working on the frontend development, including HTML, CSS, and Javascript. He will be helping with the user interface design and responsible for managing the database. Lastly, he will also be writing the test cases to make sure the system functions as set out.

####3.1.2 Hardware and Software Resources

The following is neccessary to the development of this project:

**Hardware:**
* Machine for hosting, provided by FIU
* Personal computer with at least 2.0 GHz processor
* 4 GB of RAM
* At least 4 GB of free hard disk space

**Software:**
* Linux or Mac Operating System
* PyCharm or similar IDE
* Python 2.7
* Django 1.7 
* Text Editor (OpenOffice, Gedit, etc.)

###3.2 Identification of Tasks, Milestones, and Deliverables
Milestone | Description | Date
-----------|-------------|-----
1 | Feasibilty and Project Plan, Requirements Document | February 1
2 | Design Document | April 22
3 | Final Deliverable | April 30


######[top](#deliverable-1---feasibility-study-and-project-plan)
-------

##4. Appendix

###4.1 Appendix A - Project Schedule

####4.1.1 Spring 2015 Gantt Chart

Part 1:
![Image of First Half of Gantt Chart](images/Gantt1-10.png?raw=true)

Part 2:
![Image of First Half of Gantt Chart](images/Gantt10-18.png?raw=true)

###4.2 Appendix B - Feasibility Matrix
Maximum points possible for a given criteria is 5.

####4.2.1 Feasiblity Matrix for website construction

Criteria | Java | PHP | Python
---------|------|-----|-------
Speed to get going | Websites abound, but a little weighty **3** | Highly verbose, still a standard **2**  | Usually considered a get-up-and-go type **4**
Teammate knowledge | General knowledge, but research needed for creating website in Java **3** | Limited knowledge, lots of research probably needed **2**  | Less knowledge than Java, but easy to pick up (teamat brightgauge has knowledge) **3**
Frameworks | Probably very useful libraries **3** | Not sure, expect some libraries **3** | Experience with flask, team uses Django **4**
Resources | Tons **3** | Tons **3** | Not as many as others, still has tutorials **3**
Total points | **12** | **10** | **14** :star:


####4.2.2 Feasiblity Matrix for database choice

Criteria | PostgreSQL | MySQL | SQLite
---------|------|-----|-------
Security | Standard **3**| Advanced **4** | Standard **3**
Reliability | Standard, a little slow **3** | Has some funcionality issues **2** | Database is single file makes it easily portable **4**
Integrationalability | Not quite as popular, has integration with Django **3** | Most popular and used almost everywhere **4** | Comes preloaded with Django for python **5**
Resources | Strong community **3** | Lots **4** | Probably some **2**
Total points | **12** | **14** | **14** :star: (Due to Django integration)

###4.3 Appendix C - Cost Matrix

####4.3.1 Cost Matrix for website construction
Website is hosted on FIU servers.

Criteria | Java | PHP | Python
---------|------|-----|-------
Infrastructure | $0 | $0 | $0
Development | $0 | $0 | $0
Operation | $0 | $0 | $0
Total | $0 | $0 | $0

####4.3.1 Cost Matrix for website construction

Criteria | PostgreSQL | MySQL | SQLite
---------|------|-----|-------
Infrastructure | $0 | $0 | $0
Development | $0 | $0 | $0
Operation | $0 | $0 | $0
Total | $0 | $0 | $0

###4.4 Appendix D - Diary of Meetings

**Diary Entry** - January 22 2015

**Location:** BrightGauge

**Start time:** 10:00 AM

**End time:** 11:30 AM

**In attendance:** Adam, Brian, Orlando, Steve

**Agenda:** Product introduction, User stories discussion, why this product

**Summary of discussion:** Discussed use cases pertaining to SaaS Integration Library, particularly Trello data source retrieval by means of authentication and API calls.

**Assigned tasks:** Adam - Research Trello API, begin working on documentation and Mingle set up
____


**Diary Entry** - January 29 2015

**Location:** BrightGauge

**Start time:** 10:00 AM

**End time:** 11:30 AM

**In attendance:** Adam, Brian, Orlando, Steve

**Agenda:** Go over possible architecture, user interface envisioned by product owner

**Summary of discussion:** Mapped out basic data management system, user interface design, git branching

**Assigned tasks:** Adam - Continue documentation, learn about Django	
____


**Diary Entry** - February 12,  2015

**Location:** BrightGauge

**Start time:** 3:30 PM

**End time:** 4:00 PM

**In attendance:** Adam, Brian, Orlando, Steve

**Agenda:** Sprint Review

**Summary of discussion:** 
User Stories:
	attribute/fields list
	high level view without data
	Highcharts

Next time:
	more code reviews
	demo at end of sprint

**Assigned tasks:** Adam - 
	--variables in init
	--no camel case
	--format strings
	--requests.get takes params
	--checks inside of get all cards
	try, except
	move KEY to Settings
____


**Diary Entry** - February 25,  2015

**Location:** BrightGauge

**Start time:** 3:30 PM

**End time:** 4:00 PM

**In attendance:** Adam, Brian, Orlando, Steve

**Agenda:** Sprint Review

**Summary of discussion:** shortcut to render_to_response, check newer docs called render()

__iexact() case insensitive searching

views - apicall - just delete query no need to check

no need to change response to json, keep as data obj

python mock library

get list of items to pass to template, then get keys() and then loop through to get items()

**Assigned tasks:** Adam - above recommendations in addition to assigned user stories
____


**Diary Entry** - March 19,  2015

**Location:** BrightGauge

**Start time:** 3:30 PM

**End time:** 4:00 PM

**In attendance:** Adam, Brian, Orlando, Steve

**Agenda:** Sprint Review

**Summary of discussion:** discussed sprint review and job offer

**Assigned tasks:** Adam - 
Overflow hidden css element
Use oauth for Trello
send javascript issues to Orlando and work on fixing
____


**Diary Entry** - April 2,  2015

**Location:** BrightGauge

**Start time:** 3:30 PM

**End time:** 4:00 PM

**In attendance:** Adam, Brian, Orlando, Steve

**Agenda:** Sprint Review

**Summary of discussion:** discussed sprint review

**Assigned tasks:** Adam - Footer, move css to dedicated folder, rm footer line, Datatables js,  grab labels out of all calls (e.g. get all cards, get lists)
____


**Diary Entry** - April 16,  2015

**Location:** BrightGauge

**Start time:** 3:30 PM

**End time:** 4:00 PM

**In attendance:** Adam, Brian, Orlando, Steve

**Agenda:** Sprint Review

**Summary of discussion:** discussed sprint review

**Assigned tasks:** Adam - work on dynamic spacing of divs for metrics on get all cards page


######[top](#deliverable-1---feasibility-study-and-project-plan)
-------

##5. References

* Draw IO: https://www.draw.io/ used for all diagrams except gantt.

* Tom's Planner: http://www.tomsplanner.com/ used for gantt chart creation


######[top](#deliverable-1---feasibility-study-and-project-plan)
