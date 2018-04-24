"""
Illuminate
Control smart devices with a RESTful API
By Dylan Hamer
"""

from flask import Flask  # Web server
from flask import request  # Get information about requests

app = Flask(__name__)  # Initialise web server class

def controlDevice(device, mode, value):
    """Control a smart home device"""
    if device in controller.devices:
        try:
            getattr(controller, mode)()
        except AttributeError:
            return "Mode not supported."
        except ValueError:
            return "Mode is not a function."
    return "Set {} to {}.".format(device, value)

@app.route("/", allowed_methods = ["POST", "GET"])
def main():
    """Main function"""
    if request.type == "GET":
        return app.send_static_file("defaultpage.html")
    else:
        json = request.get_json()  # Get POSTed JSON
        try:
            device = json["device"]
            mode = json["mode"]
            value = json["value"]
        except ValueError:
            return "Please supply all variables."
        controlDevice(device, mode, value)
 