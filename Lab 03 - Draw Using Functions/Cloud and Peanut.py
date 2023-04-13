import arcade

arcade.open_window(600, 600, "Cloud and peanut")
arcade.set_background_color((5,234,250))
arcade.start_render()

#cloud
arcade.draw_circle_filled(175,75,40,arcade.color.WHITE)
arcade.draw_circle_filled(135,80,45,arcade.color.WHITE)
arcade.draw_circle_filled(155,135,40,arcade.color.WHITE)
arcade.draw_circle_filled(220,130,40,arcade.color.WHITE)
arcade.draw_circle_filled(100,100,45,arcade.color.WHITE)
arcade.draw_circle_filled(210,75,40,arcade.color.WHITE)
arcade.draw_circle_filled(245,110,35,arcade.color.WHITE)

#PEANUT
arcade.draw_circle_filled(375,200,45,arcade.color.DARK_TAN)
arcade.draw_circle_filled(375,265,45,arcade.color.DARK_TAN)
arcade.draw_line(375,155,375,310,arcade.color.BLACK)
arcade.draw_line(345,168,345,298,arcade.color.BLACK)
arcade.draw_line(405,168,405,298,arcade.color.BLACK)
arcade.draw_line(330,200,420,200,arcade.color.BLACK)
arcade.draw_line(330,265,420,265,arcade.color.BLACK)
arcade.draw_line(335,180,415,180,arcade.color.BLACK)
arcade.draw_line(335,220,415,220,arcade.color.BLACK)
arcade.draw_line(335,245,415,245,arcade.color.BLACK)
arcade.draw_line(335,285,415,285,arcade.color.BLACK)

arcade.finish_render()
arcade.run()

