class Dish(object):
    def __init__(self, kitchen, dish, menutable):
        self.kitchen = kitchen
        self.table = menutable
        self.dish = dish

        self.__set_values()

    def __set_values(self):
        cells = self.table.find_all("td")
        self.energy = int(
            cells[1].text.split("(")[1].split("kcal")[0].replace("'", "").strip()
        )
        self.protein = float(cells[3].text.split("g")[0].strip())
        self.fat = float(cells[5].text.split("g")[0].strip())
        self.carbs = float(cells[7].text.split("g")[0].strip())

    def __str__(self):
        return self.kitchen

    def __repr__(self):
        return self.kitchen

    @property
    def summary(self):
        summary = (
            f"{self.kitchen.upper()}\n"
            f"{self.dish}: \n"
            f"Energy: {self.energy} kcal \n"
            f"Protein: {self.protein}g\n"
            f"Fat: {self.fat}g\n"
            f"Carbs: {self.carbs}g"
        )

        return summary