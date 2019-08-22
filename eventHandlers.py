import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from dimensions import *;
import random;


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, vel  # these are vectors stored as lists
    global score1, score2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        vel = [random.randrange(120, 240) / 60, -(random.randrange(60, 180) / 60)]
    else:
        vel = [-(random.randrange(120, 240) / 60), -(random.randrange(60, 180) / 60)]
        # print score1," ",score2

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = (HEIGHT - PAD_HEIGHT) / 2
    paddle2_pos = (HEIGHT - PAD_HEIGHT) / 2
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(LEFT)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # collide and reflect off of all sides of canvas
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            vel[0] = -1.1 * vel[0]
        else:
            score2 += 1
            spawn_ball(RIGHT)
    if ball_pos[0] >= (WIDTH - PAD_WIDTH) - BALL_RADIUS:
        if paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            vel[0] = -1.1 * vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        vel[1] = - vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, 20, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel

    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT],
                     PAD_WIDTH, "White")

    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 2 - 50, 50], 50, "Red")
    canvas.draw_text(str(score2), [WIDTH / 2 + 50, 50], 50, "Red")


def keydown(key):
    global paddle1_vel, paddle2_vel
    v = 5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = v
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -v
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = v
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -v


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"] or key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
