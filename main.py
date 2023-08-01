import os
import datetime

#constants
SMALL_AREA_CAPACITY = 46
MEDIUM_AREA_CAPACITY = 14
LARGE_AREA_CAPACITY = 12
SMALL_BOX = 'X'
MEDIUM_BOX = ' X '
LARGE_BOX = '  X  '

#initialize the compartments
small_boxes, medium_boxes, large_boxes = [], [], []
for i in range(SMALL_AREA_CAPACITY):
    small_boxes.append(' ')
    
    if i < 14:
        medium_boxes.append('   ')
    
    if i < 12:
        large_boxes.append('     ')

#draw the storage
def drawMap():
    os.system('cls')
    print("          /---------------------------\\")
    print(f"          |", end='')
    for i in range(14):
        print(small_boxes[i], end='|')
    print("\n          |                           |")
    print("          |                          -|")
    print("    /-----|  Small                    |")
    print("    |               |", end='') 
    for i in range(14, 23):
        print(small_boxes[i], end='|')
    print("\n    |        Boxes  ------------------|")
    print("    |               |", end='') 
    for i in range(23, 32):
        print(small_boxes[i], end='|')
    print("\n    |     |  Area                     |")
    print("    |     |                          -|")
    print("    |     |                           |")
    print("    |     |", end='')
    for i in range(32, 46):
        print(small_boxes[i], end='|')
    print("\n    |     |---------------------------|")
    print("    |     |", end='')
    for i in range(7):
        print(medium_boxes[i], end='|')
    print("\n ----                                 |")
    print("Entrance        Medium Boxes Area    -|")
    print(" ----                                 |")
    print("    |     |",end='')
    for i in range(7, 14):
        print(medium_boxes[i], end='|')
    print("\n    |     |-------------------|-----------------|")
    print("    |     |  ", end='')
    for i in range(6):
        print(large_boxes[i], end='|')
    print("\n    |                                           |")
    print("    |                  Large Boxes Area        -|")
    print("    |                                           |")
    print("    |     |  ",end='')
    for i in range(6, 12):
        print(large_boxes[i], end='|')
    print("\n    \\-------------------------------------------/")
    input("\n Press enter to exit...")

history = []
customer_list = []
#Customer object
class Customer():
    def __init__(self, first_name, last_name, phone_number, storage_index):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.storage_index = storage_index
        if storage_index[0] in ['s', 'S']:
            self.box = SMALL_BOX
        
        elif storage_index[0] in ['m', 'M']:
            self.box = MEDIUM_BOX
        
        elif storage_index[0] in ['l', 'L']:
            self.box = LARGE_BOX

def success(name):
    input("Transaction successful! Storage allocated to customer " + name + "! Press enter to continue!")
    log = f"{name}'s package stored at {datetime.datetime.now()}"
    history.append(log)
    os.system('cls')

def reject():
    print("\nNot enough space")
    input("Press enter to continue")
    os.system('cls')

