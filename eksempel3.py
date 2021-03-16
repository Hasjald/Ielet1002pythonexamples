import time
import requests
import json

state ={0: "state1"}

KEY_T   ="160"                
KEY_H   = "325"
TOKEN_1  ="eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzNjc0In0.iXsl3X05KGJ3ZtRLc-PrqeAJy_KpmTHRG"

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

"""funksjon som bare lager en liste med 2 members T=20 og H=50 og returnerer den"""
def generer_data():
    T=20
    H=50
    L=[T,H]
    return L #returnerer ett array

def main(): 
    """setup, sett ting her som bare skal kjøres en gang eller initialbetingelser"""
    currentstate=state[0]
    A=1
    nextstate=0
    while(True):
        """her er loop """
        time.sleep(1)
        print()
        
         """Mangler en state machine/logikk"""

        data=generer_data()
        print(data)
        currentstate=state[nextstate]

if __name__ == '__main__':
    print('starting')
    main()
