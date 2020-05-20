import sys
# from lab_7 import MyApp
from src_cw.MainProcess import MainProcess

def main():
    test = MainProcess(1, 10, 20, 3)
    test.start()
    # a = MyApp()
    # sys.exit(a.exec())

if __name__ == "__main__":
    main()