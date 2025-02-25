from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc', methods=['POST'])
def calculator():
    try:
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        operation = request.form.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'multi':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Cannot divide by zero!"
            result = num1 / num2
        else:
            return "Error: Invalid operation!"

        return f"The Answer is: {result:.2f}"

    except (TypeError, ValueError):
        return "Error: Invalid input! Please enter numbers."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT or default to 5000
    app.run(host='0.0.0.0', port=port, debug=False)