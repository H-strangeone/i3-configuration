#!/usr/bin/env python3

import curses
import time

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    
    # Get screen dimensions
    height, width = stdscr.getmaxyx()
    
    # Initial position for our character
    y, x = height // 2, width // 2
    character = '@'
    
    # Create a border
    stdscr.box()
    
    # Add instructions
    stdscr.addstr(0, 2, " Use arrow keys to move. Press 'q' to quit. ")
    
    # Show the initial character
    stdscr.addstr(y, x, character)
    stdscr.refresh()
    
    # Set input timeout (makes getch non-blocking)
    stdscr.timeout(100)
    
    # Main loop
    while True:
        # Display current position
        position_text = f"Position: ({y}, {x})"
        stdscr.addstr(height - 1, 2, position_text)
        stdscr.refresh()
        
        # Get user input
        key = stdscr.getch()
        
        # Check for quit
        if key == ord('q'):
            break
        
        # Clear previous character position
        stdscr.addstr(y, x, ' ')
        
        # Update position based on arrow key
        if key == curses.KEY_UP and y > 1:
            y -= 1
        elif key == curses.KEY_DOWN and y < height - 2:
            y += 1
        elif key == curses.KEY_LEFT and x > 1:
            x -= 1
        elif key == curses.KEY_RIGHT and x < width - 2:
            x += 1
        
        # Draw character at new position
        stdscr.addstr(y, x, character)
        
        # Add a key pressed message
        if key != -1:  # -1 is returned when no key is pressed (timeout)
            key_name = ""
            if key == curses.KEY_UP:
                key_name = "UP"
            elif key == curses.KEY_DOWN:
                key_name = "DOWN"
            elif key == curses.KEY_LEFT:
                key_name = "LEFT"
            elif key == curses.KEY_RIGHT:
                key_name = "RIGHT"
            elif key == -1:
                key_name = "NONE"
            else:
                key_name = chr(key)
                
            key_msg = f"Key pressed: {key_name}   "
            stdscr.addstr(height - 2, 2, key_msg)
        
        # Refresh screen to show updates
        stdscr.refresh()

if __name__ == "__main__":
    try:
        # Initialize curses environment
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        print("Key Demo Finished!")
        print("\nWhat you just saw:")
        print("1. Real-time keyboard input handling")
        print("2. Screen position coordination (y, x)")
        print("3. Character movement with boundaries")
        print("4. Screen updates and refreshing")
        print("\nThese are essential concepts for building the Snake game!")

