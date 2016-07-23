from datetime import date, datetime, timedelta
import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from org.uschina.conf.readreceiver import ReadCSV
from org.uschina.conf.SendEmailToUser import SendEmailToUserService

class sendMail(object):
    def __init__(self):


        self.currentPath = os.path.dirname(os.path.realpath(__file__))
        print ' current path', self.currentPath

        self.readcsv= ReadCSV(self.currentPath+'/receiverlist.csv')
        self.receiverEmailList=self.readcsv.read()

        # config,receivers,template, picUrlPath, reportFolder

        self.serverConfig=self.readcsv.readServerConfig(self.currentPath+'/config.txt')
        print self.serverConfig
        self.service = SendEmailToUserService(self.serverConfig, self.receiverEmailList,"")



    def send(self):
        from jinja2 import Environment, FileSystemLoader

        env = Environment(loader=FileSystemLoader(self.currentPath + '/templates/'))

        print '===email template path: ',self.currentPath + '/templates/'
        template = env.get_template('us-china-mail-template.html')
        self.service.template = template

        # self.service.reportFolder = self.currentPath + "/app/static/src/assets/studentreportfiles/progressreport"
        # self.service.picUrlPath = "../png/{1}"
        # self.service.resourceUrl = "../../../../"

        createdBy = "Xingtang Hu"
        fromuserName = "sunnychen201213@gmail.com"
        reportDate = date(2016, 5, 20)
          # def sendProgressReportToUser(self, createdBy, userName, createdDate, TEST=False, programId="1"):
        TEST=False
        self.service.sendEmailToUser(createdBy, fromuserName, reportDate,TEST)


if __name__ == '__main__':
    print 'send start...'
    service = sendMail()
    service.send()
    print 'send success'
