FROM python:3.11.3-bullseye

# create non-root user
RUN useradd -d /script -s /bin/bash simple

ADD script /script
WORKDIR /script

USER simple

# Expose the default http server ports
EXPOSE 8000/udp 8000/tcp

CMD ["python3", "simple_server.py"]
HEALTHCHECK CMD curl --fail http://127.0.0.1:8000 || exit 1