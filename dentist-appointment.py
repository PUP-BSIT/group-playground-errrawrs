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
        print("No Scheduled Appointments.")
    else:
        for appointment in appointments:
            print(appointment)

def add_appointment(appointments):
    #Adds a new appointment to the list.

    appointment_id = input("Enter appointment ID: ")
    patient_name = input("Enter patient name: ")
    procedure = input("Enter procedure type (e.g., cleaning, filling, extraction): ")
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
    print("Appointment added successfully!")

def update_appointment(appointments):
    #Updates an existing appointment's details.

    appointment_id = input("Enter the ID of the appointment to update: ")
    for appointment in appointments:
        if appointment['id'] == appointment_id:
            appointment['name'] = input("Enter new patient name: ")
            appointment['procedure'] = input("Enter new procedure type: ")
            appointment['date'] = input("Enter new appointment date (YYYY-MM-DD): ")
            appointment['time'] = input("Enter new appointment time (HH:MM): ")
            print("Appointment record updated successfully!")
            return
    print("Appointment not found.")

def delete_appointment(appointments):
    #Deletes an appointment from the list.

    appointment_id = input("Enter the ID of the appointment to delete: ")
    for delete, appointment in enumerate(appointments):
        if appointment['id'] == appointment_id:
            del appointments[delete]
            print("Appointment record deleted successfully!")
            return
    print("Appointment not found.")

def search_appointment(appointments):
    #Searches for appointments based on a specific field.

    search_field = input("Enter the field to search using (id, name, procedure, date, time): ").lower()
    search_value = input(f"Enter the value to search for in {search_field}: ")

    found_appointments = [
        appointment for appointment in appointments if appointment.get(search_field) == search_value
    ]

    if found_appointments:
        for appointment in found_appointments:
            print(appointment)
    else:
        print("No matching appointments found.")

def main_function():
    #Main function to control the flow of the program.
    appointments = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            list_all_appointments(appointments)
        elif choice == '2':
            add_appointment(appointments)
        elif choice == '3':
            update_appointment(appointments)
        elif choice == '4':
            delete_appointment(appointments)
        elif choice == '5':
            search_appointment(appointments)
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

main_function()

