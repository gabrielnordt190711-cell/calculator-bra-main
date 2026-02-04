from flask import Flask, render_template

app = Flask(__name__)

def result_calculate(size, lights, device, eco):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    eco_bonus = -20 if eco == 1 else 0  # valor baixo e econômico

    return (
        size * home_coef +
        lights * light_coef +
        device * devices_coef +
        eco_bonus
    )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:size>')
def lights(size):
    return render_template('lights.html', size=size)


@app.route('/<int:size>/<int:lights>')
def electronics(size, lights):
    return render_template(
        'electronics.html',
        size=size,
        lights=lights
    )


@app.route('/<int:size>/<int:lights>/<int:device>/<int:eco>')
def end(size, lights, device, eco):
    result = result_calculate(size, lights, device, eco)
    return render_template('end.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
