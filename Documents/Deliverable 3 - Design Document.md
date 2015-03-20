#Deliverable 3 - Design Document
#####Senior Project CIS 4911
#####SaaS Integration Library
#####Adam Merille
#####Professor Masoud Sadjadi

##1. Introduction

##2. System Design

###2.1 Overview
The main architecture for the system will be coming from the Django framework which uses a variation on Model-View-Controller. Namely it does away with controller and uses a Model-View-Template architecture. There is some discussion as to whether the framework itself acts as a controller with url mappings and such. Behind the scenes there will be some pipe and filter architecture for the various APIs and the calls they allow. As well as the client portion of the server-client architecture with the third party APIs.

###2.2 Subsystem Decomposition
![Subsystem Decomposition](images/SubsystemOverview.jpg?raw=true)
###2.3 Hardware and Software Mapping

###2.4 Persistent Data Management
![Data Management](images/DataManagement.jpg?raw=true)
###2.5 Security/Privacy
Django comes with great security features available out of the box. This includes cross site scripting protection, cross site request forgery protection, SQL injection protection, session security, and others.

In terms of privacy, on a basic level the project will have only one user that has access to create data sources. The authentication is done by third party APIs, so that privacy is outside the system. Access to the database will be restricted to the single user.

##3. Detailed Design

##4. Glossary

##5. Appendix
###5.1 Appendix A - Use Case Diagram

###5.2 Appendix B - Use Cases

###5.3 Appendix C - Class Interfaces (code)

###5.4 Appendix D - Diary of Meetings and Tasks

##6. References
