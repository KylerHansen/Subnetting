#CS 2705
#Subnet Manipulation
#Kyler Hansen

import ipaddress

#Question 1
print("Question 1 answers:")
ipInterface = ipaddress.ip_interface('192.168.1.2/2')
print("\t a. 2-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/13')
print("\t b. 13-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/5')
print("\t c. 5-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/11')
print("\t d. 11-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/9')
print("\t e. 9-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/10')
print("\t f. 10-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/4')
print("\t g. 4-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/14')
print("\t h. 14-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/6')
print("\t i. 6-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/8')
print("\t j. 8-bit mask: {}".format(ipInterface.netmask))

ipInterface = ipaddress.ip_interface('192.168.1.2/12')
print("\t k. 12-bit mask: {}".format(ipInterface.netmask))

print()

#Question 2:
print("Question 2 answers:")
ipInterface = ipaddress.ip_interface('132.8.150.67/22')
ipNetwork = ipInterface.network
print("\t a. Network address: {}".format((ipNetwork).network_address))
print("\t b. Broadcast address: {}".format((ipNetwork).broadcast_address))
print("\t c. Number of host addresses: {}".format(len(list(ipNetwork.hosts()))))
print("\t d. Valid host address range: {0} - {1}".format((((ipNetwork).network_address)+1), (((ipNetwork).broadcast_address)-1)))

print()

#Question 3:
print("Question 3 answers:")
ipInterface = ipaddress.ip_interface('200.16.5.74/30')
ipNetwork = ipInterface.network
print("\t a. Network address: {}".format((ipNetwork).network_address))
print("\t b. Broadcast address: {}".format((ipNetwork).broadcast_address))
print("\t c. Number of host addresses: {}".format(len(list(ipNetwork.hosts()))))
print("\t d. Valid host address range: {0} - {1}".format((((ipNetwork).network_address)+1), (((ipNetwork).broadcast_address)-1)))

print()

#Question 4:
print("Question 4 answers:")
ipInterface = ipaddress.ip_interface('166.0.13.8/255.255.252.0')
ipNetwork = ipInterface.network
print("\t a. Network address: {}".format((ipNetwork).network_address))
print("\t b. Broadcast address: {}".format((ipNetwork).broadcast_address))
print("\t c. Number of host addresses: {}".format(len(list(ipNetwork.hosts()))))
print("\t d. Valid host address range: {0} - {1}".format((((ipNetwork).network_address)+1), (((ipNetwork).broadcast_address)-1)))

print()

#Question 5:
print("Question 5 Answers:")
ipInterface = ipaddress.ip_interface('10.10.10.10/255.255.240.0')
ipNetwork = ipInterface.network
print("\t a. Number of bits in the subnet mask: {}".format((ipNetwork).prefixlen))
print("\t b. Number of hosts: {}".format(len(list((ipNetwork).hosts()))))

print()

#Question 6:
print("Question 6 Answers:")
ipInterface = ipaddress.ip_interface('10.10.10.10/255.255.255.192')
ipNetwork = ipInterface.network
print("\t a. Number of bits in the subnet mask: {}".format((ipNetwork).prefixlen))
print("\t b. Number of hosts: {}".format(len(list((ipNetwork).hosts()))))

#Question 7:
print("Question 7 Answers:")
ipInterface = ipaddress.ip_interface('10.10.10.10/255.255.252.0')
ipNetwork = ipInterface.network
print("\t a. Number of bits in the subnet mask: {}".format((ipNetwork).prefixlen))
print("\t b. Number of hosts: {}".format(len(list((ipNetwork).hosts()))))

#Question 8:
print("Question 8 Answers:")
ipInterface = ipaddress.ip_interface('10.10.10.10/255.255.255.248')
ipNetwork = ipInterface.network
print("\t a. Number of bits in the subnet mask: {}".format((ipNetwork).prefixlen))
print("\t b. Number of hosts: {}".format(len(list((ipNetwork).hosts()))))

print()

#Question 9:
ipInterface = ipaddress.ip_interface('10.10.10.10/16')
ipNetwork = ipInterface.network
bitsBorrowed = 6
ipSubnetLength = ipNetwork.prefixlen + bitsBorrowed
print("The Subnet mask length is: {}".format(ipSubnetLength))
print("The 56 Subbets are less than the {} subnets that were created.".format(len(list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=(bitsBorrowed))))))
ipSubnet = str('10.10.10.10/') + str(ipSubnetLength)
ipSubnetAddress = ipaddress.ip_network(ipSubnet, strict=False)
print("The 1000 addresses needed are equal to or less than the {} hosts in each subnet.".format(len(list(ipaddress.ip_network(ipSubnetAddress).hosts()))))
