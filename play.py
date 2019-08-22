from eventHandlers import *;


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)
frame.add_label("")
frame.add_label("")
frame.add_label("Instructions :")
frame.add_label("")
frame.add_label("Player 1 :")
frame.add_label("Paddle up: w")
frame.add_label("Paddle down: s")
frame.add_label("")
frame.add_label("Player 2 :")
frame.add_label("Paddle up: up arrow")
frame.add_label("Paddle down: down arrow")

# start frame
new_game()
frame.start()
