from flask import Flask, render_template, request

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    
    expression = request.form['expression']
    try:
        result = eval(expression)
        return render_template('index.html', result=result, expression=expression)
    except Exception as e:
        error_message = "Error: " + str(e)
        return render_template('index.html', error=error_message, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)