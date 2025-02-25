from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML form

@app.route('/calc', methods=['POST'])
def calculator():
    try:
        # Get input values
        num1 = float(request.form.get('num1'))  # Allow decimals
        num2 = float(request.form.get('num2'))
        operation = request.form.get('operation')

        # Perform the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':  # Ensure this matches the HTML form
            result = num1 - num2
        elif operation == 'multi':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Cannot divide by zero!"
            result = num1 / num2
        else:
            return "Error: Invalid operation!"

        return f"The Answer is: {result:.2f}"  # Formatting result to 2 decimal places

    except (TypeError, ValueError):
        return "Error: Invalid input! Please enter numbers."

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for deployment