import json
import csv
import os

DATA_FILE = "contacts_data.json"

def export_to_csv(contacts):
    """Requirement: Export contacts to CSV format."""
    if not contacts:
        print("Nothing to export!")
        return
    with open('contacts_export.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Group"])
        for name, info in contacts.items():
            writer.writerow([name, info['phone'], info['email'], info['group']])
    print("✅ Exported to contacts_export.csv")

def view_statistics(contacts):
    """Requirement: Contact statistics and analytics."""
    total = len(contacts)
    groups = {}
    for info in contacts.values():
        g = info['group']
        groups[g] = groups.get(g, 0) + 1
    
    print(f"\n--- Statistics ---")
    print(f"Total Contacts: {total}")
    for g, count in groups.items():
        print(f"- {g}: {count}")

# ... (Keep the add, search, and load functions from the previous message)
