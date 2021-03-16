import time
import datetime
import requests  #husk å installer denne
import json      

state ={0: "samle", 1:"printe"}   #lager et dict for holde string verdien, dict er veldig versatile så du kan skrive state={1:"printe",0:"samle"} 
                                  #og hvis du kaller print(state[0]) så vil den parse igjennom dictet og finne at nulll korresponderer til "samle"

"""Du må huske å legge til dine egne Keys og token"""
KEY_T   ="23423"                
KEY_H   = "3242342"
KEY_P   = "231231"

TOKEN_1  ="eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNjc0In0.iXsl3X05KGJ3ZtRLc-PrqeAJy_KpmTHRGJzF232423"

def les_cot(KEY,TOKEN):
    payload={'Key':KEY,'Value':0,'Token':TOKEN}    #her oppretter vi et dict med Key og Token for Get request så er ikke Value viktig så den trenger ikke være med.
    response=requests.get('https://circusofthings.com/ReadValue',params=payload)
    k = json.loads(response.content)     #vi får tilbake en pakke men vi må få json libbet til å behandle den slik at vi kan hente det som er inni. 
    """ returnerer verdien på signalet og epoch da signalet ble oppdatert på COT """
    return k["Value"],k["LastValueTime"]/1000       #deler lastvaluetime fordi den blir oppgitt i millisekund og datetime libbet bruker bare sekund

def main(): 
    """setup, sett ting her som bare skal kjøres en gang eller initialbetingelser"""
    currentstate=state[0]

    while(True):
        """her er loop """
        time.sleep(1)
        print()
        print("state er "+str(currentstate))
         """Mangler en state machine/logikk"""
        if(currentstate=="samle"):
            print1=les_cot(KEY_T,TOKEN_1)                                   #kaller les signal fra cot og får i retur en liste med 2 elementer value og lastvalueime
            datetime_time1 = datetime.datetime.fromtimestamp(print1[1])     #forandrer lastvaluetime til en streng som legges i datatime_time1 variablen
            nextstate=1
        elif(currentstate=="printe"):    
            print("Dato "+str(datetime_time1)+" var signalet KEY_T: "+str(print1[0]))   #printer tiden samt hva verdien er 
            nextstate=0
        
        currentstate=state[nextstate]

if __name__ == '__main__':
    print('starting')
    main()
