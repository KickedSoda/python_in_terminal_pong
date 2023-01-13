from pynput import keyboard
from screen import screen
from threading import Thread
class KeyboardListener:
    def on_press(key):
        try:
            #print('alphanumeric key {0} pressed'.format(key.char))
            if key.char == 'w' and screen.player_1_y > 2:
                screen.player_1_y -= 1
            if key.char == 's' and screen.player_1_y < screen.screen_y - 3:
                screen.player_1_y += 1

            
        except AttributeError:
            #print('special key {0} pressed'.format(key))
            if str(key) == "Key.up" and screen.player_2_y > 2:
                screen.player_2_y -= 1
            if str(key) == "Key.down" and screen.player_2_y < screen.screen_y - 3:
                screen.player_2_y += 1
            

    def on_release(key):
        #print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

screen = screen(73, 31)
screen_thread = Thread(target=screen.start, daemon=True)
screen_thread.start()

with keyboard.Listener(on_press=KeyboardListener.on_press,on_release=KeyboardListener.on_release) as listener:
    listener.join()

