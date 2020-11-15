"""
    Authors: Cedric Murairi & Mthabisi Ndlovu
    This file contains the main class for the Game board and other
    implementation details.
"""

from unittest import TestCase


class Board:
    """ This is the Python representation of the board with
        initial width and height
    """

    def __init__(self, width, height):
        # initialazing the board with its properties, width and height
        self.width = width
        self.height = height

        # define a variable resolution to store the nbr of pixels for each box
        # define the 2D arrray to store the default state of each box on the board
        # returns a canvas(window) of the same size(width x height)

    def create_cells(self):
        # function creates cells and place them on the board
        # access the Cell class and create an instance of it for each iteration
        pass

    def clean(self):
        # Iterate over the 2D array of the board, and bring all the values to zero for every
        # single cell on the board
        pass

# Test class for the Game Board which inherits from unittest TestCase


class TestBoard(TestCase):
    """
        Class contains all the possible test scenario for the game board
    """

    def setUp(self):
        # instantiate the board class with size 400, 400 and be ready for the test
        pass

    def test_dimensions(self):
        # test if the dimenssion of the instance of the board are equal
        # to the expected result, here (400, 400)
        pass

    def test_cell_resolution(self):
        # test if each cell on the canvas has the appropriate width, in this case
        # the width or the cell shoud be equal to the resolution
        pass

    def test_number_of_cells(self):
        # test if the total number of cells on the board is equal to the number
        # of pixel divided by the resolution of one cell -> if it is 16x16 for 8 resolution
        # we should get 32 cells
        pass

    def test_resizable(self):
        # test if the game window can easily be resizable
        # resize from 400, 400 to 200, 250 and check resulf if equal to 200, 250
        pass

    def test_clean_board(self):
        # test is all the values are have zero or false(dead cells) when clean
        # is called on the board instance, if not then we need to fix the code!
        pass
