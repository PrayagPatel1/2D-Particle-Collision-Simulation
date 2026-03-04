#include <stdio.h>
#include <stdlib.h>
#include <raylib.h>

#define WINDOW_WIDTH 900
#define WINDOW_HEIGHT 500
#define FPS 60
#define GRAVITY 120.0f
#define NUM_OF_PARTICLES 3

typedef struct {
	Vector2 position;
	Vector2 velocity; 
	Vector2 acceleration; 
	float radius;
}Particle;


void initializeParticles(Particle *ptr_p)
{
	for (size_t idx = 0; idx < NUM_OF_PARTICLES; idx++)
	{
		Particle particle;
		particle.position = (Vector2) {WINDOW_WIDTH/2 + idx * 50, WINDOW_HEIGHT/2 + idx * 50};
		particle.velocity = (Vector2) {5.0f, 5.0f};
		particle.acceleration = (Vector2) {0.0f, GRAVITY};
		particle.radius = 5.0f;

		ptr_p[idx] = particle;
	}

}

void renderParticles(Particle *ptr_p)
{
	for(size_t idx = 0; idx < NUM_OF_PARTICLES; idx ++)
	{
		DrawCircleV(ptr_p[idx].position, ptr_p[idx].radius, BLACK);
	}

}

void updateParticleDynamic(Particle *ptr_particle, float delta_t)
{
	for(size_t idx = 0; idx < NUM_OF_PARTICLES; idx ++)
	{

		// Uses Eulers Method to determine a new velocity and poisiton of the particle.
		ptr_particle[idx].velocity.x += (float) ptr_particle[idx].acceleration.x * delta_t; 
		ptr_particle[idx].velocity.y += (float) ptr_particle[idx].acceleration.y * delta_t;

		ptr_particle[idx].position.x += (float) ptr_particle[idx].velocity.x * delta_t;
		ptr_particle[idx].position.y += (float) ptr_particle[idx].velocity.y * delta_t;
	}
}

void handleWindowCollision(Particle *ptr_particle)
{
	// NOTE: This method of checking collisions and resolving collisions is 
	//		 discrete meaning that at each iteration the simulation checks
	//		 the collisions onece every frame and continuously. 
	
	for(size_t idx = 0; idx < NUM_OF_PARTICLES; idx ++)
	{

		// Handles when the particle is going beyond the left and right borders. 
		if ((ptr_particle[idx].position.x + ptr_particle[idx].radius) >= WINDOW_WIDTH || 
				(ptr_particle[idx].position.x - ptr_particle[idx].radius) <= 0) 
		{
			ptr_particle[idx].velocity.x *= -1;
		}
	
		// Handles when the particle is going beyond the top and bottom borders.
		if ( (ptr_particle[idx].position.y + ptr_particle[idx].radius) >= WINDOW_HEIGHT || 
				(ptr_particle[idx].position.y - ptr_particle[idx].radius) <= 0)
		{
			ptr_particle[idx].velocity.y *= -1;
		}
	}

}

int main(void)
{
	InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "2D Collision Particle Simulator");
	SetTargetFPS(FPS);

	float delta_time = (float) 1/FPS;

	Particle particles[NUM_OF_PARTICLES]; 
	initializeParticles(particles);

	// Simulation Event Loop
	while ( !WindowShouldClose() )
	{	
		BeginDrawing();

			ClearBackground(LIGHTGRAY);
			renderParticles(particles);
			updateParticleDynamic(particles, delta_time);
			handleWindowCollision(particles);

		EndDrawing();
	}

	CloseWindow();

	return 0;
}
