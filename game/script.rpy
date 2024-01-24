# The script of the game goes in this file.

init python:
    import pygame
    import math

    renpy.add_layer("background", above="master")
    renpy.add_layer("props", above="background")
    renpy.add_layer("propMods", above="props")
    renpy.add_layer("spriteLayer", above="propMods")
    renpy.add_layer("cokeLayer", above="spriteLayer")
    renpy.add_layer("windowFrame", above="cokeLayer")

    def parelaxing(trans, st, at):
        x, y = renpy.display.draw.get_mouse_pos()
        trans.xoffset = (x - config.screen_width / 2) * .05
        trans.yoffset = (y - config.screen_height / 2) * .05
        return 0


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define timp = Character("Timpbus")
define billNye = Character("The Scientist")
define e = Character("Eileen")

image BGroom = "BGroom.png"
image FGhands = "FGhands.png"
image FGnoHands = "FGnoHands.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene BGroom onlayer background

    transform parallax:
        perspective True
        subpixel True
        function parelaxing
    
    transform BGroom:
        truecenter()
        zzoom true
        zpos -1000
    
    camera background at parallax

    show FGnoHands onlayer windowFrame

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    hide FGnoHands
    show FGhands onlayer windowFrame

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
