# PracticeProject.py

# Code to practice using Git

def main():
    """Calculate the nth Fibonacci number"""
    # 1, 1, 2, 3, 5, 8, 13, 21, 34...

    # Ask users for which fib number they want
    n = int(input("Which fib number do you want "))

    # start at n = 1 -> 1
    # start at n = 2 -> 2

    if n == 1 or n == 2:
        print(f"The {n}st/nd fibonacci number is 1")


if __name__ == "__main__":
    main()
