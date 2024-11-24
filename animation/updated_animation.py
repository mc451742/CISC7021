"""
CISC7021 Applied Natural Language Processing
main animation
Title: Harnessing Analogical Reasoning for Empathy: A Unified Framework for Enhancing Large Language Model
Analogy Ability in Tiny LLM
Simple Conversation Animation
Chat Bot <-> Human User
Updated Animation (Final Version)
Author: Yumu Xie
Credit:
Bot logo comes from: https://es.vecteezy.com/arte-vectorial/10927083-icono-de-chatbot-sobre-fondo-blanco-signo-de-bot-de-servicio-de-soporte-en-linea-signo-de-bot-de-chat-para-el-concepto-de-servicio-de-soporte-estilo-plano
User logo comes from: https://es.vecteezy.com/vectores-gratis/user-icon
"""
# disable the pygame mixer to prevent ALSA-related errors
import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

# load packages
import pygame
# import time
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

# global variable
# TMP = False

# main function
def animation():
    # initialize pygame
    pygame.init()

    # screen settings
    screen_width, screen_height = 1200, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Harnessing Analogical Reasoning for Empathy: A Unified Framework for Enhancing Large Language Model")

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    # BLUE = (0, 128, 255)
    # GREEN = (0, 255, 128)

    # load images
    bot_image = pygame.image.load("./image/bot.jpg")
    user_image = pygame.image.load("./image/user.jpg")

    # resize images to fit the UI
    bot_image = pygame.transform.scale(bot_image, (100, 100))
    user_image = pygame.transform.scale(user_image, (100, 100))

    # font
    font = pygame.font.Font(None, 48)

    # messages
    messages = [
        ("N/A", "N/A"), # empty sentence to display title
        ("User", "Consider the following story: Story 1: ......"),
        ("User", "Now consider two more stories: Story A: ...... Story B: ......"),
        ("User", "Which of Story A and Story B is a better analogy to Story 1? Is the best answer Story A, Story B, or both are equally analogous?"),
        ("Bot", "Story A/B is a better analogy to Story 1 (answer), let analysis (explain the reason)......"),
    ]

    # list to store all displayed messages
    # displayed_messages = []

    # function to draw title
    def draw_title(x, y):
        text = font.render("Zero-shot Prompting Example", True, BLACK)
        screen.blit(text, (x, y))

    # function to draw a message
    # def draw_message(role, message, y):
    #     if role == "Bot":
    #         image = bot_image
    #     else: # role == "User"
    #         image = user_image
    #     # draw image and text
    #     x_text = 80
    #     screen.blit(image, (20, y))
    #     text = font.render(f"{message}", True, WHITE)
    #     screen.blit(text, (x_text, y + 10)) # offset for better alignment

    # function to draw a message
    def draw_message(role, message, y, max_width=950):
        # for role, message in displayed_messages:
        if role == "Bot":
            image = bot_image
        else: # role == "User"
            image = user_image
        # draw the role's image
        screen.blit(image, (20, y))
        # split the message into multiple lines if it exceeds max_width
        words = message.split()
        lines = []
        line = ""
        for word in words:
            test_line = f"{line} {word}".strip()
            if font.size(test_line)[0] <= max_width: # check width of the line
                line = test_line
            else:
                lines.append(line) # add the current line to lines
                line = word # start a new line with the current word
        lines.append(line) # add the last line
        # draw each line below the image
        x_text = 160
        for i, line in enumerate(lines):
            text = font.render(line, True, BLACK)
            screen.blit(text, (x_text, y + 10 + i * 30)) # 30 is line spacing
            # if TMP == True:
            #     screen.blit(text, (x_text, y + 10 + i * 30)) # 30 is line spacing
            # else:
            #     screen.blit(text, (x_text, y + 20 + i * 30)) # 30 is line spacing

    # frame storage
    frames = []

    # animation parameters
    running = True
    message_index = 0
    # y_position = 120
    fps = 120
    frame_delay = fps # number of frames to pause for each message

    # list to store all displayed messages
    displayed_messages = []

    # initialize the background
    # background color
    screen.fill(WHITE)

    # animation loop
    while running:
        # check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # display title when animation starts
        if message_index == 0:
            draw_title(350, 400)
            # add extra frames to extend the display duration for title
            for _ in range(fps * 2):
                frames.append(pygame.surfarray.array3d(screen))
            # clear title
            # background color
            screen.fill(WHITE)
            message_index += 1

        # display the current message and add it to the list
        if message_index < len(messages) and frame_delay > 0: # message_index != 0
            # if message_index == 3:
            #     TMP = True
            # else:
            #     TMP = False

            role, msg = messages[message_index]
            if frame_delay == fps: # only add to displayed_messages once
                displayed_messages.append((role, msg))
            
            frame_delay -= 1

            if frame_delay <= 0:
                message_index += 1
                # add extra frames to extend the display duration for each message
                for _ in range(fps * 2):
                    frames.append(pygame.surfarray.array3d(screen))
                frame_delay = fps

            # draw all displayed messages
            y_position = 120
            for role, msg in displayed_messages:
                draw_message(role, msg, y_position)
                y_position += 160
            
        else:
            # stop animation
            running = False

        # capture frame
        frames.append(pygame.surfarray.array3d(screen))

        # update the entire display surface to the screen
        pygame.display.flip()

    # save the video
    clip = ImageSequenceClip([frame.transpose(1, 0, 2) for frame in frames], fps=fps)
    clip.write_videofile("updated_animation.mp4", codec="libx264")

    # quit pygame
    pygame.quit()

if __name__ == "__main__":
    animation()
