import turtle as tt
import random

x_apple = random.randrange(-24, 24) * 10
y_apple = random.randrange(-23, 24) * 10
eat_sym = 10


class HungrySnake:
    # 蛇的初始运动矢量
    x_add = 10
    y_add = 0
    # 蛇的初始状态, 用坐标表示
    snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]

    # 以蛇的坐标为顶点画方块
    def draw_snake(self):
        for each in self.snake:
            square_spot(each[0], each[1], 10, 'black')

    # 运动方式: pop队首, append队尾
    def move_a_step(self):
        self.snake.pop(0)
        self.snake.append([self.snake[-1][0] + self.x_add, self.snake[-1][1] + self.y_add])

    # 改变运动方向矢量方法, 用于后面响应按键
    def change_direction(self, x_lab, y_lab):
        HungrySnake.x_add = x_lab
        HungrySnake.y_add = y_lab

    def is_crash(self):
        # 判断是否撞墙
        if \
                self.snake[-1][0] <= -250 or self.snake[-1][0] >= 240 or self.snake[-1][1] <= -240 or self.snake[-1][
                    1] >= 260:
            return True
        # 判断是否撞身体
        elif self.snake[-1] in self.snake[:-1]:
            return True
        else:
            False

    # 吃到苹果, 在append
    def eat_apple(self):
        self.snake.append(self.snake[-1])

def square_spot(x, y, width, color):
    tt.up()
    tt.goto(x, y)
    tt.down()
    tt.color(color)  # 设定填充颜色
    tt.begin_fill()  # 申明开始填充
    # 开始画图
    tt.forward(width)
    tt.right(90)
    tt.forward(width)
    tt.right(90)
    tt.forward(width)
    tt.right(90)
    tt.forward(width)
    tt.right(90)
    tt.end_fill()  # 申明填充结束
    tt.up()


def show_apple():
    global x_apple, y_apple
    if HungrySnake().snake[-1] == [x_apple,y_apple]:
        x_apple = random.randrange(-24, 24) * 10
        y_apple = random.randrange(-23, 24) * 10
        HungrySnake().eat_apple()
    else:
        square_spot(x_apple, y_apple, 10, 'red')
    #print('apple: %s' % [x_apple,y_apple])


def game_loop():
    tt.clear()
    show_apple()
    HungrySnake().draw_snake()
    HungrySnake().move_a_step()
    #print('snake: %s' % HungrySnake().snake)
    #print('speed: %s' % [HungrySnake().x_add, HungrySnake().y_add])
    #print('Crash: %s' % HungrySnake().is_crash())
    if not HungrySnake().is_crash():
        tt.ontimer(game_loop, 100)
    else:
        square_spot(HungrySnake().snake[-1][0], HungrySnake().snake[-1][1], 10, 'red')
        tt.done()


tt.setup(500, 500)

tt.hideturtle()
tt.tracer(False)
tt.listen()

tt.onkey(lambda: HungrySnake().change_direction(-10, 0), 'Left')
tt.onkey(lambda: HungrySnake().change_direction(10, 0), 'Right')
tt.onkey(lambda: HungrySnake().change_direction(0, 10), 'Up')  # 不加lambda, 后面的对象类型是None. 加lambda之后才是函数
tt.onkey(lambda: HungrySnake().change_direction(0, -10), 'Down')

game_loop()
tt.done()
