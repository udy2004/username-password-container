
def username():
    """Creating a container that adds your username and password and allows you access to something"""
    names = []
    password = []
    name = input("Enter your username or email: ")
    passwords = input("Enter your password here: ")
    names.append(name) # using the append to add both your username and password to names/password
    password.append(passwords)
    
    print("\nplease login:")
    login = input("Enter your username: ")
    secret_key = input("Enter your password: ")
    
    if login == name and secret_key == passwords:
        """using the if statement"""
        print(f"Welcome Back {login}")
    else:
        print("who you?")
    
username()


