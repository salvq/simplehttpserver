# Simple HTTP server
Very simple http server to expose local files to local http request, example of such a request

![image](https://github.com/salvq/simplehttpserver/assets/43242348/400fdff3-c062-4ef9-8f07-c993b52a6810)

# Steps

1. Create dedicated folder for filesto be exposed to http server, example `/share/Container/simplehttpserver`
2. Copy the files to this dedicated folder
3. Dedicated folder is defined in docker-run or decoker-compose.yaml below, change it accordingly
4. Folder /simplehttpserver must stay unchanged, this is docker image folder mapped to host folder `/share/Container/simplehttpserver`
5. Also change ports and network based on your requirements

# Run server via docker-run

```
docker run -d \
--name simplehttpserver \
--network=others \
--ip 172.18.5.44 \
--restart=always \
-p 8000:8080 \
-v /share/Container/simplehttpserver:/simplehttpserver \
salvq/simplehttpserver:1.2.0
```

# Run server via docker-compose.yaml
```
version: '3'
services:
  simplehttpserver:
    image: salvq/simplehttpserver:1.2.0
    container_name: simplehttpserver
    restart: unless-stopped
    ports:
      - "8000:8000"
    volumes:
      - /share/Container/simplehttpserver:/simplehttpserver
    networks:
      others:
         ipv4_address: 172.18.5.44
networks:
  others:
    external: true
```
