import os
import wmi

def vm_management():
    c = wmi.WMI()

    print("Welcome to VM Management!")
    while True:
        print("1. Create a new VM")
        print("2. Edit an existing VM")
        print("3. Delete an existing VM")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            vm_name = input("Enter the name of the VM: ")
            vm_size = int(input("Enter the memory size (in MB): "))
            vm_path = input("Enter the path where the VM will be stored: ")
            disk_size = int(input("Enter the disk size (in GB): "))
            new_vm = c.Win32_ComputerSystem.create(Name=vm_name, MemorySize=vm_size, SettingData=[{"VirtualSystemSubType":"Microsoft:Hyper-V:SubType/EnhancedSession", "VirtualHardDiskSettingData":[{"ElementName": vm_path + "\\" + vm_name + ".vhdx", "ParentPath": vm_path + "\\" + vm_name + ".vhdx", "VirtualHardDiskSize": disk_size}]}])
            
        elif choice == 2:
            vm_name = input("Enter the name of the VM to edit: ")
            for vm in c.Win32_ComputerSystem(Name=vm_name):
                print("Current memory size: ", vm.MemorySize)
                memory_size = int(input("Enter the new memory size (in MB): "))
                vm.MemorySize = memory_size
                print("Memory size updated successfully!")
                
                print("Current disk size: ", vm.VirtualHardDisk[0].DiskSize)
                disk_size = int(input("Enter the new disk size (in GB): "))
                vm.VirtualHardDisk[0].DiskSize = disk_size
                print("Disk size updated successfully!")
                
                print("Current path: ", vm.SettingData[0].VirtualHardDiskSettingData[0].ParentPath)
                path = input("Enter the new path: ")
                vm.SettingData[0].VirtualHardDiskSettingData[0].ParentPath = path
                print("Path updated successfully!")
                
        elif choice == 3:
            vm_name = input("Enter the name of the VM to delete: ")
            for vm in c.Win32_ComputerSystem(Name=vm_name):
                vm.Delete()
                print("VM deleted successfully!")
                
        elif choice == 4:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    vm_management()