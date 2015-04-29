#Deliverable 2 - Requirements Document
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

  1.2 [Scope of System](#12-scope-of-system)

  1.3 [Definition, Acronyms, and Abbreviations](#13-definition-acronyms-and-abbreviations)

  1.4 [Overview of Document](#14-overview-of-document)

2. [Current System](#2-current-system)

3. [Project Plan](#3-project-plan)

  3.1 [Project Organization](#31-project-organization)

  3.2 [Work Breakdown](#32-work-breakdown)

  3.3 [Cost Estimate](#33-cost-estimate)

4. [Proposed System Requirements](#4-proposed-system-requirements)

  4.1 [Functional Requirements](#41-functional-requirements)

  4.2 [Analysis of System Requirements](#42-analysis-of-system-requirements)

    4.2.1 [Scenarios](#421-scenarios)

    4.2.2 [Use Case Model](#422-use-case-model)

    4.2.3 [Static Model](#423-static-model)

    4.2.4 [Dynamic Model](#424-dynamic-model)

5. [Glossary](#5-glossary)

6. [Appendix](#6-appendix)

  6.1 [Appendix A](#61-appendix-a---complete-use-cases)

  6.2 [Appendix B](#62-appendix-b---use-case-diagram)

  6.3 [Appendix C](#63-appendix-c---static-uml-diagrams)

  6.4 [Appendix D](#64-appendix-d---dynamic-uml-diagrams)

  6.5 [Appendix E](#65-appendix-e---user-interface-designs)

  6.6 [Appendix F](#66-appendix-f---diary-of-meetings-and-tasks)

7. [References](#7-references)

-------

##1. Introduction

###1.1 Problem Definition

The software company Brighgauge would like a platform to test certain datasources. Namely they want the data to come back in a formatted way which would enable them to dive into the details and decide the viability of including that datasource on their platform.

###1.2 Scope of System

The scope of the system is limited for this semester. The main goal of the product owner is to enable data retrieval from the Trello API. As such, there is not outset intention to have the system integrate multiple APIs at this time. Care will be taken to design the system in such a way that will enable future APIs to be added in a simple manner, but those may come secondary to accomplishing the goal at hand.

###1.3 Definition, Acronyms, and Abbreviations

**SaaS**: Software-as-a-Service is defined as a software licensing model that is subscription based. It enables a user to have access to some business application that they can use for their own unique purposes.

###1.4 Overview of Document

This document goes on to discuss the current system in place that this project will be dealing with, chapter 2. After that, a project plan is layed out which breaksdown the work and costs associated with this project. Finally, chapter 4 introduces the functional requirements and shows an analysis of those requirements. The end of this document contains a glossary and appendices to aid in understanding the situation.

######[top](#deliverable-2---requirements-document)
-------

##2. Current System

As of right now there is now current system in place for this project. This is version zero and so is a foray into the possibility of this testing ground and the features it might contain. The company has its product which integrates data sources into a dashboard to allow users to create visualizations. This exploratory tool is an aid to that product.


######[top](#deliverable-2---requirements-document)
-------

##3. Project Plan

###3.1 Project Organization

Adam Merille will be responsible for everything for this first version. He will be writing all the documentation, creating all the diagrams and charts, setting up and creating the Django project and web app. He will also be writing the code for the api calls on the backend. He will be working on the frontend development, including HTML, CSS, and Javascript. He will be helping with the user interface design and responsible for managing the database. Lastly, he will also be writing the test cases to make sure the system functions as set out.

###3.2 Work Breakdown
Refer to [Appendix F](#66-appendix-f---diary-of-meetings-and-tasks) for diary of meetings and tasks.

Milestone | Description | Date
-----------|-------------|-----
1 | Feasibilty and Project Plan, Requirements Document | February 1
2 | Design Document | April 22
3 | Final Deliverable | April 30

###3.3 Cost Estimate

**Cost for website construction**

Criteria | Python
---------|-------
Infrastructure | $0
Development | $0
Operation | $0
Total | $0

**Cost for database**

Criteria | SQLite
---------|------
Infrastructure | $0 
Development | $0 
Operation | $0 
Total | $0 


The website is hosted on FIU servers, so that cost is assumed to be included in tuition and fees. Beyond the above technologies a personal laptop may be need (about $500 - 600 should suffice), although there are great computers in the School of Computing and Information Sciences lab. As for the labor, it is a student's joy to work for free now in the hopes of earning it back later.


######[top](#deliverable-2---requirements-document)
-------

##4. Proposed System Requirements

This chapter discusses the requirements asked for by the product owner and performs an analysis of those requirements. The chapter dives into the different scenarios that may arise and provides a use case model for the various requirements, as well as a set of sequence diagrams.

###4.1 Functional Requirements

* The system shall enable a user to add a datasource, namely via Trello.
* The system shall allow the user to add multiple accounts from the same resource.
* The system shall make a calls to get labels, get cards, get lists, get boards, and get members from Trello.
* The system shall clean the data before displaying the results in a table format.
* The system shall allow for specific filtering with the get cards request into getting the users cards, cards due in 7 days, and cards past due.
* The system shall secure the credential information in a storage format that requires password protection.

###4.2 Analysis of System Requirements

####4.2.1 Scenarios

####4.2.2 Use Case Model
![Image of Use Case Diagram](images/SILUseCaseDiagram.png?raw=true)

####4.2.3 Static Model
![Image of Trello Class Diagram](images/TrelloApiClassDiagram.jpg?raw=true)

####4.2.4 Dynamic Model
![Image of Get Data Source Sequence Diagram](images/GetDataSourceSequence.jpg?raw=true)

![Image of View Data Source Sequence Diagram](images/CreateDataSourceSequence.jpg?raw=true)

![Image of Get My Cards Sequence Diagram](images/FilterGetMyCards.jpg?raw=true)

![Image of Get Due in Seven Sequence Diagram](images/FilterGetDueinSevenCards.jpg?raw=true)

![Image of Get Past Due Sequence Diagram](images/FilterGetPastDueCards.jpg?raw=true)


######[top](#deliverable-2---requirements-document)
-------

##5. Glossary
**python**

**django**

**SaaS**: Software-as-a-Service is defined as a software licensing model that is subscription based. It enables a user to have access to some business application that they can use for their own unique purposes.


######[top](#deliverable-2---requirements-document)
-------

##6. Appendix

###6.1 Appendix A - Complete Use Cases	

**Title:** View Data Source

**Description:** After authentication, User has the ability to make API calls on that account in order to retrieve data (Card #110)

**Actor:** SaaS-Integration-Library User (SIL user) and third party API

**Preconditions:** Data source for API calls has been verified and SIL user is on API call page.

**Steps:** 

Step 1: User clicks link for an API call.

Step 2: System gets the Api model object for the call.

Step 3: System makes call to API behind the scenes, creating an API object to make the call.

Step 4: API returns data from call.

Step 5: System loads new page with data returned from API call.

**Postconditions:** User has been passed to a page containing the returned data from specific API call.
____


**Title:** Create Data Source

**Description:** After authentication, User has the ability to create a data source (Card #160)

**Actor:** SaaS-Integration-Library user (SIL user) and third party API

**Preconditions:** User has an account with third party and has navigated to Create Data Source page

**Steps:** 

Step 1: User clicks link for an API.

Step 2: System requests a token on the users behalf from the API.

Step 3: After user accepts SIL to have access to his/her account, system creates ApiCredential and Api object with token information.

Step 4: System redirects to confirmation page.

**Postconditions:** User has been passed to a page displaying successful creation.
____


**Title:** Get My Cards

**Description:** Filter to get cards only for user from the get_all_cards method (which returns all cards user can see)

**Actor:**  SaaS-Integration-Library user (SIL user)

**Preconditions:** The user has selected the call "Get all cards" from the dataset and is on the "Get all cards" page

**Steps:** 

Step 1: The user clicks the metric which says "My Cards"

Step 2: The system filters the cards

Step 3: The system reloads the table 

**Postconditions:** The table updates and displays only the cards associated with the user
____


**Title:** Get Due in Seven

**Description:** Filter to get cards that are due in seven days from the get_all_cards method (which returns all cards user can see)

**Actor:**  SaaS-Integration-Library user (SIL user)

**Preconditions:** The user has selected the call "Get all cards" from the dataset and is on the "Get all cards" page

**Steps:** 

Step 1: The user clicks the metric which says "Due in Seven"

Step 2: The system filters the cards

Step 3: The system reloads the table 

**Postconditions:** The table updates and displays only the cards due in seven days
____


**Title:** Get Past Due

**Description:** Filter to get cards which are past due from the get_all_cards method (which returns all cards user can see)

**Actor:**  SaaS-Integration-Library user (SIL user)

**Preconditions:** The user has selected the call "Get all cards" from the dataset and is on the "Get all cards" page

**Steps:** 

Step 1: The user clicks the metric which says "Past Due"

Step 2: The system filters the cards

Step 3: The system reloads the table 

**Postconditions:** The table updates and displays only the cards which are past due


###6.2 Appendix B - Use Case Diagram

![Image of Use Case Diagram](images/SILUseCaseDiagram.png?raw=true)

###6.3 Appendix C - Static UML Diagrams

![Image of Trello Class Diagram](images/TrelloApiClassDiagram.jpg?raw=true)

###6.4 Appendix D - Dynamic UML Diagrams

![Image of Get Data Source Sequence Diagram](images/GetDataSourceSequence.jpg?raw=true)

![Image of View Data Source Sequence Diagram](images/CreateDataSourceSequence.jpg?raw=true)

![Image of Get My Cards Sequence Diagram](images/FilterGetMyCards.jpg?raw=true)

![Image of Get Due in Seven Sequence Diagram](images/FilterGetDueinSevenCards.jpg?raw=true)

![Image of Get Past Due Sequence Diagram](images/FilterGetPastDueCards.jpg?raw=true)

###6.5 Appendix E - User Interface Designs

![Image of Index UI](images/IndexUI.png?raw=true)

![Image of Datasource UI](images/DatasourceUI.png?raw=true)

![Image of Datasets UI](images/DatasetsUI.png?raw=true)

![Image of Trello Calls UI](images/TrelloCallsUI.png?raw=true)

![Image of Get All Cards UI](images/GetAllCardsUI.png?raw=true)

![Image of Get All Boards UI](images/GetAllBoardsUI.png?raw=true)

![Image of Get My Cards UI](images/FilterMyCardsUI.png?raw=true)

###6.6 Appendix F - Diary of Meetings and Tasks
	
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


######[top](#deliverable-2---requirements-document)
-------

##7. References

* Draw IO: https://www.draw.io/ used for all diagrams.


######[top](#deliverable-2---requirements-document)
-------
