import pizza2

def hello():
    """ This function is used to prit Hello Worls """
    print("Hello")


def animal_type(animal_type, animal_name):
    print("i have a ", animal_type)
    print(f"my {animal_type}'s name is {animal_name}")

hello()
animal_type('Hamster', 'Harry')

animal_type(animal_type='Hamster', animal_name='Harry')

def describe_animal(animal_type, animal_name='Sally'):
    print("i have a ", animal_type)
    print(f"my {animal_type}'s name is {animal_name}")

describe_animal(animal_type='Hamster')

# Format a name

def get_formatted_name (first,last,middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


musician = get_formatted_name("amit", "kumar")
print(musician)
musician = get_formatted_name("amit", "arora","kumar")
print(musician)

## Define and use a function using a list


def unprinted(unprinted_design,printed_design):
    """ To Print all unprinted data """
    while unprinted_design:
        cd = unprinted_design.pop()
        printed_design.append(cd)

def completed(printed_design ):
    while printed_design:
        print ( "I had printed ", printed_design.pop())

unprinted_design  = ['abc','def','ghi']
printed_design = []

unprinted(unprinted_design,printed_design)
completed(printed_design)

### Using arbitrary number of arguments using dictionary

def build_profile(fname, lname , **user_info):
    user_info['first_name'] = fname # append to last
    user_info['last_name'] = lname   # Append to last
    return user_info

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field = 'physics')

print(user_profile)

#
pizza2.make_pizza(16,'abc')