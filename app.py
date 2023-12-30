from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/buy-stock')
def trigger_buy_stock():
    subprocess.run(["python", "buy_stock.py"])
    return 'Stock buying process initiated.'

if __name__ == '__main__':
    app.run()
