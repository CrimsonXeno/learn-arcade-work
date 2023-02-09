import arcade
from arcade import draw_triangle_filled

arcade.open_window(600, 600, "My Drawing Lab")
arcade.set_background_color((5,234,250))
arcade.start_render()

#left ear and right ear
arcade.draw_polygon_filled([(200,375),(130,430),(85,175),(200,175)],arcade.color.BLACK)
arcade.draw_polygon_filled([(400,375),(470,430),(515,175),(400,175)],arcade.color.WHITE)
arcade.draw_polygon_filled([(200,375),(140,400),(100,185),(190,185)],arcade.color.WHITE)
arcade.draw_polygon_filled([(400,375),(460,400),(500,185),(410,185)],arcade.color.BLACK)

#forehead
arcade.draw_polygon_filled([(230,400),(200,375),(370,400),(400,375)],arcade.color.ORANGE)
draw_triangle_filled(200,375,300,375,250,300,arcade.color.YELLOW)
draw_triangle_filled(200,375,170,300,250,300,arcade.color.GREEN)
draw_triangle_filled(300,375,250,300,350,300,arcade.color.PINK)
draw_triangle_filled(300,375,350,300,400,375,arcade.color.VIOLET)
draw_triangle_filled(350,300,400,375,430,300,arcade.color.BLUE)

#brow and eyes
arcade.draw_polygon_filled([(170,300),(185,280),(415,280),(430,300)],arcade.color.RED)
draw_triangle_filled(250,300,350,300,300,225,arcade.color.PURPLE)
arcade.draw_polygon_filled([(185,280),(170,260),(430,260),(415,280)],arcade.color.ORANGE)
arcade.draw_circle_filled(210,280,10,arcade.color.SKY_BLUE)
arcade.draw_circle_filled(390,280,10,arcade.color.SKY_BLUE)

#cheeks and base trunk
arcade.draw_polygon_filled([(170,260),(280,260),(300,225),(275,190),(155,235)],arcade.color.VIOLET)
arcade.draw_polygon_filled([(430,260),(320,260),(300,225),(325,190),(445,235)],arcade.color.PINK)
arcade.draw_polygon_filled([(263,280),(337,280),(355,260),(245,260)],arcade.color.YELLOW)
arcade.draw_polygon_filled([(355,260),(245,260),(255,190),(345,190)],arcade.color.RED)
arcade.draw_polygon_filled([(255,190),(345,190),(335,140),(265,140)],arcade.color.GREEN)

arcade.finish_render()
arcade.run()
