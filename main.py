# hello_xss.py
#
# A tiny Flask “Hello World” web-app with a **deliberate XSS flaw**.
#   Run:  pip install flask
#   Start: python hello_xss.py   → browse to http://localhost:5000
#
# ⚠️  SECURITY WARNING: never copy this pattern into production code.

from flask import Flask, request, render_template_string
import random, string

app = Flask(__name__)

WORDS = ["sunrise", "galaxy", "forest", "ocean", "nebula", "comet"]

TEMPLATE = """
<!doctype html>
<title>Hello</title>
<style>
  body {font-family: system-ui; background:#f7f9fb; text-align:center; margin-top:4rem;}
  h1   {color:#4a90e2; font-size:3rem; margin-bottom:.5rem;}
  small{color:#888;}
  input,button{padding:.4rem .8rem; font-size:1rem;}
  .echo{margin-top:1rem; padding:1rem; border:1px solid #faa; background:#fff5f5;}
</style>

<h1>Hello, World! 🌍</h1>
<small>Random pick: <strong>{{ word }}</strong> &nbsp;|&nbsp; Lucky number: <strong>{{ num }}</strong></small>

<form>
  <p>Echo anything back <em>(vulnerable!)</em></p>
  <input name="q" placeholder="type here">
  <button type="submit">Go</button>
</form>

{% if q %}
  <div class="echo">
    <h2>You said …</h2>
    <!-- ✗ UNSAFE: ‘q’ is rendered without escaping, enabling XSS -->
    {{ q|safe }}
  </div>
{% endif %}
"""

@app.route("/")
def index():
    return render_template_string(
        TEMPLATE,
        num=random.randint(1000, 9999),
        word=random.choice(WORDS),
        q=request.args.get("q")
    )

if __name__ == "__main__":
    app.run(debug=True)
