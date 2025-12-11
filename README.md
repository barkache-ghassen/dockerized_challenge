

# web3-debian-vnc

```shell
docker build -t web3-debian-vnc .


docker run -d --name web3-debian-vnc -p 5901:5901 -p 8080:8080 web3-debian-vnc
```
you need to run the challenge from within the container: 
```shell
docker exec -it <container> /bin/bash
cd root 
./run_challenge.sh
```