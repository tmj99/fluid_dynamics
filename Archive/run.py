import pygame

def running(blob_loc_list):

    pygame.init()
    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])

    running = True

    screen.fill((0, 0, 0))

    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        for i in blob_loc_list:
            for j in i.location:
                x,y = j
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)

        # Flip the display
        pygame.display.flip()

    pygame.quit()