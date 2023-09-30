# -*- coding: utf-8 -*-
"""
OOPL Spring 2020
Programming project 3 - Electronic Address Book

by Marisha Kulseng, 4/16/20

"""

import os

#############################################
"""Begin function/class definition section"""
#############################################

def print_menu():
    print("\n\t**MENU**")
    print("\t   (1) Add Entry")
    print("\t   (2) Delete Entry")
    print("\t   (3) Display a Single Entry")
    print("\t   (4) Display All")
    print("\t   (5) Quit the Program\n")
    
    
def print_submenu():
    print("\n\t**MENU: Display All**")
    print("\t   (1) Sort by (Last) Name")
    print("\t   (2) Sort by Address (Zip -> State -> City)")
    print("\t   (3) Sort by Address (State-> City -> Zip)")
    print("\t   (4) Sort by Email")
    print("\t   (5) Return to Main Menu\n")
    
class contact:
    """class that provides structure for data about contacts in address book"""	
    def __init__(self, f_name, l_name, st_addy, city, state, zip_code, t_num, email):
	    """initialize a contact object"""
	    self.f_name = f_name
	    self.l_name = l_name
	    self.st_addy = st_addy
	    self.city = city
	    self.state = state
	    self.zip_code = zip_code
	    self.t_num = t_num
	    self.email = email
        
    def get_new_contact():
        fname = input("First name: ")
        lname = input("Last name: ")
        address = input("Street Address: ")
        cty = input("City: ")
        sta = input("State: ")
        zcode = input("Zip Code: ")
        telnum = input("Phone number: ")
        em = input("Email address: ")
        return contact(fname, lname, address, cty, sta, zcode, telnum, em)
    
    def print_contact(self):
        print('{:<15} {:15} {:15} {:15} {:15} {:10} {:15} {:15}'.format(self.f_name, self.l_name, self.st_addy, 
                                                                 self.city, self.state, self.zip_code, 
                                                                 self.t_num, self.email))
        
    def __repr__(self):
        return repr('{:<15} {:15} {:15} {:15} {:15} {:10} {:15} {:15}'.format(self.f_name, self.l_name, self.st_addy, 
                                                                 self.city, self.state, self.zip_code, 
                                                                 self.t_num, self.email))

    def print_contact_header(self):
        print('{:15} {:15} {:15} {:15} {:15} {:10} {:15} {:15}'.rstrip().format("First Name", "Last Name", "Street Address", 
                                                                 "City", "State", "Zip Code", 
                                                                 "Phone Number", "Email"))
        print('----------------------------------------------------------------------------------------------------------------------------------')
        
		
#############################################
"""Begin initialization of test data"""		
#############################################
    
contact_list = []
contact_list.append(contact(f_name = "Susie", l_name = "Smith", st_addy = "123 Lala Ave", 
                    city = "Everett", state = "Massachusetts", zip_code = "12394",
                    t_num= "233-484-2827", email = "email@somewhere.edu"))
contact_list.append(contact(f_name = "Sally", l_name = "Smith", st_addy = "33 DoReMi St", 
                    city = "Brookline", state = "Massachusetts", zip_code = "12324",
                    t_num= "233-484-2844", email = "artists@somewhere.edu"))
contact_list.append(contact(f_name = "Archie", l_name = "Smith", st_addy = "123 Lala Ave", 
                    city = "Everett", state = "Massachusetts", zip_code = "12394",
                    t_num= "233-484-2827", email = "flying_monkey@somewhere.edu"))
contact_list.append(contact(f_name = "Zoe", l_name = "Smith", st_addy = "39 FaSo Blvd", 
                    city = "Braintree", state = "Massachusetts", zip_code = "02394",
                    t_num= "233-484-3327", email = "darlin_clementine@somewhere.edu"))
contact_list.append(contact(f_name = "Chidi", l_name = "Anagonye", st_addy = "39 TiDo St", 
                    city = "Braintree", state = "Massachusetts", zip_code = "02394",
                    t_num= "233-484-7492", email = "moral_philosopher@somewhere.edu"))
contact_list.append(contact(f_name = "Eleanor", l_name = "Shellstrop", st_addy = "12385W Place", 
                    city = "Tempe", state = "Arizona", zip_code = "75553",
                    t_num= "472-863-9493", email = "arizona_trashbag@somewhere.edu"))
contact_list.append(contact(f_name = "Jason", l_name = "Mendoza", st_addy = "1 Acidcat Way", 
                    city = "Jacksonville", state = "Florida", zip_code = "53253",
                    t_num= "393-884-9453", email = "jaguars_rule@somewhere.edu"))
contact_list.append(contact(f_name = "Archie", l_name = "Smith", st_addy = "93 Park Ave", 
                    city = "Malden", state = "Massachusetts", zip_code = "01927",
                    t_num= "112-567-3232", email = "smith.archie@somewhereelse.edu"))

