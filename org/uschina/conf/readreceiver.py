__author__ = 'georgehu'

import csv
import re

class ReadCSV(object):
    def __init__(self, filename):
        self.filename=filename
        self.D={}


    def read(self):
        receiverEmailList=[]

        with open(self.filename, 'rb') as csvfile:
          spamreader = csv.reader(csvfile, delimiter='	', quotechar='|')
          i = 0
          for row in spamreader:
              # print ', '.join(row)
              # print row['Email']
              print row[0]
              if i >0:
                  cellindex=0
                  for cell in row:
                      if cellindex==0:
                          # print "cell", cell
                          receiverEmailList.append(cell)
                      else:
                          break;
                      cellindex = cellindex+1


                  #receiverEmailList.append(row[0])
              i=i+1
        # print  receiverEmailList
        return receiverEmailList



    def readServerConfig(self,serverConfigureFileName):


        regex = re.compile(r"\s+")
        f = None
        try:
            f = open(serverConfigureFileName, 'r')
            for line in f:
                # print "====line",line,
                line = regex.sub("",line)
                if line == "":
                    continue
                if "#" not in line:
                    key=line.split("=")[0]
                    value=line.split("=")[1].rstrip('\n')
                    # print "{",key,"=",value,"}"
                    self.D[key]=value

        finally:
            if f is not None:
               f.close()


        return self.D
