"""Randomization of list"""
import random

inventory = []
def acquire_item(inventory, item):
    """Appends items to empty inventory list"""
    inventory.append(item)
    print(f"You acquired a {item}")
    return inventory

def display_inventory(inventory):
    """Prints player's current inventory whether blank or filled"""
    if inventory == []:
        print("Your inventory is empty.")
    else:
        print("Your inventory: ")
        item_number = 1
        for item in inventory:
            print(f"{item_number}. {item}")
            item_number += 1

def display_player_status(player_health):
    """Displays the players current health."""
    print(f"Your current health: {player_health}")

def handle_path_choice(player_health):
    """Determine path choice and return updated player health."""
    chosen_path = random.choice(["left", "right"])
    if chosen_path == "left":
        if player_health <= 90:
            player_health += 10
            print("You encounter a friendly gnome who heals you for 10 health points.")
        else:
            player_health = 100
    elif chosen_path == "right":
        player_health -= 15
        print("You fall into a pit and lose 15 health points.")
        if player_health <= 0:
            player_health = 0
            print("You are barely alive!")
    return player_health

def player_attack(monster_health):
    """Simulates player's attack on the monster."""
    monster_health -= 15
    print("You strike the monster for 15 damage!")
    return monster_health

def monster_attack(player_health):
    """Simulates randomized monster attack on the player"""
    if random.random() < 0.5:
        player_health -= 20
        print("The monster lands a critical hit for 20 damage!")
    else:
        player_health -= 10
        print("The monster hits you for 10 damage!")
    return player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """Show player and monster fight until one dies, determines if player wins and finds treasure"""
    while (player_health > 0) and (monster_health > 0):
        monster_health = player_attack(monster_health)
        display_player_status(player_health)
        if monster_health <= 0:
            print("You defeated the monster!")
            return has_treasure
        if player_health <= 0:
            print("Game over!")
            return False
        player_health = monster_attack(player_health)
        display_player_status(player_health)
    return False # boolean

def check_for_treasure(has_treasure):
    """Checks if player obtained the treasure and prints a message to the player"""
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue on your journey")

def main():
    """Initializes variables and sets things up"""
    player_health = 100
    monster_health = 65
    has_treasure = False
    has_treasure = random.choice([True, False])

    player_health = handle_path_choice(player_health)

    treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)

    check_for_treasure(treasure_obtained_in_combat)

    dungeon_rooms = [("old alchemy lab", "healing potion", "puzzle", ("Puzzle solved.", "it's unsolved.", +4))]
    dungeon_rooms.extend(("Abandoned armory", "sword", "trap", ("avoided the trap.", "Trap triggered.", -8)))
    dungeon_rooms.extend(("A dusty library", "map", "none", None))

if __name__ == "__main__":
    main()
