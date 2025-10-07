def main():
    difficulty = input("Choose a difficulty level (easy, medium, hard): ")
    player = input("Multiplayer or single player? ")
    if difficulty == "Difficulty":
        if player == "Multiplayer":
            recommend("Chess")
        elif player == "Single player":
            recommend("Minesweeper")
        else:
            print("Enter a valid option")
    elif difficulty == "casual":
        if player == "Multiplayer":
            recommend("Checkers")
        else:
            recommend("Sudoku")        
    else:
        if player == "Multiplayer":
            recommend("Among Us")
            
        else:
            recommend("Solitaire")
def recommend(game):
    print("You might like ", game)
    
    
    
main()