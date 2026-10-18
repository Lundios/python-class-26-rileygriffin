# Starting file for LAB 3-1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Lab Activity 3
# October 15, 2026
# Riley Griffin
# display a welcome message
print("The Miles Per Gallon program")
print()

more_trips = "y"
while more_trips.lower() == "y":

# get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:   "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
    # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        total_gas_cost = round(gallons_used * cost_per_gallon, 2)
        cost_per_mile = round(total_gas_cost / miles_driven, 1)

        print()
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost)
        print("Cost Per Mile:             ", cost_per_mile)

    print()
    more_trips = input("Get entries for another trip (y/n)? ")

print()
print("Bye!")
