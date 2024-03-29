import random

def main():
  dice_rolls = int(input("How many dice would you like to roll? "))
  dice_size = int(input("How many sides are the dice? "))
  

  player_count = int(input("How many players? "))
  player_names = [''] * player_count
  for j in range(0,player_count):
    player_names[j] = input(f"Name of player {j}: ")
  
  for p in player_names:
    print(f"{p}'s round:")
    dice_sum = 0

    for i in range(0,dice_rolls):
      roll = random.randint(1, dice_size)
      dice_sum = dice_sum+roll

      if roll == 1:
        print(f"You rolled a {roll}! Critical Fail")
      elif roll == dice_size:
        print(f"You rolled a {roll}! Critical Success!")
      else:
        print(f'You rolled a {roll}')

    print(f"{p} have rolled a total of {dice_sum}")

if __name__== "__main__":
  main()