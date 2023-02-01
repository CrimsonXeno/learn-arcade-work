import arcade
arcade.open_window(600, 600, "My Drawing Lab")
arcade.set_background_color((107,71,13))
arcade.start_render()

arcade.draw_polygon_filled([(230,400),(200,375),(370,400),(400,375)],arcade.color.CYAN)
arcade.draw_triangle_filled(200,375,300,375,250,300,arcade.color.YELLOW)
arcade.draw_triangle_filled(200,375,170,300,250,300,arcade.color.GREEN)
arcade.draw_triangle_filled(300,375,250,300,350,300,arcade.color.PINK)
arcade.
arcade.draw_triangle_

arcade.finish_render()
arcade.run()
