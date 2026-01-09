import decks
import random


def show_roles(playercount):
    for i in range(playercount):
        player_num = i+1
        # if player_num != imposter_player_num:
            # print("Category: " + )
        imposter_player_num = random.randint(1,playercount)
        
def get_category(category):
    if category in decks.master_deck:
            return decks.master_deck[category]

def pick_key_value(category_deck):
    # Picks a random key-value pair from the selected category deck
    category_list = list(category_deck.keys())
    key = random.sample(category_list,1)[0]
    value = category_deck[key]
    return key, value
def main():
    print("Welcome to Imposter!")
    playercount = int(input("How many players are playing? "))
    print(playercount)
    category = input("What category would you like to play? (Options: Animals, Clash Royale)")
    category_deck = get_category(category.lower())
    print(category_deck)
    key, value = pick_key_value(category_deck)
    print("Word: " + key)
    print("Hint: " + value)
    

if __name__ == "__main__":
    main()
