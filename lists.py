numbers=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]

for x in numbers:
	if x%2 ==0:
		even.append(x)
	else:
		odd.append(x)

print even
print odd

total_even=sum(even)
print "The total of the even numbers is : ", total_even

total_odd=sum(odd)
print "The total of the odd numbers is : ", total_odd

max_even= max(even)
print "The biggest even number is: ", max_even



max_odd= max(odd)
print "The highest odd number is: ", max_odd