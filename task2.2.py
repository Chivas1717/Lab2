# import json
# from datetime import date
# import calendar
#
#
# class Pizeria:
#     def __init__(self):
#         data = {"Monday": {"name": "Four seasons", "price": 100},
#                 "Tuesday": {"name": "Margarita", "price": 80},
#                 "Wednesday": {"name": "Gavaian", "price": 150},
#                 "Thursday": {"name": "Pineappled", "price": 50},
#                 "Friday": {"name": "Four cheeses", "price": 120},
#                 "Saturday": {"name": "Family-pizza", "price": 350},
#                 "Sunday": {"name": "Cono-pizza", "price": 115}
#                 }
#         with open("dayPizza.json", "w") as json_file:
#             json.dump(data, json_file, indent=2)
#
#     def __str__(self):
#         with open("dayPizza.json", "r") as json_file:
#             json_object = json.load(json_file)
#         data = "\n".join(list(map(str, json_object.items())))
#         data = data.replace("{", " ")
#         data = data.replace("}", " ")
#         return data
#
#
# class Pizzaoftheday():
#     def __init__(self):
#         today = date.today()
#         self.day = calendar.day_name[today.weekday()]
#         if self.day == "Monday":
#             self.pizza == Monday()
#         elif self.day == "Thursday":
#             self.pizza = Thursday()
#         elif self.day == "Tuesday":
#             self.pizza = Tuesday()
#         elif self.day == "Wednesday":
#             self.pizza = Wednesday()
#         elif self.day == "Friday":
#             self.pizza == Friday()
#         elif self.day == "Saturday":
#             self.pizza == Saturday()
#         else:
#             self.pizza == Sunday()
#
#     def get_price(self):
#         return self.pizza.price
#
#     def get_info(self):
#         return self.pizza.name
#
#
# class Monday(Pizzaoftheday):
#     def __init__(self):
#         with open("pizzaoftheday.json", "r") as json_file:
#             json_object = json.load(json_file)
#         self.day = "Monday"
#         self.price = json_object["Monday"]["price"]
#         self.name = json_object["Monday"]["name"]
#
#     def __str__(self):
#         return f'Monday pizza: {self.name}, price: {self.price}'
#
#
# class Wednesday(Pizzaoftheday):
#     def __init__(self):
#         with open("pizzaoftheday.json", "r") as json_file:
#             json_object = json.load(json_file)
#         self.day = "Wednesday"
#         self.price = json_object["Wednesday"]["price"]
#         self.name = json_object["Wednesday"]["name"]
#
#     def __str__(self):
#         return f'Wednesday pizza: {self.name}, price: {self.price}'
#
#
# class Tuesday(Pizzaoftheday):
#     def __init__(self):
#         with open("pizzaoftheday.json", "r") as json_file:
#             json_object = json.load(json_file)
#         self.day = "Tuesday"
#         self.price = json_object["Tuesday"]["price"]
#         self.name = json_object["Tuesday"]["name"]
#
#     def __str__(self):
#         return f'Tuesday pizza: {self.name}, price: {self.price}'
#
#
# class Thursday(Pizzaoftheday):
#     def __init__(self):
#         with open("pizzaoftheday.json", "r") as json_file:
#             json_object = json.load(json_file)
#         self.day = "Thursday"
#         self.price = json_object["Thursday"]["price"]
#         self.name = json_object["Thursday"]["name"]
#
#     def __str__(self):
#         return f'Thursday pizza: {self.name}, price: {self.price}'
#
#
# class Friday(Pizzaoftheday):
#     def __init__(self):
#         with open("pizzaoftheday.json", "r") as json_file:
#             json_object = json.load(json_file)
#         self.day = "Friday"
#         self.price = json_object["Friday"]["price"]
#         self.name = json_object["Friday"]["name"]
#
#     def __str__(self):
#         return f'Friday pizza: {self.name}, price: {self.price}'
#
#
# class Saturday(Pizzaoftheday):
#     def __init__(self):
#         with open("pizzaoftheday.json", "r") as json_file:
#             json_object = json.load(json_file)
#         self.day = "Saturday"
#         self.price = json_object["Saturday"]["price"]
#         self.name = json_object["Saturday"]["name"]
#
#     def __str__(self):
#         return f'Saturday pizza: {self.name}, price: {self.price}'
#
#
# class Sunday(Pizzaoftheday):
#     def __init__(self):
#         with open("pizzaoftheday.json", "r") as json_file:
#             json_object = json.load(json_file)
#         self.day = "Sunday"
#         self.price = json_object["Sunday"]["price"]
#         self.name = json_object["Sunday"]["name"]
#
#     def __str__(self):
#         return f'Sunday pizza: {self.name}, price: {self.price}'
#
#
# class CustomPizza:
#
#     def __init__(self):
#         self.pizza = Pizzaoftheday()
#         self.add_ingredients
#         self.price = self.add_ingredients()
#
#     def add_ingredients(self):
#         with open("ingredients.json", "r") as json_file:
#             json_object = json.load(json_file)
#         total = self.pizza.get_price()
#         print(json_object)
#         while 1 == 1:
#             data = input("Enter ingredient you want to add: ")
#             if data in json_object.keys():
#                 total += json_object[str(data)]
#                 print(total)
#             if data == "x":
#                 break
#         return total
#
#     def get_price(self):
#         return self.price
#
#     def get_info(self):
#         return f'Custom pizza-of-the-day'
#
#
# class Order():
#     def __init__(self):
#         self.make_order
#         self.total_price = self.make_order()
#
#     def make_order(self):
#
#         order = {}
#         number = input("How many pizzas u want to order? ")
#         dayspizzas = input("How many of them is pizza-of-the-day? ")
#         custompizzas = int(number) - int(dayspizzas)
#         for item in range(int(dayspizzas)):
#             order[item] = Pizzaoftheday()
#         for value in range(int(custompizzas)):
#             order[value + int(dayspizzas)] = CustomPizza()
#         total = 0
#         for item in order:
#             total += order[item].get_price()
#
#         return total
#
#     def get_price(self):
#         return f'Total price of order: {self.total_price}'
#
#
# x = Pizeria()
# z = Order()
# print(z.get_price())
