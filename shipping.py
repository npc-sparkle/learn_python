weight = 41.5

## ground shipping

flat_charge = 20

if weight <= 2:
  print(flat_charge + weight * 1.50)
if weight > 2 and weight <= 6:
  print(flat_charge + weight * 3)
if weight > 6 and weight <= 10:
  print(flat_charge + weight * 4)
if weight > 10:
  print(flat_charge + weight * 4.75)

## ground shipping premium
ground_shipping_premium = 125
print("Ground shipping premium costs $", ground_shipping_premium)


## drone shipping
if weight <= 2:
  print(weight * 4.50)
if weight > 2 and weight <= 6:
  print(weight * 9)
if weight > 6 and weight <= 10:
  print(+ weight * 12)
if weight > 10:
  print(+ weight * 14.25)
