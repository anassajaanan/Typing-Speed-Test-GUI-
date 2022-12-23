# Typing Speed Test GUI

This is a simple Python program that creates a GUI for testing and improving typing speed. When run, the program displays a window with a background image and a sentence. The user can then type the sentence into the text entry box and click the "START" button to begin the test.

While the test is running, the program continuously tracks the number of words typed and the time elapsed. It then uses this information to compute the user's words per minute (WPM) speed, which is displayed on the window. The test ends when the user has typed the entire sentence or when the number of words typed is greater than or equal to the number of words in the original sentence.

## Requirements

- Python 3
- Tkinter library
- PIL library (for handling images)

## Running the Program

To run the program, simply run the `typing_speed_test.py` script using Python 3:
```bash
python3 typing_speed_test.py
```

## Customizing the Program

The program can be easily customized by modifying the following variables in the script:

- `sentence`: the sentence displayed on the window. This can be modified by changing the text in the `canvas.create_text()` method.
- `img`: the background image displayed on the window. This can be modified by replacing the file `"images/background.png"` with a different image file.

## Features

- Simple and intuitive interface
- Accurate words per minute (WPM) calculation
- Customizable sentence and background image

