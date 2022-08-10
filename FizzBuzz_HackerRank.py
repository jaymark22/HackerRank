#if 3 and 5 fizz buzz
#if 3 only fizz
#if 5 only Buzz
# if not value
#FirsSolution Without Function
BaseNumber = 1
MaxNumber = int(input("Enter your choice: "))

while BaseNumber != (MaxNumber +1):
    Result = {
   "Mod15": "FizzBuzz",
   "Mod3": "Fizz",
   "Mod5": "Buzz"}
    if BaseNumber % 15 == 0:
        print(Result.get("Mod15"))
    elif BaseNumber % 3 == 0:
        print(Result.get("Mod3"))
    elif BaseNumber % 5 == 0:
        print(Result.get("Mod5"))
    else:
        print(BaseNumber)
    BaseNumber += 1
