from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
import time
from functools import reduce
from collections import Counter

def createExamples():
    numberArrayExamples= open("numArEx.txt",'a')
    numberswehave=range(0,10)
    versionswehave=range(1,10)

    for eachn in numberswehave:
        for eachversion in versionswehave:
            #print(str(eachn)+'.'+ str(eachversion))
            imgFilePath= "images/numbers/"+ str(eachn)+'.'+str(eachversion)+'.png'
            ei=Image.open(imgFilePath)
            eiar=np.array(ei)
            eiar1= str(eiar.tolist())

            linetowrite= str(eachn)+'::'+eiar1+'\n'
            numberArrayExamples.write(linetowrite)
            
            
    

def threshold(imageArray):
    balanceAr=[]
    newAr= imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum= reduce(lambda x, y: x+y, eachPix[:3]/len(eachPix[:3]))
            balanceAr.append(avgNum)
                           
    balance= reduce(lambda x, y: x+y, balanceAr)/len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x+y, eachPix[:3]/len(eachPix[:3])) > balance:
                eachPix[0]= 255
                eachPix[1]= 255
                eachPix[2]= 255
                eachPix[3]= 255

            else:
                eachPix[0]= 0
                eachPix[1]= 0
                eachPix[2]= 0
                eachPix[3]= 255
    return newAr            
        

           
def whatnumisthis(filepath):
    matchedAr=[]
    loadExamps=open('numArEx.txt','r').read()
   
    loadExamps=loadExamps.split('\n')

    i= Image.open(filepath)
    iar=np.array(i)
    iarl= iar.tolist()

    inquestion =str(iarl)

    for eachEx in loadExamps:
        if len(eachEx)>3:
            splitEx= eachEx.split('::')
            currentNum= splitEx[0]
            currentAr= splitEx[1]

            eachPixEx= currentAr.split('],')

            eachPixInQ= inquestion.split('],')

            x=0

            while x <len(eachPixEx):
                if eachPixEx[x]==eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x+=1
                
    print(matchedAr)
    x= Counter(matchedAr)
    print(x)



    graphX=[]
    graphY=[]

    for eachthing in x:
        print(eachthing)
        graphX.append(eachthing)
        print(x[eachthing])
        graphY.append(x[eachthing])

    fig= plt.figure()
    ax1=plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4 )
    ax2=plt.subplot2grid((4,4),(1,0), rowspan=1, colspan=4 )

    ax1.imshow(iar)

    ax2.bar(graphX,graphY, align='center')

    plt.ylim(400)

    xloc= plt.MaxNLocator(12)

    ax2.xaxis.set_major_locator(xloc)

    plt.show()
        
    





whatnumisthis( 'images/numbers/7.1.png') 
            
        







                       
