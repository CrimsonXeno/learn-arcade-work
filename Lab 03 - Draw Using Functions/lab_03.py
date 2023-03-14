import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with functions")
arcade.set_background_color(arcade.color.DARK_BLUE)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.DARK_GREEN)

arcade.finish_render()
arcade.run()