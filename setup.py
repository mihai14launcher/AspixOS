import os
import sys
import zipfile
import requests
import shutil
from pathlib import Path

def download_and_extract_zip(url, dest_folder):
    """Download a ZIP file and extract it to the specified folder."""
    print(f"Downloading {url}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check for download errors

    zip_path = os.path.join(dest_folder, 'latest.zip')
    
    with open(zip_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)

    os.remove(zip_path)  # Remove the ZIP file after extraction
    print("Extraction completed.")

def create_boot_script(root_folder, script_name, script_content):
    """Create a boot script with the provided content."""
    script_path = os.path.join(root_folder, script_name)
    
    with open(script_path, 'w') as file:
        file.write(script_content)
    
    # Make the script executable on Unix-based systems
    if os.name == 'posix':
        st = os.stat(script_path)
        os.chmod(script_path, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    
    print(f"Created boot script: {script_path}")

def setup_virtualenv(root_folder):
    """Create and set up a virtual environment."""
    venv_dir = os.path.join(root_folder, 'venv')
    print("Setting up virtual environment...")
    if os.name == 'nt':  # Windows
        subprocess.run(['python', '-m', 'venv', venv_dir], check=True)
        subprocess.run([os.path.join(venv_dir, 'Scripts', 'activate.bat')], shell=True, check=True)
        subprocess.run([os.path.join(venv_dir, 'Scripts', 'pip'), 'install', 'psutil', 'curses'], check=True)
    elif os.name == 'posix':  # Unix-based
        subprocess.run(['python3', '-m', 'venv', venv_dir], check=True)
        subprocess.run(['source', os.path.join(venv_dir, 'bin', 'activate')], shell=True, check=True)
        subprocess.run([os.path.join(venv_dir, 'bin', 'pip'), 'install', 'psutil'], check=True)
        subprocess.run(['pip', 'install', 'curses'], check=True)

def main():
    # Prompt for the root folder
    root_folder = input("Enter the root folder for AspixOS: ").strip()
    
    if not os.path.isdir(root_folder):
        print(f"The specified folder does not exist: {root_folder}")
        return
    
    # Download and extract AspixOS
    download_and_extract_zip('https://releases-aspixdatacenter.netlify.app/latest/latest.zip', root_folder)
    
    # Detect the operating system
    if os.name == 'nt':  # Windows
        boot_script_name = 'boot.bat'
        boot_script_content = '@echo off\npython main.py\n'
    elif os.name == 'posix':  # Unix-based (Linux, macOS)
        boot_script_name = 'boot.sh'
        boot_script_content = '#!/bin/bash\npython3 main.py\n'
    else:
        print("Unsupported operating system.")
        return
    
    # Create the boot script
    create_boot_script(root_folder, boot_script_name, boot_script_content)
    
    # Setup virtual environment
    setup_virtualenv(root_folder)
    
    print("Setup completed. Please run the generated boot script to start AspixOS.")

if __name__ == "__main__":
    main()
