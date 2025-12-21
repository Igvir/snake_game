#!/bin/bash
# Snake Game Launcher

echo "Starting Snake Game..."
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
cd /home/iramirez/code/snake
source venv/bin/activate
python snake_game.py
