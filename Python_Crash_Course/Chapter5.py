cars = ['audi','bmw','subaru','toyota']

for car in cars :
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# you can use the .lower() function to test for values that are not case sensitive.

requested_toppings = ['mushrooms', 'onions','green peppers', 'pineapple']
print ("\n",'mushrooms' in requested_toppings)

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry , no green peppers ")
    else :
        print("adding ", requested_topping)

# search for requesed toppings in the available toppings list

available_toppings = ['mushrooms', 'olives', 'green peppers',
                         'pepperoni', 'pineapple', 'extra cheese']

# iterate
for requested_topping in requested_toppings :
    if requested_topping in available_toppings:
        print("Adding ", requested_topping)
    else:
        print( requested_topping, "Requested topping is not avaailable")

# example

username = ['amit','mayank', 'reyansh','ss','admin']
username = []
if not username:
    print("We need to find some users!")
for user in username:

    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else :
        print("Hello ", user, "thank you for logging in again.")

