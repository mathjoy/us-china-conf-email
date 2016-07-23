
Run the folloing commant:

#clone project to your local folder

git clone https://github.com/mathjoy/us-china-conf-email.git

cd us-china-conf-email

#create python virtual environment

virtualenv venv
source  venv/bin/activate

#install python package

pip install -r requirements.txt


#setup Gmail server account at conifg.txt file


#setup sender email list at receiverlist.csv

#setup Email Template at : templates/us-china-mail-template.html


#run :  python sendemail.py


