#!/bin/bash

# Stop All Challenges Script
# This script stops all blockchain CTF challenges

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
echo "  TCP1P CTF Blockchain - Stop All"
echo "=========================================="
echo ""

for challenge in "${CHALLENGES[@]}"; do
    echo "🛑 Stopping $challenge..."
    cd "$SCRIPT_DIR/$challenge"
    docker-compose down
    echo "✅ $challenge stopped!"
    echo ""
done

echo "=========================================="
echo "  All challenges have been stopped!"
echo "=========================================="
