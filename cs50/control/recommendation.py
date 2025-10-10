def main():
    difficulty = input("Difficulty or Casual?: ")
    if not (difficulty == "Difficulty" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    
    
    player = input("Multiplayer or single player? ")
    if not (player == "Multiplayer" or player == "Single player"):
        print("Enter a valid option") 
        return

    if difficulty == "Difficulty" and player == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficulty" and player == "Single player":
        recommend("Solitaire")
    elif difficulty == "Casual" and player == "Multiplayer":
        recommend("Checkers")
    elif difficulty == "Casual" and player == "Single player":
        recommend("Sudoku")
    else:
        recommend("Go Fish")

    
def recommend(game):
    print("You might like ", game)
    
    
    
main()