import hashlib
from template import askChoice

CREDENTIALS_FILE = "credentials.txt"

MAIN_MENU_OPTIONS = [
    "1 - Login",
    "2 - Register",
    "0 - Exit"
]

USER_MENU_OPTIONS = [
    "1 - View profile",
    "2 - Change password",
    "0 - Logout"
]

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode("utf-8")).hexdigest()

def load_credentials() -> list[list[str]]:
    credentials = []
    try:
        with open(CREDENTIALS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(";")
                    if len(parts) == 3:
                        credentials.append(parts)
    except FileNotFoundError:
        pass
    return credentials

def save_credentials(credentials: list[list[str]]) -> None:
    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as file:
        for cred in credentials:
            file.write(";".join(cred) + "\n")

def register_user():
    credentials = load_credentials()
    username = input("Insert username: ").strip()
    password = input("Insert password: ").strip()
    hashed = hash_password(password)
    # ID alkaa 0 ensimmäisestä rekisteröidystä (admin voi olla 0)
    user_id = str(len([c for c in credentials if c[1] != "admin"]))
    credentials.append([user_id, username, hashed])
    save_credentials(credentials)
    print("User registration completed!\n")

def login_user():
    credentials = load_credentials()
    username = input("Insert username: ").strip()
    password = input("Insert password: ").strip()
    hashed = hash_password(password)

    for cred in credentials:
        if cred[1] == username and cred[2] == hashed:
            print("Authentication successful!\n") 
            user_menu(cred)
            return

    print("Authentication failed!\n")

def user_menu(user_cred: list[str]):
    while True:
        print("User menu:")
        for option in USER_MENU_OPTIONS: 
            print(option)
        choice = askChoice([0, 1, 2])

        if choice == 0:
            print("Logging out...\n")
            return
        elif choice == 1:
            print(f"Profile ID {user_cred[0]} - {user_cred[1]}\n")
        elif choice == 2:
            print("Change password feature not implemented yet.")

def showMenu(options: list[str]):
    print("Options:")
    for option in options:
        print(option)

def main():
    print("Program starting.")
    while True:
        showMenu(MAIN_MENU_OPTIONS)
        choice = askChoice([0, 1, 2])

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            login_user()
        elif choice == 2:
            register_user()
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
