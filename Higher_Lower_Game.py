#Higher Power Game
from Data import celebrities
import random

def get_data_set():
  return random.choice(celebrities)


  
def get_celebs_name(aa_set):
  return aa_set["Name"]

def get_celebs_description(aa_set):
  return aa_set["Description"]

def get_celebs_country(aa_set):
  return  aa_set["Country"]
  
def get_followers_winner(aa_set, bb_set):
  count_a=  aa_set["Followers"]
  count_b=  bb_set["Followers"]
  if count_a > count_b:
    return "a"
  else:
    return "b"
    
  
  


game_continue = True
your_score = 0

a_set = get_data_set()
b_set = get_data_set()


while game_continue:
  a_set = b_set
  b_set = get_data_set()

  while a_set == b_set:
    b_set = get_data_set()
  
  name_a = get_celebs_name(a_set)
  description_a = get_celebs_description(a_set)
  country_a = get_celebs_country(a_set)
  
  name_b = get_celebs_name(b_set)
  description_b = get_celebs_description(b_set)
  country_b = get_celebs_country(b_set)
  
  print(f"Compare A: {name_a},a {description_a}, from {country_a}.")
  print("V/S")
  print(f"Compare B: {name_b},a {description_b}, from {country_b}.")

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  correct_value = get_followers_winner(a_set,b_set)
  if guess == correct_value:
    your_score += 1
    print(f"Your guess is correct, Your score: {your_score}")
  else:
    print(f"Your guess is not correct, You loose with score: {your_score}")
    game_continue = False
    
     
     
  
