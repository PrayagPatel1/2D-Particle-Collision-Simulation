#include <stdio.h>
#include <raylib.h>

#define WINDOW_WIDTH 900
#define WINDOW_HEIGHT 500
#define FPS 60
#define GRAVITY 120.0f

typedef struct {
	Vector2 position;
	Vector2 velocity; 
	Vector2 acceleration; 
	float radius;
}Particle;

void renderParticle(Particle *ptr_particle)
{
	DrawCircleV(ptr_particle->position, ptr_particle->radius, MAROON);
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
	if ( (ptr_particle->position.x + ptr_particle->radius) >= WINDOW_WIDTH || 
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

void handleWindowCollisionV2(Particle *ptr_particle)
{
	//This version of handling collisions between a particle and a window
	//border is going to be a continuous collision detection (CCD) compared
	//to the previous version which what a discrete collision detection (DCD).
	


}

int main(void)
{
	InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "2D Collision Particle Simulator");
	SetTargetFPS(FPS);

	float delta_time = (float) 1/FPS;

	printf("TimeStep: %f\n", delta_time);

	Particle p0 ={

		.position = {WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2},
		.velocity = {90.0f, -100.0f}, 
		.acceleration = {0.0f, GRAVITY},
		.radius = 6

	};

	// Simulation Event Loop
	while ( !WindowShouldClose() )
	{	
		BeginDrawing();

			ClearBackground(LIGHTGRAY);
			renderParticle(&p0);
			updateParticleDynamic(&p0, delta_time);
			handleWindowCollision(&p0);

		EndDrawing();
	}

	CloseWindow();

	return 0;
}
