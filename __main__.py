import sys
from application import Application


def main(args=None):
    if args is None:
        args = sys.argv[1:]



if __name__ == "__main__":
    main()
    app = Application()
    app.run()
    

