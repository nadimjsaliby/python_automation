import win32evtlog
import win32evtlogutil
import socket
import datetime

def analyze_windows_event_logs(event_ids):
    logs = ["Security", "System", "Application"]
    report = []
    
    for log in logs:
        try:
            handle = win32evtlog.OpenEventLog(None, log)
            flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
            events = win32evtlog.ReadEventLog(handle, flags, 0)
            hostname = socket.gethostname()
            for event in events:
                if event.EventID in event_ids:
                    data = win32evtlogutil.SafeFormatMessage(event, log)
                    report.append([event.EventID, hostname, data, event.TimeGenerated.Format()])
        except:
            print(f"Error reading the {log} log")
            
    return report

def main():
    event_ids = [4624,4625,4634,4647,4648,4768,4769,6005,6006,7036,1000,1001,1002,4004,4005,1,3,7]
    report = analyze_windows_event_logs(event_ids)
    
    print("Event ID\t\tHostname\t\tMessage\t\t\t\t\t\t\t\t\t\t\tDate and Time")
    print("-------------------------------------------------------------------------------------------------------------")
    for r in report:
        print(f"{r[0]}\t\t\t{r[1]}\t\t{r[2]}\t\t{r[3]}")

if __name__ == '__main__':
    main()
