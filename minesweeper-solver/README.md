# Minesweeper Clone and Solver
(Delete this project?)

[Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) is a fun puzzle game that used to be pre-installed on Windows computers everywhere. I used to play it during class in my first computer science course in high school and I had always wondered about implementing a way to automate playing the game.

## The solver
I used [this article](https://magnushoff.com/articles/minesweeper/) to learn about minesweeper solving. Finding the solution to a minesweeper board is said to be a NP-complete problem (see [this discussion](https://cstheory.stackexchange.com/questions/21323/is-it-np-hard-to-play-minesweeper-perfectly)). This means that even in simple puzzle boards, the solver must consider all possible game states to determine the solution. This only becomes a problem when there are lots of unsolved squares and there are millions of combinations to consider. 

To get around this complexity problem, I implemented a simple solving algorithm that always solves as much as it can before the brute force algorithm is run. The simple algorithm counts the number of bombs/empty/unrevealed squares around a given tile. If the simple algorithm is considering a "3" tile and there are exactly 3 unrevealed tiles around it, then those 3 tiles are guaranteed to be bombs. The simple solving algorithm often runs at around 80% of the solving time, so even the simple approach is very useful. 

A flaw with the game itself is that minesweeper games often end in a situation where the player must make a guess about a tile being a bomb or not. This is frustrating because it often occurs at the very end of the game in a corner, meaning that all of the prior work solving the puzzle might be wasted. It also breaks the solving algorithms because they are not designed to guess. Some people have proposed solutions to remove this problem, but I have not implemented any of the solutions in my minesweeper clone.

## The clone
I used pygame to display images of the real minesweeper game tiles, so my clone and the real game appear identical up to the pixel. This similarity allowed me to take screenshots of the board to determine the state of the game board. Using screenshots to inspect the board is probably not the most efficient method, but it was easy enough to implement and it allows my solver program to run on other implementations of the minesweeper game.

## Extensions
* Add chording: "When an uncovered square with a number has exactly the correct number of adjacent squares flagged, performing a click with both mouse buttons on it will uncover all unmarked squares" [-Minesweeper wiki](http://www.minesweeper.info/wiki/Chord)
* Try a probability-based solver for resolving the guessing situations, or as a replacement for the brute-force search
