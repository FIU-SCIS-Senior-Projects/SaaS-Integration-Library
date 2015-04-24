#Deliverable 3 - Design Document
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

###1.2 Scope of System

###1.3 Definition, Acronyms, and Abbreviations

###1.4 Overview of Document

##2. System Design

###2.1 Overview
The main architecture for the system will be coming from the Django framework which uses a variation on Model-View-Controller. Namely it does away with controller and uses a Model-View-Template architecture. There is some discussion as to whether the framework itself acts as a controller with url mappings and such. Behind the scenes there will be some pipe and filter architecture for the various APIs and the calls they allow. As well as the client portion of the server-client architecture with the third party APIs.

###2.2 Subsystem Decomposition
![Subsystem Decomposition](images/SubsystemOverview.jpg?raw=true)

###2.3 Hardware and Software Mapping

###2.4 Persistent Data Management
![Data Management](images/DataManagement.jpg?raw=true)

###2.5 Security and Privacy
Django comes with great security features available out of the box. This includes cross site scripting protection, cross site request forgery protection, SQL injection protection, session security, and others.

In terms of privacy, on a basic level the project will have only one user that has access to create data sources. The authentication is done by third party APIs, so that privacy is outside the system. Access to the database will be restricted to the single user.

##3. Detailed Design

###3.1 Overview

###3.2 Static Model

###3.3 Dynamic Model

###3.4 Code Specification

##4. Glossary

##5. Appendix

###5.1 Appendix A - Use Case Diagram

###5.2 Appendix B - Use Cases

###5.3 Appendix C - Class Interfaces 

###5.4 Appendix D - Diary of Meetings and Tasks

##6. References
