############################
#    Port Scanner Tool     #
#     By: Yuval Cohen      #
#     Date: 4.2.21         #
############################


import threading
import socket


def scan_port(ip, port):
    """
    The function checking if the port is open.
    :param ip: The ip address.
    :param port: The port number.
    """
    global ports_lst
    soc = socket.socket()
    soc.settimeout(0.5)
    try:
        soc.connect((ip, port))
        ports_lst.append(port)
        soc.close()
    except:
        pass


def main():
    global ports_lst

    ip = input("Enter Ip address: ")
    try:
        start = int(input("Enter the start port scan: "))
        end = int(input("Enter the end port scan: "))

        ports_lst = []
        print("\n" + "-" * 35)
        print(f"Starting the scan at {ip}")
        print("-" * 35)

        for port in range(start, end + 1):
            threading.Thread(target=scan_port, args=(ip, port)).start()

        # While checking ports.
        while threading.activeCount() > 1:
            pass

        ports_lst.sort()

        for port in ports_lst:
            print(f"Port Number: {port} is open !")

        print("\n" + "-" * 29)
        print(f"Scan Completed! {len(ports_lst)} Ports found!")
        print("-" * 29)

    except ValueError:
        print("\nError! Port number must be a integer num.")

    input("\n\nPress any key to continue...")


if __name__ == '__main__':
    main()
