
This application requires python, which is included on any linux machine. If the local system you are using does not have python make sure to obtain it.

Also, to get all the requirements installed we have included a piprequirements.txt file that will install the libraries needed using pip. Install pip via http://pip.readthedocs.org/en/latest/installing.html.

Once python and pip are installed make sure you also have git. Then clone this repository "git clone git@github.com:FIU-SCIS-Senior-Project-2015-Spring/SaaS-Integration-Library.git". 

After obtaining the repository navigate to /SaaS-Integration-Library/Code/Website/SaaS_Integration_Library and then run "sudo pip install -r piprequirements.txt". You now have all the required libraries!

Working on the remote server:

1. At the command line "ssh  ameri012@sil-dev.cis.fiu.edu"

![Image of ssh](images/sshScreenshot.png?raw=true)

2. Enter password

![Image of ssh logged in](images/sshLoggedIn.png?raw=true)

3. At the command line "screen -D -R"

![Image of screen command](images/remoteScreen.png?raw=true)

![Image of in screen](images/screenedIn.png?raw=true)

You are now where the remote server is running. To stop the runserver process of Django do "Ctrl+c". If you are going to exit the remote server but want to keep the django runserver option going then press "Ctrl+a" then press "d". You are now detached from the screen and can "exit" the ssh safely while the runserver process is still running.


To access the database got to http://131.94.128.118:5555/admin/ and enter the log in credentials
username: siladmin
password: sildata

![Image of in admin login](images/adminlogin.png?raw=true)

Once logged in you may now navigate the database.

![Image of in admin dashboard](images/adminloggedin.png?raw=true)
