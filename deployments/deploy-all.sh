#!/bin/bash

# Deploy All Challenges Script
# This script starts all blockchain CTF challenges using Docker Compose

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

CHALLENGES=(
    "TheGenesisCrypt"
    "EchoesOfCollision"
    "TheBifrostRelayer"
    "TheOracleParadox"
    "TheQuantumEntanglement"
)

echo "=========================================="
echo "  TCP1P CTF Blockchain - Deploy All"
echo "=========================================="
echo ""

for challenge in "${CHALLENGES[@]}"; do
    echo "🚀 Starting $challenge..."
    cd "$SCRIPT_DIR/$challenge"
    docker-compose up -d --build
    echo "✅ $challenge started!"
    echo ""
done

# Ports are hardcoded in this version for simplicity
# In a more dynamic version, we could read these from the docker-compose files or use environment variables.

echo "=========================================="
echo "  All challenges are now running!"
echo "=========================================="
echo ""
echo "Challenge URLs:"
echo "  - TheGenesisCrypt:        http://127.0.0.1:32104/"
echo "  - EchoesOfCollision:      http://127.0.0.1:49205/"
echo "  - TheBifrostRelayer:      http://127.0.0.1:33428/"
echo "  - TheOracleParadox:       http://127.0.0.1:37819/"
echo "  - TheQuantumEntanglement: http://127.0.0.1:35780/"
echo ""