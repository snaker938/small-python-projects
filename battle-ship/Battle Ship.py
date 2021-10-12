from os import name, system
import itertools


def clear():
    if name == 'nt':
        _ = system('cls')

answer = "Y"





class grid():
    id_iter = itertools.count()

    def __init__(self):

        self.id = next(self.id_iter)
        self.grid = [
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ]

        self.secret_grid = [
        ["?", "?", "?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?", "?", "?"],
        ]


        self.ship_lengths = [2, 3, 4, 5]
        self.ships = ["A", "X", "Y", "Z"]

    
    def print_grid(self):
        for row in self.grid:
            print (" ".join(row))
    def print_secret_grid(self):
        for row in self.secret_grid:
                    print (" ".join(row))

    def add_ship(self, position1, position2, ship, orientation):
        character = self.ships[ship]
        if orientation == "H":
            for i in range(0, self.ship_lengths[ship]):
                if i == 0:
                    self.grid[position1 - 1][position2 -1] = character
                else: 
                    self.grid[position1 - 1][position2 + (i - 1)] = character
        else:
            for i in range(0, self.ship_lengths[ship]):
                if i == 0:
                    self.grid[position1 - 1][position2 -1] = character
                else: 
                    self.grid[position1  + (i - 1)][position2 - 1] = character


    def check_for_good_placement(self, position1, position2, ship, orientation):

        ## Check if ship is out of bounds
        if orientation == "H":
            for i in range(0, self.ship_lengths[ship - 1] + 1):
                if i == self.ship_lengths[ship - 1]:
                    if i + position2 > 9:
                        return True, "The ship will be out of bounds"
        else:
            for i in range(0, self.ship_lengths[ship - 1] + 1):
                if i == self.ship_lengths[ship - 1]:
                    if i + position1 > 9:
                        return True, "The ship will be out of bounds"


        ## Check if ship is going to be placed on top of another ship
        if orientation == "H":
            for i in range(0, self.ship_lengths[ship - 1]):
                if i == 0:
                    if self.grid[position1 - 1][position2 -1] == "A": 
                        return True, "There is already a ship here!"
                    elif self.grid[position1 - 1][position2 -1] == "X": 
                        return True, "There is already a ship here!"
                    elif self.grid[position1 - 1][position2 -1] == "Y": 
                        return True, "There is already a ship here!"
                    elif self.grid[position1 - 1][position2 -1] == "Z": 
                        return True, "There is already a ship here!"
                else: 
                    if self.grid[position1 - 1][position2 + (i - 1)] == "A":
                        return True, "There is already a ship here!"
                    elif self.grid[position1 - 1][position2 + (i - 1)] == "X":
                        return True, "There is already a ship here!"
                    elif self.grid[position1 - 1][position2 + (i - 1)] == "Y":
                        return True, "There is already a ship here!"
                    elif self.grid[position1 - 1][position2 + (i - 1)] == "Z":
                        return True, "There is already a ship here!" 
                    
        else:
            for i in range(0, self.ship_lengths[ship - 1]):
                if i == 0:
                    if self.grid[position1 - 1][position2 -1] == "A":
                        return True, "There is already a ship here!"
                    elif self.grid[position1 - 1][position2 -1] == "X":
                        return True, "There is already a ship here!"
                    elif self.grid[position1 - 1][position2 -1] == "Y":
                        return True, "There is already a ship here!"
                    elif self.grid[position1 - 1][position2 -1] == "Z":
                        return True, "There is already a ship here!"
                else: 
                    if self.grid[position1 + (i - 1)][position2 - 1] == "A":
                        return True, "There is already a ship here!"
                    elif self.grid[position1 + (i - 1)][position2 - 1] == "X":
                        return True, "There is already a ship here!"
                    elif self.grid[position1 + (i - 1)][position2 - 1] == "Y":
                        return True, "There is already a ship here!"
                    elif self.grid[position1 + (i - 1)][position2 - 1] == "Z":
                        return True, "There is already a ship here!"
                    


        
        return False, None


    
    def clear_grid(self):
        self.grid = [
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O"],
        ]

    



