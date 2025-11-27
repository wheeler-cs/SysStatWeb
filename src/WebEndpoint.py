import FileSys

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict


class Handler(BaseHTTPRequestHandler):
    '''

    '''

    def respond_json(self, status: int, data: Dict[str, str]) -> None:
        '''

        '''
        response_body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response_body)))
        self.end_headers()
        self.wfile.write(response_body)

    def do_GET(self) -> None:
        '''

        '''
        if self.path == "/fs/percent-used":
            self.respond_json(200,
                              {"message": str(FileSys.get_fs_percent_used())})
        else:
            self.respond_json(404,
                              {"error": "Not found"})


if __name__ == "__main__":
    pass
