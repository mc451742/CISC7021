"""
CISC7021 Applied Natural Language Processing
main animation
Title: Emergent Analogy Reasoning in Tiny LLM
Analogy Ability in Tiny LLM
Simple Conversation Animation
Chat Bot <-> Human User
Author: Yumu Xie
Credit:
Bot logo comes from: https://es.vecteezy.com/arte-vectorial/10927083-icono-de-chatbot-sobre-fondo-blanco-signo-de-bot-de-servicio-de-soporte-en-linea-signo-de-bot-de-chat-para-el-concepto-de-servicio-de-soporte-estilo-plano
User logo comes from: https://es.vecteezy.com/vectores-gratis/user-icon
"""

import pygame
# import time
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

# main function
def animation():
    # initialize pygame
    pygame.init()

    # screen settings
    screen_width, screen_height = 1200, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Emergent Analogy Reasoning in Tiny LLM")

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    # BLUE = (0, 128, 255)
    # GREEN = (0, 255, 128)

    # load images
    bot_image = pygame.image.load("./image/bot.jpg")
    user_image = pygame.image.load("./image/user.jpg")

    # resize images to fit the UI
    bot_image = pygame.transform.scale(bot_image, (50, 50))
    user_image = pygame.transform.scale(user_image, (50, 50))

    # font
    font = pygame.font.Font(None, 36)

    # messages
    messages = [
        ("N/A", "N/A"),
        ("User", "Consider the following story: Story 1: ......"),
        ("User", "Now consider two more stories: Story A: ...... Story B: ......"),
        ("User", "Which of Story A and Story B is a better analogy to Story 1?"),
        ("User", "Is the best answer Story A, Story B, or both are equally analogous?"),
        ("Bot", "Story A is a better analogy to Story 1 because Story A is more realistic."),
        ("Bot", "......"),
    ]

    # function to draw title
    def draw_title(x, y):
        text = font.render("Emergent Analogy Reasoning in Tiny LLM: Zero-shot Prompting Example", True, WHITE)
        screen.blit(text, (x, y))

    # function to draw a message
    def draw_message(role, message, y):
        if role == "Bot":
            image = bot_image
        else: # role == "User"
            image = user_image
        # draw image and text
        x_text = 80
        screen.blit(image, (20, y))
        text = font.render(f"{message}", True, WHITE)
        screen.blit(text, (x_text, y + 10)) # offset for better alignment

    # frame storage
    frames = []

    # animation parameters
    running = True
    message_index = 0
    y_position = 40
    fps = 120
    frame_delay = fps # number of frames to pause for each message

    # animation loop
    while running:

        # quit animation if key is pressed
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False

        # background color
        screen.fill(BLACK)

        # display title when animation starts
        if message_index == 0:
            # display title
            draw_title(160, 400)
            # time.sleep(1)
            # add extra frames to extend the display duration for title
            for _ in range(fps * 2):
                frames.append(pygame.surfarray.array3d(screen))
            message_index += 1

        # main loop to display messages
        if message_index < len(messages) and message_index != 0:
            role, msg = messages[message_index]
            draw_message(role, msg, y_position)
            frame_delay -= 1
            if frame_delay <= 0:
                y_position += 120
                message_index += 1
                # add extra frames to extend the display duration for each message
                for _ in range(fps * 2):
                    frames.append(pygame.surfarray.array3d(screen))
                # reset frame delay
                frame_delay = fps
        else:
            running = False

        # capture frame
        frames.append(pygame.surfarray.array3d(screen))

        # update the entire display surface to the screen
        pygame.display.flip()

    # save the video
    clip = ImageSequenceClip([frame.transpose(1, 0, 2) for frame in frames], fps=fps)
    clip.write_videofile("main_animation.mp4", codec="libx264")

    # quit pygame
    pygame.quit()

if __name__ == "__main__":
    animation()
