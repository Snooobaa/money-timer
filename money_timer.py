import time
import os
    
def money_timer():
    os.system('cls' if os.name == 'nt' else 'clear')
    hourly_rate = float(input('Enter your hourly rate: '))
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Starting timer in 3 seconds...')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Starting timer in 2 seconds...')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Starting timer in 1 second...')
    time.sleep(1)
    earnt_so_far = 0.0
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # checks if the operating system is windows or not and clears the screen accordingly
        earnt_so_far += (hourly_rate / 60) / 60 / 10 # calculates the amount of money earnt in a tenth of a second and assigns it to the variable earnt_so_far
        print(f'${earnt_so_far:.3f}') # prints earnt_so_far to 3 decimal places
        time.sleep(0.1) # waits for a tenth of a second then loops again


money_timer()