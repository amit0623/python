# age = input ("how old are you ")
#
# print (age)
# if (int(age) > 18) :
#     print("you can vote ")
# else:
#     print ( "you cant vote ")



# While loop

curr_num =1
while curr_num <= 15 :
    print("Video" , curr_num)
    curr_num +=1

prompt = "\n Tell me something, and i will repeat it back to you : "
prompt += "\n Enter 'quit' to exit"

active= True
#
# while active == True:
#     message = str(input(prompt))
#
#     print('You entered ', message )
#
#     if message == 'quit' :
#         active = False
#     else:
#         print(message)
#
# prompt = "\n Tell me something, and i will repeat it back to you : "
# prompt += "\n Enter 'quit' to exit"

# active= True
#
# while active == True:
#     message = str(input(prompt))
#
#     print('You entered ', message )
#
#     if message == 'quit' :
#         break
#     else:
#         print(message)
print("curr num")
curr_num = 0
while curr_num < 10 :
    curr_num += 1
    if curr_num % 2 == 0 :
        continue
    print(curr_num)

# Moving items fromone list to another

unconfirmed_user = ['amit','brian','shelley']
confirmed_user = []

while unconfirmed_user :
    curr_user = unconfirmed_user.pop()
    print("Verifying User :" ,curr_user)
    confirmed_user.append(curr_user)

#Display
print("The following ")
for cu in confirmed_user:
    print ( "The confirmed user is \t" , cu )

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets  :
    print(pets )
    pets.remove('cat')

print(pets)

# Filling a Dict based on user prompt
responses = {}
# set a flag based on the user polling
polling_active = True


while polling_active:
    name = input ("\n What is your name ")
    response = input("\nWhat mountain you wanna climb ")
    responses[name] = response

    more = input("\n Do you wanna add one more person (yes/no)")
    if more == 'no':
        polling_active = False

print("\n Poll results " )

for name, response in responses.items():
    print("\t" , name , "Wants to climb \t", response)