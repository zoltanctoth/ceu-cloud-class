#!/usr/bin/env bash

if [ -z "$CODESPACE_VSCODE_FOLDER" ]; then
    export CODESPACE_VSCODE_FOLDER="${PWD}"
fi
