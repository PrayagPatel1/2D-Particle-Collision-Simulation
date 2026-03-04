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
		particle.velocity = (Vector2) {0.0f, 0.0f};
		particle.acceleration = (Vector2) {0.0f, 0.0f};
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
	// Uses Eulers Method to determine a new velocity and poisiton of the particle.
	ptr_particle->velocity.x += (float) ptr_particle->acceleration.x * delta_t; 
	ptr_particle->velocity.y += (float) ptr_particle->acceleration.y * delta_t;

	ptr_particle->position.x += (float) ptr_particle->velocity.x * delta_t;
	ptr_particle->position.y += (float) ptr_particle->velocity.y * delta_t;
    
	printf("Position: (%f, %f) | Velocity: (%f, %f)\n", 
			ptr_particle->position.x, 
			ptr_particle->position.y, 
			ptr_particle->velocity.x, 
			ptr_particle->velocity.y);
}

void handleWindowCollision(Particle *ptr_particle)
{
	// NOTE: This method of checking collisions and resolving collisions is 
	//		 discrete meaning that at each iteration the simulation checks
	//		 the collisions onece every frame and continuously. 
	
	// Handles when the particle is going beyond the left and right borders. 
	if ((ptr_particle->position.x + ptr_particle->radius) >= WINDOW_WIDTH || 
			(ptr_particle->position.x - ptr_particle->radius) <= 0) 
	{
		ptr_particle->velocity.x *= -1;
	}
	
	// Handles when the particle is going beyond the top and bottom borders.
	if ( (ptr_particle->position.y + ptr_particle->radius) >= WINDOW_HEIGHT || 
			(ptr_particle->position.y - ptr_particle->radius) <= 0)
	{
		ptr_particle->velocity.y *= -1;
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

		EndDrawing();
	}

	CloseWindow();

	return 0;
}
