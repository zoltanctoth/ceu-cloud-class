#!/bin/bash
set -e

# Load environment variables from .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
else
    echo "Error: .env file not found"
    exit 1
fi

# Check if GITHUB_TOKEN is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: GITHUB_TOKEN not found in .env file"
    exit 1
fi

# Configuration
IMAGE_NAME="ghcr.io/zoltanctoth/ceu-cloud-class"
IMAGE_TAG="latest"

echo "Logging in to GitHub Container Registry..."
echo "$GITHUB_TOKEN" | docker login ghcr.io -u zoltanctoth --password-stdin

echo "Building multi-architecture Docker image..."
echo "This will build for both ARM64 (Mac M1/M2/M3) and AMD64 (Intel/Codespaces)"

# Create a new builder instance if it doesn't exist
docker buildx create --name multiarch-builder --use 2>/dev/null || docker buildx use multiarch-builder

# Build and push multi-architecture image
docker buildx build \
    --platform linux/amd64,linux/arm64 \
    --tag "${IMAGE_NAME}:${IMAGE_TAG}" \
    --tag "${IMAGE_NAME}:$(date +%Y%m%d)" \
    --push \
    --file .devcontainer/Dockerfile \
    .

echo "Successfully built and pushed image to ${IMAGE_NAME}:${IMAGE_TAG}"
echo "Image is available for both ARM64 and AMD64 architectures"
