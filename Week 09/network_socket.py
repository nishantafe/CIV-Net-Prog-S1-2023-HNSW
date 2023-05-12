"""This scans an IP with a port"""
import socket
import datetime


def scan(an_ip, a_port):
    """Scan and IP with a port, display a message and write to a log file"""
    # Get the current date and time
    timestamp = datetime.datetime.now().strftime(f"%d-%b-%Y (%H:%M:%S.%f)")

    # Create a log file and write (append) to it
    log_file_out = open("ip_port_log.txt", "a")

    # Connect and scan the IP with the port
    socket.setdefaulttimeout(0.1)  # to speed up the result
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))  # if result is 0 then port is OPEN

    # Let's handle the result by generating a message to display or write...
    if result == 0:
        status_message = f"{an_ip}:{a_port:<5d} Open | Time: {timestamp}"
        print("\033[32m" + status_message)  # display the message in the console
        log_file_out.write(status_message + "\n")  # write (append) the message to the log file
    else:
        print(f"\033[31m{an_ip}:{a_port:<5d} Closed/Filtered or host is offline | Time: {timestamp}")
    sock.close()
    log_file_out.close()


host_name = socket.gethostname()
print("Host name:", host_name)

my_ip_address = socket.gethostbyname(socket.gethostname())
print("My IP address:", my_ip_address)

# The rule to convert a list to a string: separator.join(list)
my_subnet_prefix = ".".join(my_ip_address.split(".")[:3])

subnet_prefix = input(f"Enter the subnet prefix example({my_subnet_prefix}): ")
ips = [subnet_prefix + "." + str(num) for num in range(11, 256, 2)]

# TODO Create a function to retrieve port numbers as a list from lines of a text file called ports.txt
ports = [80, 445, 21]

for ip in ips:
    for port in ports:
        scan(ip, port)
