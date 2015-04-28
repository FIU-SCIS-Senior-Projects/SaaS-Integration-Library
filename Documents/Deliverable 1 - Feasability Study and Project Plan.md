#Deliverable 1 - Feasibility Study and Project Plan
#####Senior Project CIS 4911
#####SaaS Integration Library
#####Adam Merille
#####Professor Masoud Sadjadi




######Copyright :copyright: SaaS Integration Library Team 

-------

##Abstract


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

Refer to appendices [B](#42-appendix-b---feasibility-matrix) and [C](#43-appendix-c---cost-matrix) for the feasibility and cost matrices respectively.

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

####2.4.3 Analysis of Alternatives

###2.5 Recommendations


######[top](#deliverable-1---feasibility-study-and-project-plan)
-------

##3. Project Plan

###3.1 Project Organization

####3.1.1 Project Personnel Organization

####3.1.2 Hardware and Software Resources

###3.2 Identification of Tasks, Milestones, and Deliverables


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
