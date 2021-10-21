#!/bin/bash

echo "-----------------------------------------------------------------------"
echo "Execute develop building process"
echo "Export requirements_dev.txt"
echo "-----------------------------------------------------------------------"
# Poetry export
poetry export --dev --without-hashes -f requirements.txt -o requirements_dev.txt 
# Build docker image
docker build --network=host --no-cache -t demo-backend-dev:latest -f ../dockerfiles/backend-dev.dockerfile .
# Run all images
docker-compose --env-file ./env/dev.env -f ../docker_compose/backend-dev.yaml up -d