import json
import os
import tarfile
#import urllib2
#indexFileWEB = urllib2.urlopen("https://raw.githubusercontent.com/install-logos/riceDB/testing/conf/index.json").read()
workingFolder = ""
data = json.loads(open("%stest.json" % workingFolder).read())
#data = json.loads(indexFileWEB)
while 1:
 userInput = raw_input(">").split(' ',1)
 if len(userInput)>1:
   userInputP = userInput[1].lower()
 else: 
  print "Missing parameter."
  continue 
 if userInput[0] == "list":
  if data.has_key(userInputP):
   divider =  " "
   for i in range(len(data[userInputP])):
    if divider == " ": 
     divider = (lambda name, description: '*'*len(name)*2 if len(name)>len(description) else '*'*len(description)*2)(data[userInputP][i]["Name"],data[userInputP][i]["Description"])
     print divider
    print "Name:",data[userInputP][i]["Name"]
    print "Description:",data[userInputP][i]["Description"]
    print "Images:",', '.join(data[userInputP][i]["Images"])
    print "Github Repository:",data[userInputP][i]["Github Repository"] 
    print divider
  else: 
   print "Not a valid entry.\nValid entries:",', '.join([i for i in data])
  continue
 if userInput[0] == "exit":
  break
 if userInput[0] == "search":
  finds = []
  for a in data:
   for b in data[a]:   
    for c in b:
     if c == "Name":
      if userInputP in b[c].lower(): finds.append("- Config: [" + b[c] + "] in [" + a + ']')
  print "Found (%d) entries matching your string." % len(finds)
  if len(finds) > 0:
   print '\n'.join(finds)
 if userInput[0] == "install":
  candidateFound = 0
  for a in data:
   for b in data[a]:   
    for c in b:
     if c == "Name":
      if userInputP == b[c].lower():
       candidateFound = 1
       print (lambda name, description: '*'*len(name)*2 if len(name)>len(description) else '*'*len(description)*2)(b[c],b["Description"])
       print "Name:", b[c]
       print "Configuration for:", a
       print "Description:", b["Description"]    
       print (lambda name, description: '*'*len(name)*2 if len(name)>len(description) else '*'*len(description)*2)(b[c],b["Description"])
       if raw_input("Are you sure you want to install %s for %s? (Y/N)\n>" % (b[c], a)).lower() == 'y':
        print "Downloading package..."
        if os.path.exists("%s%s.tar.xz" % (workingFolder, b[c]) ):
        	 print "Extracting..."
        	 for f in os.listdir("%sconfigs/%s" % (workingFolder, b[c]) ):
        	  print "--> %s" % f
        	 tar = tarfile.open("%s%s.tar.xz" % (workingFolder, b[c]) )
        	 tar.extractall("%sconfigs/%s" % (workingFolder, b[c]) )
        	 tar.close()
        	 print "Extracted %s.tar.xz successfully." % b[c]
  if candidateFound == 0: print "No installation candidate found."
 if userInput[0] == "add":
  if os.path.exists("%s%s.json" % (workingFolder, userInputP.split(' ')[1]) ):
   newData = json.loads(open("%s%s.json" % (workingFolder, userInputP.split(' ')[1])).read()) 
   print "Adding..."
   if data.has_key(userInputP.split(' ')[0]):
    data[userInputP.split(' ')[0]].append(newData[userInputP.split(' ')[0]][0])
    print "Updating index file..."
    with open("%stest.json" % workingFolder, 'w') as indexFile:
     json.dump(data, indexFile)
    print "Done."
   else:
    print "Error: [%s] doesn't exist!" % userInputP.split(' ')[0]
  else:
   print "Error: File not found!"
