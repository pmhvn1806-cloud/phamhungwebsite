import os
from flask import Flask, render_template
app = Flask(__name__)

# --- Tạo cấu trúc thư mục ---
os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

# --- Tạo file index.html ---
with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trang chủ</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Chào mừng mọi người đến với trang Flask của tôi!</h1>
        <nav>
            <a href="/">Trang chủ</a>
            <a href="/about">Giới thiệu</a>
            <a href="/contact">Liên hệ</a>
        </nav>
    </header>

    <main>
        <h2 style="font-size: 40px;">Chào mừng bạn đã đến với web của tôi!</h2>
        <p style="font-size: 20px;">Đây là trang web đầu tiên tôi tự tay làm.</p>
        <p style="font-size: 20px;">trang web này giới thiệu về bản thân tôi</p>
    </main>

    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
""")

# --- Tạo file about.html ---
with open("templates/about.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Giới thiệu</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Giới thiệu</h1>
        <nav>
            <a href="/">Trang chủ</a>
            <a href="/about">Giới thiệu</a>
            <a href="/contact">Liên hệ</a>
        </nav>
    </header>
    <main>
        <p style="font-size: 35px;">xin tự giới thiệu</p>
        <p style="font-size: 35px;">tôi tên là Phạm Hùng, sinh năm 2009 tại tỉnh Quảng Ninh.</p>
        <p style="font-size: 35px:">tôi hiện đang học tại trường THPT Hùng Vương,lớp 11A6<p>
        <p style="font-size: 35px;">đây có thể coi là trang web đầu tay của tôi</p>             <p style="font-size: 30px;">Đây là dự án đầu tiên của mình — nơi mình thử nghiệm, học hỏi và chia sẻ về bản thân cũng như chia sẻ sự sáng tạo với công nghệ </p>
        <p style="font-size: 35px;">                        cảm ơn mọi người đã xem dòng tâm sự của tôi!  </p>
    </main>
</body>
</html>
""")

# --- Tạo file contact.html ---
with open("templates/contact.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Liên hệ</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Liên hệ</h1>
        <nav>
            <a href="/">Trang chủ</a>
            <a href="/about">Giới thiệu</a>
            <a href="/contact">Liên hệ</a>
        </nav>
    </header>
    <main>
        <p>Bạn có thể gửi email cho tôi qua: <a href="mailto:pmhvn123@gmail.com">pmhvn123@gmail.com</a></p>
        <p>số điện thoại :<a href="số điện thoại:0834140609">0834140609</a></p>
    </main>
</body>
</html>
""")

# --- Tạo file style.css ---
with open("static/style.css", "w", encoding="utf-8") as f:
    f.write("""body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: white;
    padding: 10px;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 10px;
}

nav a:hover {
    text-decoration: underline;
}

main {
    padding: 20px;
}
""")

# --- Tạo file script.js ---
with open("static/script.js", "w", encoding="utf-8") as f:
    f.write("""function thongbao() {
    alert("Bạn vừa nhấn nút!");
}
""")

# --- Khởi tạo Flask ---
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    print("👉 Mở trình duyệt và vào: http://127.0.0.1:5000")
    app.run(debug=True)
