# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
#Yunan Xu, 11.26.2019
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
file=None
row={}

class Product:
    @staticmethod
    def Addtolist(listofrow):
        Product_name = str(input("enter product name: ")).strip()
        Product_price=str(input("enter product price: ")).strip()
        row={"Productname":Product_name , "Productprice" : Product_price}
        listofrow.append(row)
        return listofrow



   # properties:
   #     product_name: (string) with the products's  name
   #     product_price: (float) with the products's standard price
   # methods:

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    @staticmethod
    def Readdile(filename, listofrows):
        file = open(filename, "r")
        for line in file:
            data = line.split(",")
            row = {"Productname": data[0].strip(), "Productprice": data[1].strip()}
            listofrows.append(row)
        file.close()
        return listofrows

    @staticmethod
    def savedata(filename, listofrow):
        file =open(filename,"w")
        for row in listofrow:
            file.write(row["Productname"] + "," +row["Productprice"] + "\n")
        file.close()







# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File
        4) Exit Program
        ''')
    # TODO: Add code to get user's choice
    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print("------------------------------------------------------")  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row["Productname"] + " (" + row["Productprice"] + ")")
        print("*******************************************")
        print("--------------------------------------------")  # Add an extra line for looks


    # TODO: Add code to get product data from user
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
while(True):
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        continue  # to show the menu

    elif (strChoice.strip() == '2'):

        # Step 3.2.a - Ask user for new task and priority
        # ToDo: Place IO code in a new function
        # strTask = str(input("What is the task? - ")).strip()  # Get task from user
        # strPriority = str(input("What is the priority? [high|low] - ")).strip()  # Get priority from user
        # print()  # Add an extra line for looks

        # Step 3.2.b  Add item to the List/Table
        # ToDo: Place processing code in a new function
        # dicRow = {"Task": strTask, "Priority": strPriority}  # Create a new dictionary row
        # lstTable.append(dicRow)  # Add the new row to the list/table

       Product.Addtolist(lstOfProductObjects)
       IO.ShowCurrentItemsInList(lstOfProductObjects)
    elif(strChoice == '3'):
        FileProcessor.savedata(strFileName,lstOfProductObjects)

    elif(strChoice == '4'):
        break


