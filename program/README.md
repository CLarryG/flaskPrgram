# Time Perception Measurement Application

## Overview

This project consists of two components:
1. `timeguess.py`: A command-line application that measures the user's perception of time.
2. `app.py`: A Flask web application that visualizes the average error in time perception based on data collected by `timeguess.py`.

## timeguess.py

### Description

`timeguess.py` is a command-line application that tests the user's ability to perceive time accurately. It generates a random time between 1 and 10 seconds, asks the user to start and stop a timer, and records the actual and guessed times in a file called `data.txt`.

### Usage

1. Ensure you have Python installed on your machine.
2. Save the `timeguess.py` script in your working directory.
3. Run the script using the command:

    ```sh
    python timeguess.py
    ```

4. Follow the on-screen prompts to start and stop the timer.
5. The script will save the actual and guessed times in `data.txt`.

### Code Structure

- `get_user_input(prompt)`: Prompts the user with the given message and waits for input.
- `main()`: Main function that handles the time perception test and records the results.

## app.py

### Description

`app.py` is a Flask web application that reads data from `data.txt`, calculates the average error for each target time between 1 and 10 seconds, generates a bar plot using Matplotlib, and displays the plot on a webpage.

### Setup and Usage

1. Ensure you have Python and the necessary packages installed. You can install the required packages using:

    ```sh
    pip install flask matplotlib
    ```

2. Save the `app.py` script in your working directory.
3. Create a `static` directory in the same location to store the generated plot.
4. Run the Flask application using the command:

    ```sh
    python app.py
    ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the plot.

### Code Structure

- `show_error_plot()`: Handles the root endpoint, reads data from `data.txt`, calculates average errors, creates a bar plot, saves it as `static/error.png` ("static/" refers to the folder that the error plot is kept in before it was used the updated image wouldn't be shown on  the webpage), and renders an HTML template to display the plot.

## data.txt

The `data.txt` file stores the results of each run of `timeguess.py`. Each line contains the actual time and the user's guessed time, separated by a space. The format is:
<actual_time> <guessed_time>
#Example
5 5.23 
3 2.98 
7 6.75


## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE below for details.
The MIT License (MIT)

Copyright © 2024 <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgements

- Flask documentation: https://flask.palletsprojects.com/
- Matplotlib documentation: https://matplotlib.org/stable/contents.html
