import random
name=input("Enter your name:")
print(f"Hello {name}, You are welcome to the number guessing game")
low=int(input("Enter the lower range:"))
high=int(input("Enter the higher range:"))
random_number=random.randint(low,high)
count=0
ans=None
while (ans!=random_number):
    count+=1
    ans=int(input(f"Guess a number between {low} and {high}:"))
    if(ans==random_number):
        print(f"Congrats {name}!! you guessed the number in {count} attempts")
    elif(ans<random_number):
        print("Your guess is too low")
    else:
        print("Your guess is too high")