__author__ = 'George Hu'

from datetime import date, datetime, timedelta
import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


import pprint



class SendEmailToUserService(object):
    def __init__(self, config,receivers,template, picUrlPath=None, reportFolder=None):
        self.config=config
        self.receivers=receivers


        self.template = template
        # self.picUrlPath = picUrlPath
        # self.reportFolder = reportFolder
        # self.resourceUrl = ""


    def createHTMLReportContent(self, reportData=None, isLocal=False, anonymous=False):


        if anonymous:
            reportData["userName"] = "XXX.XXX"

        html = self.template.render(reportData)
        # html = html.replace("../../icon/space.png", self.resourceUrl + "icon/space.png")

        return html



    def sendEmailToUser(self, createdBy, userName, createdDate, TEST=False, programId="1"):
        # reportData = self.createUserProgressReport(createdBy, userName, createdDate)
        # reportData=None, isLocal=False
        htmlReport = self.createHTMLReportContent({},False)
        # pdfAttachment = HTML(string=htmlReport).write_pdf()

        subject = "US-China Investment Summit {0} {1}".format(userName, createdDate.isoformat())
        # receivers = self.get_parents_emails_by_user_name(userName)
        sender = self.config['sender']#'support@afficienta.com'
        if TEST:
            bcc = "xingtang.hu@afficienta.com"
        else:
            bcc = self.config['bcc']#"xingtang.hu@afficienta.com"

        if TEST:
            receivers = ["xingtang.hu@afficienta.com"]
            subject = "TEST:" + subject
        if len(self.receivers) == 0:
            raise Exception("Can't find user email address!")



        self.sendHtmlAsEmail(userName, sender, self.receivers, bcc, subject, htmlReport )





    def sendHtmlAsEmail(self, user_name, sender, receivers, bccList, subject, htmlText, TEST=False,pdfAttachment=None, pdfName=None):
        try:
            smtpServer = smtplib.SMTP(self.config['SMTP'])
            smtpServer.starttls()
            smtpServer.login(self.config['GmailServerUser'],self.config['GmailServerPassword'])


            msg = MIMEMultipart('alternative')
            msg["Subject"] = subject
            msg["From"] = self.config['From']#"US-China Investment Summit<sunnychen201213@gmail.com>"
            msg["To"] = user_name
            msg['Bcc'] = bccList

            rcpt = []
            rcpt.extend(receivers)
            bccArray = bccList.split(',')
            for bcc in bccArray:
                rcpt.append(bcc)

            content = MIMEText(htmlText, 'html', "utf-8")  # there are some unicode in skill name
            msg.attach(content)

            # attachment = MIMEApplication(pdfAttachment)
            # attachment.add_header('Content-Disposition', 'attachment', filename=attachmentName)
            # msg.attach(attachment)

            smtpServer.sendmail(sender, rcpt, msg.as_string())
            smtpServer.quit()
            print "Successfully sent email to user_name,bccList: ", user_name,receivers,bccList
        except smtplib.SMTPException as e:
            print "Error: unable to send email {0}".format(e)

