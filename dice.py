import random

def parse_input(input_string):
    """Return `input_string` as num between 1 and 6.

    Check if `input_string` is num between 1 and 6.
    If so, return num with the same value. Otherwise, tell  user to enter valid number and quit program.

    """
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

def roll_dice(num_dice):
  """ Return list of integers with length `num_dice`

  Each num in return list is random num between 1 - 6 

  """
  roll_results = []
  for _ in range(num_dice):
    roll = random.randint(1, 6)
    roll_results.append(roll)
  return roll_results


# ~~~ App's main code block ~~~
# Get and validate user input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
# Roll dice
roll_results = roll_dice(num_dice)

print(roll_results)

