import http.server
import socketserver
import os

folder = '/simplehttpserver'
os.chdir(folder)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 8000), Handler)

try:
    httpd.serve_forever()

except Exception as e:
    httpd.server_close()
    print(f'{current_time} Errors in program: {e}')