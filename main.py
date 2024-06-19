import traceback

from FlaskServer import web
import sys

# host, port, debug = (0, 0, 0)
# try:
#     host, port, debug = sys.argv[1:4]
# except:
#     print("Incorrect number of args given.")
#     print("Syntax: python main.py <host ip> <port> <debug (y/n)>")
#     exit(0)

try:
    # host= "0.0.0.0"
    # port= 5000
    # web.run(host, port, (debug == 'y' or debug == '1'))
    if __name__ == "__main__":
        print("Starting Main...")

        host = '0.0.0.0'
        port = 5000
        debug = True
        web.run(host, port, debug)

    # web.run(host="0.0.0.0", port=5000, debug=True)
except:
    traceback.print_exc()
