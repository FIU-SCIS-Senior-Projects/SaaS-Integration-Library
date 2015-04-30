
This application requires python 2.7, which is included on any linux machine. If the local system you are using does not have python make sure to obtain it.

Also, to get all the requirements installed we have included a piprequirements.txt file that will install the libraries needed using pip. Install pip via http://pip.readthedocs.org/en/latest/installing.html.

It also requires Django version 1.7.

Once python and pip are installed make sure you also have git. Then clone this repository "git clone git@github.com:FIU-SCIS-Senior-Project-2015-Spring/SaaS-Integration-Library.git". 

After obtaining the repository navigate to /SaaS-Integration-Library/Code/Website/SaaS_Integration_Library and then run "sudo pip install -r piprequirements.txt". You now have all the required libraries!

**Note:**

In order to give some security I stored the Trello Developer Key in a separate folder outside of git. So there is a line of code that will have to be changed for you when you create it.

![Image of Code to change location](images/Secretlocation.png?raw=true)

Lines 8 and 9 will have to be changed with your directory name and with your file names.

![Image of Trello secret folder](images/TrelloSecretlocation.png?raw=true)

__init__.py is empty but needed for python and secret.py contains only ' TRELLO_KEY = "key here" '

To get the app running navigate to /SaaS-Integration-Library/Code/Website/SaaS_Integration_Library and type "python manage.py runserver". This will run the application on your localhost and will be viewable if you go to "http://127.0.0.1:8000/SIL/" in your browser.

![Image of runserverlocal](images/runserverlocal.png?raw=true)

![Image of runserverlocalrunning](images/runserverlocalrunning.png?raw=true)

Working on the remote server:

1. At the command line "ssh  ameri012@sil-dev.cis.fiu.edu"

![Image of ssh](images/sshScreenshot.png?raw=true)

2. Enter password

![Image of ssh logged in](images/sshLoggedIn.png?raw=true)

3. At the command line "screen -D -R"

![Image of screen command](images/remoteScreen.png?raw=true)

![Image of in screen](images/screenedIn.png?raw=true)

![Image of exit remote](images/sshexit.png?raw=true)

You are now where the remote server is running. To stop the runserver process of Django do "Ctrl+c". If you are going to exit the remote server but want to keep the django runserver option going then press "Ctrl+a" then press "d". You are now detached from the screen and can "exit" the ssh safely while the runserver process is still running.

To run on the remote server do the same as the localhost version but with the IP address added. So you would type "python manage.py runserver 131.94.128.118:555".

![Image of runserverremote](images/runserverremote.png?raw=true)

If you are wondering about that IP address it was obtained by running the "ifconfig" command on the remote server.

![Image of remote ifconfig](images/remoteifconfig.png?raw=true)

To access the database got to http://131.94.128.118:5555/admin/ and enter the log in credentials
username: siladmin
password: sildata

![Image of in admin login](images/adminlogin.png?raw=true)

Once logged in you may now navigate the database.

![Image of in admin dashboard](images/adminloggedin.png?raw=true)

**Resources:**
* Tango With Django 1.7: http://www.tangowithdjango.com/book17/, great resource for learning the Django framework.
