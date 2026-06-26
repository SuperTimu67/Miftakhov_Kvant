##def build_query_string(base_url, **kwargs):
##    result = base_url + "?"
##    for agr in agrs:
##        result += agr[0] + "=" + str(agr[1]) + "&"
##    return result[:-1]
##print(build_query_string("http://api.weather.com/v1/forecast", city="Moscow", days=3, units="metric"))



#catalog = [
#   {"name":"Чехол", "price": 500, "rating": "4.2"},
#    {"name":"Наушники", "price": 7000, "rating": "4.8"},
#    {"name":"Зарядка", "price": 1200, "rating": "4.5"}
#]
#prices_sorted = sorted(catalog, key=lambda x: x["price"])
#for arg in prices_sorted:
#    print(arg["name"]+": "+str(arg["price"])+" руб.")
#
#ratings_sorted = sorted(prices_sorted, key=lambda x: x["rating"], reverse=True)
#for arg in ratings_sorted:
#    print(arg["name"]+": "+str(arg["rating"])+" ★, "+str(arg["price"])+" руб.")


# class Animal:
#     def __init__(self, name, color,):
#         self.name = name
#         self.color = color
#
#     def speak(self):
#         print(self.name)
#
# class Dog(Animal):
#     def __init__(self, name, color, master):
#         Animal.__init__(self, name, color)
#         self.master = master
#
#     def speak(self):
#         print("gav")
#
# class Cat(Animal):
#     def __init__(self, name, color, quantity_life):
#         Animal.__init__(self, name, color)
#         self.quantity_life = quantity_life
#
#     def speak(self):
#         print("maw")
#
# dog = Dog("IIIapuk", "blue", True)
#
#
# cat = Cat("Barsik", "red", 9)
#
# dog.speak()
# cat.speak()


# class Transport:
#     def __init__(self, speed, capacity):
#         self.speed = speed
#         self.capacity = capacity
#
#     def movement(self):
#         print("moving")
#
# class Car:
#     def __init__(self, speed, capacity, wheel_diameter):
#         Transport.__init__(self, speed, capacity)
#         self.wheel_diameter = wheel_diameter
#
#     def movement(self):
#         print("driving")
#
# class Plane:
#     def __init__(self, speed, capacity, wingspan):
#         Transport.__init__(self, speed, capacity)
#         self.wingspan = wingspan
#
#     def movement(self):
#         print("flying")
#
# class Steamboat:
#     def __init__(self, speed, capacity, reserve_buoyancy):
#         Transport.__init__(self, speed, capacity)
#         self.reserve_buoyancy = reserve_buoyancy
#
# car = Car()

print("Hello")

