#------------------------------------------------------------
#Name: Rasheed, Afolabi
#Program title: Victorino Health - Patient Information System
#
# GUIDE FOR READERS:
# This program manages patient records for Victorino Health clinics.
# Key programming concepts demonstrated:
# - Functions and modular design
# - File I/O with CSV files
# - Input validation loops
# - List processing and sorting
# - Exception handling
# - Menu-driven interface
#------------------------------------------------------------

import csv
import os
from shutil import copyfile
from operator import itemgetter

# Global constants - Gaddis Chapter 2.11
BACKUP_FILE = "patients-BKUP.csv"
MAIN_FILE = "patients.csv"
TEMP_FILE = "patients-temp.csv"

def main():
    """Main function - controls program flow with menu loop (Gaddis Ch 4.2)"""
    app_name = "Victorino Health - Patient Information System"
    
    # Main program loop - continues until user exits
    while True:
        display_menu(app_name)
        choice = get_valid_menu_choice()
        
        # Process menu selection using if-elif structure (Gaddis Ch 3.4)
        if choice == '1':
            view_patient_details()
        elif choice == '2':
            add_new_patient()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            display_patient_report()
        elif choice == '9':
            restore_from_backup()
        else:  # choice == 'X'
            print("\n   Exiting program...")
            print(f"\n{'*' * 60}\n{'Thank you for using':^60}\n{app_name:^60}\n{'*' * 60}")
            break

def display_menu(app_name):
    """Display main menu - simple output formatting"""
    print(f"\n{'*' * 60}")
    print(f"{app_name:^60}")
    print(f"{'*' * 60}")
    print("   1 - View Patient Details")
    print("   2 - Add New Patient") 
    print("   3 - Update Patient")
    print("   4 - Delete Patient")
    print("   5 - Display Patient Listing")
    print("   " + "-" * 54)
    print("   9 - Restore Patient Data")
    print("   X - Exit")

def get_valid_menu_choice():
    """Input validation loop - Gaddis Chapter 4.6"""
    valid_choices = ['1', '2', '3', '4', '5', '9', 'X']
    
    while True:  # Validation loop continues until valid input
        choice = input("\n   Enter menu option: ").upper().strip()
        if choice in valid_choices:
            return choice
        print("   Invalid option. Try again.")

