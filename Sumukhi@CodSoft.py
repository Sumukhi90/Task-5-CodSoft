# Contact Book
Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.

  contactList=[]
newContact={}
choice=0

def printcontactlist():
    for i in range(len(contactList)):
        print(f"{i+1}: {contactList[i]}")
while choice!=6:
    print("Welcome to your contact book!")
    print("Enter 1 to view the contact list\nEnter 2 to add new contact to the list")
    print("Enter 3 to search the contact list\nEnter 4 to update any contact\nEnter 5 to delete any contact")
    print("Enter 6 to EXIT")
    choice=int(input("Enter your choice\n"))
    
    if choice==1:
        if len(contactList)==0:
            print("No contacts in the list!")
        else:
            print("Your contact list:")
            printcontactList()
    if choice==2:
        contactName=input("Enter the contact name:").lower()
        contactPhone=input("Enter the phone number:")
        contactMail=input("Enter the contact E-mail:").lower()
        contactAddress=input("Enter the contact address:")
        newContact.update({"name": contactName, "phone": contactPhone, "email": contactMail, "address": contactAddress})
        contactList.append(newContact)
        print("New contact added!")
    if choice==3:
        search=input("Search the contact by name or number:").lower()
        for item in contactList:
            if search in item.values():
                print("Contact found!")
                print(item)
    if choice==4:
        print("This is your contact list")
        printcontactlist()
        updateChoice=int(input("Enter the number in front of the contact you want to update:"))
        contactName=input("Enter the contact name:").lower()
        contactPhone=input("Enter the phone number:")
        contactMail=input("Enter the contact E-mail:").lower()
        contactAddress=input("Enter the contact address:")
        contactList[updateChoice - 1].update({"name":contactName, "phone": contactPhone,"Mail": contactMail, "address":contactAddress})
        print("Your updated contact list is :")
        printcontactlist()
    if choice==5:
        print("This is your contact list")
        printcontactlist()
        deleteChoice=int(input("Enter the number in front of the contact you want to delete:"))
        contactList.pop(deleteChoice -1)
        print("Contact deleted. Your updated contact list is :")
        printcontactlist()
        
