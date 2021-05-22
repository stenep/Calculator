# -*- coding: utf-8 -*-
import connexion
import argparse
from waitress import serve
from flask import render_template

# Create server app and load yml-file with api routes
app = connexion.FlaskApp(__name__, specification_dir=".")
app.add_api("api_routes.yml")

# Calculator entry point
@app.route("/")
def index():
    """"""
    return render_template(
        "index.html",
        )

if __name__ == "__main__":

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Calculator server')
    parser.add_argument('--mode', help='Serve mode: "development" or "production"')
    args = parser.parse_args()

    # Start server
    mode = args.mode
    if mode == 'development':
        app.run(host="0.0.0.0", port=5000, debug=True)
    elif mode =='production':
        serve(app, host="0.0.0.0", port=5000)
    else:
        error = f'Serve mode {"unknown" if mode else "not given"}!'
        print(error)
