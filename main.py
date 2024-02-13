from utils.program1 import word_frequency
from utils.program2 import Shape, Square
import threading


def main():
    # Read input from file
    with open('subfolder/input.txt', 'r') as file:
        input_text = file.read()

    # Program 1
    thread1 = threading.Thread(target=word_frequency, args=(input_text,))

    # Program 2
    square = Square(16)
    shape = Shape()

    thread2 = threading.Thread(target=square.area)
    thread3 = threading.Thread(target=shape.area)

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to finish
    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    main()
