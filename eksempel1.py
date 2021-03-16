#Dette er en uferdig state maskin, den printer bare meldingen i state 0
import time

state ={0: "null", 1:"en", 2:"to",3:"tre"} #vi bruker dette dictet som en enum i arduino. Det er likevel stor forskjell mellom datatypene så undersøk hva et dict er om du er usikker.
currentstate=state[0] #setter første state til null.

def antall_epler(num): #denne funksjonen printer antall epler
    a=1
    print("jeg har "+str(a)+" epler") #printer "jeg har N epler" ved concatenating


def main(): 
    """setup, sett ting her som bare skal kjøres en gang eller initialbetingelser"""
   
    while(True):
        """her er loop """
        time.sleep(1) #vent i ett sekund
        print()
        print("state er "+str(currentstate)) 
         """Mangler en state machine/logikk"""
        if(currentstate=="null"):
            antall_epler(0)             
        elif(currentstate=="en"):    
            antall_epler(1)


if __name__ == '__main__':
    print('starting')
    main()
