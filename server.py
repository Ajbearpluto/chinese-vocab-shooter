# -*- coding: utf-8 -*-
import http.server
import socketserver
import socket
import os
import sys

PORT = 8080

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 不需要真正連通外網，僅用於取得本機出站網卡 IP
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 允許跨域與防止快取干擾開發
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def print_qr_hint(ip, port):
    url = f"http://{ip}:{port}"
    print("=" * 68)
    print("  【三角洲字點：特種識字部隊】戰術伺服器已成功啟動！")
    print("=" * 68)
    print(f"  [本機電腦瀏覽網址] : http://localhost:{port}")
    print(f"  [iPad / 平板連線網址] : {url}")
    print("-" * 68)
    print("  提示：請確保您的 iPad 與此電腦連接在「同一個 Wi-Fi 區域網路」")
    print("  在 iPad 開啟 Safari 瀏覽器輸入上述 iPad 網址即可秒開！")
    print("=" * 68)
    print("  伺服器運行中... 按 Ctrl + C 即可停止")
    print("=" * 68)

if __name__ == '__main__':
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    ip = get_local_ip()
    
    # 嘗試綁定端口
    try:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print_qr_hint(ip, PORT)
            httpd.serve_forever()
    except OSError:
        PORT = 8081
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print_qr_hint(ip, PORT)
            httpd.serve_forever()