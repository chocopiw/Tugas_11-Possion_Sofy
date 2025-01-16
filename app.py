from flask import Flask, request, render_template
import math

app = Flask(__name__)

def poisson_probability(lmbda, k):
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            lmbda = float(request.form['lambda'])
            max_k = int(request.form['max_k'])
            probabilities = []

            for k in range(max_k + 1):
                prob = poisson_probability(lmbda, k)
                probabilities.append({'k': k, 'probability': prob, 'percentage': prob * 100})

            return render_template('index.html', lmbda=lmbda, max_k=max_k, probabilities=probabilities)
        except ValueError:
            return render_template('index.html', error="Invalid input. Please enter numeric values.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
