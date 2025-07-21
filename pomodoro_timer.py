

import time

def pomodoro_timer(work_minutes, break_minutes, cycles):
    print("Welcome to the Pomodoro Timer!")
    for i in range(cycles):
        print(f"\n--- Cycle {i+1}/{cycles} ---")
        print(f"Work for {work_minutes} minutes...")
        time.sleep(work_minutes * 60)
        print("Work time finished!")

        if i < cycles - 1:
            print(f"Take a {break_minutes} minute break...")
            time.sleep(break_minutes * 60)
            print("Break time finished!")
    print("\nPomodoro session complete!")

if __name__ == "__main__":
    try:
        work = int(input("Enter work duration in minutes: "))
        break_time = int(input("Enter break duration in minutes: "))
        num_cycles = int(input("Enter number of Pomodoro cycles: "))
        pomodoro_timer(work, break_time, num_cycles)
    except ValueError:
        print("Invalid input. Please enter whole numbers for durations and cycles.")

