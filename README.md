# Simple 2D Particle Collision Simulation

The purpose of this project is to create a 2d particle simulation, that simulates collisions between a particle and the window boundary, and 
collisions between a particle and another particle. This project is written in C23 using raylib as a graphical interface to see the particle
interacting with the world and each other. 

## Simulation Parameters

Window Size: 900 x 500 
Target FPS: 60 
Fixed Time Step: 1 / 60 seconds 
Integration Method: Semi-Implicit Euler 

## Inital Assumptions

One assumption about the system that is being simulated is that the collisions between a particle and a window border is perfectly elastic. A perfectly elastic collisions would ensure that the momentum and kinetic energy of the particle is conserved. The same assumption will apply between particle-particle collisions, once that gets implemented. 

## Integration Method: Semi-Implicit Euler

The way that a particle is getting updated in terms of their dynamics is through Euler's Integration where the velocity of the next frame in the simulation will be determined by the particles previous velocity plus the product between the time step and the acceleration of the particle. The same goes fordetermineing the position of the particle in the next frame by using the previous position of the particle plus the product between the time step and the particles previous velocity. This method basically, integrates the acceleration of the particle until you get the velocity and position of the particel and add that value to the new position and velocity. 

## Discrete Collision Detection

The collision detection system is currently implemented between one particle and the window borders. The collision detection method that was used is called discrete collision detection, where the simulation will check whether or not the boundary of a particle intersects or goes beyond the window borders, once every frame. The collision resoulution would to simply invert the direction of the particles velocity vector, so that the particle can bounce of the borders. Using this collision system is easy, but once the initial velocity increases, the particle will move faster and faster to the point where it will fall out of the simulation. This is called tunnelling and can be resolved by creating a speed constraint in the simulation, add more frames to the animation for a smaller and more accurate time step, or implement a continuous collision detection (CCD) system. 
