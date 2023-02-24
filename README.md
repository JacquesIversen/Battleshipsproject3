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

# Battleships Game
Introduction

This is a Python implementation of the popular Battleships game. The game is played on a grid where a hidden fleet of battleships is marked. The locations of the fleet are concealed from the player. The player take shots at the opponents ships, and the objective of the game is to destroy the opposing player's fleet.

## Site Goals

The goal of this application is to provide a working Battleships game for a single user to play against the computer. 

## Target Audience
---
Anyone who enjoys playing strategy games.

### User Stories
---
- As a player, I want to be able to easily start a new game.
- As a player, I want to be able to set the grid size.
- As a player, I want to be able to call shots at the computer's ships.
- As a player, I want to be notified of a hit or miss on my shots.
- As a player, I want to be notified when I have destroyed all of the computer's ships.


## Features Planned
---
- Ability to set grid size
- Ability to call shots at the computer's ships
- Notification of hit or miss on shots
- Notification of destruction of all of the computer's ships

## Structure
---
The game will be played on a grid of variable size, where the player will use their turns calling shots at the computers ships. The game ends when the player has either hit half of the invading Navy's ships, or run out of shots. 

## Features
--- 
### Starting a New Game
- The user can start a new game by running the program. The program will prompt the user to set the grid size and display the output.

### Setting the Grid Size
- The user can set the grid size by entering a number between 5 & 9

| Input | Grid size | Enemys | Points to win | Turns |
| ------ | ------ | ------ | ------ | ----- |
| 5 | 25 | 10 | 5 | 15 |
| 6 | 36 | 12 | 6 | 18 |
| 7 | 49 | 14 | 7 | 21 |
| 8 | 64 | 16 | 8 | 24 |
| 9 | 81 | 18 | 9 | 27 |


### Placing Battleships
- The computer will randomly place 2 times the prompted data in ships. 

### Calling Shots
- The user can call shots on the computer's ships by entering the coordinates they would like to target.

### Notification of Hit or Miss
- The program will notify the user if their shot was a hit or a miss.

### Notification of Destruction of Ships
- The program will notify the user when they have destroyed half of the computer's ships.

## Features Left to Implement
--- 
- Multiplayer functionality
- Variable difficulty 
- Improved user interface

## Logical Flow
--- 

# insert flowchart here.
1. Start game
2. Set grid size
3. Pick a row value
4. Pick column value
5. Feedback for hit or miss (X for hit / - for miss)
6. Turn is withdrawn, unless input has already been used. 
7. Will continue until lost or won.

## Technologies
- Python, Main language used to build this application.

## Testing
---
Functional testing has been performed to ensure that all features are working as intended:
### Wrong User Inputs: (variable game set to 5)
1. Enter board size inbetween 5-9: If value is other than asked, line will run again.
2. Pick a row between 1 & 5: If value is other than asked, system will print:
-     You were supposed to pick a number between 1 & 5
-     Let's try again. Pick a number between 1 & 5: 
3. Place a latitude letter from A - E: If value is other than asked, system will print: 
-     I though you understood the rules here.. -.-
-     A letter from A - E please: 
4. If same / used value is placed, system will run again, not deducting the user a turn.



---
Deployment
The application can be deployed locally by running the Python script. No additional setup is required.
Credits
Pygame Documentation - Reference for Pygame functionality.