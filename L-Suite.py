import sys
import os
import time
from time import sleep

os.system('clear')

# adjust the animation speed if you want
speed = 0.1 #default = 1

ascii_art = """

                        @@                        @@@@
                   @@@@@@@@@@@@@       @@@   @@@@@@@@@@
                 @@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@
                @@@@@@@@@@@@@@@@@@@@@@@   @@@@@@
               @@@      @@@@@@@@ @@@@@   @@@@@@
               @                @@@@@   @@@@@@@
                               @@@@@@   @@@@@@@@
                              @@@@@@@   @@@@@@@@
                             @@@@@@@@   @@@@@@@@
                             @@@@@@@@   @@@@@@@@
                             @@@@@@@@   @@@@@@@@
                             @@@@@@@@   @@@@@@@@
                             @@@@@@@@   @@@@@@@@
                       @@@@@@@@@@@@@@   @@@@@@@@
                     @@@@@@@@@@@@@@@@    @@@@@@@
                         @@@@@@@@@@@@    @@@@@@@
                            @@@@@@@@@    @@@@@@@
                             @@@@@@@@    @@@@@@
                         @@@@@@@@@@@@   @@@@@@
                        @@@@@@@@@@@@@   @@@@@@
                            @@@@@@@@   @@@@@@
                             @@@@@@@   @@@@
                             @@@@@@   @@@
                             @@@@@  @@@
                             @@@@  @@     @@@@@@@@@@
                            @@@@  @@@@@@@@@@@@@@@@@@@@@@@     @
                           @@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                       @@@@@@@@               @@@@@@@@@@@@@@
                     @@@@@                         @@@@@@@
                                                      @@
"""


def print_animated(text, delay=(speed / 1000)):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()  
    time.sleep(delay)
print_animated(ascii_art)

print(f"\n Welcome to the L-Suite. Free, open source, powerful tools. You should not have paid for this software.") 
print(f"Select an application to get started: \n |[ L Redact (A)")
def acceptPrompt():
    selectedApp = input()
    if selectedApp == "A":
        import redact
        return 1
    else:
        sleep(1) #remove this line - lowk just bullshit

        print("Unrecognised command! Please enter A, B, C, D or E")
        return 0

while acceptPrompt()  != 1:
    acceptPrompt()
