"""
Requirements
- pywin32 to be installed (ideally as admin) Example: By Installing Anaconda
- To be on Windows operating system
- You code editor/IDE (Pycharm/Visual studio code) to be configured correctly
"""
import win32evtlogutil
import os

# Change or set the current working directory to the location of this file
os.chdir(os.path.dirname(__file__))

def write_event_viewer_log(status_messages_list, event_type):
    win32evtlogutil.ReportEvent(
        appName="CheckIPPort - IP/Port Scanner",
        eventID=1320,
        eventCategory=9000,
        eventType=event_type,
        strings=[message for message in status_messages_list],
        data=b"CheckIPPort")


# Test list
status_messages = ["10.56.17.11:80    Closed/Filtered", "10.56.17.11:445   Open"]

write_event_viewer_log(status_messages, event_type=2)  # event types: 0=info 1=error 2=warning

print(*status_messages, sep="\n")
print("The messages above were logged to Event Viewer")