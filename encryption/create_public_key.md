# Creating a public keypair

The environment variable `CODESPACE_VSCODE_FOLDER` stores your project folder in this codespace:
```
echo "My project folder is ${CODESPACE_VSCODE_FOLDER}"
```

Generate SSH keys
```
ssh-keygen -t rsa -f ${CODESPACE_VSCODE_FOLDER}/my_keypair -N ''
```

Where: 
* `ssh-keygen` is a standard command for generating a keypair`
* `-t rsa` tells the keygen that we want to create an RSA keypair (there are many different algorithms for keypair generation)
* `-f ${CODESPACE_VSCODE_FOLDER}` indicates where the key files will be located
* `-N ''` means we don't want to protect the keypair with a password

## Taking a look at the results
Public Key:
```cat ${CODESPACE_VSCODE_FOLDER}/my_keypair.pub```

Private Key:
```cat ${CODESPACE_VSCODE_FOLDER}/my_keypair```
