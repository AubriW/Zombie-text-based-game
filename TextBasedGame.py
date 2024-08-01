#Aub

import os


# Welcome prompt for player
def prompt():
    print("Welcome to the zombie apocalypse game!!\n"
          "You must collect all the items to escape this desolate town run by the evil scientist.\n"
          "But beware, running into him can lead to death\n"
          "Moves: go {north, south, east, west}\n"
          "get {item}\n")
    input("Press a key to continue to the game")


# Clearing screen for player
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Room Dictionary
rooms = {
    'Hospital': {'North': 'Abandoned House', 'South': 'Train station', 'West': 'Weapon Supplies', 'East': 'Sewer'},
    'Abandoned House': {'East': 'Supermarket', 'South': 'Hospital', 'Item': 'Survivors journal'},
    'Supermarket': {'West': 'Abandoned House', 'Item': 'Edible food'},
    'Weapon Supplies': {'East': 'Hospital', 'Item': 'Tactical gear'},
    'Train station': {'East': 'Nursery', 'North': 'Hospital', 'Item': 'Flashlight'},
    'Nursery': {'West': 'Train station', 'Boss': 'Mad scientist'},
    'Sewer': {'West': 'Hospital', 'North': 'Secret lab', 'Item': 'Crowbar'},
    'Secret lab': {'South': 'Sewer', 'Item': 'Virus serum'}
}

# Player's state
player_state = {
    'current_room': 'Hospital',
    'inventory': []
}


def get_item(nxtMove, player_state, rooms):
    # Check if the action is to get an item
    if len(nxtMove) > 1 and nxtMove[0].lower() == 'get':
        item_name = ' '.join(nxtMove[1:]).title()
        current_room = player_state['current_room']
        if 'Item' in rooms[current_room] and rooms[current_room]['Item'].title() == item_name:
            player_state['inventory'].append(item_name)
            print('You have collected: ' + item_name)
            del rooms[current_room]['Item']
        else:
            print('No such item here.')


def display_current_room_info(player_state, rooms):
    current_room = player_state['current_room']
    print('\nYour current room is the ' + current_room + '.')
    print('Survival bag : ' + str(player_state['inventory']))

    if 'Item' in rooms[current_room]:
        print('You have found an item, the ' + rooms[current_room]['Item'] + '!')
        print('Available item: "' + rooms[current_room]['Item'] + '"')

    directions = [direction for direction in rooms[current_room] if direction in ['North', 'South', 'East', 'West']]
    if directions:
        print('Available directions: ' + ', '.join(['"Go ' + direction + '"' for direction in directions]))

    print('   ----------------------\n')
    print('   ----------------------\n')


def main():
    prompt()
    clear()
    while True:
        display_current_room_info(player_state, rooms)

        # Check if the player has collected all 6 items
        if len(player_state['inventory']) == 6:
            print('Congratulations! You have collected all the items and defeated the mad scientist!')
            print('Humanity is saved!')
            break

        # Check if the player encounters the boss
        current_room = player_state['current_room']
        if 'Boss' in rooms[current_room]:
            if len(player_state['inventory']) < 6:
                print('Oh no! You lost to the ' + rooms[current_room]['Boss'] + ', humanity is doomed forever!')
                break
            else:
                print('You have conquered the ' + rooms[current_room]['Boss'] + '! You have saved the town!')
                break

        # Get the player's next action
        nxtMove = input("What is your next action? ").split()

        # Do the action
        if len(nxtMove) > 0:
            action = nxtMove[0].lower()
            if action == 'get':
                get_item(nxtMove, player_state, rooms)
            elif action == 'go':
                if len(nxtMove) > 1:
                    direction = nxtMove[1].title()
                    current_room = player_state['current_room']
                    if direction in rooms[current_room]:
                        player_state['current_room'] = rooms[current_room][direction]
                        print('You moved to the ' + player_state['current_room'] + '.')
                    else:
                        print('You cannot travel there!')
                else:
                    print('No direction specified.')
            else:
                print('Invalid action.')
        else:
            print('No action specified.')


# Run the game
main()
