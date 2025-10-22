from network.client.client import NetworkClient

HOST = '127.0.0.1'
PORT = 5000

if __name__=="__main__":
    client = NetworkClient(HOST, PORT)
    client.connect(delay = 1)

    print("Running main entry function")

    if client.is_connected():
        print("Connected to server!")
        try:
            client.send_command()

            while(client.is_connected()):
                data = client.receive_JSON()
                if data is None:
                    print("No data, conneciton may be closed.")
                    break

                print("Received data: ", data)

        except Exception as e:
            print(f"Exception occurred: {e}")
    else:
        print("Server disconnected! Exiting")

# import pygame

# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720)) # set screen size???
# clock = pygame.time.Clock()
# running = True

# HOST = '127.0.0.1'
# PORT = 5000

# while running:
#     # poll for events
#     # pygame.QUIT event means the user exited with X
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     ## set bckground
#     screen.fill("purple")

#     ## TODO make something happen
#     pygame.draw.rect(screen, "red", pygame.Rect(0, 0, 50, 50))

#     # flip() the display to put work on screen????
#     pygame.display.flip()

#     clock.tick(60) # limits FPS to 60


# pygame.quit()