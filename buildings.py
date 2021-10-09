#buildings for the program

class Safehouse:
  def __init__(self,name,lat = 0, lon =0): #target for robber 
    self.name = name #name of object
    self.lat = lat #down(-)/up(+)coordinates
    self.lon = lon #right(-)/left(+)coordinates
    
  def position(self): #location of safehouse
   l1=(self.lat,self.lon)
   return(l1)

  def locate(self):
    return str("The {}'s position is {} latitude and {} longitude".format(self.name,self.lat,self.lon))
  
  
  
