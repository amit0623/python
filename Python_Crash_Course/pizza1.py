def make_pizza(size , *toppings) :
    print(f"\n Making a {size}-inch pizza using these toppings : ")
    for toping in toppings:
        print(f"- {toping}")
