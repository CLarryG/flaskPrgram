import os
from flask import Flask, send_file, render_template_string
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def show_error_plot():
    """ This function handles the root endpoint '/' of the Flask application. It reads the time perception data from 'data.txt', calculates the average error for each target time between 1 and 10 seconds, creates a bar plot using Matplotlib, saves the plot as 'error.png' in the 'static' directory, and renders an HTML template to display the plot on a webpage. Returns: A rendered HTML template displaying the time perception error plot. """
    # Read data from file
    times = []
    guesses = []
    if os.path.exists('data.txt'):
        with open('data.txt', 'r') as file:
            for line in file:
                actual, guess = line.split()
                times.append(int(actual))
                guesses.append(float(guess))
    
    # Calculate average errors for each time between 1 and 10
    actual_times = range(1, 11)
    avg_errors = []
    for t in actual_times:
        errors = [abs(t - guess) for actual, guess in zip(times, guesses) if actual == t]
        avg_errors.append(np.mean(errors) if errors else 0)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.bar(actual_times, avg_errors, color='skyblue')
    plt.xlabel('Actual Time (seconds)')
    plt.ylabel('Average Error (seconds)')
    plt.title('Average Error in Time Perception')
    plt.xticks(actual_times)
    plt.savefig('static/error.png')
    plt.close()
    
    # HTML template for displaying the plot
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Time Perception Error</title>
    </head>
    <body>
        <h1>Time Perception Error Visualization</h1>
        <p>This plot shows the average error in the user's perception of time for each target duration (1 to 10 seconds).</p>
        <img height="600" width="1000" src="{{ url_for('static', filename='error.png') }}" alt="Error Plot"></img>
    </body>
    </html>
    """
    
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
