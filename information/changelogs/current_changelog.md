
---
<h1>Changelog dated 19, 05, 2026:</h1>
<h2>Overview:</h2>
Today I've managed to make it so that there is collision checking and validating.


<h2>Added:</h2>
- Classes:
  1. The main object class:
     - Added a function to see if something is in the path of a character's movement.
       - This then checks if it's considered impassable like a wall.
- Misc:
  1. Added a world objects that stores the data for the objects in the world.


<h2>Changed:</h2>
- Classes:
  1. The main class:
     - Changed the movement slightly so that it uses a separate function to check its collisions before attempting to move.
  2. The wall class is now called obstacle class
     - This is to futureproof the class for generalised obstacles.
- Misc:
  1. Changed the name of a group from 'walls' to 'obstacles'
     - This is so that when adding an obstacle it goes into a correctly named group.

<h2>Removed:</h2>
Nothing this time

