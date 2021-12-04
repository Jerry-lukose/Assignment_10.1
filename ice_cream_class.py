#Jerry Lukose Assignment 10.1: Your own class
#This program contains a class which makes customized ice cream objects.
import random

#My icecream class which creates an instance of an icecream.
class Icecream():
    #class variable for type of icecream cone
    cone = "waffle"

    def __init__(self, flavor, drizzle = None, toppings = None):
        #private data attributes for flavor of icecream, toppings, and what kind of drizzle
        self.__flavor = flavor
        self.__drizzle = drizzle
        self.__toppings = toppings
    #method that returns flavor of icecream
    def get_flavor(self):
        return(self.__flavor)
    #method that returns type of drizzle
    def get_drizzle(self):
        return(self.__drizzle)
    #method that returns toppings
    def get_toppings(self):
        return(self.__toppings)
    #method that changes drizzle type
    def set_drizzle(self, drizzle):
        self.__drizzle = drizzle
    #method that changes toppings
    def set_toppings(self, toppings):
        self.__toppings = toppings
    #method that describes customized icecream
    def get_ice_cream(self):
        order = (f"ordered a {self.__flavor} icecream with a {self.cone} cone and {self.__drizzle} drizzle and {self.__toppings} on top.")
        order2 = (f"ordered a {self.__flavor} icecream with a {self.cone} cone and {self.__drizzle} drizzle and {self.__toppings} toppings.")
        # if any variables are "None", replaces it with no so it make sense in string
        if self.__toppings == None:
            return(order2.replace("None", "no"))
        else:
            return(order)
    #method that plays a game with order of icecream
    def pick_a_number(self, y = 0):
        #asks for number from 0 to 10 from user
        y = int(input("Please pick a number from 0 to 10: "))
        #depending on y value, different strings are printed
        if y == 3:
            print("Lesss goooo!!!!! You got a free icecream along with your order")
        elif y == 5:
            print("Lessss goooo! You get a free car along with your order")
        elif y == 8:
            print("WOW, you get to pay double for your icecream order. Awesome!")
        elif y < 0 or y > 10:
            print("I told you to pick a number between 1 and 10, bozo.")
        else:
            print("Dang, you win nothing. Better luck next time!")
    #method that plays another game with order of icecream
    def sentient_ice_cream(self, question = "none", again = "yes"):
        while again.lower() == "yes":
            # asks user to input question
            question = input("Input your question here: ")
            #some answers that are in a list
            answers = ["Probably Not", "For Sure", "No way", "Nope", "Yes", "No", "Are you joking?", "Dumb Question", "Absolutely", "Yeah", "Definitely"]
            #randomly generates a number
            value = random.randint(0,10)
            #prints answer according to element in randomly generated index position in answers list.
            print(answers[value])
            again = input("Ask another question? (Yes/No): ")
            #asks user if they want to continue asking questions
            while again.lower() != "yes" and again.lower() != "no":
                if again.lower == "no":
                    break
                else:
                    print("Please only print yes or no.")
                    again = input("Ask another question? (Yes/No): ")        

#demo program
def main():
    #list of my very close friends
    homies = ["Barack Obama", "Darth Vader", "Goku"]
    #empty list of icecreams
    icecreams = []
    # for every element in homies list, makes a customized icecream and adds it to icecreams list
    for homie in homies:
        y = random.randint(0,9)
        if y < 3:
            topping = "m&ms"
            drizzle = "maple syrup"
            flavor = "chocolate"
        elif y > 3 and y < 6:
            topping = "sprinkles"
            drizzle = "strawberry"
            flavor = "vanilla"
        else:
            topping = "sprinkles"
            drizzle = "chocolate"
            flavor = "mint"
        icecreams.append(Icecream(flavor, drizzle, topping))
    # for each element in icecreams list, describes icecream and who ordered it
    for x in icecreams:
        print(f"{homies[icecreams.index(x)]} {x.get_ice_cream()}")

    #showcases other methods of Icecream class
    your_order = Icecream("Cookies and Cream")
    print(your_order.get_flavor())
    your_order.set_drizzle("Chocolate")
    your_order.set_toppings("skittles")
    print(your_order.get_drizzle())
    print(your_order.get_toppings())
    print(f"You {your_order.get_ice_cream()}")
    
    #introduces game
    print("Along with your order, you can play a game for a chance to win something!")
    #method that plays the game
    your_order.pick_a_number()
    #introduces second game
    print("Your icecream became sentient. Ask it a yes or no question. It might have an answer for you.")
    your_order.sentient_ice_cream()
    print("End of demo program. Have a good day.")

#Runs demo program
if __name__ == '__main__':
    main()