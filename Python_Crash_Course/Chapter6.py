
alien_o = {'color' : 'green' , 'points':5 }
print(alien_o)
print(type(alien_o))

print(alien_o['color'])

print(alien_o['points'])

# add a key value pair

alien_o['x_alignment']= 0

alien_o['y_alignment']= 30

print(alien_o)

# how to fill up an empty dict

alien_o = {}
alien_o['color']='green'
alien_o['points'] = 7

print(alien_o)

# modify

alien_o['color']='orange'

print(alien_o)

# Compute the new position of alient based on speed

alien_o = {'x_position':0 , 'y_position':25,'speed':'medium'}
x_increment = 0
print(alien_o)

if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium' :
    x_increment = 2
else:
    x_increment = 3
alien_o['x_position'] +=  + x_increment

print(alien_o)

del alien_o['speed']
print(alien_o)

fav_lang = {
    'amit' : 'python' ,
    'sasha' : 'c',
    'mayank' : 'java'
}

print(fav_lang['amit'])

# using the get function

alien_o = {'color': 'green', 'speed': 'slow'}

color_val =alien_o.get('color')
print("value of color = " ,color_val)

x_cor =alien_o.get('x_position','Not found')
print("value of x_position = " ,x_cor)


# Iteratinf over a dck

user_0  = {
    'username':'amit0623',
    'first':'amit',
    'last':'kumar'

}
for key,value in user_0.items():
    print ("key = " , key,"" )
    print("value = " , value, "\n")

#

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

my_friend = ['jen']

for name in favorite_languages:
    if name in my_friend:
        print("The fac lang of my fiend " ,name, "is" , favorite_languages.get(name))


for name in sorted(favorite_languages) :
    print("name in sorted order = " , name)

for language in favorite_languages.values():
    print ( "languages selected = " , language)

    # uniq
for language in set(favorite_languages.values()):
    print("distinct languages entered = " ,language)

# building a pizzza

pizza = {
    'crust':'thick',
    'toppings':['mishroom','olives','cheese','jalepino']
}

print("You order a pizza of type " , pizza['crust'],
      "with following toppings " )
for topping in pizza['toppings']:
    print("\t " , topping)

    # Extract and show key data of a dict consisting
    # of lists

favorite_languages = {
    'jen':['python','ruby','lisp'],
    'sarah':['c'],
    'amit':['java','python'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

for name, language in favorite_languages.items() :
    print("For the person named " , name)
    for language_name in language :
        print("\t",language_name)

# Nesting Dict in a Dict

users = {
    'aeinstein' : {
        'first':'albert',
        'last':'einstein',
        'location' : 'princeton'
    },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'
    }
}

for name , user_info in users.items():
    print("name = " , name)
    print("\t" ,user_info['first'] , "  " , user_info['last'] )
    print("location : " , user_info['location'])

