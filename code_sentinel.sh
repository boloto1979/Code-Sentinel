#!/bin/bash

# Code Sentinel Launcher Script
# Launches the Code Sentinel program with or without GUI

echo "
    _____ ____  _____  ______    _____ ______ _   _ _______ _____ _   _ ______ _      
   / ____/ __ \|  __ \|  ____|  / ____|  ____| \ | |__   __|_   _| \ | |  ____| |     
  | |   | |  | | |  | | |__    | (___ | |__  |  \| |  | |    | | |  \| | |__  | |     
  | |   | |  | | |  | |  __|    \___ \|  __| | .   |  | |    | | | .   |  __| | |     
  | |____ |__| | |__| | |____   ____) | |____| |\  |  | |   _| |_| |\  | |____| |____ 
   \_____\____/|_____/|______| |_____/|______|_| \_|  |_|  |_____|_| \_|______|______|                                                                                           
"

function show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "Launches the Code Sentinel program with or without GUI."
    echo ""
    echo "Options:"
    echo "  [1] Install Required Dependencies"
    echo "  [2] Start Code Sentinel with GUI"
    echo "  [3] Open GitHub Repository"
    echo "  [4] Sponsor me on GitHub"
    echo "  [5] Help"
    echo "  [6] Exit"
}

show_options=true

if ! command -v python3 &>/dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 before running the program."
    exit 1
fi

if [ ! -f "CodeSentinel.py" ]; then
    echo "Error: CodeSentinel.py file not found. Make sure the file exists in the current directory."
    exit 1
fi

while true; do
    if [ "$show_options" = true ]; then
        echo ""
        echo "Options:"
        echo "  [1] Install Required Dependencies"
        echo "  [2] Start Code Sentinel with GUI"
        echo "  [3] Open GitHub Repository"
        echo "  [4] Sponsor me on GitHub"
        echo "  [5] Help"
        echo "  [6] Exit"
    fi

    read -p "> " option
    case $option in
        1)
            echo "Installing required dependencies..."
            if ! pip3 install -r requirements.txt; then
                echo "Error: Failed to install dependencies. Please make sure you have the necessary permissions."
                exit 1
            fi
            ;;
        2)
            echo "Opening the program with graphical interface..."
            python3 sentinel.py
            show_options=false
            ;;
        3)
            echo "Opening the GitHub repository..."
            xdg-open "https://github.com/boloto1979/Code-Sentinel" 2>/dev/null
            show_options=false
            ;;
        4)
            echo "Opening the Sponsor..."
            xdg-open "https://github.com/sponsors/boloto1979" 2>/dev/null
            show_options=false
            ;;
        5)
            show_help
            show_options=false
            ;;
        6)
            echo "Closing the program..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please enter a valid option number."
            ;;
    esac
done

echo "Thank you for using Code Sentinel!"
