import psutil
import time
import curses

def display_system_metrics(stdscr):
    # Hide the cursor
    curses.curs_set(0)  
    stdscr.nodelay(1)   
    stdscr.timeout(1000)  # Refresh every second

    while True:
        # Get system metrics
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')

        # Clear the screen to start drawing
        stdscr.clear()

        # Display system information
        stdscr.addstr(0, 0, "AspixOS System Monitor")
        stdscr.addstr(2, 0, f"CPU Usage: {cpu_usage}%")
        stdscr.addstr(3, 0, f"Memory Usage: {memory_info.percent}%")
        stdscr.addstr(4, 0, f"Disk Usage: {disk_info.percent}%")

        # Refresh the screen to update the display
        stdscr.refresh()

        # Check for user input to exit the monitoring (e.g., pressing 'q')
        key = stdscr.getch()
        if key == ord('q'):
            break

        time.sleep(1)  # Adjust the refresh rate if needed

if __name__ == "__main__":
    curses.wrapper(display_system_metrics)
