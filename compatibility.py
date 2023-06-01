class Roommate:
  def __init__(self, list):
    self.showerNight = list[0]
    self.clean = list[1]
    self.temp = list[2]
    self.yesPet = list[3]
    self.sleep = list[4]
    self.awake = list[5]

  def compare(self, other):
    counter = 0
    if (not(self.showerNight == other.showerNight)):
      counter += 1
    diff = abs(self.clean - other.clean)
    if diff <= 2:
      counter += 1
      if diff == 0:
        counter += 1
    tempDiff = abs(self.temp - other.temp)
    if tempDiff <= 2:
      counter += 1
      if tempDiff == 0:
        counter += 1
    if self.yesPet == other.yesPet:
      counter += 1
    sleepDiff = abs(self.sleep - other.sleep)
    if(sleepDiff > 12):
      sleepDiff = abs(sleepDiff - 24)
    if sleepDiff <= 3:
      counter += 1
      if sleepDiff == 0:
        counter += 1
    awakeDiff = abs(self.awake - other.awake)
    if(awakeDiff > 12):
      awakeDiff = abs(awakeDiff - 24)
    if awakeDiff <= 3:
      counter += 1
      if awakeDiff == 0:
        counter += 1

    return (counter/10.0 * 100)
  