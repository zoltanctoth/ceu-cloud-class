FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye
COPY requirements.txt /tmp/requirements.txt
USER vscode
ENV PATH=/home/vscode/.local/bin:$PATH
RUN pip install --user -r /tmp/requirements.txt
USER root

# Install AWS CLI v2
RUN pwd=$(pwd)
RUN cd /tmp
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN sudo ./aws/install
RUN cd $pwd

# RUN pip freeze > /requirements.txt
