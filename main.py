import os
import subprocess
import sys

# Paths to the license files
LICENSE_FILES = {
    "boot": os.path.join("etc", "licenses", "boot.license"),
    "commands": os.path.join("etc", "licenses", "commands.license"),
    "fullcontrol": os.path.join("etc", "licenses", "fullcontrol.license"),
    "system": os.path.join("etc", "licenses", "system.license")
}

def check_license():
    missing_files = []
    
    for license_type, file_path in LICENSE_FILES.items():
        if not os.path.exists(file_path):
            missing_files.append(license_type)
    
    if missing_files:
        print(f"Missing license files: {', '.join(missing_files)}")
        return False
    return True

def prompt_recovery():
    response = input("One or more license files are missing. Do you want to enter recovery mode? (Y/N): ").strip().upper()
    if response == 'Y':
        enter_recovery_mode()
    else:
        print("Exiting program.")
        sys.exit(1)

def enter_recovery_mode():
    print("Entering recovery mode...")
    recreate_licenses()
    recreate_folders()
    print("Recovery mode completed. Please restart the program.")
    sys.exit(0)

def recreate_licenses():
    # Define the content of the license files
    license_contents = {
        "boot": "OS= AspixOS\nData= 104901929381\nPACKAGE = FREE\nWorkaround = PY * JS\n\nLICENSES = 4",
        "commands": "COMMANDS = TRUE\nFULL CONTROL = 00 & 00 & 01\nREGISTRY = ZTE\nALLOW_X = TRUE\n\nLICENSES = 4",
        "fullcontrol": "[fullcontrol]@aspixos> = TRUE\nPREFIX = 00 - 1 - 01\nUSER-PERM = ALL\nPY = JS\nJS = 0\nPY = 2\n\nLICENSES = 4",
        "system": "OS = ASPIXOS\nDEFAULT PREFIX = aspixos >\n> = TRUE\n\n00 00 10 01 00 10 01 = 2\nPY = 5\nJS = 10\n\nEND"
    }
    
    for license_type, content in license_contents.items():
        file_path = LICENSE_FILES[license_type]
        directory = os.path.dirname(file_path)
        
        # Debugging: Print the directory path
        if directory:
            print(f"Creating directory if not exists: {directory}")
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
        
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Created missing license file: {file_path}")

def recreate_folders():
    folders = [
        os.path.join("etc", "licenses"),
        "commands",
        "commands/admin",
        "commands/admin/sudo",
        "commands/admin/sudo/users"
    ]
    
    for folder in folders:
        # Debugging: Print the folder path
        print(f"Creating folder if not exists: {folder}")
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
            print(f"Created missing folder: {folder}")

