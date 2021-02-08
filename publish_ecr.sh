#!/bin/bash

set -e

# fill in your values
AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}
AWS_ACCOUNT=${AWS_ACCOUNT}
IMAGE_REPO_NAME=example
IMAGE_TAG=latest

echo Logging in to Amazon ECR...
aws ecr get-login-password | docker login --username AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.us-east-1.amazonaws.com

echo "Building the Docker image..."
export PIP_INDEX_URL=`python3 -m pip config get global.index-url`

docker build --build-arg pip_index_url="${PIP_INDEX_URL}" -t ${IMAGE_REPO_NAME}:${IMAGE_TAG} .
docker tag $IMAGE_REPO_NAME:${IMAGE_TAG} ${AWS_ACCOUNT}.dkr.ecr.us-east-1.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}

echo "Pushing the Docker image..."
docker push ${AWS_ACCOUNT}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}
echo "Build succeeded"
