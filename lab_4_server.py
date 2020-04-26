import socket, time, json
from src_04.Polynomial import Polynomial
from src_04.number import number
from src_04.config import UDP_IP, UDP_PORT


def main():
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print(addr)
        tn = time.strftime('%Y-%m-%d_%H:%M', time.localtime())
        print(f"[{tn}] received:\n", data.decode(), sep='')
        data = json.loads(data.decode())
        l = [number(x) for x in data['poly']]
        poly = Polynomial(l)
        ret = {
            'info': str(poly),
            'roots': [f"{x.real:.3f} + {x.imag:.3f}j" for x in poly.roots()]
        }
        sock.sendto(json.dumps(ret, ensure_ascii=False, indent=2).encode(), addr)


if __name__ == "__main__":
    main()