#############################################
"""Begin the main section of the program"""
#############################################
while(True):
    contact_list = sorted(contact_list, key=lambda contact: (contact.l_name, contact.f_name, contact.state, contact.city, contact.st_addy)) #default sort by name -> address
    print_menu()
    choice = input("Please enter your selection from the menu: ")
    if (choice == '1'):
        new_contact = contact.get_new_contact()
        contact_list.append(new_contact)        
        print("Contact has been added! \n\tReturning to menu...")
        contact_list = sorted(contact_list, key=lambda contact: (contact.l_name, contact.f_name)) #default sort by name
        os.system("pause")
        os.system("cls")
        
    elif(choice == '2'):
        last = input("Who do you want to delete? Enter their last name. ")
        counter = -1
        counter2 = 0
        result_list =[]
        index_list =[]
        found_item = -1
        for x in contact_list:
            counter += 1
            if(x.l_name.upper() == last.upper()):
                found_item = counter
                result_list.append(x) # keeps running tally of search hits
                index_list.append(counter)
                #break
        #found_item = contact_list.index(l_name = last)
        if(found_item != -1 and len(result_list) == 1):
            address = contact_list[found_item].st_addy
            first = contact_list[found_item].f_name
            del_choice = input("Delete entry " + first + " " + last + " at " + address + "? (Y/N) ")
            if(del_choice == "y" or del_choice == "Y"):
                contact_list.pop(found_item) #removes the first/theoretically ONLY hit
                print("Deleting " + first + "!")
            else:
                print("Cancelling delete request.")
        elif(found_item != -1):
            print("More than one contact matches the criteria. Please select from the following: ")
            for x in result_list:
                print("(" + str(counter2) + ")", end="", flush=True)
                x.print_contact()
                counter2 += 1
            print("(" + str(counter2) + ") Cancel delete")
            while(True):
                del_choice = input()
                if(int(del_choice) < len(index_list)):
                    contact_list.pop(index_list[int(del_choice)])
                    print("Deleting contact!")
                    break
                elif(int(del_choice) == len(index_list)):
                    print("Cancelling delete request.")
                    break
                else:
                    print("Please select from the menu shown above: ")
        else:
            print("That entry does not exist! ")
        os.system("pause")
        os.system("cls")
        
    elif(choice == '3'):
        last = input("Who do you want to look up? Enter their last name. ")
        counter = -1
        found_item = -1
        found_list = []
        final_found_list = []
        for x in contact_list:
            counter += 1
            if(x.l_name.upper() == last.upper()):
                found_item = counter
                found_list.append(x)                
        if(found_item != -1 and len(found_list) == 1):
            address = contact_list[found_item].st_addy
            first = contact_list[found_item].f_name
            print("Viewing entry for " + first + " " + last + ": ")
            #print function for an entry
            entry_to_print = contact_list[found_item]
            entry_to_print.print_contact_header()
            entry_to_print.print_contact()
        elif(found_item != -1):
            first = input("More than one contact matches the criteria. Please enter first name: ")
            for x in found_list:
               if(x.f_name.upper() == first.upper()):
                   final_found_list.append(x)
            if(len(final_found_list) < 1):
                print("That entry does not exist!")
            elif(len(final_found_list) > 1):
                print("More than one contact matches all criteria. Here are the results: ")
                final_found_list[0].print_contact_header()
                for x in final_found_list:
                    x.print_contact()
            else:
                final_found_list[0].print_contact_header()
                final_found_list[0].print_contact()              
            
        else:
            print("That entry does not exist! ")
        os.system("pause")
        os.system("cls")
        
    elif(choice == '4'):
        print_list = []
        while(True):
            os.system("cls")
            print_submenu()
            print("How would you like to sort? ")
            choice2 = input("Please select from the menu: ")
            if(choice2 == '1'):
                print_list = sorted(contact_list, key=lambda contact: (contact.l_name, contact.f_name))
                break
            elif(choice2 == '2'):
                print_list = sorted(contact_list, key=lambda contact: (contact.zip_code, contact.state, contact.city))
                break
            elif(choice2 == '3'):
                print_list = sorted(contact_list, key=lambda contact: (contact.state, contact.city, contact.zip_code))
                break
            elif(choice2 == '4'):
                print_list = sorted(contact_list, key=lambda contact: (contact.email))
                break
            elif(choice2 == '5'):
                print("Returning to the menu...")
                break

        if(choice2 != '5'):   
            contact_list[0].print_contact_header()
            for x in print_list:
                x.print_contact()
        print("")
        os.system("pause")
        os.system("cls")
    
    elif(choice == '5'):
        choice3 = input("Are you sure you want to quit? (Y/N): ")
        if(choice3 == "y" or choice3 == "Y"):
            exit()
        else:
            os.system("cls")
    else:
        os.system("cls")
        #print("Please select from this menu: \n")
        
#print_submenu()
os.system("pause")