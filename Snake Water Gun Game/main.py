import random
rules = {
    's': 'w',
    'w': 'g',
    'g': 's'
}
names = {
    's': 'Snake',
    'w': 'Water',
    'g': 'Gun'
}

user_score = 0
computer_score = 0

while True:    
    computer = random.choice(['s', 'w', 'g'])
    you = input("Enter 's' (Snake), 'w' (Water), 'g' (Gun) or 'q' to quit: ").lower().strip()

    if you == 'q':
        print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing! See You Next Time!")
        break

    if you not in ['s', 'w', 'g']:
        print("Invalid input! Please choose 's', 'w', 'g' or 'q'.")
        continue

    print(f"You chose {names[you]}, Computer chose {names[computer]}")

    if you == computer:
        print("🤝 It's a tie!")
    elif rules[you] == computer:
        print("🎉 You win ")
        user_score += 1
    else:
        print("💻 Computer wins!")
        computer_score += 1

    print(f"Current Score -> You: {user_score} | Computer: {computer_score}")