def run_js_file(file_path, *args):
    try:
        print(f"Running JS file: {file_path} with args: {args}")
        result = subprocess.run(['node', file_path] + list(args), capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Error: {result.stderr}", file=sys.stderr)
        if not os.path.exists(file_path):
            print(f"File {file_path} not found.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while running the JS script: {e}")

def run_py_file(file_path, *args):
    try:
        python_executable = sys.executable
        print(f"Running Python file: {file_path} with args: {args}")
        result = subprocess.run([python_executable, file_path] + list(args), capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Error: {result.stderr}", file=sys.stderr)
        if not os.path.exists(file_path):
            print(f"File {file_path} not found.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while running the Python script: {e}")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def reload_shell():
    py_file_path = os.path.join("commands", "admin", "reload-shell.py")
    try:
        process = subprocess.Popen([sys.executable, py_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                sys.stdout.write(output)
                sys.stdout.flush()
            error = process.stderr.readline()
            if error:
                sys.stderr.write(error)
                sys.stderr.flush()
        rc = process.poll()
        if rc != 0:
            print(f"Script ended with non-zero exit status {rc}.", file=sys.stderr)
    except FileNotFoundError:
        print(f"File {py_file_path} not found.")
    except Exception as e:
        print(f"An error occurred while running the Python script: {e}")

def enter_sudo_mode():
    py_file_path = os.path.join("commands", "admin", "sudo", "sudo-mode.py")
    try:
        process = subprocess.Popen([sys.executable, py_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                sys.stdout.write(output)
                sys.stdout.flush()
            error = process.stderr.readline()
            if error:
                sys.stderr.write(error)
                sys.stderr.flush()
        rc = process.poll()
        if rc != 0:
            print(f"Script ended with non-zero exit status {rc}.", file=sys.stderr)
    except FileNotFoundError:
        print(f"File {py_file_path} not found.")
    except Exception as e:
        print(f"An error occurred while running the Python script: {e}")

def activate_key():
    py_file_path = os.path.join("commands", "admin", "sudo", "activate-key.py")
    try:
        process = subprocess.Popen([sys.executable, py_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                sys.stdout.write(output)
                sys.stdout.flush()
            error = process.stderr.readline()
            if error:
                sys.stderr.write(error)
                sys.stderr.flush()
        rc = process.poll()
        if rc != 0:
            print(f"Script ended with non-zero exit status {rc}.", file=sys.stderr)
    except FileNotFoundError:
        print(f"File {py_file_path} not found.")
    except Exception as e:
        print(f"An error occurred while running the Python script: {e}")

def create_user(username):
    py_file_path = os.path.join("commands", "admin", "sudo", "users", "createuser.py")
    try:
        process = subprocess.Popen([sys.executable, py_file_path, '--user', username], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                sys.stdout.write(output)
                sys.stdout.flush()
            error = process.stderr.readline()
            if error:
                sys.stderr.write(error)
                sys.stderr.flush()
        rc = process.poll()
        if rc != 0:
            print(f"Script ended with non-zero exit status {rc}.", file=sys.stderr)
    except FileNotFoundError:
        print(f"File {py_file_path} not found.")
    except Exception as e:
        print(f"An error occurred while running the Python script: {e}")

def delete_user(username):
    py_file_path = os.path.join("commands", "admin", "sudo", "users", "deleteuser.py")
    try:
        process = subprocess.Popen([sys.executable, py_file_path, '--user', username], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                sys.stdout.write(output)
                sys.stdout.flush()
            error = process.stderr.readline()
            if error:
                sys.stderr.write(error)
                sys.stderr.flush()
        rc = process.poll()
        if rc != 0:
            print(f"Script ended with non-zero exit status {rc}.", file=sys.stderr)
    except FileNotFoundError:
        print(f"File {py_file_path} not found.")
    except Exception as e:
        print(f"An error occurred while running the Python script: {e}")

def enter_user(username):
    user_file = os.path.join("etc", "users", f"{username}.json")
    if not os.path.exists(user_file):
        print(f"User file {user_file} does not exist.")
        return None
    
    print(f"Entering user '{username}'")
    return username

def main():
    if not check_license():
        prompt_recovery()
    
    print("Welcome to AspixOS terminal. Type 'exit' to quit.")
    
    in_sudo_mode = False
    current_user = None

    while True:
        if in_sudo_mode:
            prompt = f"[FULL CONTROL]@aspixos> "
        else:
            prompt = "aspixos> "
        
        command = input(prompt).strip()
        cmd_parts = command.split()
        cmd = cmd_parts[0]
        args = cmd_parts[1:]

        if cmd == "exit":
            break

        if cmd == "aspixos" and "--reload" in args and "--shell" in args:
            reload_shell()

        elif not in_sudo_mode and cmd == "aspixos" and "--sudo" in args and "--bypass" in args and "--full-control" in args:
            enter_sudo_mode()
            in_sudo_mode = True

        elif in_sudo_mode and cmd == "sudo" and "activate" in args and "--key" in args:
            activate_key()

        elif in_sudo_mode and cmd == "sudo" and "create" in args and "--user" in args:
            username = args[args.index("--user") + 1]
            create_user(username)

        elif in_sudo_mode and cmd == "enter" and "--user" in args:
            username = args[args.index("--user") + 1]
            current_user = enter_user(username)
            if current_user:
                print(f"Switched to user '{current_user}'")

        elif in_sudo_mode and cmd == "sudo" and "delete" in args and "--user" in args:
            username = args[args.index("--user") + 1]
            delete_user(username)

        else:
            print(f"Command '{cmd}' not recognized.")

if __name__ == "__main__":
    main()
