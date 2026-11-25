# Starting file for LAB 8
# Include your course number, student first and last name, and date in the comment header
# CS 31 Lab Activity 8
# November 25, 2026
# Riley Griffin

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale

#set currency to usd
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)  

    subtotal = order_total - discount

    #Add a shipping cost
    shipping_percent = Decimal(".085")
    shipping_cost = subtotal * shipping_percent
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)

    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP) 

    invoice_total = subtotal + sales_tax + shipping_cost

    #format to dollar sign
    order_total_str = locale.currency(order_total, grouping=True)
    invoice_total_str = locale.currency(invoice_total, grouping=True)

    # display the results
    print(f"Order total:        {order_total_str:>10}")
    print(f"Discount amount:    {discount:>10}")
    print(f"Subtotal:           {subtotal:>10}")
    print(f"Shipping cost:      {shipping_cost:>10}")
    print(f"Sales tax:          {sales_tax:>10}")
    print(f"Invoice total:      {invoice_total_str:>10}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
