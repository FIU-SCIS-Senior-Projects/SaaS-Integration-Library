#Deliverable 2 - Requirements Document
#####Senior Project CIS 4911
#####SaaS Integration Library
#####Adam Merille
#####Professor Masoud Sadjadi


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

###1.2 Scope of System

###1.3 Definition, Acronyms, and Abbreviations

###1.4 Overview of Document


######[top](#deliverable-2---requirements-document)
-------

##2. Current System


######[top](#deliverable-2---requirements-document)
-------

##3. Project Plan

###3.1 Project Organization

###3.2 Work Breakdown

###3.3 Cost Estimate


######[top](#deliverable-2---requirements-document)
-------

##4. Proposed System Requirements

###4.1 Functional Requirements

###4.2 Analysis of System Requirements

####4.2.1 Scenarios

####4.2.2 Use Case Model
![Image of Use Case Diagram](images/SILUseCaseDiagram.png?raw=true)

####4.2.3 Static Model

####4.2.4 Dynamic Model


######[top](#deliverable-2---requirements-document)
-------

##5. Glossary


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


**Title:**

**Description:** 

**Actor:**

**Preconditions:**

**Postconditions:**


###6.2 Appendix B - Use Case Diagram

###6.3 Appendix C - Static UML Diagrams

![Image of Trello Class Diagram](images/TrelloApiClassDiagram.jpg?raw=true)

###6.4 Appendix D - Dynamic UML Diagrams

![Image of Get Data Source Sequence Diagram](images/GetDataSourceSequence.jpg?raw=true)

![Image of View Data Source Sequence Diagram](images/CreateDataSourceSequence.jpg?raw=true)
![Image of Get My Cards Sequence Diagram](images/FilterGetAllCards.jpg?raw=true)

###6.5 Appendix E - User Interface Designs

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
__


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
__


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
send javascript issues to Orland and work on fixing


######[top](#deliverable-2---requirements-document)
-------

##7. References
