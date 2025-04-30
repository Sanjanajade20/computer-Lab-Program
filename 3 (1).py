# Accept contact details from the user and create a vcard that we can directly store in our mobile.

name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")
address = input("Enter address: ")

vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
ADR;TYPE=HOME:;;{address}
END:VCARD
"""

filename = name.replace(" ", "_") + ".vcf"
with open(filename, 'w') as vcf_file:
    vcf_file.write(vcard_content)

print(f"\nvCard '{filename}' created successfully!")
