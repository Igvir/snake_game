#!/usr/bin/env python3
import sys
import os

# Add library path before importing pygame
os.environ['LD_LIBRARY_PATH'] = '/usr/lib/x86_64-linux-gnu:' + os.environ.get('LD_LIBRARY_PATH', '')

import pygame

def test_snake_game():
    """Test basic snake game functionality"""
    try:
        # Import the game
        from snake_game import Snake, CELLS, WINDOW_SIZE, CELL_SIZE
        
        # Test Snake class
        snake = Snake()
        assert len(snake.body) == 1, "Snake should start with 1 segment"
        assert snake.direction == (1, 0), "Snake should start moving right"
        
        # Test snake movement
        initial_pos = snake.body[0]
        tail = snake.move()
        new_pos = snake.body[0]
        assert new_pos != initial_pos, "Snake should move to new position"
        assert len(snake.body) == 1, "Snake should still have 1 segment after move"
        
        # Test snake growth
        snake.grow()
        assert len(snake.body) == 2, "Snake should have 2 segments after growing"
        
        # Test collision detection
        # Move snake to boundary
        snake.body[0] = (-1, 0)  # Outside left boundary
        assert snake.check_collision(), "Snake should detect collision at boundary"
        
        # Test constants
        assert WINDOW_SIZE == 600, "Window size should be 600"
        assert CELL_SIZE == 20, "Cell size should be 20"
        assert CELLS == 30, "Should have 30 cells"
        
        print("✓ All basic functionality tests passed!")
        print(f"✓ Game window: {WINDOW_SIZE}x{WINDOW_SIZE}")
        print(f"✓ Grid: {CELLS}x{CELLS} cells")
        print(f"✓ Cell size: {CELL_SIZE}px")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_snake_game()
    sys.exit(0 if success else 1)
