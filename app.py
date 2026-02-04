from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return  """
<h1 style='color: #2a4dff; font-family: Arial; text-align: center; margin-top: 50px;'>
    Welcome to Version 2 🚀
</h1>
<p style='font-size: 20px; text-align: center; color: #333;'>
    ה־CI/CD שלך עובד בצורה מושלמת!
</p>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)