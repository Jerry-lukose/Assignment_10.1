#READ ME
https://github.com/Jerry-lukose/Assignment_10.1.git

Class Documentation

The class Icecream() is a class that can take up to 3 arguments. 
It takes in an argument for the flavor of the ice cream, toppings, and drizzle. 
The class has 1 class variable and 3 private data variables. 
The class also has 8 different methods.
The purpose of the class is to make a customized ice cream order, complete with two games that come along with it. 

The class variable "cone" describes the cone of the ice cream order. It is set to "waffle" and is the same for every object made with the Icecream() class.
There are 3 data variables. The data variable __flavor takes in the flavor of the ice cream. 
The data variable __drizzle takes in the type of drizzle, like chocolate drizzle. 
Finally the data variable __toppings takes in the type of toppings on the ice cream.

The method get_flavor() returns the flavor of the ice cream. It takes no arguments except for self. The method get_drizzle() returns the type of drizzle. It only takes self as an argument. The method get_toppings() returns the toppings on the ice cream object. It also only takes in self. 
The method set_drizzle() changes the type of drizzle. This method takes in self and a string to describe the type of drizzle. The method set_toppings() changes the toppings on the ice cream. This method also take in self, as well as a string for kind of topping. The method get_ice_cream() returns a string describing the entire ice cream order. It makes use of all of the private data variables. 
The method pick_a_number() plays a game where you pick a number and you get a prize according to that number. This method asks the user to input a number and uses if statements to pick a prize. It takes in self and a value as arguments.
The method sentient_ice_cream() also has the user play a game. It asks the user to ask a question and prints out a response. This method takes in self as an argument and the arguments "question" and 'again', which have default values. 

Demo Program Documentation

In my demo program, I have a list of people. 
For each person, an object is created using the Icecream() class. 
It then prints out what ice cream each person got. 
Then another ice cream object is created using the Icecream() class and different methods are applied to it to showcase the class's capabilites.
The two methods that have games are run at the end of the demo program. For those methods, the user will have to input words or numbers with their keyboard.

Instructions

The program can be downloaded and run in the terminal. The user will need to be able to input words or numbers when the program prompts them to. 
