n = int(input("Enter a number : "))

for i in range(1, n):
    if(n%i) == 0:
        print("number is not prime")
        break

else:
    print("number is prime")