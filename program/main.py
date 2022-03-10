from names import name


def main():

    name_query = name_search_db(name)
    gender_query = gender_search_db(name)

main()

#Your main method should ask the user to enter values for both of your search parameters,
# and use the readNames() method of Names.py to fetch the matching Name objects. Then, it
# should write those objects to the console just as in the previous lab.

# collecting inputs

def name_search_db(name, name_query):
    while True:
        try:
            name_query = input("Enter the name you're searching for: ")
            if name_query not in name:
                print("Name not found in database. Please try again.")
                name_search = input("Enter the name you're searching for: ")
            else:
                for name_query in name.readNames():
                    print(name_query["Name"])
        except:
            print("Invalid input")

def gender_search_db(name, gender_query):
    gender_query = ''
    gender_query = input("Enter the gender you're searching for. Either M or F: ")
    gender_query = gender_query.upper()
    while gender_query != 'M' and gender_query != 'F':
        print("Please enter M or F for gender.")
        gender_query = input("Enter the gender you're searching for. Either M or F: ")
        gender_query = gender_query.upper()
    else:
        for gender_query in name.readNames():
            print(gender_query["Gender"])

