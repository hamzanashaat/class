from SobTask import membership
def create_membership(name, membership_ID, borrowed_books, returned_books):
    return membership(name, membership_ID, borrowed_books, returned_books)

my_membership = membership(
    "Robert",
    "M12345",
    ["DanDaDan Manga", "Jujutsu Kaisen", "Death Note"],
    ["DanDaDan Manga"]
)
my_membership2 = membership(
    "Harry",
    "M12456",
    ["My Hero Academia", "One Piece", "Naruto"],
    ["One Piece"]
)
print(f"Membership Name: {my_membership.name}, ID: {my_membership.membership_id}, Borrowed Books: {my_membership.borrowed_books}, Returned Books: {my_membership.returned_books}")
print(f"Membership Name: {my_membership2.name}, ID: {my_membership2.membership_id}, Borrowed Books: {my_membership2.borrowed_books}, Returned Books: {my_membership2.returned_books}")
print("Memberships are Valid and Up to Date!")
print("Memberships Created Successfully!")