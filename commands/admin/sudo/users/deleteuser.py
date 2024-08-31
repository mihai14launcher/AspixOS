import sys
import os

def delete_user(username):
    # Path to the user's JSON file
    user_file_path = os.path.join("etc", "users", f"{username}.json")

    # Check if the user file exists
    if not os.path.exists(user_file_path):
        print(f"User '{username}' does not exist.")
        return

    # Remove the user file
    os.remove(user_file_path)
    print(f"User '{username}' has been deleted.")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "--user":
        print("Usage: python deleteuser.py --user {name}")
        sys.exit(1)

    username = sys.argv[2]
    delete_user(username)

if __name__ == "__main__":
    main()
