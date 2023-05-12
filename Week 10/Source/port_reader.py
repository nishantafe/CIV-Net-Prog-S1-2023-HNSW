import os


# print("Current working directory -->", os.getcwd())
# os.chdir("../Parameters")
# print("New working directory -->", os.getcwd())

# print(os.path.isfile("../Parameters/ports.txt"))

# TODO Create a function to read ports.txt into a list
# IF ports.txt exits
#     READ ports.txt
#     FOR a port in the file ports.txt
#         IF port is in the list (ports_list)
#             DISPLAY "Port already exits"
#         ELSE append the port into (ports_list)
#     CLOSE ports.txt
# ELSE DISPLAY "The file does not exit"

def read_port_file_into_list(a_ports_file, a_ports_list):
    if os.path.isfile(a_ports_file):
        ports_file_in = open(a_ports_file, "r")
        for port in ports_file_in:
            port = int(port.rstrip())  # cast to int to get a list of integers
            if port in a_ports_list:
                print("This port already exists")
            else:
                a_ports_list.append(port)
        ports_file_in.close()
    else:
        print("The file does not exist")


PORTS_FILE = "../Parameters/ports.txt"
ports_list = []

read_port_file_into_list(PORTS_FILE, ports_list)
print(ports_list)
