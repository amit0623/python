from C11_name_function import get_formatted_name

print("Enter 'q' to quit any time " )

while True:
    first = input("\n Please give me first name : ")
    if first == 'q' :
        break

    last = input("\n Please enter the last name ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last )
    print(f"\t Neatly formatted Name : {formatted_name}. ")
