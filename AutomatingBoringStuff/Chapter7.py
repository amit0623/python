import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mobile = phoneNumberRegex.search('My number is 145-555-4224')
print('Phone number found : ' + mobile.group())


ppp
