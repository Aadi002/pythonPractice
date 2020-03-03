from abc import abstractmethod

class Bird():
    fly = True

    def noise(self):
        print("Birdnoise")


    babies = 0

    def reproduce(self):
        self.babies += 1


    @abstractmethod
    def eat(self):
        pass

    extinct = False



class Owl(Bird):

    def reproduce(self):
        self.babies += 6
        return self.babies
    
    def eat(self):
        print("owl owl peck")


class Dodo(Owl):
    fly = False
    extinct = True

    def eat(self):
        print("Dodo Dodo peck")



doodle = Dodo()
doodle.eat
#num = doodle.reproduce
#print(num)