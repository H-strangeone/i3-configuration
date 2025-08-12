#!/usr/bin/env python3

import curses
import random
import time

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Food color
    
    # Get screen dimensions
    height, width = stdscr.getmaxyx()
    
    # Game variables
    snake = [(height // 2, width // 4)]  # Initial snake position
    direction = curses.KEY_RIGHT
    
    # Create initial food
    food = (height // 2, width // 2)
    
    # Set up game area
    box = curses.newwin(height - 2, width - 2, 1, 1)
    box.keypad(1)
    box.timeout(100)  # Refresh rate
    
    score = 0
    game_over = False
    
    # Draw border
    stdscr.box()
    stdscr.refresh()
    
    # Game loop
    while not game_over:
        # Display score
        stdscr.addstr(0, 2, f" Score: {score} ")
        stdscr.addstr(height - 1, 2, " Press 'q' to quit or 'r' to restart ")
        stdscr.refresh()
        
        # Get user input
        key = box.getch()
        
        # Check for quit or restart
        if key == ord('q'):
            break
        elif key == ord('r'):
            snake = [(height // 2, width // 4)]
            direction = curses.KEY_RIGHT
            food = (height // 2, width // 2)
            score = 0
            continue
        
        # Determine new direction
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            # Don't allow 180-degree turns
            if (key == curses.KEY_UP and direction != curses.KEY_DOWN) or \
               (key == curses.KEY_DOWN and direction != curses.KEY_UP) or \
               (key == curses.KEY_LEFT and direction != curses.KEY_RIGHT) or \
               (key == curses.KEY_RIGHT and direction != curses.KEY_LEFT):
                direction = key
        
        # Calculate new head position
        y, x = snake[0]
        if direction == curses.KEY_UP:
            y -= 1
        elif direction == curses.KEY_DOWN:
            y += 1
        elif direction == curses.KEY_LEFT:
            x -= 1
        elif direction == curses.KEY_RIGHT:
            x += 1
        
        new_head = (y, x)
        
        # Check for game over
        if (y <= 0 or y >= height - 1 or x <= 0 or x >= width - 1 or 
            new_head in snake):
            stdscr.addstr(height // 2, width // 2 - 5, "GAME OVER!", curses.A_BOLD)
            stdscr.addstr(height // 2 + 1, width // 2 - 14, "Press 'r' to restart or 'q' to quit", curses.A_BOLD)
            stdscr.refresh()
            
            # Wait for restart or quit
            while True:
                key = stdscr.getch()
                if key == ord('q'):
                    game_over = True
                    break
                elif key == ord('r'):
                    snake = [(height // 2, width // 4)]
                    direction = curses.KEY_RIGHT
                    food = (height // 2, width // 2)
                    score = 0
                    box.clear()
                    stdscr.clear()
                    stdscr.box()
                    stdscr.refresh()
                    break
            
            continue
        
        # Add new head
        snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == food:
            # Increase score
            score += 10
            
            # Generate new food
            while True:
                food_y = random.randint(2, height - 3)
                food_x = random.randint(2, width - 3)
                food = (food_y, food_x)
                if food not in snake:
                    break
        else:
            # Remove tail
            tail = snake.pop()
            # Clear the tail position
            box.addch(tail[0] - 1, tail[1] - 1, ' ')
        
        # Draw food
        box.addch(food[0] - 1, food[1] - 1, 'O', curses.color_pair(2))
        
        # Draw snake
        for i, (y, x) in enumerate(snake):
            if i == 0:
                box.addch(y - 1, x - 1, '@', curses.color_pair(1) | curses.A_BOLD)  # Head
            else:
                box.addch(y - 1, x - 1, '#', curses.color_pair(1))  # Body
        
        box.refresh()

if __name__ == "__main__":
    try:
        # Initialize curses and start the game
        curses.wrapper(main)
        # The wrapper function already handles proper setup and cleanup
        print("Thanks for playing Snake Game!")
    except KeyboardInterrupt:
        # Handle CTRL+C gracefully
        print("\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"An error occurred: {e}")
