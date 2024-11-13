def print_menu():
    # Displays the menu options to the user.
    print("Welcome to Dentist Appointment")
    print("1. List All Appointments")
    print("2. Add Appointment")
    print("3. Update Appointment")
    print("4. Delete Appointment")
    print("5. Search Appointment")
    print("6. Exit")

def list_all_appointments(appointments):
    #Lists all appointments in the list.
    
    if not appointments:
        print("No Scheduled Appointments.\n")
    else:
        for appointment in appointments:
            print(f"{appointment}\n")

def add_appointment(appointments):
    # Adds a new appointment to the list.

    appointment_id = input("Enter appointment ID: ")
    patient_name = input("Enter patient name: ")
    
    print("Available procedures:")
    print("1. Cleaning")
    print("2. Filling")
    print("3. Extraction")
    print("4. Whitening")
    print("5. Root Canal")  # Adding a new procedure
    
    procedure_options = {
        '1': 'cleaning',
        '2': 'filling',
        '3': 'extraction',
        '4': 'whitening',
        '5': 'root canal'
    }
    
    procedure_choice = input("Enter the number corresponding to the procedure type: ")
    procedure = procedure_options.get(procedure_choice, "Unknown Procedure")
    
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM): ")

    appointment = {
        'id': appointment_id,
        'name': patient_name,
        'procedure': procedure,
        'date': date,
        'time': time
    }
    
    appointments.append(appointment)
    print("Appointment added successfully!\n")

def update_appointment(appointments):
    #Updates an existing appointment's details.

    appointment_id = input("Enter the ID of the appointment to update: ")

    for appointment in appointments:
        if appointment['id'] == appointment_id:
            appointment['name'] = input("Enter new patient name: ")
            appointment['procedure'] = input("Enter new procedure type: ")
            appointment['date'] = input("Enter new appointment date (YYYY-MM-DD): ")
            appointment['time'] = input("Enter new appointment time (HH:MM): ")
            print("Appointment record updated successfully!\n")
            return
        
    print("Appointment not found.\n")

def delete_appointment(appointments):
    #Deletes an appointment from the list.

    appointment_id = input("Enter the ID of the appointment to delete: ")

    for delete, appointment in enumerate(appointments):
        if appointment['id'] == appointment_id:
            del appointments[delete]
            print("Appointment record deleted successfully!\n")
            return
        
    print("Appointment not found.\n")

def search_appointment(appointments):
    #Searches for appointments based on a specific field.

    search_field = input("Would you like to search by ID or name?  ")
    search_value = input(f"Enter the value to search for in {search_field}:  ")

    found_appointments = [
        appointment for appointment in appointments if
        appointment.get(search_field) == search_value
    ]

    if found_appointments:
        for appointment in found_appointments:
            print(f"{appointment}")
    else:
        print("No matching appointments found.\n")

def main_function():
    #Main function to control the flow of the program.
    appointments = []

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("\n")
            list_all_appointments(appointments)
        elif choice == '2':
            print("\n")
            add_appointment(appointments)
        elif choice == '3':
            print("\n")
            update_appointment(appointments)
        elif choice == '4':
            print("\n")
            delete_appointment(appointments)
        elif choice == '5':
            print("\n")
            search_appointment(appointments)
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

main_function()
