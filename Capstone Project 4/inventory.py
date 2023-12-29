# importing the tabulate module
from tabulate import tabulate

# defining the shoe class
class Shoes:

    """
    This is for creating a shoe object from data read from an inventory file

    Attributes of the data
       
        country : country it is available in
        code : each shoe type has a unique code
        product : name of the shoe
        cost : price of the shoe
        quantity : number of available shoes
    
    """

    def __init__(self,country,code,product,cost,quantity):

        """
        Constructor function to initialize the attributes of a Shoe object

        """
        # class attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # method to get the cost of the shoe
    def get_cost(self):

        """
        This method returns the cost value of a Shoe class object.

        """
        # returning the Shoe object cost
        return float(self.cost)
    
    # Method to get the quantity of a shoe type
    def get_quanty(self):

        """
        This method returns the quantity value of a Shoe class object.

        """
        # returning the Shoe object quantity
        return float(self.quantity)
    
    def __str__(self):

        """This method returns a string representation of a class."""

        # string containing information about the class objects
        string = f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
        
        return string

# list to store shoe objects
shoe_objects = []

def read_shoes_data():

    """
    This function reads an inventory file containing information about the shoes.
    Creates a shoe object for each shoe and store it in a list.

    """
    # asking the user for the file they want to read
    file_name = input("Enter the file name with shoe data: ")
    
    # no exceptions
    try:
        
        file = open(file_name,'r') # opening the file

        line_number = 0 # initializing line count 
        
        # going through each line
        for line in file:

            line_number += 1 # updating line count
            
            # avoiding creating a header object
            if line_number != 1:
 
                line = line.split(",") # list of line data
                
                # creating a shoe_object for each line 
                shoe_object = Shoes(line[0],line[1],line[2],line[3],int(line[4]))

                # adding object to the list of shoe objects
                shoe_objects.append(shoe_object)
        
        print("Shoe data has been read successfully.")
        
        file.close() # closing file

    # if the file does not exist
    except FileNotFoundError as file_error:
        
        # error messages to display
        print("Entered file cannot be found! \n")
        print(file_error,"\n")

def capture_shoes():

    """
    This function adds a new shoe object to the shoe object list.

    """
    # exception handling for attribute inputs
    try:
        
        # asking the user to input the shoe object attributes
        country = input("Enter the country: ")
        code = input("Enter code: ")
        product = input("Enter product name: ")
        cost = round(float(input("Enter cost of product: ")),2)
        quantity = int(input("Enter quantity of stock: "))
    
        # creating a new shoe object
        shoe_object = Shoes(country,code,product,cost,quantity)

        # adding the new shoe to the list of shoes available
        shoe_objects.append(shoe_object)
    
    # handling value error for attribute inputs
    except ValueError as error:

        print("Invalid input.\n") 

        print(error) # displaying error
    
def view_all():

    """
    This function displays a table containing information of each shoe object.

    """
    # displaying the information in a table format
    header = ['Country','Code','Product','Cost {R}','Quantity']
    
    # list of a list of each object attributes
    shoes = [shoe.__str__().split(',') for shoe in shoe_objects]
    
    # displaying the table
    print(tabulate(shoes, headers = header))

def re_stock():

    """
    This function finds a shoe object with the lowest quantity,the shoes that needs restocking.
    Asks the user if they wants to update the quantity of the shoes and then updates it. 
    This quantity should be updated on the inventory file for this shoe.

    """
    # getting the minimum quantity in all object quantities
    quantity = min([shoe.get_quanty() for shoe in shoe_objects])

    # storage for the object when found
    shoe_object = []

    shoes = [] # list to store shoe objects

    # iterating through objects list              
    for shoe in shoe_objects:
        
        # checking if the objects quantity is the lowest quantity
        if shoe.get_quanty() == quantity:
            
            # storing a list of the objects attributes in another list
            shoe_object.append(shoe.__str__().split(','))
            
            # storing all shoe objects with smallest quantity
            shoes.append(shoe)

    # headers for the table        
    header = ['Country','Code','Product','Cost {R}','Quantity']
            
    # displaying the information in a table format
    print(tabulate(shoe_object, headers = header))
    
    print() # empty line

    # asking the user if they want to restock
    print("Enter yes or no below.")
    restock = input("Would you like to restock the item? ").lower()
    
    if restock == 'yes':
        
        # getting new quantity from the user
        quantity = int(input("Enter the quatity of the item: "))

        # asking the user for the code of the item
        code = input("Enter the code item: ")
        
        # searching for the item to update
        for item in shoes:

            if item.code == code:
                
                # updating item quantity
                item.quantity = quantity # updating shoe quantity

        #updating the information on the inventory file
        print("Enter the inventory file name to add updated shoe quantity")
        file_name = input("File name: ")
        
        # updating information on file
        try:
            
            file = open(file_name,'w') # opening file

            file.write("Country,Code,Product,Cost,Quantity\n") # updating file

            for shoe in shoe_objects:

                file.write(shoe.__str__() + "\n") # updating file
            
            file.truncate()
            file.close() # closing file
        
        # if the file does not exist
        except FileNotFoundError as file_error:
            
            # error messages to display
            print("Entered file cannot be found! \n")
            print(file_error,"\n")

    elif restock == 'no':
        pass # do nothing

    else: 
        print("Invalid input!\n")

