# Game of Life: Implementation Guide
_Author: Cedric Murairi_ <br>
_Email: murairicedric@gmail.com_ <br>

Welcome to the technical guide of the incredible **Conway’s Game of Life**. Here we will go through the description of different classes we need to implement our project and discuss the relationship between them.

Since **Conway’s Game of Life** is a 2 dimensional game, we will be working with a **2D** board as our game field which is divided into cells making up the entire grid of pixels. Each box(cell) has two possible states, **live** or **dead**;

For that matter, we are going to need digital representation or Data Structures to work perfectly with the game complexity and perform all operations. Hence, our use of **Python Classes** and **Arrays**:

 - A **Game** class that plays as the center core of the program, referencing the **Board** game and **Cells**; the Game class would have different methods to handle different features of the game like: playing sound in the background, starting game, pausing or stopping the game; replay game, provide help, etc.

 - **Board** class to represent the game board: our class **Board** will hold all the details about our board game: **width** and **height**; makes up the foundation or pixel frame we will use to define and track the position of our cells. To define such a Data structure, we’re going to use a 2D array to store all the cell boxes e.g.

     [0, 0, 0, 0, 0, 0, 0, 0],<br>
     [0, 0, 0, 0, 0, 0, 0, 0],<br>
     [0, 0, 0, 1, 1, 1, 0, 0],<br>
     [0, 0, 0, 0, 0, 0, 0, 0],<br>
     [0, 0, 0, 0, 0, 0, 0, 0],<br>
     [0, 0, 0, 0, 0, 0, 0, 0],<br>
     [0, 0, 0, 0, 0, 0, 0, 0],<br>
     [0, 0, 0, 0, 0, 0, 0, 0]

would represent the board as an 8 × 8 grid with 3 live cells.

- **SpaceshipBoard** class which will inherit from the main **Board** class and will play a role in generating initial cells to play as **Heavy-Weight Spaceship**
in our game. It will inherits most of its methods from the parent class and will just have a single one: **change_spaceship** which will change from to the different types of spaceships and display them on the screen: **Glider**, **Light-weight spaceship**, **Middle-weight spaceship** and **Heavy-weight spaceship**

 - **Cell** class to represent the cells on the board: our second class **Cell** includes all the details and properties of the cells on the board: **coordinates**(location on the board), **status**(live or dead), **resolution**(how many pixels a cell box occupies on the grid)

This game is a zero player game, that is why there is not such a class representation of the player, once you launch the game the different cells will directly start the reproduction process.
