from flask import Flask, render_template, request

app = Flask(__name__)

def format_number(num):
    """Format number to remove .0 if it's a whole number"""
    if isinstance(num, float) and num.is_integer():
        return int(num)
    return num

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return render_template('result.html', error='Cannot divide by zero!')
            result = num1 / num2
        else:
            return render_template('result.html', error='Invalid operation!')
        
        num1_formatted = format_number(num1)
        num2_formatted = format_number(num2)
        result_formatted = format_number(result)
        
        return render_template('result.html', 
                             num1=num1_formatted, 
                             num2=num2_formatted, 
                             operation=operation, 
                             result=result_formatted)
    except ValueError:
        return render_template('result.html', error='Please enter valid numbers!')

@app.route('/api/calculate', methods=['GET'])
def calculate_api():
    try:
        a = float(request.args.get('a', ''))
        b = float(request.args.get('b', ''))
        op = request.args.get('op', '+')
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                return {"error": "Division by zero"}, 400
            result = a / b
        else:
            return {"error": "Unsupported operation"}, 400
        
        result_formatted = format_number(result)
        
        return {"result": result_formatted}
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
