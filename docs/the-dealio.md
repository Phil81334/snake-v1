here's the deal..

loop with 1s delay

list containing cell nums that snake is taking up
snake len to begin with is 5 cells

snake will spawn in the middle of the screen, horizontally

with each loop iteration, we move tail to new head pos (curr cell pos + direction)

we detect user input (arrow keys)

we have a func that tells us if new head pos is wall, self, food

if wall or self, game over

if food, grow snake by 1 cell via adding new head cell. leave tail

if food, spawn new food

if food, update score