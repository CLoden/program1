from names import name


def main():

    name_search_db(name)
    gender_search_db(name)

main()

#Your main method should ask the user to enter values for both of your search parameters,
# and use the readNames() method of Names.py to fetch the matching Name objects. Then, it
# should write those objects to the console just as in the previous lab.

# collecting inputs

def name_search_db():
    while True:
        try:
            name_search = input("Enter the name you're searching for: ")
            if name_search not in name:
                print("Name not found in database. Please try again.")
                name_search = input("Enter the name you're searching for: ")
            else:
                for name_search in name:
                    print(name_search)
        except:
            print("Invalid input")

def gender_search_db():
    gender = ''
    gender = input("Enter the gender you're searching for. Either M or F: ")
    gender = gender.upper()
    while gender != 'M' and gender != 'F':
        print("Please enter M or F for gender.")
        gender = input("Enter the gender you're searching for. Either M or F: ")
        gender = gender.upper()
    else:
        for gender in name:
            print(gender)

