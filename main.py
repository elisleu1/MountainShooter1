import pygame

pygame.init()  # Starts pygame
window = pygame.display.set_mode(size=(600, 480))  # Create window run

while True: # Loop that's maintain window run
# Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # Close window
            quit()  # End pygame