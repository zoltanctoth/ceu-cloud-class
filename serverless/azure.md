# Azure authentication

Azure CLI is already instaled within the container.

### Configure the AZURE CLI for storage:
```
az login --use-device-code
```
Navigate to the provided link, enter the given code, and then sign in to your account.

Select the subscription you would like to use.

### To use services other than storage, you need to set the apikey variable.