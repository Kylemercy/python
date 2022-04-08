# email slicer
email = input("Enter your email: \n").strip()
username = email[: email.index("@")]
domain = email[email.index("@")+1:]
print(f"your username is {username}.\ndomain name is {domain}.")