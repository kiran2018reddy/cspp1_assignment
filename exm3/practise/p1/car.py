class vechile(object):
	def __inti__(self):
		self.wheels=wheels
		self.fuel = fuel
		self.colour = colour
		self.number = num

class car(vechile):
	def __inti__(self,wheel,fuel,colour,num,seats):
	    vechile __inti__(self,wheels,fuel,colour,num)
	    self.seats = seats
	    self.air bags = air bags
class maruthi(car)
    def __inti__(self,wheel,fuel,colour,num,seats):
        car.__inti__(self,wheels,fuel,colour,num,seats)
        self.seats=seats
        self