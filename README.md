<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Snake Cube Solver</h3>

  <p align="center">
    An algorithmic solver for snake cube puzzles
    <br />
    <a href="https://github.com/ahaziv/snake-cube-puzzle-solver"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/ahaziv/snake-cube-puzzle-solver/snake_cube_solution.png)

This solver was written following a dinner at a friends house, He had this 4x4 snake cube puzzle which I picked up and couldn't solve by hand. This code was written on the next weekend so the cube could sit nice and tidy on my friends shelf. 

This code was written purely for the sports of it, and I found tackling the problem pretty educational  
* It has some neat implementation of algorithmic principles (such of BFS) over 3D grid space. 
* Demonstrates how such simple problems can have high complexity.

The initial solver takes a purely brute force approach. It sets the snake end at one of several potential initial positions and then recursively, link by link tries all possible link positions. 
Stopping conditions are either reaching a solution or reaching a dead end (where no viable link placement is found).
This approach provided a highly complex solution averaging at O(1.465^n), where n is the nuber of straight links in the snake. 

To improve algorithm performance I added another stopping condition, which is reached when discontinuity of two vacant cube regions is found.
Discontinuity is found by describing the remaining vacant space as a simple undirected graph. Where each cube is a vertex and each two adjacent cube faces are an edge.
With each snake link placed, the filled in space is removed from the graph, and continuity is checked using BFS.
This addition reduced the complexity base from 1.465 to 1.309, Yet added the BFS algorithm complexity for each iteration.
All in all, I estimate and improvement of about 30% to running times (for 4 dimensional cube)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

simply load the files and run the main file (numpy and matplotlib required).


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Your Name - [@ziv_aharoni](https://www.linkedin.com/in/ziv-aharoni-3909271b0/) - ahaziv@gmail.com

Project Link: [https://github.com/ahaziv/snake-cube-puzzle-solver](https://github.com/ahaziv/snake-cube-puzzle-solver)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: snake_cube_solution.png
