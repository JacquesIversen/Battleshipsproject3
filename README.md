![battleshipgif](https://user-images.githubusercontent.com/116496979/221361050-c7d792fe-8b53-4e69-a3d2-f3b5f8a0e2c6.gif)


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
- The user can start a new game by running the program. The program will prompt the user to set the grid size and display the output. (This example will use input:5 )

<a href="https://imgbb.com/"><img src="https://i.ibb.co/7rSwT7M/Screen-Shot-2023-02-25-at-2-22-53-PM.png" alt="Screen-Shot-2023-02-25-at-2-22-53-PM" border="0"></a>

### Setting the Grid Size
- The user can set the grid size by entering a number between 5 & 9 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/72998gt/Screen-Shot-2023-02-25-at-2-23-01-PM.png" alt="Screen-Shot-2023-02-25-at-2-23-01-PM" border="0"></a>

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
- The user can call shots on the computer's ships by entering the coordinates they would like to target. First they'll type a longitutude value in numbers. Second they'll type a latitude value in letters. The Program will not allow empty input, or higher/lower input than asked upon. 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/6nZmYDQ/Screen-Shot-2023-02-25-at-2-23-19-PM.png" alt="Screen-Shot-2023-02-25-at-2-23-19-PM" border="0"></a>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/ZzPt9zp/Screen-Shot-2023-02-25-at-2-23-29-PM.png" alt="Screen-Shot-2023-02-25-at-2-23-29-PM" border="0"></a>


### Notification of Hit or Miss
- The program will notify the user if their shot was a hit or a miss. 
- Hit: X
- Miss : -


### Notification of Destruction of Ships
- The program will notify the user when they have destroyed half of the computer's ships. The user is not aware of the amount of ships in their enemy fleet. 
- If amount of hits to win is higher than shots remaining, game will end. 
- If shots remaining hit 0, game will end. 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/HG5tgdN/Screen-Shot-2023-02-25-at-2-24-19-PM.png" alt="Screen-Shot-2023-02-25-at-2-24-19-PM" border="0"></a>


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

## Bugs and Fixes
---
### Code checked in Pythonchecker.com, following has been adjusted.
- Double/Two empty lines between all functions & comments.
- Additional variables were added to have line > 80 characters
- Linter-mistakes corrected, mainly "trailing whitespace"
- 92 % in Pythonchecker (Not recognizing whitespace)

<a href="https://ibb.co/7zxcfZK"><img src="https://i.ibb.co/H2LvSbq/Screen-Shot-2023-02-25-at-1-56-33-PM.png" alt="Screen-Shot-2023-02-25-at-1-56-33-PM" border="0"></a>
<a href="https://ibb.co/nQjQbHR"><img src="https://i.ibb.co/r5H5mCv/Screen-Shot-2023-02-25-at-1-56-40-PM.png" alt="Screen-Shot-2023-02-25-at-1-56-40-PM" border="0"></a>
- 0 Faults remaining PEP8.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/bKCY3dx/Screen-Shot-2023-02-25-at-2-06-09-PM.png" alt="Screen-Shot-2023-02-25-at-2-06-09-PM" border="0"></a>

## Deployment
---
The site was created using the Visual Studio Code editor and pushed to github to the repository Battleshipsproject3.

### Heroku Deployment
The below steps were followed to deploy this project to Heroku:

- Go to Heroku and click "New" to create a new app.
- Choose an app name and region region, click "Create app".
- Go to "Settings" and navigate to Config Vars. Add the following config variables:
- PORT : 8000
- Navigate to Buildpacks and add buildpacks for Python and NodeJS (in that order).
- Navigate to "Deploy". Set the deployment method to Github and enter repository name and connect.
- Scroll down to Manual Deploy, select "main" branch and click "Deploy Branch".
The app will now be deployed to heroku

Live Link:  !!!

## Credits:
This project would not have been completed if not for numerous Youtube Heroes, and type-copying 4 project before building this one. 
- Deployment, thanks to Codeinstitute's LoveSandwiches project tutorial.
- PEP8 Validation thanks to StackOverflow.
- https://www.youtube.com/watch?v=tF1WRCrd_HQ YT link, first used in testing.
- https://www.youtube.com/watch?v=u3yo-TjeIDg Refactoring, part 1 & 2. 
- https://www.youtube.com/watch?v=G6JTM-zt-dQ Cloning, used in testing. 
- https://www.youtube.com/watch?v=QVdf0LgmICw Working with the global/local statement.
- https://imgbb.com/ for creating an URL on PNG to inout in readme. 
