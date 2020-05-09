# calc grade on user input , display average

from statistics import mean, median, mode

grades = [ 85, 93,45,89, 85,99 ]

print(sum(grades) )
print ( 'Average = ' , sum(grades) / len ( grades ))
print ("using statistics library  \n ")
print ("Mean : " , mean(grades))
print ("Median : " , median(grades))
print ("Mode : " , mode(grades))
print ("Sorted  : " , sorted(grades))

