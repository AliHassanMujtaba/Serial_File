import os
import pickle

class product():
    Product_ID = 0
    Name = ""
    Unit_price = 0.0
    Dicountinued = False

def add_record():

    file = open("Record.dat","ab")
    temp_record = product()
    temp_record.Product_ID = int(input("Enter Product ID : "))
    temp_record.Name = input("Enter the Name : ")
    temp_record.Unit_price = float(input("Enter the price : "))
    temp = int(input("1 for True or 0 for False : "))
    print("**************************")
    if temp == 1:
        temp_record.Dicountinued = True
    else:
        temp_record.Dicountinued = False

    pickle.dump(temp_record,file)
    file.close()

def print_all() :
    temp_record = product()
    file = open("Record.dat","rb")
    file.read()
    eof = file.tell()
    file.seek(0)
    if eof == file.tell():
        print("File is Empty")
    else:
        while file.tell() != eof:
            temp_record = pickle.load(file)
            print("Product ID   : ", temp_record.Product_ID)
            print("Product Name : ", temp_record.Name)
            print("Product Price: ", temp_record.Unit_price)
            print("Discontinued : ", temp_record.Dicountinued)
            print("**************************")

    file.close()

def search(s_item):
    temp_record = product()
    file = open("Record.dat",'rb')
    file.read()
    eof = file.tell()
    file.seek(0)
    Found = False
    while file.tell() != eof and Found != True:
        temp_record = pickle.load(file)
        if temp_record.Product_ID == s_item:
            Found = True
            print("Product ID   : ", temp_record.Product_ID)
            print("Product Name : ", temp_record.Name)
            print("Product Price: ", temp_record.Unit_price)
            print("Discontinued : ", temp_record.Dicountinued)
            print("**************************")
    file.close()
    if Found == False:
        print("Item Not Found")

def delete_self(del_id):
    temp_record = product()
    temp_array = [product()] * 50
    counter = 0
    found = False
    file = open("Record.dat", "rb")
    file.read()
    eof = file.tell()
    file.seek(0)
    while file.tell() != eof:
        temp_record = pickle.load(file)
        if temp_record.Product_ID == del_id:
            found = True
        else:
            temp_array[counter] = temp_record
            counter = counter + 1
    file.close()
    if found == True:
        file = open("Record.dat", "wb")
        temp_record = product()
        count = 0
        while count < counter:
            temp_record = temp_array[count]
            pickle.dump(temp_record, file)
            count = count + 1
    else:
        print("Item not found.")

def delete_Book(del_id):
    temp_record = product()
    file = open("Record.dat", "rb")
    file.read()
    eof = file.tell()
    file.seek(0)
    found = False
    while eof != file.tell() and found == False:
        temp_record = pickle.load(file)
        if temp_record.Product_ID == del_id:
            found = True
    file.close()
    if found == True:
        file = open("Record.dat", "rb")
        temp = open("Temp.dat", "wb")
        file.seek(0)
        while eof != file.tell():
            temp_record = pickle.load(file)
            if temp_record.Product_ID != del_id:
                pickle.dump(temp_record,temp)
        file.close()
        temp.close()
        os.remove("Record.dat")
        os.rename('Temp.dat','Record.dat')
    else:
        print("Such Item doesn't exist in the file")




def value_of_stock():
    file = open("Record.dat","rb")
    temp_record = product()
    file.read()
    eof = file.tell()
    file.seek(0)
    total = 0.0
    while file.tell() != eof:
        temp_record = pickle.load(file)
        total = total + temp_record.Unit_price
    file.close()
    return total

def print_discontinued_products():
    temp_record = product()
    file = open("Record.dat","rb")
    file.read()
    eof = file.tell()
    file.seek(0)
    while file.tell() != eof:
        temp_record = pickle.load(file)
        if temp_record.Dicountinued == True:
            print("Product ID   : ", temp_record.Product_ID)
            print("Product Name : ", temp_record.Name)
            print("Product Price: ", temp_record.Unit_price)
            print("Discontinued : ", temp_record.Dicountinued)
            print("**************************")

    file.close()

def print_continued_products():
    file = open("Record.dat","rb")
    temp_record = product()
    file.read()
    eof = file.tell()
    file.seek(0)
    while file.tell() != eof:
        temp_record = pickle.load(file)
        if temp_record.Dicountinued == False:
            print("Product ID   : ", temp_record.Product_ID)
            print("Product Name : ", temp_record.Name)
            print("Product Price: ", temp_record.Unit_price)
            print("Discontinued : ", temp_record.Dicountinued)
            print("**************************")

    file.close()

def print_products_expensive_then_100():
    file = open("Record.dat","rb")
    temp_record = product()
    file.read()
    eof = file.tell()
    file.seek(0)
    while file.tell() != eof:
        temp_record = pickle.load(file)
        if temp_record.Unit_price > 100:
            print("Product ID   : ", temp_record.Product_ID)
            print("Product Name : ", temp_record.Name)
            print("Product Price: ", temp_record.Unit_price)
            print("Discontinued : ", temp_record.Dicountinued)
            print("**************************")
    file.close()

def main():

    choice = ""
    while choice != "9":
        print(" 1 To Add Record")
        print(" 2 To Print All")
        print(" 3 To Search a Record")
        print(" 4 Delete a Record")
        print(" 5 Total Stock Value")
        print(" 6 List the Discontinued Products")
        print(" 7 List the continued Product")
        print(" 8 List the item above 100")
        print(" 9 Quit")

        print("**************************")
        choice = input("Enter your choice : ")

        if choice == "1":
            add_record()

        elif choice == "2":
            print_all()

        elif choice == "3":
            s_item = int(input("Enter the Product ID of the Product you want to search : "))
            search(s_item)

        elif choice == "4":
            id = int(input("Enter the Id you want to delete : "))
            delete_Book(id)

        elif choice == "5":
            print("Total Value of Stock is = $",value_of_stock())

        elif choice == "6":
            print_discontinued_products()

        elif choice == "7":
            print_continued_products()

        elif choice == "8":
            print_products_expensive_then_100()

        elif choice == "9":
            print("Good Bye !")

        else:
            print("Invalid Input")

main()

