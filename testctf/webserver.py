from http.server import BaseHTTPRequestHandler, HTTPServer
import time

Could_not_find_page = "pagenotfound.html"


pages = ["ctfsrv"]
hostName = 'localhost'
serverPort = 8000
f2 = open(Could_not_find_page,"r")
pagenotfound = f2.read()
f2.close()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        webpath = self.path
        htmlfile = webpath.split("/")
        f3 = open('tilesheet.png', 'rb')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        try:
            f = open(htmlfile[1] + ".html","r")
            webpage = f.read()
            f.close
            self.wfile.write(bytes(webpage, "utf8"))
            
        except:
            self.wfile.write(bytes(pagenotfound, "utf8"))
            
            print("err")
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


   
