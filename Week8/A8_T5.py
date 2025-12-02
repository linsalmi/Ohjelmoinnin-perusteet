
import hashlib

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def register(PUsername: str, PPassword: str) -> None:
    try:
        with open(CREDENTIALS_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    user_id = len(lines)
    hashed = hash_password(PPassword)
    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{user_id}{DELIMITER}{PUsername}{DELIMITER}{hashed}\n")


def login(PUsername: str, PPassword: str) -> bool:
    hashed = hash_password(PPassword)
    try:
        with open(CREDENTIALS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(DELIMITER)
                if len(parts) == 3 and parts[1] == PUsername and parts[2] == hashed:
                    return True
    except FileNotFoundError:
        return False
    return False


def viewProfile(PUsername: str) -> list[str]:
    try:
        with open(CREDENTIALS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(DELIMITER)
                if len(parts) == 3 and parts[1] == PUsername:
                    return [parts[0], parts[1]]
    except FileNotFoundError:
        return []
    return []


def change_password(PUsername: str, PNewPassword: str) -> None:
    pass 


def main() -> None:
    print("Program starting.")
    while True:
        print("Options:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            username = input("Insert username: ").strip()
            password = input("Insert password: ").strip()
            if login(username, password):
                print("Authentication successful!")
                while True:
                    print("User menu:")
                    print("1 - View profile")
                    print("2 - Change password")
                    print("0 - Logout")
                    sub_choice = input("Your choice: ").strip()
                    if sub_choice == "1":
                        profile = viewProfile(username)
                        if profile:
                            print(f"Profile ID {profile[0]} - {profile[1]}")
                    elif sub_choice == "0":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Authentication failed!")

        elif choice == "2":
            username = input("Insert username: ").strip()
            password = input("Insert password: ").strip()
            register(username, password)
            print("User registration completed!")

        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
    print("Program ending.")


if __name__ == "__main__":
    main()
