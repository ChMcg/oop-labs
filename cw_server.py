import socket, time, json
from src_cw.ConnectionManager import ConnectionManager
from src_cw.MainProcess import MainProcess


def main():
    process = MainProcess(2, 10, 3, 3, 5)
    while True:
        try:
            process.start()
        except Exception as e:
            process.conn.clients.clear()
            print(e)
            continue

if __name__ == "__main__":
    main()