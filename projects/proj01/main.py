# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Project 1
# October 31, 2026
# Riley Griffin

#Greet the customer and introduce your sales program.
print("=" * 47)
print(" Welcome to super amazing and awesome products".upper())
print("=" * 47)
print("Hey, I'm John a sales associate\n")

while True:
    price = 2.00
    userInterest = input("Would you like to learn about our products? ").lower()

    #If yes, provide a short overview of the product or service.
    if userInterest == "y" or userInterest == "yes" :
        #Provide a creative paragraph overview of your product or service.
        print("\nOh...\nno one is actually supposed to say yes...")
        print("Well to be honest I wasn't ready for this, give me a second\n")
        print("Honestly I don't have any products to sell")
        print("But! I do have this!\n")
        print("*pulls out a pen*\n")
        print("Here it is! The amazing, trusty, Ballpoint Pen!")
        print("This puppy comes with PLENTY of features,\nInk!\nA point that is a ball!\n And a button that clicks!")
        print("Now don't be too amazed with this rare find.\n")

        #Ask if the user would like to make a purchase.
        while True:
            buy = input("Would you be interested in buying this PEN? ").lower()

            #If yes, continue with the sale.
            if buy == "y" or buy == "yes" :
                #Ask for the customer’s first and last name and store them in variables.
                print("\nYou're seriously doing this??")
                print("Thank you!\nI'm just going to need some of your information.")
                firstName = input("What is your first name? ")
                lastName = input("What is your last name? ")

                #Ask for their email address and phone number (no validation needed at this point).
                print()
                email = input("What is your email address? ")
                phone = input("What is your phone number? ")

                #Tell the customer how much the product or service costs.
                print()
                print(f"Thank you for providing your information {firstName} {lastName}.")
                print(f"These Pens will cost you ${price} each!\n")

                #Ask how many items they want to purchase.
                while True:
                    quantity = (input("how many pens would you like? "))
                    if quantity.isdigit() and int(quantity) > 0 :
                        quantity = int(quantity)
                        break
                    else : 
                        print("\nThat is NOT a number try again.")
                if quantity > 10 :
                    print("\nDo you think I'm some kind of joke? carrying around that many pens? Do I look like a pen salesman?\n Have it your way but the price is going up")
                    price = 3.00
                elif quantity > 3 :
                    print(f"\nUmmm.. I'm sorry to say {firstName} but I only have a limited amount of pens so lets just call it 3!")
                    quantity = 3

                #Calculate and display the subtotal (quantity × price).
                subtotal = quantity * price

                #Apply a 10% sales tax.
                tax = subtotal * .10

                #Calculate and display the total amount due.
                total = subtotal + tax
                print()
                print(f"Subtotal:  ${subtotal}")
                print(f"Tax (10%): ${tax}")
                print(f"Total:     ${total}")

                #Create a formatted receipt
                print()
                print("*" * 32)
                print("          pen receipt".upper())
                print("*" * 32)

                print(f"Customer:   {firstName} {lastName}")
                print(f"Email:      {email}")
                print(f"Phone:      {phone}")
                print("-" * 32)

                print("Item:        PEN")
                print(f"Quantity:   {quantity}")
                print(f"Price per:  {price}")
                print("-" * 32)

                print(f"Subtotal:  ${subtotal}")
                print(f"Tax (10%): ${tax}")
                print(f"Total:     ${total}")
                print("*" * 32)
                print()

                #End with a thank-you message and farewell.
                print("Thank you so much for the money I needed this.")
                print("Toodaloo!")
                break

            #If no, display a farewell and end the program.
            elif buy == "n" or buy == "no" :
                print("\nJust what I expected, another rejection. Whatever. Bye.")
                break
            else : 
                print("\nI'm not familiar with what that means...")
                print("you're supposed to say like, yes or no....")
                print("even a Y or a n would work... try harder..")
        break

    #If no, end the conversation politely with a farewell message.
    elif userInterest == "n" or userInterest == "no" :
       print("\nJust what I expected, another rejection. Whatever. Bye.")
       break
    else:
      print("\nI'm not familiar with what that means...")
      print("you're supposed to say like, yes or no....")
      print("even a Y or a n would work... try harder..")
