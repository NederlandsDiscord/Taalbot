# Build stage.
FROM python:3.10-slim as builder

# Create virtual environment.
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies.
COPY requirements-prod.txt .
RUN apt-get update && pip install -r requirements-prod.txt

# Run stage.
FROM python:3.10-slim

# Create unprivileged user.
RUN addgroup --system taalbot && adduser --system --group taalbot
USER taalbot

# Copy venv from build stage.
COPY --from=builder /opt/venv /home/taalbot/venv
ENV PATH="/home/taalbot/venv/bin:$PATH"

# Setup a working directory and copy the source code to it.
#RUN mkdir -p /home/taalbot/src
COPY src/ /home/taalbot/src
WORKDIR /home/taalbot/src

# Run main.py when started as container.
CMD [ "python3", "main.py" ]
