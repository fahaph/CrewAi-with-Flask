from flask import Flask, request, jsonify, render_template
from crew import crew

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # ใช้ฟอร์ม HTML

@app.route('/process', methods=['POST'])
def process():
    data = request.json  # รับ JSON ที่ส่งมาจาก JavaScript
    province = data.get("province", "")
    days = data.get("days", "")
    budget = data.get("budget", "")

    # ตัวอย่างการประมวลผลข้อมูล
    result = crew.kickoff(inputs={'province': {province}, 'days': {days}, 'budget': {budget}})
    # print(result)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
