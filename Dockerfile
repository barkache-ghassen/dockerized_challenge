FROM web3-debian-vnc:latest

USER root

COPY challenge1 /root/challenge1
RUN chmod +x /root/challenge1/run_challenge.sh



COPY challenge1/solution /home/web3challenger/Desktop/solution

