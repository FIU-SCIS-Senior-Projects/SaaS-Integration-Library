#Deliverable 3 - Design Document
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

  1.2 [Design Methodology](#12-design-methodology)

  1.3 [Definition, Acronyms, and Abbreviations](#13-definition-acronyms-and-abbreviations)

  1.4 [Overview of Document](#14-overview-of-document)

2. [System Design](#2-system-design)
  
   2.1 [Overview](#21-overview)
  
   2.2 [Subsystem Decomposition](#22-subsystem-decomposition)

   2.3 [Hardware and Software Mapping](#23-hardware-and-software-mapping)

   2.4 [Persistent Data Management](#24-persistent-data-management)
  
   2.5 [Security and Privacy](#25-security-and-privacy)

3. [Detailed Design](#3-detailed-design)

  3.1 [Overview](#31-overview)

  3.2 [Static Model](#32-static-model)

  3.3 [Dynamic Model](#33-dynamic-model)
  
  3.4 [Code Specification](#34-code-specification)

4. [Glossary](#4-glossary)

5. [Appendix](#5-appendix)
  5.1 [Appendix A](#61-appendix-a---use-case-diagram)

  5.2 [Appendix B](#62-appendix-b---use-cases)

  5.3 [Appendix C](#63-appendix-c---class-interfaces)

  5.4 [Appendix D](#64-appendix-d---diary-of-meetings-and-tasks)

6. [References](#6-references)

-------

##1. Introduction

###1.1 Problem Definition

The software company Brighgauge would like a platform to test certain datasources. Namely they want the data to come back in a formatted way which would enable them to dive into the details and decide the viability of including that datasource on their platform.

The scope of the system is limited for this semester. The main goal of the product owner is to enable data retrieval from the Trello API. As such, there is not outset intention to have the system integrate multiple APIs at this time. Care will be taken to design the system in such a way that will enable future APIs to be added in a simple manner, but those may come secondary to accomplishing the goal at hand.

###1.2 Design Methodology

The software process follows an agile methodology. This allows the developers to get the requirements from the product owner, formulate those into user stories, create use cases and sequence diagrams, append to class diagrams, write the code, and test the code. It enables the process to iterate throughout the development cycle. By using the sequence, class, use case, package model diagrams from the UML format going back when something isn't working or needs to be changed is relatively simple. The difficulty is making sure the overarching design is one that can be modified throughout for the big picture of the project.

###1.3 Definition, Acronyms, and Abbreviations

**SaaS**: Software-as-a-Service is defined as a software licensing model that is subscription based. It enables a user to have access to some business application that they can use for their own unique purposes.

###1.4 Overview of Document

This document dives into the system design first via chapter 2. That chapter covers the subsystem decomposition, hardware and software mappings, the persistent data management, and the security and privacy parameters. Following that is the detailed design in chapter 3, this covers the static and dynamic models as well as code specification. The document finishes with a glossary and appendices to aid the chapters.

######[top](#deliverable-3---design-document)
-------

##2. System Design

The following sections give an overview of the system design by showing the subsystem decomposition, the hardware and software mappings, the persistent data management, and the security and privacy designs.

###2.1 Overview
The main architecture for the system will be coming from the Django framework which uses a variation on Model-View-Controller. Namely it does away with controller and uses a Model-View-Template architecture. There is some discussion as to whether the framework itself acts as a controller with url mappings and such. Behind the scenes there will be some pipe and filter architecture for the various APIs and the calls they allow. As well as the client portion of the server-client architecture with the third party APIs.

**Package Diagram**

![Package Diagram](images/PackageDiagram.jpg?raw=true)

###2.2 Subsystem Decomposition

The Templates subsystem will deal with how the website looks and reacts. This will be handled by the various template html documents. They will handle how the pages look and if any data is passed to the page, whether or not to show it.

The Views subsystem is the behind the scenes operator for being able to deal with multiple third-party APIs. This decides what information should be passed to the Tempalates subsystem by recieving queries and reaching out to the APIs subsystem and SQLite RDBMS subsystems.

The APIs subsystem contains the logic for a given third-party API. The main focus for this semester was the Trello API. This will handle the details of making the call, cleaning the response, and deciding what will be available to the Views subsystem.

The SQLite RDBMS subsystem will contain the data that is retrieved from the APIs subsystem. The Views subsystem will be relaying the data retrieved from the APIs subsystem to the SQLite RDBMS as well as reading from the storage when needed from the Templates subsystem.

###2.3 Hardware and Software Mapping

**Deployment Diagram**

![Deployment Diagram](images/DeploymentDiagram.jpg?raw=true)

The system has three main components. The host which contains the webserver, templates, views, models, and database, the client pc which reaches out to the host, and the third party API host that our host reaches out to for data retrieval.

###2.4 Persistent Data Management

**Structure of Data**

![Data Management](images/databasemodels.png?raw=true)

This data is stored on the SQLite RDBMS within Django. The above code is the model that is used to create the tables and attributes. As can be seen the Api class contains only a name and calls field. The ApiCredential class has a name, settings, and api foreign key. Finally the Call class has a foreign key to an api, a name field, and a response field.

###2.5 Security and Privacy
Django comes with great security features available out of the box. This includes cross site scripting protection, cross site request forgery protection, SQL injection protection, session security, and others.

In terms of privacy, on a basic level the project will have only one user that has access to create data sources. The authentication is done by third party APIs, so that privacy is outside the system. Access to the database will be restricted to the single user.


######[top](#deliverable-3---design-document)
-------

##3. Detailed Design

###3.1 Overview

The Templates subsystem will deal with how the website looks and reacts. This will be handled by the various template html documents. They will handle how the pages look and if any data is passed to the page, whether or not to show it.

The Views subsystem is the behind the scenes operator for being able to deal with multiple third-party APIs. This decides what information should be passed to the Tempalates subsystem by recieving queries and reaching out to the APIs subsystem and SQLite RDBMS subsystems.

The APIs subsystem contains the logic for a given third-party API. The main focus for this semester was the Trello API. This will handle the details of making the call, cleaning the response, and deciding what will be available to the Views subsystem.

The SQLite RDBMS subsystem will contain the data that is retrieved from the APIs subsystem. The Views subsystem will be relaying the data retrieved from the APIs subsystem to the SQLite RDBMS as well as reading from the storage when needed from the Templates subsystem.


###3.2 Static Model

**Class Diagram**
![Image of Class Diagram](images/TrelloApiClassDiagram.jpg?raw=true)


###3.3 Dynamic Model

The following are sequence diagrams relating to the user stories captured to be fulfilled by the system design.

**Get Data Source Sequence Diagram**
![Image of Get Data Source Sequence Diagram](images/GetDataSourceSequence.jpg?raw=true)

**View Data Source Sequence Diagram**
![Image of View Data Source Sequence Diagram](images/CreateDataSourceSequence.jpg?raw=true)

**Get My Cards Sequence Diagram**
![Image of Get My Cards Sequence Diagram](images/FilterGetMyCards.jpg?raw=true)

**Get Due in Seven Sequence Diagram**
![Image of Get Due in Seven Sequence Diagram](images/FilterGetDueinSevenCards.jpg?raw=true)

**Get Past Due Sequence Diagram**
![Image of Get Past Due Sequence Diagram](images/FilterGetPastDueCards.jpg?raw=true)


###3.4 Code Specification

The Templates subsystem will contain multiple simple html files. The files which pertain to call responses will have javascript in them to render the datables libary. The filtering on the get all cards call will contain further javascript for re-rendering the datatables after a metric filter has been selected.

The Vies subsytem has multiple methods, including index(request), datasource(request), confirmation(request, api_name), datasets(request), api(request, api_cred), and apicall(request, api_cred, action_name).

Within the APIs subsystem the Trello class will be used to get data from Trello. This class will need to be passed a user token. For a list of all the methods within this class refer to the [Class Diagram](#32-static-model) above.

######[top](#deliverable-3---design-document)
-------

##4. Glossary

**django**: Web framework that is open source. Follows similar style to model-view-controller, except the framework become the controller. Architectual pattern is called model-view-template, with template relating to view in MVC.

**python**: General purpose language. Highly readable code that is not very verbose. Has dynamic typing. 

**RDBMS**: Relational Database Management System.

**SaaS**: Software-as-a-Service is defined as a software licensing model that is subscription based. It enables a user to have access to some business application that they can use for their own unique purposes.


######[top](#deliverable-3---design-document)
-------

##5. Appendix

###5.1 Appendix A - Use Case Diagram

![Image of Use Case Diagram](images/SILUseCaseDiagram.png?raw=true)

###5.2 Appendix B - Use Cases

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


###5.3 Appendix C - Class Interfaces 

**Code for Views subsystem**:

```
def index(request)

def datasource(request)

def confirmation(request, api_name)

def datasets(request)

def api(request, api_cred)

def apicall(request, api_cred, action_name)
```

**Code for Trello class**:

```
def __init__(self, token)

def make_call(self, address)

def get_records(self)

def get_all_boards(self)

def get_board(self, id)

def get_all_cards(self)

def get_lists(self)

def get_labels(self)

def get_members(self)
```


###5.4 Appendix D - Diary of Meetings and Tasks

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


######[top](#deliverable-3---design-document)
-------

##6. References

* Draw IO: https://www.draw.io/ used for all diagrams.

######[top](#deliverable-3---design-document)
-------

