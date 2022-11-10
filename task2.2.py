from datetime import datetime as date
import json

extraIngredient = 7
database = "dayPizza.json"

class Pizza:
    def __init__(self, type, *ingredients):
        self.type = type
        with open(database, 'r') as f:
            pizza_data = json.load(f)["pizzaoftheday"][type]
        self.price = pizza_data["price"]
        self.ingredients = pizza_data["ingredients"]
        if ingredients:
            for additional in ingredients:
                self.price += extraIngredient
                self.ingredients[additional] = 1

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, t):
        if not isinstance(t, str) or not t:
            raise TypeError("Input correct pizza type")
        self.__type = t

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        if isinstance(p, int) or isinstance(p, float) and p > 0:
            self.__price = p
        else:
            raise ValueError("Incorrect price")

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, t):
        if not isinstance(t, dict) or not t:
            raise TypeError("Input correct ingredient")
        self.__ingredients = t


class Pizza_of_the_day(Pizza):
    def __init__(self, *ingredients):
        day = date.today().strftime("%A")
        match day:
            case "Monday":
                type = "54 cheese"
            case "Tuesday":
                type = "pepperoni"
            case "Wednesday":
                type = "margorita"
            case "Thursday":
                type = "hawaiian"
            case "Friday":
                type = "buffalo"
            case "Saturday":
                type = "bbq_chicken"
            case "Sunday":
                type = "veggie"
        super().__init__(type, *ingredients)
        with open(database, 'r') as f:
            pizza_data = json.load(f)["pizzaoftheday"][type]
        self.price = int(pizza_data["price"]) * 0.5
        for x in ingredients:
            self.price += extraIngredient


class Order:
    def __init__(self, name, *args):
        self.name = name
        self.pizza = args

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if not isinstance(n, str) or not n:
            raise TypeError("Incorect name")
        self.__name = n

    def show_order_short(self):
        p = 0
        print("Customer name: " + self.name)
        for x in self.pizza:
            print(x.type + "    ", x.price)
            p += x.price
        print("Overal: ", p)

    def show_order(self):
        p = 0
        print("Customer name: " + self.name)
        for x in self.pizza:
            print(x.type + " ingredients: ", x.ingredients)
            p += x.price
        print("Overal: ", p)


Maks = Pizza("54 cheese", "tomatoes", "mushrooms", "meat")
day = Pizza_of_the_day("mushrooms")
zakaz = Order("Gudzovskyi Mark", day, Maks)
zakaz.show_order_short()