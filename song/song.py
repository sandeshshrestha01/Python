import sys
from time import sleep

def song():
    lines = [
        ("Ohh, mero baalakaal dekhiko milne saati", 0.1),
        ("Haamro Mitrataa aru sambandha bhanda maathi", 0.1),
        ("Hami sahar ghumna janthiyou rati rati bhagi bhagi", 0.1),
        ("Ghar ma aama buwa lai dhati", 0.1),
        ("Marna ra maarna thyaar ek arkaa ko lagi", 0.1),
        ("Sadhai sangai basthyou school padha Hami ", 0.1),
        ("Dubai Na jaane yedi euta birami", 0.1),
        ("Je pani baadne haamro ramro thiyo baani", 0.1),
    ]
    delays = [0.01 , 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')  # Print each character
            sys.stdout.flush()  # Ensure real-time display
            sleep(char_delay)   # Delay for each character
        print()  # Move to the next line
        if i < len(delays):  # Add delay between lines if applicable
            sleep(delays[i])

song()
