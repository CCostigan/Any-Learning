import pygame

pygame.init()
# Create a tiny window to capture keyboard focus
screen = pygame.display.set_mode((100, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)} {event.dict}")
            if 'unicode' in event.dict.keys() and event.dict['unicode'] == 'q':
               running=False
done = False
while not done:
  pressed = pygame.key.get_pressed()
  # print(f"{pressed[pygame.K_BREAK]} {pressed}")
  # if pressed[pygame.K_LEFT]:
  #   done=True
  if pressed[pygame.key.key_code("w")]:
    print("Moving forward!")
    done=True

pygame.quit()


