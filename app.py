from flask import Flask, request, jsonify, render_template

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
    processed_data = {
        "province": province.upper(),
        "days": days,
        "budget": budget
    }

    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)
