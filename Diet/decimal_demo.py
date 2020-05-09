# calc grade on user input , display average

from decimal import Decimal
principal =  Decimal('100000')
rate = Decimal('0.05')

# Do calculation among decimal objects.

# Add / Sub / Mult is allowed 

for year in range ( 1 , 11 ):
    amount = principal* (1 + rate) ** year # New Prin amount 
    print(f'{year:>2}{amount:>10.2f}')
     