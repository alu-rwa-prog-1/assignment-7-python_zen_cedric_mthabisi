# Game of Life: Project Proposal
_Author: Mthabisi Ndlovu_ <br>
_Email: mtndlovu81@gmail.com_ <br>

## Description

We are going to work on the classical programming problem called **Game of Life** simply known as **Life**. It was invented in **1970** by a **British mathematician named John Horton Conway**. **Life** is a zero-player game where cells in a grid generate other cells or die based on a set of specific rules. Its evolution depends on the initial state of the game. The universe of the **Game of Life** is an infinite two-dimensional grid of square cells, each with two possible states, alive or dead. Every cell interacts with its eight neighbors. After each round, the board evolves as governed by the following rules: 

 - Any live cell with fewer than 2 live neighbors dies (from isolation).
 - Any live cell with 2 or 3 live neighbors survives.
 - Any live cell with more than 3 live neighbors dies (from overpopulation).
 - Any dead cell with exactly 3 live neighbors becomes alive

**Game of Life** can generate very interesting patterns, some of which terminate in a few moves and others that seem to go on forever.

## Technology

To build this game, we will use **Python** and **Pygame**. Python is the programming language in which we will write our code to define our objects and write the logic of the game. Pygame is a set of Python modules ideal for creating sprites and animations for our game.

## Features

### Main Scene
 - Welcome text
 - Start button

### Game Scene
 - Board (n × n grid)
 - Clickable square cells
 - Sound effects
 - Color transition to show birth, death, and survival
 - Generation number display
 - Play / stop button
 - Help button

### Help Scene
 - Text
 - Back button

### End of Life Scene (when Life terminates)
 - Text
 - Replay button

## Implementation 
 - see [implementation guide](https://github.com/alu-rwa-prog-1/assignment-7-python_zen_cedric_mthabisi/blob/main/implementation_guide.md)
