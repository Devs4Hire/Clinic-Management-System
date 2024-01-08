# Importing the necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date as dt

# Reading and storing the necessary CSV files into dataframes
p_d = pd.read_csv('CSV/Patients_Details.csv')
a_d = pd.read_csv('CSV/Admin_Details.csv')
appoint= pd.read_csv('CSV/Appointment.csv')


def calculateAge(birthDate):
    today = dt.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def create_patient_account():
    # Add the patient's details to the dataframe
    pid = len(p_d) + 1
    pname = input("Enter Patient First Name: ")
    plname = input("Enter Patient Last Name: ")
    pgender = input("Enter Patient Gender(M/F): ")
    pbday = input("Enter Patient Date of Birth (yyyy-mm-dd): ")
    pcontact = input("Enter Patient Contact Number: ")
    pemail = input("Enter Patient Gmail Address: ")
    pallergies = input("Enter Patient Allergies(If Any): ")
    dob = pbday.split('-')
    age = calculateAge(dt(int(dob[0]), int(dob[1]), int(dob[2])))
    p_d.loc[len(p_d.index)] = [pid, pname, plname, pgender, dt.today() , pbday, pcontact, pemail, pallergies,age]

    # Save the dataframe to the CSV file
    p_d.to_csv('CSV/Patients_Details.csv', index=False)
    print("New Patient detail is entered")


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
        print("7. Age")

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
        elif which_info == 7:
            page = p_d.at[ index_to_update , 'DOB']
            dob = page.split('-')
            age = calculateAge(dt(int(dob[0]), int(dob[1]), int(dob[2])))
            p_d.at[index_to_update, 'Age'] = age

        # Save the dataframe to the CSV file
        p_d.to_csv('CSV/Patients_Details.csv', index=False)
        print("Age updated successfully.")
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
    v = p_d.groupby('Age')['Age'].size()
    print(v.index)
    print('1 - Patients Age wise \n2 - No of appointments made month wise')
    g_ch = int(input("Kind of Graph you want to see ->"))
    if g_ch == 1:
        plt.bar(v.index, v)
        plt.xticks(v.index)
        plt.title("Number of Patients age Wise(Bar)")
        plt.show()

    elif g_ch == 2:
    # Convert the 'AppointmentDate' column to datetime format
        appoint['AppointmentDay'] = pd.to_datetime(appoint['AppointmentDay'])

        # Extract month from the 'AppointmentDate' column and create a new column
        appoint['Month'] = appoint['AppointmentDay'].dt.to_period('M')

        # Group by month and count the number of bookings
        monthly_bookings = appoint.groupby('Month').size()

        # Plotting
        plt.figure(figsize=(10, 6))
        monthly_bookings.plot(kind='bar', color='skyblue')
        plt.title('Number of Appointments per Month')
        plt.xlabel('Month')
        plt.ylabel('Number of Appointments')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
  
    else:
        print("Invalid Option")


def make_book_appointment(appoint):
    # Add the patient's details to the dataframe
    pid = input("Enter Patient Id: ")
    available_patient = p_d[(p_d['Patient_ID'] == int(pid))]

    if available_patient.empty:
        print('Patient ID is not available')
        menu()
    else:
        pappoint = input("Enter Appointment ID: ")
        psch = input("Enter Schedule Day (yyyy-mm-dd): ")  # Adjusted input format
        
        # Calculate patient's age based on date of birth
        dob = available_patient['DOB'].values[0]
        today = pd.to_datetime('today').date()
        age = today.year - pd.to_datetime(dob).year - ((today.month, today.day) < (pd.to_datetime(dob).month, pd.to_datetime(dob).day))
        
        no_show = 'No'  # Assuming default value for No-show is 'No'
        
        # Adding the appointment details to the 'Appointment.csv' dataframe
        appoint.loc[len(appoint)] = [pid, pappoint, pd.to_datetime(psch), pd.to_datetime(psch).date(), age, no_show]

        # Save the dataframe to the CSV file
        appoint.to_csv('CSV/Appointment.csv', index=False)
        print("Appointment is made")



def menu(appoint):
    while True:
        print("\n1. Create Patient Account\n2. Patient Details\n3. Update Patient Account\n4. Delete Patient Details\n5. Graph\n6.Book Appointment\n7. Exit")
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
            make_book_appointment(appoint)
        elif option == 7:
            break
        else:
            print("Invalid Option")



def admin_login(appoint):
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
        menu(appoint)

admin_login(appoint)


