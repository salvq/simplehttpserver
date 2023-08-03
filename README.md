# Simple HTTP server
Very simple http server to expose local files to local http request, example of such a request

![image](https://github.com/salvq/simplehttpserver/assets/43242348/400fdff3-c062-4ef9-8f07-c993b52a6810)

Docker image is available on https://hub.docker.com/r/salvq/simplehttpserver

# Steps

1. Create dedicated folder for the files you plan to expose via http server, example `/share/Container/simplehttpserver`
2. Copy the files to this dedicated folder, example of `dump.txt` file location
```
[test@NASEFCasd2 simplehttpserver]$
[test@NASEFCasd2 simplehttpserver]$ pwd
/share/Container/simplehttpserver
[test@NASEFCasd2 simplehttpserver]$ ls -ll
total 67696
-rw-rw-rw- 1 user   everyone             32 2023-08-03 08:23 dump.txt
[test@NASEFCasd2 simplehttpserver]$
```
4. Dedicated folder `/share/Container/simplehttpserver` is defined in docker-run or decoker-compose.yaml below, change it accordingly
5. Folder `/simplehttpserver` must stay unchanged, this is docker image folder mapped to host folder `/share/Container/simplehttpserver`
6. Also change ports and network based on your requirements

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

# Connect to docker container
```
[test@NASEFCasd2 simplehttpserver]$
[test@NASEFCasd2 simplehttpserver]$ docker exec -it simplehttpserver bash
simple@cd0b998d23cd:~$ pwd
/script
simple@cd0b998d23cd:~$ ls -ll
total 4
-rw-rw-rw- 1 root root 343 Jul 16 10:50 simple_server.py
simple@cd0b998d23cd:~$ exit
exit
[test@NASEFCasd2 simplehttpserver]$
```
