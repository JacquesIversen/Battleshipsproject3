![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome JacquesIversen,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!Battleships Game README
Introduction
This is a Python implementation of the popular Battleships game. The game is played on a grid, where each player's fleet of battleships is marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
Site Goals
The goal of this application is to provide a working Battleships game for a single user to play against the computer.
Target Audience
Anyone who enjoys playing strategy games.
User Stories
As a player, I want to be able to easily start a new game.
As a player, I want to be able to set the grid size.
As a player, I want to be able to place my battleships on the grid.
As a player, I want to be able to call shots at the computer's ships.
As a player, I want to be notified of a hit or miss on my shots.
As a player, I want to be notified when I have destroyed all of the computer's ships.
As a player, I want to be able to quit the game at any time.
Features Planned
Ability to set grid size
Ability to place battleships on the grid
Ability to call shots at the computer's ships
Notification of hit or miss on shots
Notification of destruction of all of the computer's ships
Ability to quit the game at any time
Structure
The game will be played on a grid of variable size, where each player will place their battleships. The players will then take turns calling shots at the other player's ships. The game ends when one player has destroyed all of the other player's ships.
Features
Starting a New Game
The user can start a new game by running the program. The program will prompt the user to set the grid size and place their battleships.
Setting the Grid Size
The user can set the grid size by entering the number of rows and columns they would like.
Placing Battleships
The user can place their battleships on the grid by entering the coordinates of the starting point and the direction they would like the battleship to be placed.
Calling Shots
The user can call shots on the computer's ships by entering the coordinates they would like to target.
Notification of Hit or Miss
The program will notify the user if their shot was a hit or a miss.
Notification of Destruction of Ships
The program will notify the user when they have destroyed all of the computer's ships.
Quitting the Game
The user can quit the game at any time by typing "quit" into the console.
Features Left to Implement
Multiplayer functionality
Improved user interface
Logical Flow
Start game
Set grid size
Place battleships
Begin turn-based gameplay
Call shots
Check for hit or miss
Check for destruction of ships
Alternate turns until one player has destroyed all of the other player's ships
Technologies
Python
Pygame
Testing
Functional testing will be performed to ensure that all features are working as intended.
Deployment
The application can be deployed locally by running the Python script. No additional setup is required.
Credits
Pygame Documentation - Reference for Pygame functionality.