def FizzBuzz(n):
    Output = []
    Base = 1
    m = n +1
    while Base != m:
        if (Base % 3 ==0) and (Base % 5 ==0):
            Output.append("FizzBuzz")
        elif (Base % 3 ==0) and (Base % 5 !=0):
            Output.append("Fizz")
        elif (Base % 3 !=0) and (Base % 5 ==0):
            Output.append("Buzz")
        else:
            Output.append(str(Base))
        Base += 1
    return Output



 


User = int(input("Your favorite number is: "))
print(FizzBuzz(User))

