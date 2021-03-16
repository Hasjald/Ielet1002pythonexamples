
import time
import requests
import json

state={0:"getdata",1:"writedata",2:"readdata"}
currentstate=state[0]
""" denne funskjonen åpner filen som spesifisert i file og appender den med writelines """
def writetofile(file,data1,data2,data3,data4):
    file2write=open(file,'a') #append to text file
    file2write.writelines(str(data1[0])+" "+str(data1[1])+" "+str(data2[0])+" "+str(data2[1])+" "+str(data3[0])+" "+str(data3[1])+" "+str(data4[0])+" "+str(data4[1])+"\n")
    file2write.close()

""" åpner filen som spesifisert i file og putter kolonnene som spesifiser i col1 og col2 i liste x og y"""
def readfile(file,col1,col2): 
    with open(file) as f:
        lines = f.readlines()
        x=[line.split()[col1] for line in lines]
        y=[line.split()[col2] for line in lines]
    return x,y

"""funksjonen lager en streng"""
def sjekkomnytxtfil():
    timestr = time.strftime("%Y%m%d-%H") ##timesbasert 
    nyfile="dover/EX4"+"-"+timestr+".txt"  # hvis du ikke har laget en folder som heter dover så funker dette ikke, bare ta å slette dover/ fra strengen
    
    return nyfile
    
    """bare en liste med 8 members """
def data():
    k=[1,2,3,4,5,6,7,8]
    return k

def main(): 
    """setup, sett ting her som bare skal kjøres en gang eller initialbetingelser"""
    currentstate=state[0]
    nextstate=0
    count=0
    while(True):
        """her er loop """
        time.sleep(0.25)
        print()
        print("state er "+str(currentstate))
        
        """Mangler en state machine/logikk"""

        currentstate=state[nextstate]

if __name__ == '__main__':
    print('starting')
    main()