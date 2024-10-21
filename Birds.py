from Collections import *
import csv

#each instance represents a bird
class Bird:
    #create a class attribute binary search tree of all birds
    all_birds = BinarySearchTree()
    #each bird has a name, color, and conservation status and gets added to the tree of all birds
    def __init__(self, name, color, status):
        self.name = name
        self.color = color
        self.status = status
        Bird.all_birds.insert(self)

    def __repr__(self):
        return f"Name: {self.name}, Primary Color: {self.color}, Conservation Status: {self.status}"


    @classmethod
    def import_birds_from_csv(cls, filename: str):
        #reads each column in the csv file
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            birdlist = list(reader)
            #for each line in the csv file
            #create a bird object based on the data in that row
            for bird in birdlist:
                Bird(
                    name = bird['Name'],
                    color = bird['Primary Color'],
                    status = bird['Conservation Status']
                )

# this program simulates an aviary where one can view birds and buy them. 
if __name__ == '__main__':
    #import 100 birds of the world into the binary search tree of all birds
    Bird.import_birds_from_csv("Examples/100 Birds of the World.csv")
    #create a stack for viewed birds and a queue of owned birds
    viewed_birds = Stack()
    owned_birds = Queue()
    #welcome statement, ask before printing the list of all birds
    print("Welcome to the aviary!")
    the_input = input("Would you like to see a list of our birds (y/n)")
    while the_input != "q":
        if the_input == "n":
            break
        elif the_input == "y":
            Bird.all_birds.print_name()
        #allow the user to view the attributes of birds in the list by typing the name
        while the_input != "x":
            the_input = input("Enter a bird you would like to view: (x to move on from viewing birds)")
            print(Bird.all_birds.get_bird(the_input))
            viewed_birds.push(the_input)
        #when the user types x, print the birds they've viewed
        print(f"Viewing history: \n {viewed_birds}")
        #allow the user to buy a bird by typing the name and add it to their owned birds
        the_input = input("Would you like to buy a bird? (y/n)")
        if the_input == "n":
            break
        elif the_input == "y":
            the_input = input("Enter the bird you would like to purchase: ")
            owned_birds.push(the_input)
            print(f"Thank you for purchasing a {the_input}!")
            #ask them if they want to view/purchase more birds or quit and see the birds they bought
            the_input = input("\n What would you like to do? \n View and purchase more birds (v) \n View owned birds and quit (o) \n ")
            #if they want to quit
            if the_input == "o":
                #print owned birds
                print(f"\n Owned birds: \n {owned_birds}")
                #if they have more than 3 birds, remove the first birds they bought until it is down to 3
                if owned_birds.num_nodes > 3:
                    print("It is unlawful to own more than three birds. Selling excess back to the aviary")
                    for x in range(owned_birds.num_nodes-3):
                        owned_birds.pop()
                    #print the owned birds again and quit
                    print(f"\n Owned birds: \n {owned_birds}")
                    break
                break
            #if they wanted to view and purchase more birds
            elif the_input == "v":
                #delete their viewing history
                for x in range(viewed_birds.num_nodes):
                    viewed_birds.pop()
                pass