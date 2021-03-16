
import requests    
import json     
import time

state ={0: "Idle", 1:"sample_data", 2:"send_response"}

currentstate=state[0]

"""COT variables and constants"""
KEY_T   ="8173"                #put your signal key here 
KEY_H   = "12074"
KEY_P   = "16071"
KEY_W   = "32585"
KEY_SW  = "5990"
KEY_response ="21446"
TOKEN_1  ="eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNjc0In0.iXsl3X05KGJ3ZtRLc-PrqeAJy_KpmTHRGJzF2xutp4s"

def errorhandling(code_): #errorbehandling

    if(code_==200):
        print("succsess")
    else:
        print("error %d" % (code_))

"""leser ifra COT"""
def read_cot(KEY,TOKEN):
    payload={'Key':KEY,'Value':0,'Token':TOKEN}
    response=requests.get('https://circusofthings.com/ReadValue',params=payload)
    k = json.loads(response.content)
    
    return k["Value"],k["LastValueTime"]

"""skriver til COT """
def write_cot(KEY,VALUE,TOKEN):
    payload_1={'Key':KEY,'Value':VALUE,'Token':TOKEN}    
    response=requests.put('https://circusofthings.com/WriteValue',
                data=json.dumps(payload_1),headers={'Content-Type':'application/json'}) 
    errorhandling(response.status_code)

"""skriver til tekst fil """
def writetofile(file,data1,data2,data3,data4):
    file2write=open(file,'a') #append to text file
    file2write.writelines(str(data1[0])+" "+str(data1[1])+" "+str(data2[0])+" "+str(data2[1])+" "+str(data3[0])+" "+str(data3[1])+" "+str(data4[0])+" "+str(data4[1])+"\n")
    file2write.close()

""" tar inn de 4 signalene og skriver de i tekst fila"""
def sample_data(filename):
    
    T=read_cot(KEY_T,TOKEN_1)
    H=read_cot(KEY_H,TOKEN_1)
    P=read_cot(KEY_P,TOKEN_1)
    W=read_cot(KEY_W,TOKEN_1)
    writetofile(filename,T,H,P,W)
    
"""sender respons til cot signalet KEY_respons"""    
def send_response(Val):
    write_cot(KEY_response,Val,TOKEN_1)
    print("done")


def main(): 
    """setup, things that only runs once"""
    lastcheck=0
    currentstate=state[0]
    edge=0 #edge variable, we want to know if it is a positive edge or a  negative edge

    while(True):
        time.sleep(1)
        check=read_cot(KEY_SW, TOKEN_1) #read the switch value.
        
        """Mangler en state machine/logikk"""

        print(currentstate)
        print(edge)
        


if __name__ == '__main__':
    print('starting')
    main()