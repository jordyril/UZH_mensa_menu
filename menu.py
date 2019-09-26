from meal import Meal


class Menu(object):
    def __init__(self):
        self.meals = []

    def add_meal(self, meal):
        self.meals[meal.kitchen] = meal

    def add_meals(self, pagecontent):
        options = pagecontent.find_all("h3")
        tables = pagecontent.find_all("table")
        foods = pagecontent.find_all("p")

        nbr_meals = len(tables)

        for i in range(nbr_meals):
            meal_descr = foods[i * 2].text.replace("  ", " ").strip()
            kitchen = options[i].text.split("|")[0].strip()
            table = tables[i]
            self.meals.append(Meal(kitchen, meal_descr, table))

