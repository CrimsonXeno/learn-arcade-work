import arcade
arcade.open_window(600, 600, "My Drawing")
arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
arcade.set_background_color((52, 198, 235))
arcade.start_render()

# between here
#type arcade.draw ... see what tools are in the box

#ugly bus!
arcade.draw_polygon_filled([(25,345),(50,400),(350,400),(375,345)],arcade.color.BLUE)
arcade.draw_rectangle_filled(200,320,350,50,arcade.color.GREEN)
arcade.draw_ellipse_filled(100,300,50,50,arcade.color.BLACK)
arcade.draw_ellipse_filled(300,300,50,50,arcade.color.BLACK)

# and draw here be creative

arcade.finish_render()
arcade.run()