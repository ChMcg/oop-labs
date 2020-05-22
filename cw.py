import sys
from src_cw.App import MyApp

def main():
    a = MyApp()
    sys.exit(a.exec())

if __name__ == "__main__":
    main()