def newCustomer():
    os.system('cls')
    #create new storage customer
    print("-----CREATE A NEW STORAGE CUSTOMER-----")
    first_name = ''
    while first_name == '':
        first_name = input("Enter customer first name: ")
        if first_name == '':
            input("\nFIELD REQUIRED! PRESS ENTER TO RETURN! \n")
            os.system('cls')

    last_name = ''
    while last_name == '':
        last_name = input("Enter customer last name: ")
        if last_name == '':
            input("\nFIELD REQUIRED! PRESS ENTER TO RETURN! \n")
            os.system('cls')

    phone_number = ''
    while phone_number == '':
        phone_number = input("Enter customer phone_number: ")
        if phone_number == '':
            input("\nFIELD REQUIRED! PRESS ENTER TO RETURN! \n")
            os.system('cls')

    #get customer storage size
    storage_size_valid = False
    while not storage_size_valid:
        storage_size = input("Enter customer desired storage size(S, M, L): ")
        if storage_size not in ['s', 'S', 'm', 'M', 'l', 'L']:
            input('Invalid input! Please try again.')
            os.system('cls')
        
        else:
            #check if there's an available compartment
            if storage_size in ['s', 'S']:
                for i in range(SMALL_AREA_CAPACITY):
                    if small_boxes[i] != SMALL_BOX:
                        customer_list.append(Customer(first_name, last_name, phone_number, (storage_size + str(i))))
                        small_boxes[i] = SMALL_BOX
                        success(first_name)
                        break

                    elif i == SMALL_AREA_CAPACITY - 1 and small_boxes[i] == SMALL_BOX:
                        reject()
                
            
            elif storage_size in ['m', 'M']:
                for i in range(MEDIUM_AREA_CAPACITY):
                    if medium_boxes[i] != MEDIUM_BOX:
                        customer_list.append(Customer(first_name, last_name, phone_number, (storage_size + str(i))))
                        medium_boxes[i] = MEDIUM_BOX
                        success(first_name)
                        break
                    else:
                        reject()
                    
            elif storage_size in ['l', 'L']:
                for i in range(LARGE_AREA_CAPACITY):
                    if large_boxes[i] != LARGE_BOX:
                        customer_list.append(Customer(first_name, last_name, phone_number, (storage_size + str(i))))
                        large_boxes[i] = LARGE_BOX
                        success(first_name)
                        break
                    else:
                        reject()

            storage_size_valid = True

def retrieveCustomer():
    os.system('cls')
    query = input("Please enter customer phone number: ")
    #Find in database
    for i in range(len(customer_list)):
        if customer_list[i].phone_number == query:
            query = customer_list[i]
            input("Customer Available! Press enter to confirm retrieval.")
            #remove from storage
            if query.storage_index[0] in ['s', 'S']:
                small_boxes[int(query.storage_index[1:])] = ' '
            elif query.storage_index[0] in ['m', 'M']:
                medium_boxes[int(query.storage_index[1:])] = '   '
            elif query.storage_index[0] in ['l', 'L']:
                large_boxes[int(query.storage_index[1:])] = '     '

            history.append(f"{query.first_name}'s package was retrieved at {datetime.datetime.now()}")
            os.system('cls')
        
        elif i == len(customer_list) - 1 and customer_list[i].first_name.lower() != query.lower():
            input("Customer not found. Press enter to return to main menu.")
            os.system('cls')
    
def checkCompartments():
    os.system('cls')
    small_count = 0
    medium_count = 0
    large_count = 0
    for i in range(SMALL_AREA_CAPACITY):
        if i < LARGE_AREA_CAPACITY and large_boxes[i] != LARGE_BOX:
            large_count += 1

        if i < MEDIUM_AREA_CAPACITY and medium_boxes[i] != MEDIUM_BOX:
            medium_count += 1
        
        if small_boxes[i] != SMALL_BOX:
            small_count += 1
    
    print(f"\nThere are {small_count} slots available for small boxes, {medium_count} slots available for medium boxes, and {large_count} slots available for large boxes.")
    input("Press enter to return to main screen")
    os.system('cls')

def logs():
    os.system('cls')
    print("Logs: ")
    for log in history:
        print(log)
    input("Press enter to exit...")

def main():  
    run = True
    while run:
        os.system('cls')
        print("-----WELCOME TO FRONTDESKAPP-----")
        print("""Press
            1: View the storage
            2: Enter a customer
            3: Retrieve customer package
            4: Check available compartments
            5: View logs
            6: Quit Terminal
            """)
        
        menu = input()
        if menu == '1':
            drawMap()
        
        elif menu == '2':
            newCustomer()
        
        elif menu == '3':
            retrieveCustomer()

        elif menu == '4':
            checkCompartments()
        
        elif menu == '5':
            logs()

        elif menu == '6':
            os.system('cls')
            run = False

if __name__ == '__main__':
    main()       