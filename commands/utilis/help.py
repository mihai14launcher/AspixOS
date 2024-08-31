import sys

def display_help():
    help_text = """
Available Commands:

1. aspix --version
   - Show information about the OS version.

2. cdir {name of directory}
   - Create a new directory.

3. rdir {name of directory}
   - Delete an existing directory.

4. cfile {name of file}.{extension}
   - Create a new file.

5. rfile {name of file}.{extension}
   - Delete an existing file.

6. clear
   - Clear the terminal.

7. help
   - Show this list.

8. monit
   - Show info about CPU RAM and Storage in real time if you want to go back just press q   

9. aspixos --sudo --bypass --full-control
   - Entering in Admin mode of AspixOS

10. sudo activate --key 0000
    - Activating Full Control of AspixOS   
    """

    # Display text using utf-8 encoding
    sys.stdout.buffer.write(help_text.encode('utf-8'))
    sys.stdout.buffer.write(b'\n')

if __name__ == "__main__":
    display_help()
