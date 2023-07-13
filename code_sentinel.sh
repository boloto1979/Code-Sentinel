#!/bin/bash

echo "  #####  ####### ######  #######     #####  ####### #     # ####### ### #     # ####### # #
 #     # #     # #     # #          #     # #       ##    #    #     #  ##    # #       # #
 #       #     # #     # #          #       #       # #   #    #     #  # #   # #       # #
 #       #     # #     # #####       #####  #####   #  #  #    #     #  #  #  # #####   # #
 #       #     # #     # #                # #       #   # #    #     #  #   # # #       # #
 #     # #     # #     # #          #     # #       #    ##    #     #  #    ## #       # #
  #####  ####### ######  #######     #####  ####### #     #    #    ### #     # ####### ####### #

"

echo "Do you want to use a GUI? (y/n)"
read choice

if [ "$choice" == "y" ]; then
    echo "Opening the program with graphical interface..."
    python3 CodeSentinel.py
else
    echo "Closing the program..."
fi
