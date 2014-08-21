import re
import os
import csv
from datetime import datetime

fileMatch = []

# Search Regular MSO
for root, dirs in os.walk("Y:\\aaaprojects\BMSO"):
        for dir in dirs:
                
                for file in files:
                fileMatch.append(os.path.join(root,file))

# Search DM Special Events
for root, dris, files in os.walk("Y:\\aaaprojects\Promo Other"):
        for file in files:
                fileMatch.append(os.path.join(root,file))

# For Python Regex negative lookup, to avoid greedy
#  search, we have to us ^(?!.*Pattern)
regex = re.compile("^(?!.*Old|.*old|.*OLD|.*TEST).*(2012|2013|2014)+.*(IT|it).csv$")
files = filter(regex.search,fileMatch)

#print '\n'.join(files)
f = open("bigfile5.csv",'w')
fcsv = csv.writer(f,delimiter = ',')

ftest = open("log.csv",'w')
fcsvtest = csv.writer(ftest,delimiter = ',')

#Define some offer code pattern
offerPattern = re.compile("^C[A-Z0-9]{4,}$")



filecurrent = []

for file in files:
        with open(file,'r') as f1:
                reader = csv.reader(f1)
                next(reader,None) # Skip the headers
                for line in reader: #Read each line
                        elementfilter = filter(offerPattern.search,line) # Srub out the offer code

                        if not elementfilter: # Check if the elementfilter is empty
                                continue
                        else:
                          # IT file only lists 3 nights offer, manually add 2 nights as second offer code
                                if elementfilter[0][-2] == '3':
                                        data=[line[0],elementfilter[0],elementfilter[0][:-2]+'2'+elementfilter[0][-1]]
                                else:
                                        data = [line[0],elementfilter[0],'']
                                fcsv.writerow(data)# write to excel file

                        # Print out the troubled files
##                        except:
##                                if filecurrent != file:
##                                        print file
##                                        print line
##                                        filecurrent = file
##                                continue



f.close()

fout = csv.writer(open("output.csv",'wb'))
f = open("bigfile5.csv",'rb')
seen = set()
for line in f:
	if line[:-1] not in seen:
                seen.add(line[:-1])
                fout.writerow(line)
f.close()



#-------------------------- Test Code --------------------------------------------------------
for file in files:
        with open(file,'r') as f1:
                reader = csv.reader(f1)
                # next(reader,None) # Skip the headers
                header = next(reader)
                for line in reader: #Read each line
                        elementfilter = filter(offerPattern.search,line) # Srub out the offer code

                        if not elementfilter: # Check if the elementfilter is empty
                                continue
                        else:
                          # IT file only lists 3 nights offer, manually add 2 nights as second offer code
                                if elementfilter[0][-2] == '3':
                                        data=[line[0],elementfilter[0],elementfilter[0][:-2]+'2'+elementfilter[0][-1]]
                                else:
                                        data = [line[0],elementfilter[0],'']
                                fcsv.writerow(data)# write to excel file






varMatch = ['id','CARD','game','tier','offercode']
year = 2013
month = 4
for file in files:
        fileDate = os.path.getmtime(file)
        print fileDate, file
        if datetime.fromtimestamp(fileDate).year  == year and datetime.fromtimestamp(fileDate).month  == month:
                with open(file, 'r') as f:
                        reader = csv.reader(f)
                        header = next(reader)
                        print header
                        # something matching names, and pick out index
                        varIndex = [header.index(i) for i in varMatch]
                        for line in reader:
                                out = [line[i] for i in varIndex] # Select var as we want
                                print out # write to excel file


