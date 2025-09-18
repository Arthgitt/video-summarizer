#!/usr/bin/env bash
set -e
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

# Install CPU-only PyTorch wheel (this keeps things from trying to build from source)
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Then install the rest
pip install -r requirements.txt

echo "Done. Activate venv with: source .venv/bin/activate"
