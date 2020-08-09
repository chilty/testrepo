fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
names = dict()
for line in fh:
    line = line.rstrip()
    #guardian line in case the code breaks when there is no data in a line
    if line == " " : continue
    if line.startswith('From') :#only getting the lines with email
        words = line.split()
        if(len(words)) > 2:#only getting the email lines with date info aka LOOK AT SOURCE INFO
            words = words[1] #TAKING THE SECOND WORD

            names[words] = names.get(words,0)+1     #idiom: retrieve/create/update coutner
#^adds words to names


largest = -1 #sets the largests as something below 0
theword = None #there is no word yetttt
for k,v in names.items():    #items is a method inside dic that gives the key,value pair
    #print(k,v) #prints key value then next line format
    if v > largest:
        largest = v
        theword = k #capture/remember the key that was alrgest

print(theword, largest)
