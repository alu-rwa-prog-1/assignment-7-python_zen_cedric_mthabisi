"""
Authors: Cedric Murairi & Mthabisi Ndlovu

This program describes the Cell class.

Cell
-> Instance Variables
    - status
    - color

-> Methods
    - set_dead
    - set_alive
    - is_alive
"""

# define Cell class
# initialize cell
# set status to dead
# set color to black (default color of the board)

# set_dead
# set status to dead
# set color to black

# set_alive
# set status to alive
# set color to green

# is_alive
# return true if status is alive, otherwise return false

# Tests

# Test# | Test Type |   Test Data  |             Reason             |   Expected Outcome    |
#  1    |   Valid   |  status=dead | Apply set_dead method to cell  |  Calling is_alive     |
#       |           |              |  to see if it remains dead     |  method returns False |
#  2    |   Valid   | status=alive | Apply set_dead method to cell  |  Calling is_alive     |
#       |           |              |  to see if it becomes dead     |  method returns False |
#  3    |   Valid   | status=alive | Apply set_alive method to cell |  Calling is_alive     |
#       |           |              |  to see if it remains alive    |  method return True   |
#  4    |   Valid   | status=alive | Apply set_alive method to cell |  Calling is_alive     |
#       |           |              |  to see if it becomes alive    |  method return True   |
#  5    |  Invalid  | status=null  | Check if status=alive          |  Returns False        |
