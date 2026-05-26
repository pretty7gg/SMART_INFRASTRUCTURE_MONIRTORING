from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/')

def dashboard():

    cpu = psutil.cpu_percent()

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    html = f"""

    <html>

    <head>

        <title>Smart Infra Monitor</title>

        <style>

            body {{

                font-family: Arial;

                background-color: #f4f4f4;

                padding: 40px;
            }}

            .card {{

                background: white;

                padding: 20px;

                margin: 20px;

                border-radius: 10px;

                box-shadow: 0px 0px 10px gray;

                width: 300px;
            }}

            h1 {{

                color: #333;
            }}

        </style>

    </head>

    <body>

        <h1>Smart Infrastructure Monitoring Dashboard</h1>

        <div class="card">

            <h2>CPU Usage</h2>

            <p>{cpu}%</p>

        </div>

        <div class="card">

            <h2>Memory Usage</h2>

            <p>{memory}%</p>

        </div>

        <div class="card">

            <h2>Disk Usage</h2>

            <p>{disk}%</p>

        </div>

    </body>

    </html>

    """

    return html


if __name__ == '__main__':

    app.run(debug=True,port = 8000)