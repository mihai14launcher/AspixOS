import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Please wait until the shell is fully reloaded")
    time.sleep(4)  # Wait for 4 seconds
    clear_screen()
    print("Shell reloaded.")

if __name__ == "__main__":
    main()
