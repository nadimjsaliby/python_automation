import os
import shutil
import time
import schedule
import datetime

def backup():
    # Ask the user for the source and destination directories
    src_dir = input("Enter the source directory: ")
    backup_dir = input("Enter the destination directory: ")

    # Create a timestamp to be used as part of the backup file name
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")

    # Create the backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Copy the contents of the source directory to the backup directory
    shutil.copytree(src_dir, os.path.join(backup_dir, timestamp))
    print("Backup complete.")

def schedule_backup():
    # Ask the user if they want to schedule the backup
    schedule_choice = input("Do you want to schedule the backup to run automatically? (yes/no) ")
    if schedule_choice.lower() == "yes":
        # Ask the user how often they want to schedule the backup
        frequency = input("How often do you want to schedule the backup? (daily/weekly/monthly) ")
        if frequency.lower() == "daily":
            schedule.every().day.at("1:00").do(backup)
        elif frequency.lower() == "weekly":
            schedule.every().week.at("1:00").do(backup)
        elif frequency.lower() == "monthly":
            schedule.every().month.at("1:00").do(backup)
        else:
            print("Invalid choice. Backup will not be scheduled.")
            return

        # Save the source and destination directories for future reference
        with open("backup_config.txt", "w") as f:
            f.write(src_dir + "\n")
            f.write(backup_dir + "\n")
        
        # Keep running the scheduled tasks in the background
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    # Check if a backup configuration file exists
    if os.path.exists("backup_config.txt"):
        # Load the source and destination directories from the configuration file
        with open("backup_config.txt", "r") as f:
            src_dir = f.readline().strip()
            backup_dir = f.readline().strip()
        schedule_backup()
    else:
        backup()
        schedule_backup()