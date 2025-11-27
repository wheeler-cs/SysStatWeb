import FileSys
import WebEndpoint

import argparse
from http.server import HTTPServer

if __name__ == "__main__":
    argv = argparse.ArgumentParser(prog="SysStatWeb",
                                   description="System statistic endpoint using REST API")
    argv.add_argument("-a", "--address",
                      help="IP address web server should listen on",
                      type=str)
    argv.add_argument("-p", "--port",
                      help="port web server should listen on",
                      type=int)
    argv = argv.parse_args()
    web_server = HTTPServer((argv.address, argv.port),
                            WebEndpoint.Handler)
    print(f"[INFO] Web server running on {argv.address}:{argv.port}")
    web_server.serve_forever()
