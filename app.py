from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/echo/')
@app.route('/echo/<name>')
def echo(name=None):
    msg = request.args.get('msg')
    return render_template('echo.html', name=name, msg=msg)
