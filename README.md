# battleship

NOTES:
- init_board function modified --> board has become a local variable instead of global variable, change main accordingly
- graphics.print_outro() --> define more thoroughly


Battleship

Péter Juhász & Márk Kovács
Mar 28, 2017

Concept

Implementation of the original Battleship board game, currently available only in 2-player version. There are 2 phases of the game. In the placement phase, players place their ships on their own board to initialize the starting set-up, which is then proceeded by the battle phase, where players take turns to eliminate each other’s ships. Victory is reached, when one of the players manage to annihilate all the ships of the other player, or draw if turn-counter reaches the maximum number of turns, set by the players.


Placement phase

   place ships on a 10x10 grid
   be able to create special-shape ships (horizontal, vertical, L-shaped, square, ..etc)
   prevent placing ships out of the board
   prevent placing ships to coords where there is not enough space
   validate user input – filter out syntactically invalid input formats and also check logically


Battle phase

   After placement phase, battle phase starts immediately
   Players take turns by guessing a coordinate (A1-J10), which is the very definition of shooting to a targeted area
   Result of each shot can be either of the following:
       Shot hit target, ship is not sunk
       Shot hit target, that ship has sunk
       Shot hit target, that ship has sunk, all ships are sunk (game over)
       Shot missed
       Targeted coordinate was already shot at (missed opportunity, turn passes)
   Validate user input - filter out syntactically invalid input formats and also check logically


Known issues

   minor bug: when there is not enough space to place your ship we raise an error for the first time, but if you try to place your ship again into the same place then there is no error message


Upgrade plans

We are going to implement this list step-by-step, AI will only be implemented if we have enough time:

   restructure code (variable scope, main, abolish code redundancy, separate code into several files)
   maintain clean code (pep8)
   remove bug when trying to place a ship in the corner again
   further bug tests(!)
   improve graphics: print out own board when placing ships
   implement AI: play against the computer
