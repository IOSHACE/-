from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

API_URL = "https://wappass.baidu.com/wp/api/login/sms"

HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://wappass.baidu.com",
    "Referer": "https://wappass.baidu.com/passport/?login&tpl=wise&sms=1",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1",
}

COOKIES = {
    "BAIDUID": "1146F46345FF5F2DEB0392A9A4D6872C:FG=1",
    "fuid": "687be74252dd95d88613ab30d0e7989a"
}

# ⚠️这里必须替换成你最新抓包的表单，旧数据已经失效
POST_DATA = """在这里粘贴抓包完整表单参数"""

HTML_TEMPLATE = """你的界面HTML代码（之前给你的完整页面）"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/send", methods=["POST"])
def send():
    phone = request.form.get("phone")
    count = int(request.form.get("count"))
    if count <= 0:
        return "发送次数为0，终止执行"
    try:
        response = requests.post(
            url=API_URL,
            headers=HEADERS,
            cookies=COOKIES,
            data=POST_DATA.strip(),
            timeout=15
        )
        output = f"""手机号：{phone}\n状态码：{response.status_code}\n返回：{response.text}"""
        return output
    except Exception as e:
        return f"错误：{str(e)}"

# Vercel Serverless必须加这一行
def handler(event, context):
    return app(event, context)