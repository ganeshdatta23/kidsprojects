import time

def countdown_timer():
    try:
        minutes = int(input("Enter the number of minutes for the countdown: "))
        seconds = minutes * 60
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    countdown_timer()
