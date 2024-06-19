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

        if len(sys.argv) != 4:
            print(f"Usage: python main.py <host> <port> <debug>")
            print("<host>: Optional. Default is 0.0.0.0.")
            print("<port>: Optional. Default is 5000.")
            print("<debug>: Optional. True or False. Default is False.")
        else:
            host = sys.argv[1] or '0.0.0.0'
            port = int(sys.argv[2]) or 5000
            debug = eval(sys.argv[3].lower()) or False
            web.run(host, port, debug)
            print("Web Server Running...")

        
        print("Exiting Main...")

    # web.run(host="0.0.0.0", port=5000, debug=True)
except:
    traceback.print_exc()
