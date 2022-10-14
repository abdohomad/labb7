import os


def get_valid_integer():
    while True:
        try:
            user_input = input("Enter the minimum mpg ==> ")
            user_input = int(user_input)
            if (user_input <=0 or user_input > 100):
                raise ValueError
        except ValueError:
            print("You must enter a number for the fuel economy")
        else:
            return user_input
def get_file_from_user():
    pass
    
        
def read_file():
    
    #while True:
        #if not os.path.isfile(file_name):
             
            #print(f"Could not open file {file_name}")
        #try:
        #file_name = input("Enter the name of the input vehicle file ==>")
        vehicle = open('vehicles2.txt','r')
        #except IOError:
            #print(f"There is an IO Error {file_name}")
        #else:
        data = vehicle.read()
        print(data)

get_valid_integer()
read_file()

msg = "Enter the name of the input vehicle file ==>"
msg2 = "Enter the name of the input vehicle file ==>"
