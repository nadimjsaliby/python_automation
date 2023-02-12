import platform
import subprocess
import psutil

def free_up_disk_space():
    # Check if the system is Windows or Linux
    operating_system = platform.system()

    # Get the disk usage using the psutil library
    disk_usage = psutil.disk_usage("/")

    # Check if the disk usage is greater than 85%
    if disk_usage.percent > 85:
        if operating_system == "Windows":
            # For Windows, run the disk cleanup utility
            subprocess.run("cleanmgr", shell=True)
        elif operating_system == "Linux":
            # For Linux, remove unnecessary files
            subprocess.run("sudo apt-get clean", shell=True)
            subprocess.run("sudo apt-get autoremove", shell=True)

# Call the function to free up disk space
free_up_disk_space()
