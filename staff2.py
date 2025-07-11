from StaffTask import staff as Staff

def create_Staff(name, Staff_ID, position):
    return Staff(name, Staff_ID, position)

staff1 = Staff("Alice", "S12345", "Manager")
staff2 = Staff("Johny", "S14665", "Senior Staff")

print(f"Staff Name: {staff1.name}, ID: {staff1.staff_ID}, Staff Position: {staff1.position}")
print(f"Staff Name: {staff2.name}, ID: {staff2.staff_ID}, Staff Position: {staff2.position}")
staff = input("Enter Staff name to Add The Book to the Borrow:")
staff = input("Enter Book Name to add to the Borrow List:")
if staff1.name == staff:
    print(f"Staff {staff1.name} has added the following book to the shelves: {staff}")
elif staff2.name == staff:
    print(f"Staff {staff2.name} has added the following book to the shelves: {staff}")
else:
    print("invalid staff name or book name")