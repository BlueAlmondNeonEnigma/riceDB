import json
import search
from search import search_packages as searchPak
from search import search_keywords as searchKey
workingFolder = ""
question = "Are you sure you want to install %s for %s? (Y/N)\n>"
data = json.loads(open("%sindex.json" % workingFolder).read())
while 1:
    userInput = input(">").split(' ', 1)
    if len(userInput) > 1:
        userInputP = userInput[1]
    else:
        print("Missing parameter.")
        continue
    if userInput[0] == "install":
        inputParsed = userInputP.split(' ')
        if len(inputParsed) > 1:
            if inputParsed[0] in data:
                searchResult = searchPak(inputParsed[0], inputParsed[1], searchKey)
                if searchResult is None:
                    print("No matching packages were found.")
                    continue
                else:
                    print("Which package would you like to install?")
                    currentPackageNum = 0
                    for i in searchResult:
                        currentPackageNum += 1
                        packageN = i["Name"]
                        print("%d) %s" % (currentPackageNum, packageN))
                        choice = int(input('(#)>'))-1
                        if searchResult[choice]:
                            packageN = searchResult[choice]["Name"]
                            packageD = searchResult[choice]["Description"]
                            packageI = searchResult[choice]["Images"]
                            packageR = searchResult[choice]["Github Repository"]
                            divider = '*'*50
                            print(divider)
                            print("Name: %s" % packageN)
                            print("Description: %s" % packageD)
                            print("Images: %s" % ', '.join(packageI))
                            print("Github Repository: %s" % packageR)
                            print(divider)
                            response = input(question % (packageN, inputParsed[0]))
                            if response.lower() == 'y':
                                print("Okay.")
                            else:
                                print("Invalid option chosen.")
                        else:
                            print("Invalid software name.")
                            continue
        else:
            print("Missing parameter.")
