import paramiko
import os

# Function to create backup of network devices
def backup_network_devices():
    device_name = input("Enter the name of the device: ")
    hostname = input("Enter the hostname or IP address of the device: ")
    username = input("Enter the username for the device: ")
    password = input("Enter the password for the device: ")
    backup_folder = input("Enter the path to the backup folder: ")

    # Create the backup folder if it doesn't exist
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Connect to the device
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)

    # Execute the command to backup the configuration
    stdin, stdout, stderr = ssh.exec_command("show running-config")
    config = stdout.read().decode()

    # Save the configuration to a file
    filename = os.path.join(backup_folder, device_name + ".txt")
    with open(filename, "w") as f:
        f.write(config)

    print("Backup complete for device " + device_name)

# Ask the user if they want to backup another device
backup_another = True
while backup_another:
    backup_network_devices()
    backup_another = input("Do you want to backup another device (yes/no)? ") == "yes"