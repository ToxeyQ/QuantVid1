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

The video aims to introduce and solve this problem in a easy to follow and visually pleasing way. 

---

## Tech Stack

- **Python 3.13** 
- **Manim Community 0.18+** for creating animations
- **Git/GitHub** for version control

---

## Project Structure

```plaintext
Quant1/
├── Scenes
    ├──intro.py                     # Short intro to vid
    ├──problem_statement.py         # Code for introducing the problem
    ├──main.py                      # Code for the main solution
    ├──testing.py                   # A file to test quick renders
