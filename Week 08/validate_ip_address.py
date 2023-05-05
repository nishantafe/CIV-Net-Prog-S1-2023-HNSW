import ipaddress


def validate_ip_address(my_ip_address):
    """Validate the ip address"""
    try:
        ipaddress.IPv4Address(my_ip_address)
        # print("Valid IP address")
        return True
    except ipaddress.AddressValueError:
        print("Invalid IP address")
        return False


subnet_prefix = input("Enter the subnet prefix example(192.168.0): ")
valid_ip = validate_ip_address(subnet_prefix + ".1")
while not valid_ip:
    subnet_prefix = input("Enter the subnet prefix example(192.168.0): ")
    valid_ip = validate_ip_address(subnet_prefix + ".1")

ips_list = [subnet_prefix + "." + str(num) for num in range(11, 256, 2)]
print(ips_list)
