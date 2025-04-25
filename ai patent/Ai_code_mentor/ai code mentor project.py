from flask import Flask, request, jsonify
import subprocess
import os
import tempfile
import platform
import re

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Code Mentor</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                height: 100vh;
                background: linear-gradient(135deg, #667eea, #764ba2);
                display: flex;
                justify-content: center;
                align-items: center;
                color: black;
            }
            .container {
                background: rgba(255, 255, 255, 0.95);
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
                width: 650px;
                max-width: 90%;
            }
            h1 {
                color: #4b0082;
                text-align: center;
                margin-bottom: 1.5rem;
            }
            select, textarea {
                width: 100%;
                padding: 12px;
                font-size: 16px;
                border-radius: 10px;
                border: 1px solid #aaa;
                margin-bottom: 12px;
                background-color: #f7f7ff;
                color: #333;
                font-family: 'Courier New', Courier, monospace;
            }
            button {
                background: linear-gradient(to right, #00c9ff, #92fe9d);
                color: #fff;
                padding: 12px 25px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                font-size: 16px;
                font-weight: bold;
                display: block;
                margin: 0 auto;
            }
            h3 {
                margin-top: 25px;
                color: #4b0082;
                text-align: center;
            }
            pre {
                background-color: #f0f4f8;
                padding: 15px;
                border-radius: 12px;
                font-size: 15px;
                border: 1px solid #ccc;
                max-height: 300px;
                overflow-y: auto;
                white-space: pre-wrap;
                color: #2d2d2d;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 AI Code Mentor</h1>
            <form onsubmit="reviewCode(); return false;">
                <select id="language">
                    <option value="python">Python</option>
                    <option value="c">C</option>
                    <option value="cpp">C++</option>
                    <option value="java">Java</option>
                </select>
                <textarea id="code" rows="10" placeholder="Paste your code here..."></textarea>
                <button type="submit">💬 Review My Code</button>
            </form>
            <h3>Review Result:</h3>
            <pre id="result">Waiting for code...</pre>
        </div>
        <script>
            async function reviewCode() {
                const code = document.getElementById("code").value;
                const language = document.getElementById("language").value;

                const res = await fetch("/ai/get-review", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ code, language })
                });
                const data = await res.json();
                document.getElementById("result").innerText = data.review;
            }
        </script>
    </body>
    </html>
    '''

def run_compiler(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError as e:
        return -1, "", f"Compiler not found: {command[0]}. Please ensure it is installed and added to PATH."
    except Exception as e:
        return -1, "", f"Exception: {type(e).__name__}: {str(e)}"

@app.route('/ai/get-review', methods=['POST'])
def get_review():
    data = request.get_json()
    code = data.get("code", "")
    language = data.get("language", "python")

    if not code.strip():
        return jsonify({"review": "❌ Code is empty. Please paste your code."})

    is_windows = platform.system().lower().startswith("win")

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            if language == "python":
                try:
                    compile(code, "<string>", "exec")
                    review = "✅ Python code is syntactically correct.\nTip: Consider adding comments and following PEP8."
                except SyntaxError as e:
                    review = f"⚠️ Python Syntax Error:\n{e}"

            elif language == "c":
                file_path = os.path.join(temp_dir, "temp.c")
                output_path = os.path.join(temp_dir, "temp.exe" if is_windows else "temp.out")
                with open(file_path, "w") as f:
                    f.write(code)
                ret, out, err = run_compiler(["gcc", file_path, "-o", output_path])
                if ret == 0:
                    review = "✅ C code is syntactically correct."
                elif "Compiler not found" in err:
                    review = "❌ C compiler (gcc) not found.\n➡️ Please install GCC and add it to your PATH."
                else:
                    review = f"⚠️ C Compiler Error:\n{err}"

            elif language == "cpp":
                file_path = os.path.join(temp_dir, "temp.cpp")
                output_path = os.path.join(temp_dir, "temp.exe" if is_windows else "temp.out")
                with open(file_path, "w") as f:
                    f.write(code)
                ret, out, err = run_compiler(["g++", file_path, "-o", output_path])
                if ret == 0:
                    review = "✅ C++ code is syntactically correct."
                elif "Compiler not found" in err:
                    review = "❌ C++ compiler (g++) not found.\n➡️ Please install GCC/G++ and add it to your PATH."
                else:
                    review = f"⚠️ C++ Compiler Error:\n{err}"

            elif language == "java":
                match = re.search(r'public\s+class\s+(\w+)', code)
                if not match:
                    review = "❌ Java code must contain a public class."
                else:
                    original_class = match.group(1)
                    modified_code = re.sub(rf'\bpublic\s+class\s+{original_class}\b', 'public class Temp', code)
                    file_path = os.path.join(temp_dir, "Temp.java")
                    with open(file_path, "w") as f:
                        f.write(modified_code)
                    ret, out, err = run_compiler(["javac", file_path])
                    if ret == 0:
                        review = "✅ Java code is syntactically correct.\nTip: Remember to keep class names and file names consistent."
                    elif "Compiler not found" in err:
                        review = "❌ Java compiler (javac) not found.\n➡️ Please install Java SDK and add it to your PATH."
                    else:
                        review = f"⚠️ Java Compiler Error:\n{err}"
            else:
                review = "❌ Unsupported language."

    except Exception as e:
        review = f"⚠️ Internal Error: {type(e).__name__}: {str(e)}"

    return jsonify({"review": review})

if __name__ == '__main__':
    app.run(debug=True, port=5050)
