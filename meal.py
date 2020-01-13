class Meal(object):
    def __init__(self, kitchen, meal, menutable):
        self.kitchen = kitchen
        self.table = menutable
        self.meal = meal
        self.values = {}

        self.__set_values()

    def __set_values(self):
        cells = self.table.find_all("td")
        try:
            self.values["energy"] = int(
                cells[1].text.split("(")[1].split(
                    "kcal")[0].replace("'", "").strip()
            )
            self.values["protein"] = float(cells[3].text.split("g")[0].strip())
            self.values["fat"] = float(cells[5].text.split("g")[0].strip())
            self.values["carbs"] = float(cells[7].text.split("g")[0].strip())
        except IndexError:
            for i in ['energy', 'protein', 'fat', 'carbs']:
                self.values[i] = '/'

    def __str__(self):
        return self.kitchen

    def __repr__(self):
        return self.kitchen

    @property
    def summary(self):
        summary = (
            f"{self.kitchen.upper()}\n"
            f"{self.meal}: \n"
            f"Energy: {self.values['energy']} kcal \n"
            f"Protein: {self.values['protein']}g\n"
            f"Fat: {self.values['fat']}g\n"
            f"Carbs: {self.values['carbs']}g"
        )

        return summary