class player(grid):

    def __init__(self):
        super().__init__()

        
    

    def check_guess(position1, position2, defending_player):


        def check_if_destroyed(ship, defending_player):

            def check_for_win():
                global win
                if num_player1 < 1:
                    win[0] = True
                    win[1] = 2
                elif num_player2 < 1:
                    win[0] = True
                    win[1] = 1
                
    

            ship_lengths = [2, 3, 4, 5]
            ships = ["A", "X", "Y", "Z"]
            character = ship
            index = ships.index(character)

            if any(character in sublist for sublist in defending_player.grid):
                return False, None
            else:
                if defending_player.id == 0:
                    global num_player1
                    num_player1 -= 1
                    check_for_win()
                else:
                    global num_player2
                    num_player2 -= 1
                    check_for_win()
                return True, ship_lengths[index]    


        if defending_player.grid[position1 - 1][position2 -1] == "A":
            defending_player.grid[position1 - 1][position2 -1] = "/"
            defending_player.secret_grid[position1 - 1][position2 -1] = "A"
            destroyed, length = check_if_destroyed("A", defending_player)
            if destroyed:
                return True, True, length
            return True, False, "You hit the enemy's boat!"
        elif defending_player.grid[position1 - 1][position2 -1] == "Y":
            defending_player.grid[position1 - 1][position2 -1] = "/"
            defending_player.secret_grid[position1 - 1][position2 -1] = "Y"
            destroyed, length = check_if_destroyed("Y", defending_player)
            if destroyed:
                return True, True, length
            return True, False, "You hit the enemy's boat!"
        elif defending_player.grid[position1 - 1][position2 -1] == "Z":
            defending_player.grid[position1 - 1][position2 -1] = "/"
            defending_player.secret_grid[position1 - 1][position2 -1] = "Z"
            destroyed, length = check_if_destroyed("Z", defending_player)
            if destroyed:
                return True, True, length
            return True, False, "You hit the enemy's boat!"
        elif defending_player.grid[position1 - 1][position2 -1] == "X":
            defending_player.grid[position1 - 1][position2 -1] = "/"
            defending_player.secret_grid[position1 - 1][position2 -1] = "X"
            destroyed, length = check_if_destroyed("X", defending_player)
            if destroyed:
                return True, True, length
            return True, False, "You hit the enemy's boat!"
        else:
            return False, False, "You didn't hit anything!"

    
    

    

    

        

player1 = player()
player2 = player()
win = [False, None, None]
num_player1 = 4
num_player2 = 4
   


print("Welcome to battleship!")
input("\nPress Enter to continue... ")

go_back = True

