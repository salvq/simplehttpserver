# Simple HTTP server
Very simple http server to expose local files to local http request, example of such a request

![image](https://github.com/salvq/simplehttpserver/assets/43242348/400fdff3-c062-4ef9-8f07-c993b52a6810)

# Steps

1. Create dedicated folder where you start storing your files for exposure, example /share/Container/simplehttpserver
2. Copy the files to this dedicated folder
3. Dedicated folder is defined in docker-run or decoker-compose.yaml, change accordingly


In attached docker-compose the folder you place the file is server path /share/Container/simplehttpserver, this is optional and you can change to your fit.. Path /simplehttpserver is folder in docker image that HTTP server is exposing to and must stay unchaged (possible youcan update the script and re-create the image).
    volumes:
      - /share/Container/simplehttpserver:/simplehttpserver

