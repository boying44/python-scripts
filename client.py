import socket

TCP_IP = 'misc.chal.csaw.io'
TCP_PORT = 4239
BUFF_SIZE = 12

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    #Read information
    sock.recv(BUFF_SIZE)
    sock.send("\n")


if __name__ == "__main__":
    main()