def seach_shoe():

    """
    This function searches for a shoe based on its code.

    """
    # asking the user for the code of the shoes they want
    code = input("Enter the shoe code: ")

    # variable to update when shoe is found
    found = False
    
    # looking for the specific shoe in the list
    for shoe in shoe_objects:
        
        # when the shoe is found
        if shoe.code == code:

            found = True # updating that the shoe is found

            # displaying the shoe information in a table form
            header = ['Country','Code','Product','Cost {R}','Quantity']
            
            shoe = [shoe.__str__().split(',')]
            
            # displaying table
            return tabulate(shoe, headers = header)
    
    # when the shoe is not found
    if found == False:

        return f"The shoe with code {code} could not be found!"

def value_per_item():

    """
    This function displays the total value of each shoe in a table.

    """
    # displaying the information in a table format
    header = ['Country','Code','Product','Stock Value {R}']
    
    # list to store the required information
    shoes= []

    for shoe in shoe_objects:
        
        # storing data for each shoe object
        shoes.append([shoe.country,shoe.code,shoe.product,shoe.get_cost()*shoe.get_quanty()])
    
    # displaying the table
    print(tabulate(shoes, headers = header))

def highest_qty():

    """
    This function searches for the shoe with the highest quatity.
    The shoe is then shown to be on sale.

    """
    # checking the highest quantity in the shoes
    quantity = max([shoe.get_quanty() for shoe in shoe_objects])
    
    # list to store object attributes
    shoe_list = []

    # looking for the specific              
    for shoe in shoe_objects:
        
        # confirming quantity of the shoe object
        if shoe.get_quanty() == quantity:
            
            # preparing shoe information for displaying
            shoe_list.append(shoe.__str__().split(','))
            
    print() # empty line

    print("This shoe is on sale now.\n")

    # displaying shoe information in a table form
    header = ['Country','code','Product','Cost {R}','Quantity']

    # displaying the table
    print(tabulate(shoe_list, headers = header))

def main():

    """
    main function to perform all required operations of the code.

    """
    # initializing looping condition
    user_choice = -1

    # while loop to view and update shoes information
    while user_choice != 0:
        
        print("Enter the number of what you would like to do?\n")
        
        # creating input string
        choices = "1 read shoe data\n2 add a shoe\n3 view all shoes\n4 view smallest quantity shoes\n"
        more_choices = "5 search for a shoe\n6 view value per item\n7 view highest quantity shoes\n0 quit\n\n"
    
        # input string to display to user
        options = choices + more_choices

        # asking user to enter their choice
        user_choice = int(input(options))
    
        # analysing user choices and performing the necessary tasks
        if user_choice == 1:
            
            # reading the inventory file for shoe information
            read_shoes_data()

        elif user_choice == 2:
            
            # adding a new shoe to the list
            capture_shoes()

        elif user_choice == 3:
            
            # checking if shoe data has been read in
            if len(shoe_objects) != 0:

                view_all() # viewing all shoes information
            
            else:
                print("There is no shoe information available")
        
        elif user_choice == 4:
            
            # checking if shoe data has been read in
            if len(shoe_objects) != 0:
                
                # checking items that are ruuning out and restocking
                re_stock() 
            
            else:
                print("There is no shoe information available")
            
        elif user_choice == 5:
            
            # checking if shoe data has been read in
            if len(shoe_objects) != 0:

                print(seach_shoe()) # displaying shoe information
            
            else:
                print("There is no shoe information available")
    
        elif user_choice == 6:
            
            # checking if shoe data has been read in 
            if len(shoe_objects) != 0:

                value_per_item() # displaying value of all items
            
            else:
                print("There is no shoe information available")
            
        elif user_choice == 7:
            
            # checking if shoe data has been read in
            if len(shoe_objects) != 0:

                highest_qty() # viewing highest quantity shoes
            
            else:
                print("There is no shoe information available")
        
        # to exit the code
        elif user_choice == 0:
            
            print("Goodbye") # Exiting the code
        
        # when the user enters an unexpected input
        else:
            print("Incorrect input entered, try again!")
        
        print() # empty line

# invoking the main function
if __name__ == "__main__":
    main()