# Function 1: View Patient Details
def view_patient_details():
    """Look up and display single patient by ID"""
    print(f"\n{'View Patient Details':^37}")
    print("=" * 37)
    
    patient_id = input("   Enter Patient ID: ").strip()
    
    # File processing with exception handling (Gaddis Ch 7.5)
    try:
        with open(MAIN_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            
            # Search through records
            for row in reader:
                if row[0] == patient_id:
                    display_patient_data(row)
                    input("   Press Enter to continue...")
                    return
            
            print("   Patient not found.")
    except FileNotFoundError:
        print("   Error: Patient file not found.")
    
    input("   Press Enter to continue...")

def display_patient_data(row):
    """Format and display patient information"""
    centers = {'10': 'North Waco', '20': 'West Waco', '30': 'Hewitt'}
    
    print(f"\n   Patient ID: {row[0]}")
    print(f"   Name: {row[2]} {row[1]}")  # First Last
    print(f"   City: {row[3]}")
    print(f"   ZIP: {row[4]}")
    print(f"   Birth Date: {row[5]}")
    print(f"   Phone: {row[6]}")
    print(f"   Center: {row[7]} - {centers.get(row[7], 'Unknown')}")
    print(f"   Balance: ${float(row[8]):,.2f}")
    print(f"   Days Late: {row[9]}")

# Function 2: Add New Patient
def add_new_patient():
    """Add new patient with data validation"""
    print(f"\n{'Add New Patient':^37}")
    print("=" * 37)
    
    # Collect patient data with validation functions
    last_name = get_required_input("   Last name: ").title()
    first_name = get_required_input("   First name: ").title()
    city = get_required_input("   City: ").title()
    zip_code = get_valid_zip()
    birth_date = get_valid_date()
    phone = get_valid_phone()
    center = get_valid_center()
    
    # Generate new ID and create record
    new_id = get_next_patient_id()
    new_record = [new_id, last_name, first_name, city, zip_code, 
                  birth_date, phone, center, '0', '0']
    
    # Append to file
    try:
        with open(MAIN_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_record)
        print(f"\n   Patient added successfully! ID: {new_id}")
    except Exception as e:
        print(f"   Error: {e}")
    
    input("   Press Enter to continue...")

def get_required_input(prompt):
    """Input validation for required fields"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("   This field is required.")

def get_valid_zip():
    """Validate ZIP code - exactly 5 digits"""
    while True:
        zip_code = input("   ZIP code (5 digits): ").strip()
        if zip_code.isdigit() and len(zip_code) == 5:
            return zip_code
        print("   Invalid. Must be 5 digits.")

def get_valid_date():
    """Validate birth date MM/DD/YYYY format"""
    while True:
        date = input("   Birth date (MM/DD/YYYY): ").strip()
        parts = date.split('/')
        
        # Check format and values
        if (len(parts) == 3 and len(parts[2]) == 4 and
            all(part.isdigit() for part in parts)):
            month, day = int(parts[0]), int(parts[1])
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f"{month:02d}/{day:02d}/{parts[2]}"
        print("   Invalid date. Use MM/DD/YYYY format.")

def get_valid_phone():
    """Validate phone XXX-XXX-XXXX format"""
    while True:
        phone = input("   Phone (254-555-5555): ").strip()
        parts = phone.split('-')
        
        if (len(parts) == 3 and len(parts[0]) == 3 and 
            len(parts[1]) == 3 and len(parts[2]) == 4 and
            all(part.isdigit() for part in parts)):
            return phone
        print("   Invalid format. Use XXX-XXX-XXXX.")

def get_valid_center():
    """Validate and select clinic center"""
    while True:
        print("   Centers: 10-North Waco, 20-West Waco, 30-Hewitt")
        center = input("   Enter center number: ").strip()
        if center in ['10', '20', '30']:
            return center
        print("   Invalid. Choose 10, 20, or 30.")

def get_next_patient_id():
    """Generate next available patient ID"""
    max_id = 0
    try:
        with open(MAIN_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[0].isdigit():
                    max_id = max(max_id, int(row[0]))
    except FileNotFoundError:
        pass
    return max_id + 1

# Function 3: Update Patient
def update_patient():
    """Update existing patient record"""
    print(f"\n{'Update Patient':^37}")
    print("=" * 37)
    
    patient_id = input("   Enter Patient ID: ").strip()
    
    # Process file with temporary file for updates (Gaddis file processing)
    found = False
    try:
        with open(MAIN_FILE, 'r') as infile, open(TEMP_FILE, 'w', newline='') as outfile:
            reader, writer = csv.reader(infile), csv.writer(outfile)
            header = next(reader)
            writer.writerow(header)
            
            for row in reader:
                if row[0] == patient_id:
                    found = True
                    updated_row = get_updates(row, header)
                    writer.writerow(updated_row)
                else:
                    writer.writerow(row)
        
        if found:
            os.remove(MAIN_FILE)
            os.rename(TEMP_FILE, MAIN_FILE)
            print("   Update successful!")
        else:
            os.remove(TEMP_FILE)
            print("   Patient not found.")
            
    except Exception as e:
        print(f"   Error: {e}")
    
    input("   Press Enter to continue...")

def get_updates(row, header):
    """Get updated values for patient fields"""
    print("\n   Current data:")
    for i, value in enumerate(row):
        print(f"   {header[i]}: {value}")
    
    updated = row[:]
    # Update specific fields with simple validation
    fields_to_update = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Skip PatientID
    
    for i in fields_to_update:
        new_val = input(f"   New {header[i]} (Enter to skip): ").strip()
        if new_val:
            updated[i] = new_val.title() if i <= 3 else new_val
    
    return updated

# Function 4: Delete Patient
def delete_patient():
    """Delete patient with confirmation"""
    print(f"\n{'Delete Patient':^37}")
    print("=" * 37)
    
    patient_id = input("   Enter Patient ID: ").strip()
    
    found = False
    try:
        with open(MAIN_FILE, 'r') as infile, open(TEMP_FILE, 'w', newline='') as outfile:
            reader, writer = csv.reader(infile), csv.writer(outfile)
            header = next(reader)
            writer.writerow(header)
            
            for row in reader:
                if row[0] == patient_id:
                    found = True
                    display_patient_data(row)
                    confirm = input("\n   Delete this patient? (Y/N): ").upper()
                    if confirm != 'Y':
                        writer.writerow(row)  # Keep the record
                        print("   Deletion canceled.")
                    else:
                        print("   Patient deleted.")
                else:
                    writer.writerow(row)
        
        if found:
            os.remove(MAIN_FILE)
            os.rename(TEMP_FILE, MAIN_FILE)
        else:
            os.remove(TEMP_FILE)
            print("   Patient not found.")
            
    except Exception as e:
        print(f"   Error: {e}")
    
    input("   Press Enter to continue...")

# Function 5: Display Patient Report
def display_patient_report():
    """Filter, sort and display patient listings"""
    print(f"\n{'Patient Report':^37}")
    print("=" * 37)
    
    while True:
        # Get filters from user
        filters = get_filter_criteria()
        patients = filter_patients(filters)
        
        if not patients:
            print("   No records found.")
            input("   Press Enter to continue...")
            return
        
        print(f"\n   Records found: {len(patients)}")
        
        # Check if too many records
        if len(patients) > 50:
            proceed = input("   Show all records? (Y/N): ").upper()
            if proceed != 'Y':
                return
        
        # Apply sorting
        patients = sort_patients(patients)
        
        # Display formatted report
        display_report(patients)
        
        # Ask for new filter
        again = input("\n   New filter? (Y/N): ").upper()
        if again != 'Y':
            break

def get_filter_criteria():
    """Collect filter criteria from user"""
    print("\n   FILTERS (Enter to skip):")
    return {
        'last': input("   Last name starts with: ").lower().strip(),
        'first': input("   First name starts with: ").lower().strip(), 
        'city': input("   City: ").lower().strip(),
        'center': input("   Center (10/20/30): ").strip(),
        'balance_min': input("   Min balance: ").strip(),
        'days_late': input("   Days late: ").strip()
    }

def filter_patients(filters):
    """Apply filters to patient data - List processing (Gaddis Ch 6)"""
    filtered = []
    
    try:
        with open(MAIN_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            
            for row in reader:
                if matches_criteria(row, filters):
                    filtered.append(row)
    except FileNotFoundError:
        print("   Error: File not found.")
    
    return filtered

def matches_criteria(row, filters):
    """Check if patient record matches filter criteria"""
    try:
        # Simple pattern matching and exact matches
        if filters['last'] and not row[1].lower().startswith(filters['last']):
            return False
        if filters['first'] and not row[2].lower().startswith(filters['first']):
            return False
        if filters['city'] and row[3].lower() != filters['city']:
            return False
        if filters['center'] and row[7] != filters['center']:
            return False
        if filters['balance_min'] and float(row[8]) < float(filters['balance_min']):
            return False
        if filters['days_late'] and row[9] != filters['days_late']:
            return False
        return True
    except (ValueError, IndexError):
        return False

def sort_patients(patients):
    """Apply user-selected sorting - Gaddis Ch 6 sorting"""
    print("\n   SORT OPTIONS:")
    print("   1 - Patient ID    2 - Name    3 - Center    4 - Days Late")
    choice = input("   Sort by (Enter to skip): ").strip()
    
    # Using operator.itemgetter for sorting (Gaddis advanced sorting)
    if choice == '1':
        return sorted(patients, key=lambda x: int(x[0]))
    elif choice == '2':
        return sorted(patients, key=itemgetter(1, 2))  # Last, First
    elif choice == '3':
        return sorted(patients, key=itemgetter(7, 1, 2))  # Center, Last, First
    elif choice == '4':
        return sorted(patients, key=lambda x: (-int(x[9]), x[1], x[2]))  # Days desc, name asc
    
    return patients

def display_report(patients):
    """Display formatted patient report with pagination"""
    print(f"\n{'-' * 80}")
    print(f"{'PATIENT REPORT':^80}")
    print(f"{'-' * 80}")
    
    # Simple columnar format
    print(f"{'ID':<6} {'Last':<12} {'First':<12} {'City':<12} {'Center':<8} {'Balance':<10} {'Late':<6}")
    print("=" * 80)
    
    # Display with pagination (Gaddis Ch 4 - counter-controlled loop)
    for i, row in enumerate(patients):
        balance = float(row[8])
        print(f"{row[0]:<6} {row[1]:<12} {row[2]:<12} {row[3]:<12} {row[7]:<8} ${balance:<9,.2f} {row[9]:<6}")
        
        # Pause every 20 records
        if (i + 1) % 20 == 0:
            input("   Press Enter for more...")

# Function 9: Restore from Backup  
def restore_from_backup():
    """Restore patient data from backup file"""
    try:
        copyfile(BACKUP_FILE, MAIN_FILE)
        print("\n   Data restored from backup successfully!")
    except FileNotFoundError:
        print("   Error: Backup file not found.")
    
    input("   Press Enter to continue...")

# Start the program - Gaddis Ch 5.10 main function pattern
if __name__ == "__main__":
    main()