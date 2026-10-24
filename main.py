import math_test
from flask import Flask

app = Flask(__name__)

PAGE_HTML = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>liuGrape</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:system-ui}
body{background:#f4f7fa;color:#333}
header{background:#2563eb;color:#fff;padding:1rem 5%;position:sticky;top:0;display:flex;justify-content:space-between;align-items:center}
.logo{font-size:1.5rem;font-weight:bold}
nav a{color:#fff;text-decoration:none;margin-left:16px}
.banner{background:#2563eb;color:#fff;text-align:center;padding:60px 20px}
.banner h1{font-size:2.2rem;margin-bottom:12px}
.banner p{max-width:600px;margin:0 auto 24px;opacity:.9}
.banner button{padding:10px 22px;border:none;border-radius:6px;background:#fff;color:#2563eb;cursor:pointer}
.wrap{width:90%;max-width:1000px;margin:40px auto}
h2{text-align:center;font-size:1.5rem;margin-bottom:24px}
.card{background:#fff;padding:20px;border-radius:10px;box-shadow:0 2px 8px #00000010}
footer{background:#1e293b;color:#aaa;text-align:center;padding:24px;margin-top:40px}
@media(max-width:600px){header{flex-direction:column;gap:10px}}
</style>
</head>
<body>
<header>
    <div class="logo">MyHome</div>
    <nav>
        <a href="#home">首页</a>
        <a href="#about">关于</a>
        <a href="#service">服务</a>
        <a href="#contact">联系</a>
    </nav>
</header>
<section class="banner" id="home">
    <h1>欢迎来到我的主页</h1>
    <p>响应式主页，手机电脑均可浏览。</p>
    <button onclick="alert('欢迎！')">了解更多</button>
</section>
<div class="wrap" id="service">
    <h2>功能卡片</h2>
    <div class="card">
        <h3>简洁美观</h3>
        <p>好久没用python了。</p>
    </div>
</div>
<div class="wrap" id="about">
    <h2>关于我</h2>
    <div class="card">
        <p>GitHub换到新的用户去了也是写个小项目玩玩。</p>
    </div>
</div>
<div class="wrap" id="contact">
    <h2>联系我</h2>
    <div class="card">
        <p>邮箱：liuGrapeDevelop@outlook.com</p>
        <p>GitHub：<a href="https://github.com/liuGrape" target="_blank">github.com/liuGrape</a></p>
    </div>
</div>
<footer>
    <p>© 2026 liuGrape</p>
</footer>
</body>
</html>
"""

@app.route('/')
def index():
    return PAGE_HTML

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
