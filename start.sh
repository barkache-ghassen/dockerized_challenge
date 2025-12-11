#!/bin/bash
set -e

# Run challenge script in background
/root/challenge1/run_challenge.sh &

# Execute base image CMD
exec "$@"

