class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach

        self.points = 0

    def add_player(self, new_player_name):
        self.players.append(new_player_name)

    def has_player(self, player_name):

        if player_name in self.players:
            # for player in self.players:
            #     if player == player_name:
            return True

        return False

    def play_game(self, did_team_win):
        if did_team_win:
            self.points += 3
