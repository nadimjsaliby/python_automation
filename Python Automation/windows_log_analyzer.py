import win32evtlog # Import the required library
import win32evtlogutil
import datetime

def analyze_logs():
    # Specify the log type, in this case it's the system log
    log_type = "System"

    # Open the log
    log = win32evtlog.OpenEventLog("", log_type)

    # Get the number of events in the log
    num_events = win32evtlog.GetNumberOfEventLogRecords(log)

    # Initialize a list to store the log events
    log_events = []

    # Loop through all the events in the log
    for event_id in range(num_events):
        # Get the event information
        flags, event_id, category, time_generated, time_written, event_type, data, sid = win32evtlog.ReadEventLogRecord(log, event_id)

        # Check if the event is related to security
        if event_type == 4:
            # Parse the event information
            event_data = win32evtlogutil.SafeFormatMessage(event_id, data, log_type)
            hostname = win32evtlogutil.GetHostName(event_id, data, log_type)
            event_time = datetime.datetime.fromtimestamp(time_written).strftime('%Y-%m-%d %H:%M:%S')
            ip_address = "" # IP address can be retrieved using another library

            # Store the event information in the list
            log_events.append([event_id, event_data, hostname, event_time, ip_address])

    # Close the log
    win32evtlog.CloseEventLog(log)

    # Write the log events to a file
    with open("log_report.txt", "w") as f:
        for event in log_events:
            f.write("Event ID: {}\n".format(event[0]))
            f.write("Event Data: {}\n".format(event[1]))
            f.write("Hostname: {}\n".format(event[2]))
            f.write("Event Time: {}\n".format(event[3]))
            f.write("IP Address: {}\n\n".format(event[4]))

    print("The log analysis is complete and the report has been generated.")

# Call the function to analyze the logs
analyze_logs()
