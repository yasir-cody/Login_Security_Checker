given_name = input("Enter username: ")
given_pass = input("Enter password: ")

username = "admin"
password = "Cyber123!"


def login_security_checker(username, password):
    
    if given_name == username and given_pass == password:
        print("Access granted!")
    elif given_name != username:
        print("Access denied!")
        print("Reason for login-fail: Incorrect username.")
    elif given_pass != password:
        print("Access denied!")
        print("Reason for login-fail: Incorrect password.")
    else:
        print("Access denied!")


login_security_checker(username, password)
