FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye
COPY requirements.txt /tmp/requirements.txt
USER vscode
ENV PATH=/home/vscode/.local/bin:$PATH
RUN pip install --user -r /tmp/requirements.txt
USER root
RUN rm /tmp/requirements.txt