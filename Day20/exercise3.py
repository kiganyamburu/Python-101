class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
        
Eric = Player("Eric", 116700)
John = Player("John", 24327)
Terry = Player("Terry", 150000)
player_list = ["Eric", "John", "Terry"]
sorted_players = sorted(player_list, key=lambda player: Player.score, reverse=True)

print(Player.name for player in player_list)