import os
import sys

def enter_sudo_mode():
    # Change the prompt to [FULL CONTROL]@aspixos>
    sys.stdout.write("[FULL CONTROL]@aspixos> ")
    sys.stdout.flush()

def main():
    enter_sudo_mode()

if __name__ == "__main__":
    main()
