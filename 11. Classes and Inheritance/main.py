from Player import Player

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


    def print(self):
        variable = ""

        if self.weight_kg < 90:
            variable = "because"
        else:
            variable = "aldo"
        print("This player is {0} {1}. He made {2} point {3} his weight is {4} kg.".format(self.first_name,
                                                                                            self.last_name,
                                                                                            self.goals,
                                                                                            variable,
                                                                                            self.weight_kg))


lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)
jens = BasketballPlayer(first_name="Jens", last_name="Polspoel", height_cm=203, weight_kg=75, points=50, rebounds=7.4, assists=90)
messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

basketballPlayers = [lebron, jens]

for player in basketballPlayers:
    player.print()

    print(str(player.weight_kg) + "kg - " + str(player.weight_to_lbs()) + "lbs.")

messi.print()