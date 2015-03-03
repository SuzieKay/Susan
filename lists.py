numbers=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]

#Determining the even and odd numbers from the list
for x in numbers:
	if x%2 ==0:
		even.append(x)
	else:
		odd.append(x)

print even
print odd

#sum of the integers in the even list
total_even=sum(even)
print "The total of the even numbers is : ", total_even

#sum of the integers in the odd list
total_odd=sum(odd)
print "The total of the odd numbers is : ", total_odd

#maximum number in the even list
max_even= max(even)
print "The biggest even number is: ", max_even

#maximum number in the odd list
max_odd= max(odd)
print "The highest odd number is: ", max_odd