import http.server
import socketserver
import os

print(f'HTTP server is starting up')

folder = '/simplehttpserver'
os.chdir(folder)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 8000), Handler)

try:
    print(f'HTTP server is running')
    httpd.serve_forever()

except Exception as e:
    httpd.server_close()
    print(f'Errors in program: {e}')
