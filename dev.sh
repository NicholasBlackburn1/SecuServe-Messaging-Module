#!/bin/bash 

echo "setting up env..."
source /home/nicky/.cache/pypoetry/virtualenvs/secuserve-messaging-module-hZGHCc-t-py3.8/bin/activate

echo "running Messaging"
poetry run python3 MessagingMod/__main__.py