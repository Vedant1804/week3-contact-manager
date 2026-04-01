Contact Management System
## Project Description
A comprehensive contact management system built with Python using dictionaries and functions. This system allows for full CRUD operations, ensuring that user data is validated and saved permanently in a JSON format.

## What I Learned
Functions: Organizing code into independent blocks for adding, searching, and deleting.

Dictionaries: Using nested dictionaries to store complex contact metadata.

File Operations: Implementing json module to load/save data automatically.

Validation: Using string methods to verify phone numbers and names.

## How to Run
Navigate to: cd week3-contact-manager

Run: python contacts_manager.py
## Data Structure
We use a Dictionary of Dictionaries  lookup time:Pythoncontacts = {
    "Vedant": {
        "phone": "9876543210",
        "email": "vedant@coep.edu.in",
        "group": "University"
    }
}
## Challenges & Solutions
Challenge: Data loss when the program closes.
Solution: Implemented json.dump and json.load to read from a local contacts.json file on startup.
