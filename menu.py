class Menu(object):
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes[dish.kitchen] = dish

    def add_dishes(self, pagecontent):
        options = pagecontent.find_all("h3")
        tables = pagecontent.find_all("table")
        foods = pagecontent.find_all("p")

        nbr_dishes = len(tables)

        for i in range(nbr_dishes):
            dish_descr = foods[i * 2].text.strip().replace("  ", " ")
            kitchen = options[i].text.split("|")[0].strip()
            table = tables[i]
            self.dishes.append(Dish(kitchen, dish_descr, table))



