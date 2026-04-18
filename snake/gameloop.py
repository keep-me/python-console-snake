
import time
import graphics
import game
import config
import controls

last_update = None
playing = False
state = 0
paused = False


def update():
    game.update()
    graphics.update()


def step():
    global last_update

    cur_time = time.time()

    if last_update:
        elapsed = cur_time - last_update
    else:
        elapsed = 0

    if not elapsed or elapsed > config.frame_len:

        if not elapsed:
            until_next = config.frame_len
        else:
            until_next = elapsed - config.frame_len
            time.sleep(until_next)

        update()
        last_update = time.time()
    else:
        time.sleep(0.01)


def start():
    global playing, state, paused

    playing = True

    init()
    while playing:
        controls.update()
        if state == 0 and not paused:
            step()
        elif state == 0 and paused:
            graphics.drawPaused()
            time.sleep(0.05)
        elif state == 1:
            graphics.drawGameOver()
            time.sleep(0.05)


def stop():
    global playing, frame, last_update

    playing = False


def init():
    global state, paused

    game.init()
    graphics.drawGame()
    state = 0
    paused = False


def reset():
    game.reset()
    graphics.drawGame()


def toggle_pause():
    global paused
    paused = not paused
