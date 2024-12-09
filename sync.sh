#!/bin/bash

# Usage: curl -s https://raw.githubusercontent.com/CEU-Economics-and-Business/ECBS-5147-Data-Engineering-2-Cloud-Computing/main/sync.sh | bash

echo "Syncing with template repository..."


# Sync serverless folder
rm -rf pipeline
curl -sL https://github.com/CEU-Economics-and-Business/ECBS-5147-Data-Engineering-2-Cloud-Computing/archive/main.zip -o main.zip
unzip -q main.zip "ECBS-5147-Data-Engineering-2-Cloud-Computing-main/pipeline/*" -d temp
mv temp/ECBS-5147-Data-Engineering-2-Cloud-Computing-main/pipeline pipeline
rm -rf temp main.zip

echo "Sync completed!"
