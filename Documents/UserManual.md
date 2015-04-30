#User Manual
#####Senior Project CIS 4911
#####SaaS Integration Library
#####Adam Merille
#####Professor Masoud Sadjadi




######Copyright :copyright: SaaS Integration Library Team 

-------

##Introduction

This is a web application aimed at helping Brightgauge test third-party APIs. Namely it allows a user to add a datasource (Trello) and then make queries on that datasource to view the results in a formatted way. This will allow Brightgauge to discern the business value of various APIs.

##Hardware and Software Requirements

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

##Installation and Setup

This application requires python 2.7, which is included on any linux machine. If the local system you are using does not have python make sure to obtain it.

Also, to get all the requirements installed we have included a piprequirements.txt file that will install the libraries needed using pip. Install pip via http://pip.readthedocs.org/en/latest/installing.html.

It also requires Django version 1.7.

Once python and pip are installed make sure you also have git. Then clone this repository "git clone git@github.com:FIU-SCIS-Senior-Project-2015-Spring/SaaS-Integration-Library.git". 

After obtaining the repository navigate to /SaaS-Integration-Library/Code/Website/SaaS_Integration_Library and then run "sudo pip install -r piprequirements.txt". You now have all the required libraries!

In order to get the project up and running the current method is using Django's runserver command. Inside the terminal for the develop environment go to /SaaS-Integration-Library/Code/Website/SaaS_Integration_Library then type "python manage.py runserver 131.94.128.118:5555".

This will run the web application at the given address and can be access via any browser at http://131.94.128.118:5555/SIL.

This is covered in more detail in the Installation and Design document


##Getting Started

From the main page selet the Datasources link:

**Image of Index UI**
![Image of Index UI](images/IndexUI.png?raw=true)

On the next page you can select Trello to add a datasource:

**Image of Datasource UI**
![Image of Datasource UI](images/DatasourceUI.png?raw=true)

After submitting your information and be redirected to a confirmation page you can selec the datasets link:

**Image of Datasets UI**
![Image of Datasets UI](images/DatasetsUI.png?raw=true)

From here you can select the dataset you just added (should be Trello "username") in order to make calls on that dataset:

**Image of Trello Calls UI**
![Image of Trello Calls UI](images/TrelloCallsUI.png?raw=true)


**References:**
* Tango With Django 1.7: http://www.tangowithdjango.com/book17/, great resource for learning the Django framework.


