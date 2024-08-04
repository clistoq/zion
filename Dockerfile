FROM gcr.io/distroless/python3-debian12:debug
COPY venv /venv
ENTRYPOINT ["/venv/bin/python3", "zion"]
