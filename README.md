# CopsAndRobbers
Cops and Robbers Game - Application Development Class @ UT  in Spring 2020

Program Description:

Cops and Robbers is a classic game that has been played over multiple generations. The
goal of the game is quite simple, the cop is trying to catch the robber and the robber is trying to
avoid being caught by reaching safety. Through the use of python coding, this timeless game can
now be enjoyed and played online. The Cops and Robbers program that we have developed
encompasses three modules, two classes and multiple methods that are used to define locations and
movements of objects, while making the program user friendly.
The first class in the program is called Cop_Robber and can be found in the user module.
Cop_Robber has the main purpose of defining the position of each player through longitude and
latitude coordinates, while also allowing each player to move and alter their coordinates. In more
technical terms, the way this class works is through the initiation of the player object with default
latitude and longitude coordinates of 0. In order for the players to move up, the latitude coordinate
is subtracted by 1, while if the player wishes to move down the latitude coordinate is added by 1.
On the other hand, if the player aims to move left the longitude coordinate is subtracted by 1 and to
move right the longitude coordinate is added by 1. To avoid the player moving off of the provided
grid, else statements that define invalid coordinates are used. The second class that is used in the
program is called Safehouse and can be found in the buildings module. Safehouse initiates the
safehouse object with default latitude and longitude coordinates of 0, allowing for the location to
be specified in the main module.
The main module creates an interactive user interface that is easy to use and follow.
Through the implementation of a grid using the grid function, the user is able to visualize and track
where each player is. The second function that is used in the main module is called motion. The
motion function has two main purposes, the first being the ability of the program to detect which
control the user inputted, while also recognizing invalid inputs and allowing the user to reenter a
valid option. The second purpose of the function is to differentiate when each player will have the
chance to move, with the cop moving on the even turns and the robber moving on the odd turns.
The rest of the main module sets the starting positions of the cop and robber, while also setting the
location of the safehouse. The welcoming statement, directions, and goals of the game are also
printed to the user’s screen. Overall, the main module brings the game to life by tying all the
different elements of the program together to create an enjoyable experience for the user.


Program Instructions:

Welcome to Cops and Robbers! Grab a friend and enjoy some satisfying gameplay from
your favorite UT Application Developers. The goal of the game is for the Robber(R) to reach the
Safehouse (marked with a $) without being caught by the Cop(C). The users are given a 9X9 grid
to navigate with starting positions at (5,5) and (9,1). Who will Prevail?!
The instructions for gameplay are as follows:
1. Assign roles to both players. One will be the Cop, the other will be the Robber.
2. During each turn the players are given the option to move up, down, left, or right.
3. The Cop should attempt to catch the Robber and the Robber should attempt to get to the
Safehouse without getting caught.
Winning Scenarios:
Cop Wins: The Robber is caught before reaching the Safehouse.
Displaying- ”CAUGHT!! See you in court…”
Robber Wins: The Robber reaches the Safehouse without getting caught.
Displaying - “SAFE!!! Play again soon…”
