number = int(input("Enter a number : "))
count = 0

for i in range(2, number+1):
	if number%i == 0:
		count+=1
if count==1:
	print("It's prime...")
else:
	print("It's not prime...")
