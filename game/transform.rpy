# Game

transform letterbox:
    # centered above the bottom text
    xanchor 0.5
    xpos 0.5
    yanchor 0.5
    ypos 0.4

transform inside_letterbox(x, y):
    # from letterbox center (support only pixel coords)
    xanchor 0.5
    yanchor 0.5
    xpos int(config.screen_width * 0.5) + int(x)
    ypos int(config.screen_height * 0.4) + int(y)
