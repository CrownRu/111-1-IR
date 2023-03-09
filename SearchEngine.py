import tkinter as tk
import pathlib
from tkinter import messagebox

fileDir="./ir_data/"
fileExt="*.txt"
News=[]


def onOK():
    print("{}.".format(entry.get()))

    #----------------------------------------------take keyword
    resault=[]
    keyword=(entry.get()).replace(",", "").split(" ")
    f = open("weight1.txt","r")
    for line in f:
        content=line.split(",")
        for i in keyword:
            if i==content[0]:
                resault.append(content)
    #print(len(resault))
    f.close()
    #----------------------------------------------------------
    fileNum=[]
    filePOS=0
    #-------------------------------------------search the match file 
    for i in range(len(resault)):
        for j in range(len(resault[i])-1):
            if(j==0):
                resault[i][j]=resault[i][j]
            else:
                #print(j)
                if(resault[i][j]==' '):
                    filePOS+=1
                else:
                    resault[i][j]=float(resault[i][j])
                    fileNum.append([filePOS,resault[i][j]])
                    filePOS+=1
        filePOS=0
    #print(fileNum)
    #----------------------------------------filesorted
    fileNum.sort(key=lambda x:x[1])
    #print(fileNum)
    sort_fileNum=fileNum[::-1]
    #for i in range(len(fileNum)):
        #sort_file.insert(len(fileNum)-1-i,fileNum[i])
    #print(sort_fileNum)
    #--------------------------------------------------

    for fileName in pathlib.Path(fileDir).glob(fileExt):
        News.append(str(fileName))
    
    finalNews=[]
    for i in range(len(sort_fileNum)):
        j= sort_fileNum[i][0]
        finalNews.append(News[j])
    
    print(finalNews)
    f2=open("searchResult.txt","w")
    f2.write("Result according to the value of\n")
    for i in range(len(sort_fileNum)):
        f2.write(finalNews[i]+":")
        for j in range(len(sort_fileNum[i])):
            if j==0:
                continue
            else:
                f2.write(str(sort_fileNum[i][j])+" ")
    
    
    f2.write("\n---------------------------------------------\n"+"Here is the search result according to "+entry.get()+":\n")
    for n in finalNews:
        f1=open(n,"r")
        content=f1.read()
        f2.write(n+content+"\n")
        f1.close()
        
    f2.close()
    messagebox.showinfo("Search Result", "Check out the search result according to, "+entry.get()+" in file searchResult.txt")

window = tk.Tk()
window.title('Search Engine')
window.geometry("300x100+250+150")

label = tk.Label(window, text = 'Search')
label.pack()

entry = tk.Entry(window,     
                 width = 20) 
entry.pack()

button = tk.Button(window, text = "Go", command = onOK)
button.pack()

window.mainloop()
