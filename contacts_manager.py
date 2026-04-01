import json
import csv
import os

# File to store data
DATA_FILE = "contacts.json"

def load_contacts():
    """Requirement: Data persistence with JSON."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def validate_phone(phone):
    """Requirement: Input validation for phone numbers."""
    return phone.isdigit() and len(phone) >= 10

def add_contact(contacts):
    name = input("Enter Name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    
    phone = input("Enter Phone: ").strip()
    if not validate_phone(phone):
        print("Invalid phone format! Use at least 10 digits.")
        return
        
    email = input("Enter Email: ").strip()
    group = input("Group (Friends/Work/Family): ").strip() or "General"
    
    contacts[name] = {"phone": phone, "email": email, "group": group}
    save_contacts(contacts)
    print(f"✅ {name} added successfully!")

def search_contact(contacts):
    query = input("Search by name: ").lower()
    results = {k: v for k, v in contacts.items() if query in k.lower()}
    
    if not results:
        print("No contacts found.")
        return
        
    print(f"\nFound {len(results)} match(es):")
    for name, info in results.items():
        print(f"- {name}: {info['phone']} | {info['group']}")

def display_all(contacts):
    if not contacts:
        print("Your contact list is empty.")
        return
    print(f"\n{'Name':<20} | {'Phone':<15} | {'Group'}")
    print("-" * 50)
    for name, info in contacts.items():
        print(f"{name:<20} | {info['phone']:<15} | {info['group']}")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n" + "="*30)
        print("  CONTACT MANAGEMENT SYSTEM")
        print("="*30)
        print("1. Add Contact\n2. Search Contact\n3. Display All\n4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1': add_contact(contacts)
        elif choice == '2': search_contact(contacts)
        elif choice == '3': display_all(contacts)
        elif choice == '4': break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()
