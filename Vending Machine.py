def selection(): #Defining the function to select the item
    while True: #This makes it so that you stay here until broken free from the loop
        item = input("""What would you like to buy from the vending machine?
Gatorade: $2
Lays $3
Pringles $5 """)
        item = item.lower() #To make things easier for myself
        if item == "gatorade": #If Gatorade is bought
            price = 2
            return [item.capitalize(), price] #Returning Gatorade and its price
        elif item == "lays": #If Lays is bought
            price = 3
            return [item.capitalize(), price] #Returning Lays and its price
        elif item == "pringles": #If Pringles are bought
            price = 5
            return [item.capitalize(), price] #Returning Pringles and its price
        elif item == "exit": #If you realize that you're too fat and/or broke to be getting more snacks
            return False #Track this false as False #1
        else: #If you somehow manage to mess up a vending machine input
            print("Sorry, that is not a valid input, please try again.")
            continue #This makes you stay in the loop rather than exit it, increasing your pain and suffering

def payment(): #Defining the function to pay for the item
    items = selection() #Calling the selection function and assigning whatever value we got from it to it
    amount = 0
    while True: #Endless loop in case you deposit lesser money than you're supposed to
        if items == False: #Remember False #1?
            return False #This is False #2
        else:
            temp = input(f"You have bought {items[0]}, which costs ${items[1]}, please pay the amount: ") #Taking money
            if temp.lower() == "exit": #If you want out
                print(f"Transaction cancelled, all money spent will be refunded soon.")
                return False #This is ALSO false #2
            temp = int(temp)
            amount += temp #Adding the current balance to the overall balance
            if amount >= items[1]: #If the money is enough/more than enough
                change = amount - items[1]
                print(f"You have successfully paid for {items[0]} with ${amount}, and your change is ${change}.")
                return [items[0], items[1], amount, change] #This will be used to generate your bill
            else: #If you enter less money than needed
                print(f"You have paid ${amount} out of your balance of ${items[1]}, please pay ${items[1] - amount} more.")
                continue #We will keep you hostage until you pay up

def billing(): #Defining the function to generate the bill for the item(s)
  receipt = {} #Think of this as a blank receipt paper
  while True: #This keeps the whole process running until you want out
    bill = payment()
    if bill == False: #This is False #2; if anywhere in the chain of command there was an exit, it leads here
        return receipt #Prints your final bill
    else: #If you want to keep buying snacks (fatty)
        receipt[bill[0]] = [f"Price: ${bill[1]}", f"Paid Amount: ${bill[2]}", f"Change: ${bill[3]}"] #This prints your bill

print(billing())