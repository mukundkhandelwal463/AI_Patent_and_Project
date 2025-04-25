🧠 AI Code Mentor – Web-Based Code Reviewer
📌 Project Title:
AI Code Mentor – Smart Syntax Checker & Compiler for Multiple Languages

👨‍💻 Developed By:
Mukund Khandelwal
Email: mukundkhandelwal463@gamil.com
University: Lovely Professional University, Punjab, India

🧠 Project Overview
The AI Code Mentor is a Flask-based web application that allows users to paste and validate source code in multiple programming languages including Python, C, C++, and Java. It provides instant syntax feedback using real-time compilation and static analysis, offering beginner-friendly insights and tips.

🎯 Objectives
Enable users to instantly check code for syntax errors across popular languages.

Provide a simple web-based interface for interactive code reviews.

Serve as a lightweight educational tool for students and programmers to learn and improve code quality.

🧩 Key Features
🌍 Web Interface: Clean, responsive UI for code review.

💬 Instant Code Feedback: Quickly checks syntax using native compilers and Python's compile() function.

💡 Beginner Tips: Suggests common improvements like adding comments or fixing class names.

⚙️ Multi-Language Support: Works with Python, C, C++, and Java.

❗ Error Reporting: Displays compiler errors in a readable format.

🔍 Cross-Platform Detection: Handles OS differences (e.g., .exe vs .out).

🛠️ Technologies Used

Technology	Purpose
Flask	Backend web framework
HTML/CSS	Frontend layout and styling
Python	Code analysis and compiler logic
GCC/G++	For C/C++ code compilation
Java SDK	For Java code syntax checking
🧪 How It Works
Users visit the web interface.

They select a programming language and paste their code.

On submit, the backend:

Checks for Python syntax using compile().

Compiles C/C++ code using gcc/g++.

Compiles Java code using javac after auto-renaming the class.

Returns results as ✅ success or ⚠️ error messages.

🔧 Setup Instructions
Install Python Dependencies:

bash
Copy
Edit
pip install flask
Ensure Compilers are Installed:

Python 3 (for syntax checking)

gcc and g++ (for C/C++ code)

javac (Java SDK for Java code)

Run the Server:

bash
Copy
Edit
python app.py
Open your browser and visit:
http://localhost:5050

💻 Example Languages Supported
Python (PEP8 tip suggestions)

C/C++ (GCC/G++ compiler check)

Java (Auto class renaming to allow dynamic testing)

🔐 Security Note
This tool executes or compiles user-submitted code temporarily. It should not be exposed to the internet without sandboxing and proper security measures.

🚀 Future Improvements
Add AI-powered code quality suggestions (via Gemini, GPT, or CodeBERT)

Provide runtime execution results

Integrate custom static analysis tools

Extend support to languages like JavaScript, Rust, Kotlin, etc.

📎 Keywords
Flask Code Checker, Syntax Validator, Multi-Language Compiler, AI Code Mentor, Online IDE, Python Flask Compiler, Code Review Web App
