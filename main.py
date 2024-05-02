class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')

myCar = Car('Kitt', 180)
myOtherCar = Car('Speedy', 55)

myCar.talk('Michael')

class Race:
  def __init__(self, name, driver_limit):
    self.name = name
    self.driver_limit = driver_limit
    self.drivers = []

  def add_driver(self, driver):
    if len(self.drivers) < self.driver_limit:
      if self._within_10_points(driver):
        self.drivers.append(driver)
        print(f"{driver.name} has been added to the race.")
      else:
        print(f"{driver.name} cannot be added to the race. Their ranking is not within 10 points of the current average ranking.")
    else:
      print("Driver limit reached. Cannot add more drivers to the race.")

  def _within_10_points(self, driver):
      if self.drivers:
          average_ranking = self.get_average_ranking()
          return abs(driver.ranking - average_ranking) <= 10
      return True

  def get_average_ranking(self):
    total_ranking = sum(driver.ranking for driver in self.drivers)
    average_ranking = total_ranking / len(self.drivers) if self.drivers else 0
    return average_ranking

class Driver:
  number_of_drivers = 0
  drivers_list = []

  def __init__(self, name, age, ranking):
    self.name = name
    self.age = age
    self.ranking = ranking
    Driver.number_of_drivers += 1
    Driver.drivers_list.append(self)

  def get_ranking(self):
    return self.ranking
  
  @classmethod
  def get_global_average_ranking(cls):
        total_ranking = sum(driver.ranking for driver in cls.drivers_list)
        average_ranking = total_ranking / len(cls.drivers_list) if cls.drivers_list else 0
        return average_ranking


my_course = Race('Seattle 500', 4)
print(my_course.name, my_course.driver_limit, my_course.drivers)

my_driver = Driver('Dale Earnhardt', 29, 100)
print(my_driver.get_ranking())

driver1 = Driver("Lewis Hamilton", 36, 83)
driver2 = Driver("Eliud Kipchoge", 36, 95)
driver3 = Driver("Sebastian Vettel", 34, 76)
driver4 = Driver("Ayrton Senna", 34, 99)

my_course.add_driver(driver1)
my_course.add_driver(driver2)
my_course.add_driver(driver3)
my_course.add_driver(driver4)

print("Average Ranking of Drivers:", my_course.get_average_ranking())
print("Global Average Ranking of Drivers:", Driver.get_global_average_ranking())