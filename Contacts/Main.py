from ContactsCRUD import ContactCRUD
from Contact import Contact

class Main():
    """
        This is Main Class. It uses Contact and ContactCrud classes to get data from DB.
        This Class handles User Interaction as well
    """
    contactList = []
    contactDict = {}

    @staticmethod
    def selectContact():
        Main.contactList = ContactCRUD.getAllContacts()
        choices = list(range(1,len(Main.contactList)+1))
        Main.contactDict = dict( zip( choices , list(Main.contactList) ) )
        print("\n========All Contacts========")
        for index in Main.contactDict:
            print(index ," : " , Main.contactDict[index])

        choice = int(input("\nChoose Contact {}".format(choices)))
        print("\nChoosen Contact : \n{} \n".format(Main.contactDict[choice]))
        # contact_id = Main.contactDict[choice].id

        return Main.contactDict[choice]

    @staticmethod
    def create():
        newContact = Contact()
        print("\n================================Add Contact==================================")

        userInput1 = input("\nContact Name : ")
        if not userInput1 :
            userInput1 = "No Name"
        newContact.name = userInput1

        userInput2 = input("\nContact Number : ")
        if not userInput2 :
            userInput2 = "Unknown"
        newContact.contactNumber = userInput2

        userInput3 = input("\nAddress : ")
        if not userInput3:
            userInput3 = "No Address"
        newContact.address = userInput3

        userInput4 = input("\nEmail : ")
        if not userInput4:
            userInput4 = "Unknown"
        newContact.email = userInput4

        print("\nNew Contact \n{}".format(newContact))

        result = ContactCRUD.insert_contact(newContact)
        print("\n{} records Inserted".format(result))

    @staticmethod
    def search():
        print("\n==============================Search Contact============================")
        str = input('\nSearch Text : ')
        
        cList = ContactCRUD.search(str)
        print("\nYour Search Result\n")
        for index,cntct in enumerate(cList):
            print(index+1 , " : " ,cntct)

    @staticmethod
    def update():
        selectedContact = Main.selectContact()
        
        uContact = Contact()
        uContact.id = selectedContact.id

        print("\n================================Update Contact==================================")

        userInput1 = input("\nName : ")
        if not userInput1 :
            userInput1 = selectedContact.name
        uContact.name = userInput1

        userInput2 = input("\nContact Number : ")
        if not userInput2 :
            userInput2 = selectedContact.contactNumber
        uContact.contactNumber = userInput2

        userInput3 = input("\nAddress : ")
        if not userInput3:
            userInput3 = selectedContact.address
        uContact.address = userInput3

        userInput4 = input("\nEmail : ")
        if not userInput4:
            userInput4 = selectedContact.email
        uContact.email = userInput4

        result = ContactCRUD.update(uContact)
        print("\n{} records Updated".format(result))

 
    @staticmethod
    def delete():
        print("================================Delete Contact==================================")
        selectedContact = Main.selectContact()
        contact_id = selectedContact.id
        result = ContactCRUD.delete(contact_id)
        print("\n{} records Deleted".format(result))
    
    @staticmethod
    def get_all():
        print("\n================================Contacts Directory==================================\n")
        Main.contactList = ContactCRUD.getAllContacts()
        for index,cntct in enumerate(Main.contactList):
            print("({}) {}".format(index+1,cntct))


    @staticmethod
    def run():
        Main.get_all()
        while True:
            print("\n--------Your Menu--------")
            print("1. Add New")
            print("2. Search")
            print("3. Update")
            print("4. Delete")
            print("5. Show All")
            print("6. Quit")
            
            try:
                choice = int(input("\n Enter your Choice[1,2,3,4,5,6] "))

                if choice in [1,2,3,4,5,6] :
                    if choice == 6 :
                        print("Exit!!!")
                        break
                    elif choice == 1:
                        Main.create()
                    elif choice == 2:
                        Main.search()
                    elif choice == 3:
                        Main.update()
                    elif choice == 4:
                        Main.delete()
                    elif choice == 5:
                        Main.get_all()
                else:
                    print("\n\tWrong Choice! Please Choose one from menu")
                    continue
            
            except ValueError as ve:
                print("Value Error")
                print("Wrong Choice! Please Choose one from menu")
                continue

Main.run()