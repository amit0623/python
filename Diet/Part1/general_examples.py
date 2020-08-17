
def average(*args):
    return sum(args)/len(args)

# args = pack all the data into a tuple and pass it to the args

print(average(5,10,10,90,100))

list = [3,4,5,6]
print(average(*list))


def calculate_product(*args):
    product=1
    for num in args:
        product *= num
    return product

list1 = [3,4,5,6]
print(calculate_product(10,20,80))
print(calculate_product(*list1))
# Global
x = 7

def access_global ():
    print ("x printed from global scope ", x )

print (access_global())

def modify_global():
    global x
    x = 'hello'
    print ('x printed from modify global ', x )

print (modify_global())
print (x)
#

# functional style programming
values = [1,2,3]
print (sum(values))