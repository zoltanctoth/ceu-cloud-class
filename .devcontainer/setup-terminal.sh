#!/usr/bin/env bash

if [ -z "$CODESPACE_VSCODE_FOLDER" ]; then
    for file in ~/.bashrc ~/.bash_profile ~/.zshrc; do
        echo 'export CODESPACE_VSCODE_FOLDER="${PWD}" && echo INFO: CODESPACE_VSCODE_FOLDER set to ${PWD}' >> "$file"

    done
fi
