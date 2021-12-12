#Import Director
from game.director import Director

#Create main function
def main():
    game = Director()
    game.start_game()

#Run game
if __name__ == "__main__":
    main()