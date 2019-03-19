import math

spacer = str("\n\n\n\n\n")

print("Welcome to the Stock Manager.")
print("...")
print("Version: 0.1\nAuthor: Eraz")
print("...\nPress enter to continue.")
pressEnter = str(input(""))
print("...")

CSparValue = 0
CSissued = 0
CSout = 0
PSparValue = 0
PSissued = 0
PSout = 0
stockAuth = 0
Tstock = 0

while True:
    print("MAIN MENU:")
    print("1 - View stock information\n2 - Edit stock information")
    print("3 - Equity breakdown\n4 - Issue/authorize more shares")
    print("5 - Generate dividends\n6 - Calculate a stock split\n7 - Exit")
    menu = int(input("Enter a number: "))

    if menu == 7:
        break
    
    elif menu == 1:
        print(spacer)
        print("GENERAL:")
        print("Shares authorized: {}".format(stockAuth))
        print("Treasury stock: {}".format(Tstock))
        print("...")
        
        print("COMMON STOCK:")
        print("Issued: {}".format(CSissued))
        print("Outstanding: {}".format(CSout))
        print("Par value: ${}".format(CSparValue))
        print("...")

        print("PREFERRED STOCK:")
        print("Issued: {}".format(PSissued))
        print("Outstanding: {}".format(PSout))
        print("Par value: ${}".format(PSparValue))
        print("...")
        print("Press enter to return to menu.")
        pressEnter = str(input(""))
        print(spacer)
        
    elif menu == 2:
        print(spacer)
        print("Which stocks do you want to edit?")
        print("1 - Common stock\n2 - Preferred stock\n3 - Treasury stock\n4 - Return to menu.")
        editMenu = int(input("Enter a number: "))

        if editMenu == 4:
            print("Returning to menu...")
            print(spacer)
            
        elif editMenu == 1:
            print("...")
            print("Here are the current values for common stock:")
            print("Issued: {}\nOutstanding: {}\nPar value: ${}".format(CSissued, CSout, CSparValue))
            print("...")
            print("Enter the new values you'd like:")
            CSissued = int(input("C.S. Issued: "))
            CSout = int(input("C.S. Outstanding: "))
            CSparValue = int(input("C.S. Par value: "))
            print("Ok. Here are the new values:")
            print("Issued: {}\nOutstanding: {}\nPar value: ${}".format(CSissued, CSout, CSparValue))
            print("Press enter to return to menu.")
            pressEnter = str(input(""))
            print(spacer)
            
        elif editMenu == 2:
            print("...")
            print("Here are the current values for preferred stock:")
            print("Issued: {}\nOutstanding: {}\nPar value: ${}".format(PSissued, PSout, PSparValue))
            print("...")
            print("Enter the new values you'd like:")
            CSissued = int(input("P.S. Issued: "))
            CSout = int(input("P.S. Outstanding: "))
            CSparValue = int(input("P.S. Par value: "))
            print("Ok. Here are the new values:")
            print("Issued: {}\nOutstanding: {}\nPar value: ${}".format(PSissued, PSout, PSparValue))
            print("Press enter to return to menu.")
            pressEnter = str(input(""))
            print(spacer)
            
        elif editMenu == 3:
            print("...")
            print("Currently, the company holds {} treasury stocks.".format(Tstock))
            print("...")
            print("How many treasury stocks have been bought back?:")
            Tstock = int(input("Enter new value: "))
            print("...")
            print("Ok. There are now {} treasury stocks documented.".format(Tstock))
            print("Press enter to return to menu.")
            pressEnter = str(input(""))
            print(spacer)
            
        else:
            print("Unknown input.")
            print(spacer)

        
    elif menu == 3:
        print(spacer)
        print("To begin the equity breakdown process, some values must first be collected:")
        print("...")
        print("There are {} shares of preferred stock issued, with an individual par value of ${}".format(PSissued, PSparValue))
        psPrice = int(input("For how much money was this stock sold: $"))
        print("Ok.\nThere are {} shares of common stock issued, with an individual par value of ${}".format(CSissued, CSparValue))
        csPrice = int(input("For how much money was this stock sold: $"))
        print("Ok.\nFinally, what are the company's retained earnings?")
        retainedE = int(input("Enter: $"))
        print("...")
        print("TOTAL SHAREHOLDERS' EQUITY:")
        TSE = int(psPrice + csPrice + retainedE)
        print("${}".format(TSE))
        contSH = int(psPrice + csPrice)
        cSHperDec = float(contSH / TSE)
        cSHper = float(100 * cSHperDec)
        print("CONTRIBUTIONS BY SHAREHOLDERS/OWNERS:")
        print("${}".format(contSH))
        print("{}%".format(cSHper))
        print("CONTRIBUTIONS FROM OPERATIONS:")
        print("${}".format(retainedE))
        cOperPerDec = float(retainedE / TSE)
        cOperPer = float(100 * cOperPerDec)
        print("{}%".format(cOperPer))
        print("...\nPress enter to return to menu.")
        pressEnter = str(input(""))
        print(spacer)

    elif menu == 4:
        print(spacer)
        print("Ok. So you want to issue more shares of stock.")
        print("How many new shares have been authorized?")
        addAuth = int(input("Authorized shares: "))
        print("Next up, how many more shares of common stock should be issued?")
        addCS = int(input("Common stock: "))
        print("Now, how many more shares of preferred stock should be issued?")
        addPS = int(input("Preferred stock: "))
        print("Ok. These values will be added to the number of issued shares.")
        CSissued = CSissued + addCS
        PSissued = PSissued + addPS
        stockAuth = stockAuth + addAuth
        print("Press enter to return to menu.")
        pressEnter = str(input(""))
        print(spacer)
        
    elif menu == 5:
        break ##
    elif menu == 6: 
        break ##
    else:
        print("Unknown input. Press enter to return to main menu.")
        pressEnter = str(input(""))
        print(spacer)
