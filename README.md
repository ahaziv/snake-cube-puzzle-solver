<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



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

[![Product Name Screen Shot][product-screenshot]](https://example.com)

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
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/ahaziv/snake-cube-puzzle-solver/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ziv-aharoni-3909271b0/
[product-screenshot]: snake cube solution.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
