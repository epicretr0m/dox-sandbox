def build_record():
    record = {}

    if "Name" not in previous_record:
        name = input("Enter the name: ")
        if name:
            record["Name"] = name

    if "First Name" not in previous_record:
        first_name = input("Enter the first name: ")
        if first_name:
            record["First Name"] = first_name

    if "Address" not in previous_record:
        address = input("Enter the address: ")
        if address:
            record["Address"] = address

    if "IP" not in previous_record:
        ip = input("Enter the IP address: ")
        if ip:
            record["IP"] = ip

    if "ISP" not in previous_record:
        isp = input("Enter the ISP: ")
        if isp:
            record["ISP"] = isp

    if "Face" not in previous_record:
        face = input("Enter the face description: ")
        if face:
            record["Face"] = face

    if "Phone" not in previous_record:
        phone = input("Enter the phone number: ")
        if phone:
            record["Phone"] = phone

    if "Email" not in previous_record:
        email = input("Enter the email address: ")
        if email:
            record["Email"] = email

    if "Admin-C" not in previous_record:
        admin_c = input("Enter the admin-c code: ")
        if admin_c:
            record["Admin-C"] = admin_c

    if "Tech-C" not in previous_record:
        tech_c = input("Enter the tech-c code: ")
        if tech_c:
            record["Tech-C"] = tech_c

    if "Facebook" not in previous_record:
        facebook = input("Enter the Facebook link (optional): ")
        if facebook:
            record["Facebook"] = facebook

    return record


def save_record(record, file_name):
    with open(file_name, "w") as file:
        file.write("Record:\n")
        for key, value in record.items():
            file.write(key + ": " + value + "\n")
            file.write("-" * 30 + "\n")
    print("The record has been successfully saved to the file", file_name)


def continue_record():
    continue_option = input("Do you want to continue from a previously saved file? (Yes/No): ")
    if continue_option.lower() == "yes":
        file_name = input("Enter the file name: ")
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                record = {}
                for i in range(1, len(lines), 2):
                    info = lines[i].strip().split(": ")
                    record[info[0]] = info[1]
                return record
        except FileNotFoundError:
            print("The file", file_name, "was not found.")
    return {}


def view_info(record):
    command = input("Enter a command (section/seeall): ")
    if command.lower() == "section":
        section = input("Enter the section: ")
        if section in record:
            print(record[section])
        else:
            print("No information found for this section.")
        return section
    elif command.lower() == "seeall":
        for section, info in record.items():
            print(section + ": " + info)
        return view_info(record)
    else:
        print("Invalid command.")
        return view_info(record)


previous_record = continue_record()

record = build_record()
record.update(previous_record)

print("\nRecord:")
for key, value in record.items():
    print(key + ": " + value)
    print("-" * 30)

save_file = input("\nDo you want to save the record to a .txt file? (Yes/No): ")
if save_file.lower() == "yes":
    file_name = input("Enter the file name: ")
    save_record(record, file_name)

section = view_info(record)
if section:
    section_value = input("Enter the value for the section " + section + ": ")
    record[section] = section_value

save_file = input("\nDo you want to save the modified record to a .txt file? (Yes/No): ")
if save_file.lower() == "yes":
    file_name = input("Enter the file name: ")
    save_record(record, file_name)
