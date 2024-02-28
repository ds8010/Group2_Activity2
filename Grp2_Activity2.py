"""
Group 2
Authors:
       1.
       
       2.hamad alsaadi 
       contributed by writing the constants (converesion rates), and the functions for each conversion
       
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
    """This main function prints a menu first and prompts the user to choose an option 
    from the menu and then performs the conversions based on the user's preference."""
    while True: # This while loop helps to repeat the entire conversion process based on user's choices.
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
        if op==1:# AED to Other currencies option
            while True: # This nested while loop helps repeat the "AED to other currencies" option based on user's choices with no need to go back to the main menu.
                print("Sno. \tConversion method       \tConversion Rate ")
                print("********************************************************")
                print("1    \tAED to Euro (EUR)            \t",aed_euro)
                print("2    \tAED to British Pound (GBP)   \t",aed_pound)
                print("3    \tAED to US Dollar             \t",aed_dol) 
                print("********************************************************")
                print("4    \tExit ")
                print("********************************************************")
                choice= int(input("Enter your choice (1/2/3/4):"))
                if choice==1: #Change from AED to Euros
                    print("You are now converting from AED to Euros")
                    amount=float(input("Enter your amount:"))
                    if amount < 0:
                        print("Input Error! Amount should be positive number. " ) 
                        ans=int(input('Enter 1 to go back '))
                        if ans ==1:
                            continue
                    elif amount >=0:
                        aed_to_euro(amount)
                        input('Press Enter to continue conversion ')
                    else:
                        print('Input Error! Try again! ')
                        continue  
                elif choice==2: # Change from AED to BrPound
                    print("You are now converting from AED to British Pounds")
                    amount=float(input("Enter your amount:"))
                    if amount < 0:
                        print("Input Error! Amount should be positive number. " ) 
                        ans=int(input('Enter 1 to go back '))
                        if ans ==1:
                            continue
                    elif amount >=0:
                        aed_to_britishpound(amount)
                        input('Press Enter to continue conversion ')
                    else:
                        print('Input Error! Try again!')
                        continue
                elif choice==3:# Change from AED to Dollars
                    print("You are now converting from AED to US Dollars")
                    amount=float(input("Enter your amount:"))
                    if amount < 0:
                        print("Input Error! Amount should be positive number. " ) 
                        ans=int(input('Enter 1 to go back '))
                        if ans ==1:
                            continue
                    elif amount >=0:
                        aed_to_dollar(amount)
                        input('Press Enter to continue conversion ')
                    else:
                        print('Input Error! Try again!')
                        continue
                elif choice==4: # Exits the "AED to Other currencies" option
                    print("Currency converter is closed!")
                    break
                else:
                    print("Input Error!")
        elif op==2: # "Other currencies to AED" option
            while True: # This nested while loop helps repeat the "AED to other currencies" option based on user's choices with no need to go back to the main menu.
                    print("Sno. \tConversion method       \tConversion Rate ")
                    print("********************************************************")
                    print("1    \tEuro (EUR) to AED            \t",eur_aed)
                    print("2    \tBritish Pound (GBP) to AED   \t",pound_aed)
                    print("3    \tUS Dollar to AED             \t",dol_aed) 
                    print("********************************************************")
                    print("4    \tExit ")
                    print("********************************************************")
                    select= int(input("Enter your choice (1/2/3/4):"))
                    if select==1: #Change from Euro to AED
                        print("You are now converting from Euros to AED")
                        amount=float(input("Enter your amount:"))
                        if amount < 0:
                            print("Input Error! Amount should be positive number. " ) 
                            ans=int(input('Enter 1 to go back '))
                            if ans ==1:
                                continue
                        elif amount >=0:
                            eur_to_aed(amount)
                            input('Press Enter to continue conversion ')
                        else:
                            print('Input Error! Try again!')
                            continue
                    elif select==2: # Change from BrPound to AED 
                        print("You are now converting from British Pounds to AED")
                        amount=float(input("Enter your amount:"))
                        if amount < 0:
                            print("Input Error! Amount should be positive number. " ) 
                            ans=int(input('Enter 1 to go back '))
                            if ans ==1:
                                continue
                        elif amount >=0:
                            britishpound_to_aed(amount)
                            input('Press Enter to continue conversion ')
                        else:
                            print('Input Error! Try again!')
                            continue

                    elif select==3: # Change from Dollar to AED
                        print("You are now converting from US Dollars to AED")
                        amount=float(input("Enter your amount:"))
                        if amount < 0:
                            print("Input Error! Amount should be positive number. " ) 
                            ans=int(input('Enter 1 to go back '))
                            if ans ==1:
                                continue
                        elif amount >=0:
                            dollar_to_aed(amount)
                            input('Press Enter to continue conversion ')
                        else:
                            print('Input Error! Try again!')
                            continue
                    elif select==4:   # Exit the 'Other currencies to AED' option
                        print("Currency converter is closed!")
                        break
                    else:
                        print("Input Error! Try again.")
                        continue
        elif op==3: # Exit the whole process
            print("Currency converter is closed!")
            break
        else:
            print("Input Error! Try again.")
            continue
        a = int(input('Do you want to go back to the first menu? Enter 1 if Yes, 0 if No '))
        if a==1:
             continue
        elif a==0:
             break
        else:
             print('Input Error!')  
             break          

if __name__=="__main__":
    main()















