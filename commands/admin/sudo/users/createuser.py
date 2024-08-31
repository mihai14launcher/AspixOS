import sys
import os
import json

def create_user(username):
    # Directory where user information is stored
    user_dir = "etc/users"
    os.makedirs(user_dir, exist_ok=True)

    user_file_path = os.path.join(user_dir, f"{username}.json")

    # Check if the user already exists
    if os.path.exists(user_file_path):
        print(f"User '{username}' already exists.")
        return

    # Create new user with default info
    user_info = {
        "username": username,
        "permissions": []  # Empty permissions list
    }

    with open(user_file_path, 'w') as file:
        json.dump(user_info, file, indent=4)

    print(f"User '{username}' created successfully.")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "--user":
        print("Usage: python createuser.py --user {name}")
        sys.exit(1)
    
    username = sys.argv[2]
    create_user(username)

if __name__ == "__main__":
    main()
