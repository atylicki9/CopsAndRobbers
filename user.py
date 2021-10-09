#create a class that applies to both cop and robber
class Cop_Robber:
  def __init__(self,name,lat = 0,lon = 0): #inititiate object with latitude/longitude coordinates
    self.name = name 
    self.lat = lat #down(-)/up(+)coordinates
    self.lon = lon #right(+)/left(-)coordinates




#location features
  def locate(self):
    return str("The {}'s Position is {} Latitude and {} Longitude".format(self.name,1+(8-self.lat),1+self.lon))

  def position(self):
   l1=(self.lat,self.lon)
   return(l1)
   
#walking movements of object
  def walk_up(self):
    if self.lat!=0:
      self.lat -= 1
      print("{} walks up 1 place".format(self.name))
    else:
      self.lat=0
      print("Can't go that way!")
  def walk_down(self):
    if self.lat!=8:
      self.lat += 1
      print("{} walks down 1 place".format(self.name))
    else:
      self.lat = 8
      print("Can't go that way!")
  def walk_left(self):
    if self.lon != 0:
      self.lon -= 1
      print("{} walks left 1 place".format(self.name))
    else:
      self.lon = 0
      print("Can't go that way!")
  def walk_right(self):
    if self.lon !=8:
      self.lon +=1
      print("{} walks right 1 place".format(self.name))
    else:
      self.lon=8
      print("Can't go that way!")
  
  
