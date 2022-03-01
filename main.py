'''Open Smart Home

Authors: Aidan Sharpe, Joe Pobega, & Tyler Salamon

Private smart home, so big tech bros ain't spyin' on you
'''

import listener
from processor import process_text
from broadcaster import *

def main():
    broadcaster = Broadcaster()
    while True:
        question = listener.look_for_prompt()
        print("prompted: " + question)
        command = process_text(question)
        broadcaster.answer(command)
        broadcaster.engine.runAndWait()
        broadcaster.stop()
        
if __name__ == '__main__':
    main()