import random

#Prints first welcome message
print("Welcome to RPS 9000!")
print("====================")

#First function that converts text to emoji equivalent
def emoji(content):
  if content == "rock":
    return "🗿"
  elif content == "paper":
    return "📄"
  elif content == "scissors":
    return "✂️"

#Initiates main game loop
while True:
  possible_choices = ["rock", "paper", "scissors"]
  ai_output = random.choice(possible_choices)
  
  #User input + error handling
  while True:
    user_input = input("Rock, paper, or scissors? >> ")
    user_input = user_input.strip()
    user_input = user_input.lower()

    if user_input == "":
      print("You can't leave this field blank!")
      continue
    elif user_input not in possible_choices:
      print("Please enter a valid choice!")
      continue
    else:
      break
  
  #Conditions for results of round
  if user_input == ai_output:
    print(f"""
    ----
    You: {emoji(user_input)}
    AI: {emoji(ai_output)}
    ----
    It's a tie!
    """)

  elif user_input == "rock" and ai_output == "scissors":
    print(f"""
    ----
    You: {emoji(user_input)}
    AI: {emoji(ai_output)}
    ----
    You win!
    """)

  elif user_input == "paper" and ai_output == "rock":
    print(f"""
    ----
    You: {emoji(user_input)}
    AI: {emoji(ai_output)}
    ----
    You win!
    """)

  elif user_input == "scissors" and ai_output == "paper":
    print(f"""
    ----
    You: {emoji(user_input)}
    AI: {emoji(ai_output)}
    ----
    You win!
    """)

  else:
    print(f"""
    ----
    You: {emoji(user_input)}
    AI: {emoji(ai_output)}
    ----
    You lose!
    """)
  
  #Gives the user a chance to play again
  play_again = input("Would you like to play again? (y/n) >> ")
  play_again = play_again.strip()
  play_again = play_again.lower()
  

  if play_again == "y":
    continue
  else:
    print("Thanks for playing!")
    break