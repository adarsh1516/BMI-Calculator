from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi_result = None
    bmi_category = ''
    category_class = ''

    if request.method == 'POST':
        try:
            height_cm = float(request.form.get('height'))
            weight_kg = float(request.form.get('weight'))

            if height_cm > 0 and weight_kg > 0:
                height_m = height_cm / 100
                bmi = round(weight_kg / (height_m ** 2), 1)
                bmi_result = bmi

                if bmi < 18.5:
                    bmi_category = 'Underweight'
                    category_class = 'underweight'
                elif 18.5 <= bmi < 24.9:
                    bmi_category = 'Normal weight'
                    category_class = 'normal'
                elif 25 <= bmi < 29.9:
                    bmi_category = 'Overweight'
                    category_class = 'overweight'
                else:
                    bmi_category = 'Obese'
                    category_class = 'obese'
            else:
                bmi_category = 'Please enter positive values for height and weight.'
                category_class = 'error'

        except (ValueError, TypeError):
            bmi_category = 'Invalid input. Please enter numbers only.'
            category_class = 'error'

    return render_template('index.html', bmi_result=bmi_result, bmi_category=bmi_category, category_class=category_class)

if __name__ == '__main__':
    app.run(debug=True)
