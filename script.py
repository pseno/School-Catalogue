class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

mySchool = School("Codecademy", "high", 100)
print(mySchool)
print(mySchool.get_name())
print(mySchool.get_level())
mySchool.set_numberOfStudents(200)
print(mySchool.get_numberOfStudents())

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getPickupPolicy(self):
      return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "\n" + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(testSchool.getPickupPolicy())
print(testSchool)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
      return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "\n" + "Our sports are {sportsTeams}".format(sportsTeams = self.sportsTeams)

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams())
print(c)