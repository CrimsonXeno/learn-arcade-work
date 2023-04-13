import arcade
from arcade import draw_triangle_filled

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_colorful_elephant():

    # left ear and right ear
    arcade.draw_polygon_filled([(200, 375), (130, 430), (85, 175), (200, 175)], arcade.color.BLACK)
    arcade.draw_polygon_filled([(400, 375), (470, 430), (515, 175), (400, 175)], arcade.color.WHITE)
    arcade.draw_polygon_filled([(200, 375), (140, 400), (100, 185), (190, 185)], arcade.color.WHITE)
    arcade.draw_polygon_filled([(400, 375), (460, 400), (500, 185), (410, 185)], arcade.color.BLACK)

    # forehead
    arcade.draw_polygon_filled([(230, 400), (200, 375), (370, 400), (400, 375)], arcade.color.ORANGE)
    draw_triangle_filled(200, 375, 300, 375, 250, 300, arcade.color.YELLOW)
    draw_triangle_filled(200, 375, 170, 300, 250, 300, arcade.color.GREEN)
    draw_triangle_filled(300, 375, 250, 300, 350, 300, arcade.color.PINK)
    draw_triangle_filled(300, 375, 350, 300, 400, 375, arcade.color.VIOLET)
    draw_triangle_filled(350, 300, 400, 375, 430, 300, arcade.color.BLUE)

    # brow and eyes
    arcade.draw_polygon_filled([(170, 300), (185, 280), (415, 280), (430, 300)], arcade.color.RED)
    draw_triangle_filled(250, 300, 350, 300, 300, 225, arcade.color.PURPLE)
    arcade.draw_polygon_filled([(185, 280), (170, 260), (430, 260), (415, 280)], arcade.color.ORANGE)
    arcade.draw_circle_filled(210, 280, 10, arcade.color.SKY_BLUE)
    arcade.draw_circle_filled(390, 280, 10, arcade.color.SKY_BLUE)

    # cheeks and base trunk
    arcade.draw_polygon_filled([(170, 260), (280, 260), (300, 225), (275, 190), (155, 235)], arcade.color.VIOLET)
    arcade.draw_polygon_filled([(430, 260), (320, 260), (300, 225), (325, 190), (445, 235)], arcade.color.PINK)
    arcade.draw_polygon_filled([(263, 280), (337, 280), (355, 260), (245, 260)], arcade.color.YELLOW)
    arcade.draw_polygon_filled([(355, 260), (245, 260), (255, 190), (345, 190)], arcade.color.RED)
    arcade.draw_polygon_filled([(255, 190), (345, 190), (335, 140), (265, 140)], arcade.color.GREEN)

def draw_peanut():
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

def draw_cloud(x,y):
    arcade.draw_circle_filled(175 + x, 75 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(135 + x, 80 + y, 45, arcade.color.WHITE)
    arcade.draw_circle_filled(155 + x, 135 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(220 + x, 130 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(100 + x, 100 + y, 45, arcade.color.WHITE)
    arcade.draw_circle_filled(210 + x, 75 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(245 + x, 110 + y, 35, arcade.color.WHITE)

def draw_ground():
    #ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.DARK_GREEN)


def on_draw(delta_time):

    arcade.start_render()

    draw_ground()
    draw_cloud(-35,460)
    draw_cloud(600,370)
    draw_cloud(135,345)
    draw_cloud(500,235)
    draw_colorful_elephant()
    draw_peanut()
    draw_cloud(on_draw.cloud1_x, 400)
    draw_cloud(400, 480)

    on_draw.cloud1_x += 1


on_draw.cloud1_x = 150
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)


    arcade.schedule(on_draw, 1/60)
    arcade.run()



main()