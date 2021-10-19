from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import win32print
import win32api


data = {'result': 'this is test'}

host = ('0.0.0.0', 6088)

def printer(filename):
    win32api.ShellExecute(0, 'print', filename,
                      win32print.GetDefaultPrinterW(), ".", 0)



class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        print("do_GET")
        

    def do_POST(self):
        print("do_post")
        length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(length))
        print(post_data)
        f = open("1.txt", "w")
        f.write(post_data["no"]+"\n")
        f.write(post_data["code"])
        f.close()
        printer("1.txt")


if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting Server....")
    server.serve_forever()