while win[0] == False:

    if go_back:

        for i in range(0, 4):
            clear()
            checked = False

            while not checked:
                clear()
                player1.print_grid()
                print("\nShip 1: Length 2")
                print("Ship 2: Length 3")
                print("Ship 3: Length 4")
                print("Ship 4: Length 5")

                row = int(input(f"\nPlayer 1, enter the row number (1 - 8) for Ship {i + 1}: "))
                while row < 1 or row > 8:
                    clear()
                    player1.print_grid()
                    print("\nShip 1: Length 2")
                    print("Ship 2: Length 3")
                    print("Ship 3: Length 4")
                    print("Ship 4: Length 5")

                    row = int(input(f"\nPlayer 1, enter the row number (1 - 8) for Ship {i + 1}: "))
                

                clear()

                player1.print_grid()
                print("\nShip 1: Length 2")
                print("Ship 2: Length 3")
                print("Ship 3: Length 4")
                print("Ship 4: Length 5")
                column = int(input(f"\nPlayer 1, now enter the column number (1 - 8) for Ship {i + 1}: ")) 

                while column < 1 or column > 8:
                    clear()
                    player1.print_grid()
                    print("\nShip 1: Length 2")
                    print("Ship 2: Length 3")
                    print("Ship 3: Length 4")
                    print("Ship 4: Length 5")
                    print(f"\nYou have selected a row number of {row}")
                    column = int(input(f"\nPlayer 1, enter the column number (1 - 8) for Ship {i + 1}: "))

                
                clear()

                player1.print_grid()
                print("\nShip 1: Length 2")
                print("Ship 2: Length 3")
                print("Ship 3: Length 4")
                print("Ship 4: Length 5")
                direction = input(f"\nPlayer 1, enter the orientation (horizontal: 'H'; vertical: 'V') for Ship {i + 1}: ")

                while direction != "H" and direction != "V":
                    clear()
                    player1.print_grid()
                    print("\nShip 1: Length 2")
                    print("Ship 2: Length 3")
                    print("Ship 3: Length 4")
                    print("Ship 4: Length 5")
                    
                    direction = input(f"\nPlayer 1, enter the orientation (horizontal: 'H'; vertical: 'V') for Ship {i + 1}: ")

                cannot, message = player1.check_for_good_placement(row, column, i+1, direction)
                if cannot:
                    clear()
                    print(f"You selected a row of {row}, column of {column} and orientation of {direction}")
                    print("You cannot place this here!")
                    print(message)
                    input("\nPress Enter to continue... ")
                else:
                    clear()
                    print(f"You have selected a row number of {row}, a column number of {column}, and an orientation of {direction}")
                    input("\nPress Enter to continue... ")
                    player1.add_ship(row, column, i, direction)
                    checked = True



        ## PLAYER 2
        clear()
        print("Now Player 2's Turn")
        input("\nPress Enter to continue... ") 

        
        for i in range(0, 4):
            clear()
            checked = False

            while not checked:
                clear()
                player2.print_grid()
                print("\nShip 1: Length 2")
                print("Ship 2: Length 3")
                print("Ship 3: Length 4")
                print("Ship 4: Length 5")

                row = int(input(f"\nPlayer 2, enter the row number (1 - 8) for Ship {i + 1}: "))
                while row < 1 or row > 8:
                    clear()
                    player2.print_grid()
                    print("\nShip 1: Length 2")
                    print("Ship 2: Length 3")
                    print("Ship 3: Length 4")
                    print("Ship 4: Length 5")

                    row = int(input(f"\nPlayer 2, enter the row number (1 - 8) for Ship {i + 1}: "))
                

                clear()

                player2.print_grid()
                print("\nShip 1: Length 2")
                print("Ship 2: Length 3")
                print("Ship 3: Length 4")
                print("Ship 4: Length 5")
                column = int(input(f"\nPlayer 2, now enter the column number (1 - 8) for Ship {i + 1}: ")) 

                while column < 1 or column > 8:
                    clear()
                    player2.print_grid()
                    print("\nShip 1: Length 2")
                    print("Ship 2: Length 3")
                    print("Ship 3: Length 4")
                    print("Ship 4: Length 5")
                    print(f"\nYou have selected a row number of {row}")
                    column = int(input(f"\nPlayer 2, enter the column number (1 - 8) for Ship {i + 1}: "))

                
                clear()

                player2.print_grid()
                print("\nShip 1: Length 2")
                print("Ship 2: Length 3")
                print("Ship 3: Length 4")
                print("Ship 4: Length 5")
                direction = input(f"\nPlayer 2, enter the orientation (horizontal: 'H'; vertical: 'V') for Ship {i + 1}: ")

                while direction != "H" and direction != "V":
                    clear()
                    player2.print_grid()
                    print("\nShip 1: Length 2")
                    print("Ship 2: Length 3")
                    print("Ship 3: Length 4")
                    print("Ship 4: Length 5")
                    
                    direction = input(f"\nPlayer 2, enter the orientation (horizontal: 'H'; vertical: 'V') for Ship {i + 1}: ")

                cannot, message = player2.check_for_good_placement(row, column, i+1, direction)
                if cannot:
                    clear()
                    print(f"You selected a row of {row}, column of {column} and orientation of {direction}")
                    print("You cannot place this here!")
                    print(message)
                    input("\nPress Enter to continue... ")
                else:
                    clear()
                    print(f"You have selected a row number of {row}, a column number of {column}, and an orientation of {direction}")
                    input("\nPress Enter to continue... ")
                    player2.add_ship(row, column, i, direction)
                    checked = True

    go_back = False
    go_back2 = True

    while go_back2:
        clear()
        playing = True
        active_player = 1
        while playing:
            clear()
            print("Time to guess!")
            input("\nPress Enter to continue... ")

            while active_player == 1:
                clear()
                print("Player 1 to guess!")
                print("")
                player2.print_secret_grid()
                
                row = int(input("\nEnter the row number (1 - 8) for your guess!: "))
                while row < 1 or row > 8:
                    clear()
                    player2.print_secret_grid()
                    row = int(input("\nEnter the row number (1 - 8) for your guess!: "))

                clear()

                player2.print_secret_grid()
                
                column = int(input("\nEnter the column number (1 - 8) for your guess!: "))
                while column < 1 or column > 8:
                    clear()
                    player2.print_secret_grid()
                    print(f"\nYou have selected a row number of {row}")
                    column = int(input("\nEnter the column number (1 - 8) for your guess!: "))

                clear()
                hit, destroyed, message = player.check_guess(row, column, player2)

                if hit:
                    if destroyed:
                        print(f"You successfully destroyed the enemy's boat of length {message}")
                        if win[0] == True:
                            playing = False
                            go_back2 = False
                            active_player = 3
                            break
                    else:
                        print(message)
                    input("\nPress Enter to continue... ")
                else:
                    print(message)
                    input("\nPress Enter to continue... ")
                active_player = 2
            
            if win[0] == True:
                playing = False
                go_back2 = False
                go_back = False
                active_player = None
                break
            





            while active_player == 2:
                clear()
                print("Player 2 to guess!")
                print("")
                player1.print_secret_grid()
                
                row = int(input("\nEnter the row number (1 - 8) for your guess!: "))
                while row < 1 or row > 8:
                    clear()
                    player1.print_secret_grid()
                    row = int(input("\nEnter the row number (1 - 8) for your guess!: "))

                clear()

                player1.print_secret_grid()
                
                column = int(input("\nEnter the column number (1 - 8) for your guess!: "))
                while column < 1 or column > 8:
                    clear()
                    player1.print_secret_grid()
                    print(f"\nYou have selected a row number of {row}")
                    column = int(input("\nEnter the column number (1 - 8) for your guess!: "))

                clear()
                hit, destroyed, message = player.check_guess(row, column, player1)

                if hit:
                    if destroyed:
                        print(f"You successfully destroyed the enemy's boat of length {message}")
                        if win[0] == True:
                            go_back2 = False
                            playing = False
                            active_player = 3
                            break
                    else:
                        print(message)
                    input("\nPress Enter to continue... ")
                else:
                    print(message)
                    input("\nPress Enter to continue... ")
                active_player = 1
        
            if win[0] == True:
                go_back2 = False
                go_back = False
                playing = False
                active_player = None
                break
    

clear()
print(f"Congratulations Player {win[1]} for destroying all the enemy's boats!")
input("\nPress Enter to continue... ")





    







    












