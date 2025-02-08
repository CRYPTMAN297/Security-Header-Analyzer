from flask import Flask, request, render_template
import requests

app = Flask(__name__)  

# Security Headers List
SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Referrer-Policy",
    "Permissions-Policy"
]

@app.route("/", methods=["GET", "POST"])
def home():
    headers_info = None
    url = ""

    if request.method == "POST":  
        url = request.form["url"]
        if not url.startswith(("http://", "https://")):
            url = "https://" + url  # Default HTTPS

        try:
            response = requests.get(url, timeout=5)
            headers = response.headers
            headers_info = {header: headers.get(header, "Not Found") for header in SECURITY_HEADERS}
        except requests.exceptions.RequestException as e:
            headers_info = {"Error": str(e)}

    return render_template("index.html", headers=headers_info, url=url)  
if __name__ == "__main__":  
    app.run(debug=True)