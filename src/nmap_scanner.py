import os
from io import StringIO
from config import IP_RANGE, HOST_UNIX_PASSWORD

HOSTNAME_START_STR = 'Nmap scan report for '
MAC_START_STR = 'MAC Address: '

class Device:
    def __init__(self, ip:str, hostname:str) -> None:
        self.hostname = hostname
        self.ip = ip
        self.mac = ''
        self.mac_origin = ''

# This function is exepcting this kind of output from namp:
# Starting Nmap 7.80 ( https://nmap.org ) at some time
# Nmap scan report for hostname (ip)
# Host is up (0.0051s latency).
# MAC Address: mac (estimated mac origin)
# Nmap scan report for hostname (ip)
# Host is up (0.0051s latency).
# MAC Address: mac (estimated mac origin)
# etc

def scan_host_on_network():
    print('scanning...')

    command = 'echo '+ HOST_UNIX_PASSWORD +' | sudo -S nmap -sn ' + IP_RANGE
    output = os.popen(command).read()

    input_buffer = StringIO(output)

    output_buffer = StringIO()

    output_devices = []

    for line in input_buffer.readlines():
        if HOSTNAME_START_STR in line:
            start_ip = line.find('(')
            end_ip = line.find(')')
            hostname = line[len(HOSTNAME_START_STR):start_ip]
            ip = line[start_ip:end_ip]
            ip = ip.replace('(', '')
            hn_output = hostname + ' ' + ip
            output_buffer.write(hn_output + '\n')
            output_devices.append(Device(ip.strip(), hostname.strip()))

        elif MAC_START_STR in line:
            end_mac = line.find('(')
            mac = line[len(MAC_START_STR):end_mac]
            end_origin = line.rfind(')')
            mac_origin = line[end_mac + 1:end_origin]
            mac_output = mac + ' ' + mac_origin
            output_buffer.write(mac_output + '\n')
            output_devices[len(output_devices) - 1].mac = mac.strip()
            output_devices[len(output_devices) - 1].mac_origin = mac_origin.strip()

    print(output_buffer.getvalue())

    return output_devices
