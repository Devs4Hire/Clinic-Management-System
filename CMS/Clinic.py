# Importing the necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date as dt

# Reading and storing the necessary CSV files into dataframes
p_d = pd.read_csv('CSV/Patients_Details.csv')
a_d = pd.read_csv('CSV/Admin_Details.csv')


def create_patient_account():
    # Add the patient's details to the dataframe
    pid = len(p_d) + 1
    pname = input("Enter Patient First Name: ")
    plname = input("Enter Patient Last Name: ")
    pgender = input("Enter Patient Gender(M/F): ")
    pbday = input("Enter Patient Date of Birth (dd-mm-yyyy): ")
    pcontact = input("Enter Patient Contact Number: ")
    pemail = input("Enter Patient Gmail Address: ")
    pallergies = input("Enter Patient Allergies(If Any): ")
    p_d.loc[len(p_d.index)] = [pid, pname, plname, pgender, dt.today() , pbday, pcontact, pemail, pallergies]

    # Save the dataframe to the CSV file
    p_d.to_csv('CSV/Patients_Details.csv', index=False)
    print("Congratulations")
    print("New Account Created")


def update_patient_details():
    pid_to_update = input("Enter Patient ID to update details: ")
    
    if int(pid_to_update) in p_d['Patient_ID'].values:
        # Get the index of the patient to update
        index_to_update = p_d.index[p_d['Patient_ID'] == int(pid_to_update)].tolist()[0]
        
        print("Which information you would like to update:")
        print("1. Name")
        print("2. Last Name")
        print("3. Gender")
        print("4. DOB")
        print("5. Phone")
        print("6. Mail")

        which_info = int(input("Enter Option Number: "))

        # Get the updated details from the user
        if which_info == 1:
            pname = input("Enter Updated Patient First Name: ")
            p_d.at[index_to_update, 'Name'] = pname
        elif which_info == 2:
            plname = input("Enter Updated Patient Last Name: ")
            p_d.at[index_to_update, 'Lname'] = plname
        elif which_info == 3:
            pgender = input("Enter Updated Patient Gender(M/F): ")
            p_d.at[index_to_update, 'Gender'] = pgender
        elif which_info == 4:
            pbday = input("Enter Updated Patient Date of Birth (dd-mm-yyyy): ")
            p_d.at[index_to_update, 'DOB'] = pbday
        elif which_info == 5:
            pcontact = input("Enter Updated Patient Contact Number: ")
            p_d.at[index_to_update, 'Phone_no'] = pcontact
        elif which_info == 6:
            pemail = input("Enter Updated Patient Gmail Address: ")
            p_d.at[index_to_update, 'Mail'] = pemail

        # Save the dataframe to the CSV file
        p_d.to_csv('CSV/Patients_Details.csv', index=False)
        print("Patient details updated successfully.")
    else:
        print("Patient ID not found. Please enter a valid Patient ID.")


def patient_details():
    email = input("Enter Patient Email: ")
    password = int(input("Enter Patient Password: "))

    f = p_d[(p_d['Mail'] == email) & (p_d['Patient_ID'] == password)]

    # Use the correct dataframe name ('p_d' instead of 'p_d')
    if f.empty:
        print("Incorrect Entry")
    else:
        print("Patient ID Logged In Successfully")
        print(p_d.loc[f.index.values[0], :])


def patient_delete():
    global p_d , a_d
    email = input("Enter Patient Email: ")
    password = int(input("Enter Patient Password: "))

    f = p_d[(p_d['Mail'] == email) & (p_d['Patient_ID'] == password)]

    if f.empty:
        print("Incorrect Entry")
    else:
        p_d = p_d.drop(f.index.values[0] , axis = 'index')
        print('Patient Deleted Successfully')
        p_d.to_csv('CSV/Patients_Details.csv', index=False)

        
def graph():
    v = p_d.groupby('Gender')['Gender'].size()
    g_ch = int(input("Kind of Graph you want to see ->"))
    if g_ch == 1:
        plt.bar(v.index, v)
        plt.title("Number of Patients Gender Wise(Bar)")
        plt.show()

    elif g_ch == 2:
        pass
  
    else:
        print("Invalid Option")


def menu():
    while True:
        print("\n1. Create Patient Account\n2. Patient Details\n3. Update Patient Account\n4. Delete Patient Details\n5. Graph\n6. Exit")
        option = int(input("Enter Option Number: "))

        if option == 1:
            create_patient_account()
        elif option == 2:
            patient_details()
        elif option == 3:
            update_patient_details()
        elif option == 5:
            graph()
        elif option == 4:
            patient_delete()
        elif option == 6:
            break
        else:
            print("Invalid Option")



def admin_login():
    # Search for the admin in the dataframe
    login_id = int(input("Enter Your Login ID: "))
    login_pass = input("Enter your Password: ")
    result = a_d[(a_d["Admin_ID"] == login_id) & (a_d["Admin_Password"] == login_pass.lower())]
    
    if result.empty:
        # Print the result
        print("Entry Invalid , Try Again")
        admin_login()
    else:
        # Print the admin's details
        print("You Are Now Logged In")
        menu()

admin_login()


