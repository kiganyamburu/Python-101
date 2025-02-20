class Player:
    def __init__(self, name, score):
        self.name = name  # Fixed the typo here
        self.score = score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

# Sort by score using lambda
sorted_players = sorted(player_list, key=lambda player: player.score, reverse=True)  # Added reverse=True for descending order


print([player.name for player in sorted_players]) # Output: ['Terry', 'Eric', 'John']