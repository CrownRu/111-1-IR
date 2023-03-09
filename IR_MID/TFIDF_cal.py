import pathlib
import math

fileNum=0
totalTF=[]
totalIDF={}
fileDir="./ir_data/"
fileExt="*.wrd"

def getTF(x):
    f=open(x, "r")
    tf={}
    for line in f:
        content = line.split(' ')
        tf[content[0]]=(int(content[1]))
          
    count=0
    for y in tf:
        count+=tf[y]
    for z in tf:
        tf[z]=tf[z]/count
    return(tf)

#def getIDF(x):
    f=open(x,"r")
    idf={}
    for line in f:
        content=line.split(' ')
        if content[0] not in idf:
            idf[content[0]]=int(content[1])
        else:
            idf[x[0]]+=int(content[1])
    return(idf)
idf={}
for fileName in pathlib.Path(fileDir).glob(fileExt):
    fileNum+=1
    fileName=str(fileName)
    totalTF.append(getTF(fileName))
    #print(totalTF)
#-------------------------------IDF calculate
    f=open(fileName,"r")
    
    for line in f:
        content=line.split(' ')
        if content[0] not in idf:
            idf[content[0]]=int(content[1])
        else:
            idf[content[0]]+=int(content[1])

for word in idf:
    idf[word]=math.log(fileNum)-math.log(idf[word])
#print(idf)
#--------------------------------
f=open("weight1.txt","w")
for wordINidf in idf:
    titleANDresult=wordINidf+","
    for x in range(len(totalTF)):
        tf=totalTF[x]
        if wordINidf in tf:
            titleANDresult+=(str(tf[wordINidf]*idf[wordINidf])+",")
        else:
            titleANDresult+=" ,"
    f.write(titleANDresult+"\n")
f.close()

f1=open("weight1.txt","r")
f2=open("weight2.txt","w")
for everysentence in f1:
    everyone=everysentence.split(",")
    new=""
    #print(everyone)
    #print(len(everyone))
    for i in range(len(everyone)-1):
        if i==0:
            new+=everyone[0]+":"
        else:
            if(everyone[i]==" "):
                new+="0,"
            else:
                new+="1,"
    f2.write(new+"\n")
f1.close()
f2.close()