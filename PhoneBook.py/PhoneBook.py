'''
#  File: PhoneBook.py

#  Description: phone book that will store contact information of people that you know

#  Student Name:William Kwon4

#  Student UT EID: uk669

#  Course Name: CS 313E

#  Unique Number:51350

#  Date Created: 9/18/18

#  Date Last Modified:9/21/18
'''
class ContactInfo (object):
  # constructor
  def __init__ (self, street, city, state, zip, country, phone, email):
      self.street=street
      self.city=city
      self.state=state
      self.zip=zip
      self.country=country
      self.phone=phone
      self.email=email


  # string representation of Contact Info
  def __str__ (self):
      return (str(self.street)+str(self.city)+str(self.state)+str(self.zip)+str(self.country)+str(self.phone)+str(self.email))
# Define global dictionary to hold all the contact information
phone_book = {}


# This function adds the contact information of a new person in the
# dictionary

def add_person(self):
  # Create the ContactInfo object
  # Prompt the user to enter the name of the new person


  search = str(input("Enter name: "))

  if search in phone_book:
      print('User Already exist')# Check if name exists in phone book. If it does print a message
      return phone_book



  elif search not in phone_book:                  # Add the name and the contact information to the phone dictionary
      name=search
      street=str(input('Enter street: '))+'\n'
      city=str(input('Enter city: '))+'\n'
      state=str(input('Enter state: '))+'\n'
      zip=str(input('Enter zip: '))+'\n'
      country=str(input('Enter country: '))+'\n'
      phone=str(input('Enter phone: '))+'\n'
      email=str(input('Enter email: '))+'\n'
      contactObj = ContactInfo(street, city, state, zip, country, phone, email)# Create the ContactInfo object

      phone_book[name]=contactObj

  print('The information was added successfully')
  return phone_book






# This function deletes an existing person from the phone dictionary

def delete_person():
     # Create the ContactInfo object
    # Prompt the user to enter the name of the new person


    search = str(input("Enter name: "))


    if search in phone_book:
       del phone_book[search]
       print(search,'was delted from the phone book.')
       return phone_book # Check if name exists in phone book. If it does print a message



    elif search not in phone_book:  # Add the name and the contact information to the phone dictionary
        print(search,' does not exist in the phone book.')
        return phone_book


  # Prompt the user to enter the name of the person

  # If the name exists in phone book delete it.
  # Print message as to the action.

# This function updates the information of an existing person

def update_person():
  search=str(input('Enter name: '))
  if search in phone_book:
      name = search
      street = str(input('Enter street: ')) + '\n'
      if street is '\n':
          street=phone_book[search].street
      city = str(input('Enter city: ')) + '\n'
      if city is '\n':
          city=phone_book[search].city
      state = str(input('Enter state: ')) + '\n'
      if state is '\n':
          state=phone_book[search].state
      zip = str(input('Enter zip: ')) + '\n'
      if zip is '\n':
          zip=phone_book[search].zip
      country = str(input('Enter country: ')) + '\n'
      if country is '\n':
          country=phone_book[search].country
      phone = str(input('Enter phone: ')) + '\n'
      if phone is '\n':
          phone=phone_book[search].phone
      email = str(input('Enter email: ')) + '\n'
      if email is '\n':
          email=phone_book[search].email
      contactObj = ContactInfo(street, city, state, zip, country, phone, email)  # Create the ContactInfo object

      phone_book[name] = contactObj
      print('Update Information in the phone book was successful!')


  elif search not in phone_book:     # Add the name and the contact information to the phone dictionary'name does not exist'
      print(search,"does not exist in the phone book")

  return phone_book


  # Check if name exists in phone book. If it does prompt
  # the user to enter the required information.

  # Write a message as to the action

# This function prints the contact information of an existing person

def search_person():
     # Create the ContactInfo object
    # Prompt the user to enter the name of the new person

    search = str(input("Enter name: "))

    if search in phone_book:
        print (phone_book[search])  # Check if name exists in phone book. If it does print a message



    elif search not in phone_book:  # Add the name and the contact information to the phone dictionary
        print(search,'does not exist in the phone book.')

    return phone_book

  # Prompt the user to enter the name of the person


  # Check if name exists in phone book. If it does print the
  # information in a neat format.

  # If the name does not exist print a message to that effect.

# This function open the file for writing and writes out the contents
# of the dictionary.

def save_quit():
  # Open file for writing
  in_file = open("./phone.txt", "w")
  for i in phone_book.keys():
      in_file.write(i+'\n')
      in_file.write(phone_book[i].street)
      in_file.write(phone_book[i].city)
      in_file.write( phone_book[i].state)
      in_file.write( phone_book[i].zip)
      in_file.write( phone_book[i].country)
      in_file.write( phone_book[i].phone)
      in_file.write( phone_book[i].email)
      in_file.write('\n')




  # Iterate through the dictionary and write out the items in the file


  # Close file
  in_file.close()


  # Print  message

# This function prints the menu, prompts the user for his/her selection
# and returns it.

def menu():
    print('1. Add a Person \n')
    print('2. Delete a Person \n')
    print('3. Search for a Person \n')
    print('4. Update Information on a Person\n')
    print('5. Quit\n')
    # check user input is valid

    while True:
        try:
          selection = int(input("Enter your selection: "))

        except ValueError:
            print(" you typed str, please type numbers between 0-5 ")
            continue
        else:
            break
    while selection>5 or selection<1:
        print("please type numbers between 0-5 ")
        selection = int(input("Enter your selection: "))

    return selection

# This function opens the file for reading, reads the contact information
# for each person and adds it to the dictionary.
def create_phone_book():
  # Open file for reading
  in_file = open ("./phone.txt", "r")

  # Read first line (name)
  line = in_file.readline()
  line=line.strip()


  # Loop through the entries for each person
  while (line != ""):
    name = line


    # Read street
    line = in_file.readline()
    line = line.strip()
    street=line
    # Read city
    line = in_file.readline()
    city=line

    # Read state
    line = in_file.readline()
    state=line

    # Read zip
    line = in_file.readline()
    zip=line

    # Read country
    line = in_file.readline()
    country=line

    # Read phone number
    line = in_file.readline()
    phone=line

    # Read e-mail address
    line = in_file.readline()
    email=line


    # Read blank line
    in_file.readline()

    # Read first line of the next block of data
    line = in_file.readline()
    line = line.strip()

    # Create ContactInfo object
    contactObj = ContactInfo(street, city, state, zip, country, phone, email)

    # Add to phone dictionary
    phone_book[name]= contactObj




  # Close file
  in_file.close()




  return phone_book

def main():
  # Read file and create phone book dictionary
  phone_book=create_phone_book()
  print(phone_book)



  # Print logo
  print ("Phone Book")


  valid = False



  # Print menu and get selection
  options=0
  selection = menu()

  # Keep track of changes in the dictionary
  numChanges = 0

  # Process request, print menu and prompt again and again
  # until the user types 5 to quit.
  while selection != 5:
    if selection==1:
       add_person(phone_book)
       selection = menu()

    if selection==2:
        delete_person()
        selection = menu()
    if selection==3:
        search_person()
        selection = menu()
    if selection==4:
        update_person()
        selection = menu()

    if selection==5:
        save_quit()
        print
        print("Thank you for using the Phone Book.\n")# Goodbye message
        quit()# Save and quit

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
