class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def print(self):
        variable = ""

        if self.weight_kg < 90:
            variable = "because"
        else:
            variable = "aldo"
        print("This player is {0} {1}. He made {2} point {3} his weight is {4} kg.".format(self.first_name,
                                                                                            self.last_name,
                                                                                            self.points,
                                                                                            variable,
                                                                                            self.weight_kg))

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds