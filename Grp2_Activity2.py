"""
Group 2
Authors:
       1.
       2.
       3.Yosef Shibele
           Contributed on the main.
Manifesto :This Program is written to act like a currency converter.
           It has two options: Converting from AED to other currencies and Converting other currencies to AED.
"""

'''constant conversion rates'''
aed_euro=0.25          #conversion rate from AED to Euro
aed_pound=0.22         #conversion rate from AED to Pound  
aed_dol=0.27           #conversion rate from AED to Dollars 
dol_aed=3.67           #conversion rate from Dollar to AED 
pound_aed=4.64         #conversion rate from Pound to AED
eur_aed=3.98           #conversion rate from Euro to AED 

def aed_to_euro(money):
    """converting from AED to EURO"""
    eur=money*aed_euro
    print(money,"AED is equal to",eur,"EUR")
def aed_to_britishpound(money):
    """converting from AED to british pound""" 
    pound=money*aed_pound
    print(money,"AED is equal to",pound,"british pound")
def aed_to_dollar(money):
    """converting from aed to dollars"""
    dollar=money*aed_dol
    print(money,"AED is equal to",dollar,"USD")
def dollar_to_aed(amount):
    """converting from dollars to AED"""
    aed=amount*dol_aed
    print(amount,"USD is equal to",aed,"AED")

def britishpound_to_aed(amount):
    """converting from Pound to AED"""
    aed=amount*pound_aed
    print(amount,"pound is equal to",aed,"AED")

def eur_to_aed(amount):
    """ converting from Euro to AED"""
    aed=amount*eur_aed
    print(amount,"EUR is equal to",aed,"AED")
    
def main():
    while True:
        print('''    
*************************
    CONVERSION MENU
*************************
1. AED to other currencies
2. Other Currencies to AED
3. Exit
**************************
            ''')
        op=int(input("Enter your choice (1/2/3):"))
        if op==1:
            while True:
                print("Sno. \tConversion method       \tConversion Rate ")
                print("********************************************************")
                print("1    \tAED to Euro (EUR)            \t",aed_euro)
                print("2    \tAED to British Pound (GBP)   \t",aed_pound)
                print("3    \tAED to US Dollar             \t",aed_dol) 
                print("********************************************************")
                print("4    \tExit ")
                print("********************************************************")
                choice= int(input("Enter your choice (1/2/3/4):"))
                if choice==1:
                    print("You are now converting from AED to Euros")
                    amount=float(input("Enter your amount:"))
                    aed_to_euro(amount)   
                elif choice==2:
                    print("You are now converting from AED to British Pounds")
                    amount=float(input("Enter your amount:"))
                    aed_to_britishpound(amount)
                elif choice==3:
                    print("You are now converting from AED to US Dollars")
                    amount=float(input("Enter your amount:"))
                    aed_to_dollar(amount)
                elif choice==4:
                    print("Currency converter is closed!")
                    break
                else:
                    print("Input Error!")
        elif op==2:
            while True:
                    print("Sno. \tConversion method       \tConversion Rate ")
                    print("********************************************************")
                    print("1    \tEuro (EUR) to AED            \t",eur_aed)
                    print("2    \tBritish Pound (GBP) to AED   \t",pound_aed)
                    print("3    \tUS Dollar to AED             \t",dol_aed) 
                    print("********************************************************")
                    print("4    \tExit ")
                    print("********************************************************")
                    select= int(input("Enter your choice (1/2/3/4):"))
                    if select==1:
                        print("You are now converting from Euros to AED")
                        amount=float(input("Enter your amount:"))
                        eur_to_aed(amount) 
                    elif select==2:
                        print("You are now converting from British Pounds to AED")
                        amount=float(input("Enter your amount:"))
                        britishpound_to_aed(amount)
                    elif select==3:
                        print("You are now converting from US Dollars to AED")
                        amount=float(input("Enter your amount:"))
                        dollar_to_aed(amount)
                    elif select==4:
                        print("Currency converter is closed!")
                    else:
                        print("Input Error! Try again.")
                        continue
                    break
        elif op==3:
            print("Currency converter is closed!")
            break
        else:
            print("Input Error! Try again.")
            continue
        a = int(input('Do you want to continue conversion? Enter 1 if Yes, 0 if No '))
        if a==1:
             continue
        elif a==0:
             break
        else:
             print('Input Error!')  
             break          

if __name__=="__main__":
    main()
           















