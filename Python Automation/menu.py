def main_menu():
    print("""
    Main Menu:
    1. Create Backup
    2. Email Verification
    3. Disk Space Management
    4. Network Analysis and Monitoring
    5. Windows Logs Analyzer
    6. VM Deployment and Management
    7. Network Devices Configuration Backup
    8. Network Mapping and Topology Discovery
    9. Resource Monitoring
    """)
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        import create_backup
    elif choice == 2:
        import email_verification
    elif choice == 3:
        import disk_space_mgt
    elif choice == 4:
        import network_monitoring
    elif choice == 5:
        import windows_log_analyzer
    elif choice == 6:
        import vm_mgt
    elif choice == 7:
        import configuration_bkp
    else:
        print("Invalid option selected. Try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()