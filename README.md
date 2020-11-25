# Polymagnets 

[Jupyter Notebook](README.ipynb)


Messing around with creating interesting magnetic configurations with 3d printing and little rare earth magnets. Here is a video from my first spring/latch configuration: ![](./assets/video.gif)

## Build

## Simulation

Create a calculator that calculates the potential energy as a function of angle at different heights. Use:

$$U(\theta) = -\vec{\mu}\cdot\vec{B}$$

with

$U \textrm{potential}$$

This will be made easier by not caring about actual units (we are only looking for pole configurations at this point) and because all the magnets are the same. All the $\vec\mu$ are in the $\hat{z}$ direction and either 1 or -1. We will calculate $U(\theta)$ for each magnet with respect to each other magnet. 

$$\vec{B}(\vec{r})=\frac{\mu_0}{4\pi r^3}\big [3(\vec\mu_r\cdot\hat{r})\hat{r}-\vec\mu_r\big ]$$

$$U(r,\theta) = -\vec{\mu}\cdot\frac{\mu_0}{4\pi r^3}\big [3(\vec\mu_r\cdot\hat{r})\hat{r}-\vec\mu_r\big ] $$

3 Cases:
- Case 1: aligned N, 
- Case 2: aligned S, 
- Case 3: opposed.
