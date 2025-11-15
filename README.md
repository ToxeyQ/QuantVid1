# TheQuantumQuant – Quantitative Probability Animation

## Video Overview
This video visualizes a classic probability problem involving independent uniform random variables:

> Given five independent random variables:  
> - a ~ Uniform[0,1]  
> - b ~ Uniform[0,2]  
> - c ~ Uniform[0,3]  
> - d ~ Uniform[0,4]  
> - e ~ Uniform[0,5]  
>   
> What is the probability that:  
> a < b < c < d < e ?

The animation illustrates the **ranges of each variable** as horizontal bars, and dynamically shows how the variable names move from the problem statement to the corresponding bars. Colors, checkmarks, and crosses are used to highlight correct and incorrect positions, helping viewers intuitively understand **ordered outcomes** for continuous random variables.

---

## Tech Stack

- **Python 3.13** 
- **Manim Community 0.18+** for creating animations
- **Git/GitHub** for version control

---

## Project Structure

```plaintext
Quant1/
├── main.py         # Manim scripts for the animation
├── helpers.py      # Optional helper functions for grids, bars, symbols
└── assets/         # Optional media (images, sounds, etc.)