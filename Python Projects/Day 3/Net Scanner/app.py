# app.py
import os
import socket
import threading
import time
import webbrowser
from flask import Flask, render_template, request

# Set up base directory and Flask app
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'))

# Common ports mapped to services
common_services = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 3306: "MySQL", 8080: "HTTP-Alt"
}

# Thread-safe open ports list
open_ports = []
print_lock = threading.Lock()

def scan_port(target, port, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((target, port))
        if result == 0:
            service = common_services.get(port, "Unknown")
            with print_lock:
                open_ports.append((port, service))
        s.close()
    except:
        pass

@app.route("/", methods=["GET", "POST"])
def index():
    global open_ports
    open_ports = []

    if request.method == "POST":
        try:
            target = request.form["target"].strip()
            ports = range(1, 1025)
            timeout = 0.5

            threads = []
            for port in ports:
                thread = threading.Thread(target=scan_port, args=(target, port, timeout))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            return render_template("index.html", target=target, open_ports=open_ports)

        except Exception as e:
            return f"<h1>💥 Internal Error:</h1><pre>{e}</pre>"

    return render_template("index.html", target=None, open_ports=[])

if __name__ == "__main__":
    def open_browser():
        time.sleep(1)
        webbrowser.open("http://localhost:5000")

    threading.Thread(target=open_browser).start()
    app.run(debug=False)
