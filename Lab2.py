# Program Name: Lab2.py
# Course: IT1114/ Section BWE
# Student Name: Kendres Rhodes
# Assignment Number: Lab2
# Due Date: 09/01/2024
# Purpose: This program will calculate the total food cost for a hackathon, including the cost for pizzas and salads, number of pizzas needed, discounts, delivery charges, and total amount due.
# Sources:

# IMPORTING LIBRARY
import math

# PRICING AND DISCOUNTS
PIZZA_COST = 15.99  #COST OF 1 PIZZA
PIZZA_SLICES = 12   #NUMBER OF SLICES PER PIZZA
SALAD_COST = 7.99   #COST PER SALAD
SLICE_PER_PERSON = 3 #SLICES GIVEN TO EACH PERSON
DISCOUNT_MAX = 10   #NUMBER OF ITEMS GIVEN THE DISCOUNT
DISCOUNT_RATE = 0.15 #15% DISCOUNT RATE
DELIVERY_MIN = 20.00 #MINIMUM DELIVERY FEE
DELIVERY_RATE = 0.07 #7% DELIVERY FEE RATE

#RECIEVE USER INPUT FOR NUMBER OF PIZZAS AND SALADS ORDERED
num_pizzas_ordered = int(input("Number of pizza orders ")) #Number of people who ordered pizza
num_salads_ordered = int(input("Number of salad orders ")) #Number of people who ordered a salad

#CALCULATION OF PIZZAS NEEDED
slices_needed = num_pizzas_ordered * SLICE_PER_PERSON
pizzas_needed = math.ceil(slices_needed  / PIZZA_SLICES) #CEIL

#Calculation of pizza cost
pizza_cost = pizzas_needed * PIZZA_COST

#Calculation of salad cost
salad_cost = num_salads_ordered * SALAD_COST

#Discounts added
if pizzas_needed > DISCOUNT_MAX:
    pizza_discount = pizza_cost * DISCOUNT_RATE
else:
    pizza_discount = 0

if num_salads_ordered > DISCOUNT_MAX:
    salad_discount = salad_cost * DISCOUNT_RATE
else:
    salad_discount = 0
total_discount = pizza_discount + salad_discount
#Total cost before discount
total_cost_before_discount = pizza_cost + salad_cost

# Delivery Fee
delivery_fee = max(DELIVERY_RATE * total_cost_before_discount, DELIVERY_MIN)

#Total amount due
total_amount_due = total_cost_before_discount + delivery_fee - total_discount
#print outputs
print(f"Pizzas ordered: {pizzas_needed}")
print(f"Pizza cost $ {pizza_cost}")
print(f"Salad cost $ {salad_cost}")
print(f"Total $ {total_cost_before_discount}")
print(f"Discount $ {total_discount}")
print(f"Delivery fee $ {delivery_fee}")
print(f"Total amount due $ {total_amount_due}")