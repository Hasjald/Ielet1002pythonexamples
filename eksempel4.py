import time
import requests
import json

state ={0: "generer data", 1:"sendtilcot",2:"lesavcot"}

KEY_T   ="8173"                
KEY_H   = "12074"

TOKEN_1  ="eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNjc0In0.iXsl3X05KGJ3ZtRLc-PrqeAJy_KpmTHRGJzF2xutp4s"

def errorhaandtering(code_): #enkel errorhåndteringskode

    if(code_==200):
        print("succsess")
    else:
        print("error %d" % (code_))

"""denne funksjonen sender verdien 1 gang til COT"""
def send_til_cot(KEY,VALUE,TOKEN):
    payload_1={'Key':KEY,'Value':VALUE,'Token':TOKEN}    #dette er dictet som blir til json-packet-en KEY og TOKEN må være en streng og Value må være en int eller float 
    response=requests.put('https://circusofthings.com/WriteValue',
                data=json.dumps(payload_1),headers={'Content-Type':'application/json'})  #vi dumper dictet til json formatet og putter det i data delen av put requesten vår
    
    errorhaandtering(response.status_code) 
    
"""denne funksjonen returnerer verdien på signalet spesifisert av KEY samt når verdien på signalet ble endret"""
def les_cot(KEY,TOKEN):
    payload={'Key':KEY,'Value':0,'Token':TOKEN}    #her oppretter vi et dict med Key og Token for Get request så er ikke Value viktig så den trenger ikke være med.
    response=requests.get('https://circusofthings.com/ReadValue',params=payload)
    k = json.loads(response.content)     #vi får tilbake en pakke men vi må få json libbet til å behandle den slik at vi kan hente det som er inni. 
    """ returnerer verdien på signalet og epoch da signalet ble oppdatert på COT """
    return k["Value"],k["LastValueTime"]/1000       #deler lastvaluetime fordi den blir oppgitt i millisekund og datetime libbet bruker bare sekund

#returnerer 2 konstanter, denne kan utvides 
def generer_data():
    a=686920.00
    b=7468657265.00
    return a,b



def main(): 
    """setup, sett ting her som bare skal kjøres en gang eller initialbetingelser"""
    currentstate=state[0]
    nextstate=0
    while(True):
        """her er loop """
        time.sleep(1)
        print()
        print("state er "+str(currentstate))
        """Mangler litt logikk"""
        if(currentstate=="generer data"): #hent dataen fra generer data 
            
            nextstate=1
        elif(currentstate=="sendtilcot"):    #send dataen 
           
            nextstate=2    
        elif(currentstate=="lesavcot"):    #les dataen på cot som vi akkurat sendte
            
            print("new data is %s and %s" %(read_data[0],read_data2[0]))
            nextstate=0
        
        currentstate=state[nextstate]

if __name__ == '__main__':
    print('starting')
    main()
