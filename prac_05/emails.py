"""
emails.py

"""
name_to_email_address = {}  # empty dictionary

email_address = input("Email: ").strip()
while email_address != "":
    name_of_email = email_address.split("@")[0]
    if '.' in name_of_email:
        names = name_of_email.split(".")
        name = [i.title() for i in names]
        name = " ".join(name)
    else:
        name = name_of_email.title()
    confirmation = input(f"Is your name, {name}? (Y/n) ")
    print(confirmation)
    if confirmation == 'Y' or confirmation == 'y':
        name_to_email_address[name] = email_address
        # print(name_to_email_address)
    if confirmation == 'N' or confirmation == 'n':
        real_name = input("Name: ")
        name_to_email_address[real_name] = email_address
        # print(name_to_email_address)
        #
    email_address = input("Email: ").strip()

for name, email in name_to_email_address.items():
    print(f"{name} - ({email})")

# Email: lindsay.ward@jcu.edu.au
# Is your name Lindsay Ward? (Y/n)
# Email: abe@gmail.com
# Is your name Abe? (Y/n) y
# Email: jimbo546@hotmail.com
# Is your name Jimbo546? (Y/n) no
# Name: Jim Boh
# Email:
#
# Lindsay Ward (lindsay.ward@jcu.edu.au)
# Abe (Abe@gmail.com)
# Jim Boh (jimbo546@hotmail.com)
