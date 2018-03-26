init python:
    def show_sprite(image, x, y):
        """Show sprite at (x, y) inside letter box, on screens layer"""
        renpy.show(image, [inside_letterbox(x,y)], layer="screens")

    config.intra_transition = dissolve

label start:
    show screen _image_load_log

    jump s01
    return
