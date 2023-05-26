import ipaddress


def validate_subnet_mask(an_ip_address, a_subnet_mask):
    ip_range = an_ip_address + "/" + a_subnet_mask
    try:
        ipaddress.IPv4Network(ip_range)  # Example 192.168.0.0/255.255.255.0
        return True
    except ValueError:
        print("Invalid subnet mask")
        return False


subnet_prefix = "10.56.17"  # Make sure to validate the IP address (see Week 8)

valid_subnet_mask = False
while not valid_subnet_mask:
    subnet_mask = "255.255.255.192"
    # subnet_mask = input("Enter a subnet mask (Example: 255.255.255.0): ")
    sample_ip = subnet_prefix + ".0"
    valid_subnet_mask = validate_subnet_mask(sample_ip, subnet_mask)
