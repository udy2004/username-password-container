"""Creating a container that adds your username and password and allows you access to something"""
def username():
    names = []
    password = []
    name = input("Enter your username or email: ")
    passwords = input("Enter your password here: ")
    """using the append to add both your username and password to names/password"""
    names.append(name)
    password.append(passwords)
    
    print("\nplease login:")
    login = input("Enter your username: ")
    secret_key = input("Enter your password: ")
    
    if login == name and secret_key == passwords:
        print(f"Welcome Back {login}")
    else:
        print("who you?")
    
username()


