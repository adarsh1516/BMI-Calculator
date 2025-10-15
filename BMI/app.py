from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    """
    Main route for the BMI calculator.
    Handles both GET requests (displaying the form) and POST requests (calculating BMI).
    """
    bmi_result = None
    bmi_category = ''
    category_class = '' # CSS class for color-coding the result

    # Handle the form submission
    if request.method == 'POST':
        try:
            # Get height and weight from the form and convert to float
            height_cm = float(request.form.get('height'))
            weight_kg = float(request.form.get('weight'))

            # Ensure inputs are positive numbers
            if height_cm > 0 and weight_kg > 0:
                # Convert height from cm to meters
                height_m = height_cm / 100
                # Calculate BMI and round to one decimal place
                bmi = round(weight_kg / (height_m ** 2), 1)
                bmi_result = bmi

                # Determine the BMI category and corresponding CSS class
                if bmi < 18.5:
                    bmi_category = 'Underweight'
                    category_class = 'underweight'
                elif 18.5 <= bmi < 24.9:
                    bmi_category = 'Normal weight'
                    category_class = 'normal'
                elif 25 <= bmi < 29.9:
                    bmi_category = 'Overweight'
                    category_class = 'overweight'
                else: # BMI >= 30
                    bmi_category = 'Obese'
                    category_class = 'obese'
            else:
                 # Handle non-positive input
                 bmi_category = 'Please enter positive values for height and weight.'
                 category_class = 'error'

        except (ValueError, TypeError):
            # Handle cases where input is not a valid number
            bmi_category = 'Invalid input. Please enter numbers only.'
            category_class = 'error'

    # Render the HTML template with the results
    return render_template('index.html', bmi_result=bmi_result, bmi_category=bmi_category, category_class=category_class)

# Run the app
if __name__ == '__main__':
    # Setting debug=True allows you to see errors and auto-reloads the server on changes
    app.run(debug=True)
