import random

class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.alive = True
    
    def announce_mark(self):
        # Players must announce the mark they think is on the back of their collar
        # If they are correct, they move on to the next round
        # Otherwise, their collar explodes and they are eliminated from the game
        print(f"{self.name}, what is the mark on your collar?")
        announced_mark = input()
        if announced_mark == self.mark:
            print(f"{self.name} is correct and moves on to the next round!")
        else:
            print(f"{self.name} is incorrect and is eliminated from the game!")
            self.alive = False

class Game:
    def __init__(self, num_players):
        self.players = []
        self.time_limit = 3600  # 1 hour per round
        self.collars_exploded = False
        self.jack_of_hearts_found = False
        self.game_over = False
        
        # Assign marks to players randomly
        marks = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        
        for i in range(num_players):
            name = f"Player {i+1}"
            mark = random.choice(marks)
            player = Player(name, mark)
            self.players.append(player)
        
        # Choose one player to be the Jack of Hearts
        self.jack_of_hearts = random.choice(self.players)
    
    def start(self):
        # Main game loop
        while not self.game_over:
            # Players are free to talk and strategize for the first 55 minutes
            # of each round
            self.talk_time()
            
            # In the final 5 minutes of each round, players must enter a cell
            # and announce the mark they think is on their collar
            self.announcement_time()
            
            # Check for game over conditions
            self.check_game_over()
    
    def talk_time(self):
        # Players are free to talk and strategize for the first 55 minutes
        # of each round
        print("Players are free to talk and strategize for the next 55 minutes.")
        print("Use this time wisely.")
        print()
        input("Press Enter to continue...\n")
    
    def announcement_time(self):
        # In the final 5 minutes of each round, players must enter a cell
        # and announce the mark they think is on their collar
        print("The final 5 minutes of the round have begun. Players must enter a cell and announce the mark on their collar.")
        print()
        for player in self.players:
            if player.alive:
                player.announce_mark()
    
def check_game_over(self):
    # Check for game over conditions
    # If two players remain (including the Jack of Hearts), the game is over
    # If the Jack of Hearts has been eliminated, the game is cleared
    # If all players except for the Jack of Hearts have been eliminated, 
    # the game is over
    remaining_players = [p for p in self.players if p.alive]
    num_remaining = len(remaining_players)
    if num_remaining == 2:
        self.game_over = True
        if self.jack_of_hearts in remaining_players:
            print("The game is over. The Jack of Hearts is the winner!")
        else:
            print("The game is over. The remaining player is the winner!")
    elif self.jack_of_hearts not in remaining_players:
        self.game_over = True
        print("The game is cleared. The players have eliminated the Jack of Hearts!")
    elif num_remaining == 1:
        self.game_over = True
        print("The game is over. The Jack of Hearts is the only remaining player!")
