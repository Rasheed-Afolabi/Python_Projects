# 🏥 Medical Information Manager

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

> A comprehensive patient management system for Victorino Health multi-clinic operations

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [File Structure](#-file-structure)
- [Technical Details](#-technical-details)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 🎯 Overview

The **Medical Information Manager** is a Python-based patient record management system designed for Victorino Health's multi-clinic operations in Central Texas. This application provides a complete CRUD (Create, Read, Update, Delete) interface for managing patient information across three clinic locations.

### 🏢 Supported Clinics
| Clinic ID | Name | Location |
|-----------|------|----------|
| 10 | North Waco Clinic | North Waco, TX |
| 20 | West Waco Clinic | West Waco, TX |
| 30 | Hewitt Clinic | Hewitt, TX |

## ✨ Features

### 🔍 **Core Functionality**
- **Patient Lookup**: Search and view detailed patient information
- **Add New Patients**: Register new patients with comprehensive data validation
- **Update Records**: Modify existing patient information
- **Delete Patients**: Remove patient records with confirmation
- **Advanced Reporting**: Filter and sort patient data with multiple criteria

### 🛡️ **Data Management**
- **Automatic ID Generation**: Smart patient ID assignment
- **Data Validation**: Comprehensive input validation for all fields
- **Backup & Restore**: Built-in data protection mechanisms
- **CSV Processing**: Efficient file-based data storage

### 📊 **Advanced Features**
- **Multi-field Filtering**: Filter by name, city, center, balance, etc.
- **Flexible Sorting**: Sort by ID, name, center, or days late
- **Pagination**: Handle large datasets with 20-record pages
- **Pattern Matching**: Advanced search capabilities

## 💻 System Requirements

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: 50MB available space
- **Dependencies**: Built-in Python modules only

## 📦 Installation

### Method 1: Direct Download
```bash
# Clone the repository
git clone https://github.com/Rasheed-Afolabi/Python_Projects.git

# Navigate to project directory
cd "Python_Projects/Medical Information Manager"

# Run the application
python patient_system.py
```

### Method 2: Download ZIP
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract to your desired location
4. Run `python patient_system.py`

## 🚀 Usage

### Starting the Application
```bash
python patient_system.py
```

### Main Menu Options
```
****************************************************
    Victorino Health - Patient Information System
****************************************************
   1 - View Patient Details
   2 - Add New Patient
   3 - Update Patient
   4 - Delete Patient
   5 - Display Patient Listing
   ----------------------------------------------------
   9 - Restore Patient Data
   X - Exit
```

### Sample Workflow
1. **Add a New Patient** → Option 2
2. **View Patient Details** → Option 1
3. **Generate Reports** → Option 5
4. **Update Information** → Option 3

## 📸 Screenshots

### Main Menu Interface
```
****************************************************
    Victorino Health - Patient Information System
****************************************************
   1 - View Patient Details
   2 - Add New Patient
   3 - Update Patient
   4 - Delete Patient
   5 - Display Patient Listing
   ----------------------------------------------------
   9 - Restore Patient Data
   X - Exit
   ----------------------------------------------------

   Enter menu option: _
```

### Patient Details View
```
=====================================
           View Patient Details
=====================================

   Patient ID: 1001
   Name: John Smith
   City: Waco
   ZIP: 76701
   Birth Date: 01/15/1985
   Phone: 254-555-1234
   Center: 10 - North Waco
   Balance: $150.75
   Days Late: 0
```

### Advanced Filtering
```
   FILTERS (Enter to skip):
   Last name starts with: sm
   First name starts with: 
   City: waco
   Center (10/20/30): 10
   Min balance: 100
   Days late: 

   Records found: 3
```

### Report Output
```
--------------------------------------------------------------------------------
                                PATIENT REPORT
--------------------------------------------------------------------------------
ID     Last         First        City         Center   Balance    Late
================================================================================
1001   Smith        John         Waco         10       $150.75    0
1002   Smith        Jane         Waco         10       $200.00    5
1003   Smithson     Bob          Waco         10       $125.50    0
```

## 📁 File Structure

```
Medical Information Manager/
│
├── patient_system.py          # Main application file
├── patients.csv              # Primary patient data
├── patients-BKUP.csv         # Backup patient data
├── patients-temp.csv         # Temporary file (auto-generated)
├── README.md                 # This documentation
└── requirements.txt          # Python dependencies (optional)
```

### Data File Format (CSV)
```csv
PatientID,LastName,FirstName,City,ZipCode,BirthDate,Phone,Center,Balance,DaysLate
1001,Smith,John,Waco,76701,01/15/1985,254-555-1234,10,150.75,0
1002,Johnson,Mary,Hewitt,76643,03/22/1978,254-555-5678,30,0.00,0
```

## 🔧 Technical Details

### Programming Concepts Demonstrated
- **Modular Programming**: Function-based architecture
- **File I/O Operations**: CSV reading/writing
- **Input Validation**: Comprehensive data validation loops
- **Exception Handling**: Robust error management
- **Data Structures**: Lists, dictionaries for data processing
- **Sorting Algorithms**: Multi-field sorting capabilities

### Key Functions
| Function | Purpose |
|----------|---------|
| `main()` | Program entry point and menu control |
| `view_patient_details()` | Display individual patient information |
| `add_new_patient()` | Register new patients with validation |
| `update_patient()` | Modify existing patient records |
| `delete_patient()` | Remove patient records safely |
| `display_patient_report()` | Generate filtered and sorted reports |

### Validation Features
- **ZIP Code**: 5-digit numeric validation
- **Phone Numbers**: XXX-XXX-XXXX format enforcement
- **Dates**: MM/DD/YYYY format with range checking
- **Center Codes**: Restricted to valid clinic IDs (10, 20, 30)
- **Required Fields**: All essential data must be provided

## 🛠️ Development

### Code Style
- Follows **Gaddis Python textbook** conventions
- Comprehensive commenting and documentation
- Modular function design
- Consistent naming conventions

### Testing
- Manual testing with sample data
- Edge case validation
- Error condition handling
- Data integrity verification

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 Acknowledgments

- **Tony Gaddis** - Python Programming Textbook
- **Victorino Health** - System requirements and specifications

---

*Built with ❤️ for healthcare management*

**Last Updated**: December 2024
