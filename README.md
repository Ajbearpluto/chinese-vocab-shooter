# 《三角洲字點：特種識字部隊》(Project Delta Lexicon)
> 結合 3A 戰術射擊（類《三角洲特種部隊》/ Delta Force）沉浸體驗與台灣國小五年級國語生字教學的跨平台教育 Web 專案。

---

## 🎯 專案核心特點

1. **國小五上生字全收錄**：已結構化收錄第一課至第十三課生字之字音、部首、形似字辨析、部件拆解與戰術詞彙。
2. **四階記憶階梯 (Memory Staircase)**：
   - 第一階：CQB 突入遭遇戰 —— 形近字弱點快速標定（如辨析「瘧」vs「虐」、「疾」vs「嫉」）。
   - 第二階：C4 定時引信拆除 —— 語意引線剪線解密。
   - 第三階：高寒絕壁反狙擊 —— 8 倍率狙擊鏡測風解算與字形穿甲打擊。
   - 第四階：水密隔艙雷射破拆 —— 部首部件組合破門（如「舟 + 倉 = 艙」）。
3. **iPad 專屬人因調優**：
   - 鎖定視口防誤觸（防止雙指縮放、長按快顯功能表與滑動回彈）。
   - Web Audio 程序化音效合成（零延遲，指紋解鎖符合 iOS 聲音規範）。
   - 支援 PWA 全螢幕模式（加入主畫面後與原生 App 完全相同）。
4. **兒童隱私與資安遵循 (COPPA / GDPR-K)**：
   - 零個人識別資料 (Zero PII) 收集，自動生成隨機軍事呼號（如 `DELTA-42`）。

---

## 🚀 方式一：手邊本機電腦 + iPad 區網即刻體驗

### 步驟 1：在電腦終端啟動伺服器
打開終端機（PowerShell 或 CMD），切換至本專案目錄：
```bash
cd C:\Users\user\.gemini\antigravity\scratch\delta-lexicon
python server.py
```

### 步驟 2：連線體驗
啟動後終端機將顯示：
* **本機電腦測試**：打開瀏覽器訪問 `http://localhost:8080`
* **iPad 觸控體驗**：確保 iPad 與電腦連在**同一個 Wi-Fi**，在 iPad Safari 網址列輸入畫面提示的 IP（例如 `http://192.168.1.xxx:8080`）即可立即開玩！

### 💡 iPad 最佳操作秘訣（隱藏網址列全螢幕）
在 iPad Safari 開啟網頁後：
1. 點擊右上角（或下方）的 **「分享 (Share)」** 按鈕。
2. 選擇 **「加入主畫面 (Add to Home Screen)」**。
3. 桌面上會產生專屬的特種部隊圖示，點開即是 **無網址列、防誤觸的 100% 全螢幕原生體驗**！

---

## 🌐 方式二：在任何地方使用（發布至雲端永久網址）

若要讓學生在不同教室、不同 Wi-Fi、甚至回家用自己的 iPad 都能隨時開啟，建議透過免費雲端發布（完全 0 元，永不斷線）：

### 選項 A：使用 GitHub Pages（推薦）
1. 在 [GitHub.com](https://github.com) 建立一個新的公開或私有倉庫（例如 `delta-lexicon`）。
2. 將本目錄所有檔案上傳或透過 git 推送至倉庫：
   ```bash
   git init
   git add .
   git commit -m "feat: 初版三角洲字點 iPad Web 戰術識字部隊"
   git branch -M main
   git remote add origin https://github.com/<您的帳號>/delta-lexicon.git
   git push -u origin main
   ```
3. 進入 GitHub 倉庫的 **Settings -> Pages**，Source 選擇 `main` 分支並儲存。
4. 30 秒後即可獲得永久免費網址：`https://<您的帳號>.github.io/delta-lexicon/`。

### 選項 B：使用 Cloudflare Pages / Vercel
1. 登入 [Vercel](https://vercel.com) 或 [Cloudflare Dashboard](https://dash.cloudflare.com)。
2. 直接將專案資料夾拖曳上傳（Direct Upload）。
3. 系統將即刻生成全球 CDN 加速的專屬 HTTPS 網址（如 `https://delta-lexicon.pages.dev`）。
4. 全球任何一台 iPad 開啟 Safari 輸入此網址即可秒速遊玩！

---

## 📂 目錄結構說明

```text
delta-lexicon/
├── index.html                 # 戰術特勤 HUD 主入口 (iPad 響應式、全螢幕、三關卡與儀表板)
├── manifest.json              # PWA 應用程式清單設定 (iPad 加入主畫面全螢幕)
├── server.py                  # 本機快速啟動器 (自動偵測區域網路 IP 供 iPad 直連)
├── data/
│   └── grade5_sem1_vocab.json # 國小五年級上學期生字、注音、部首、形似干擾字資料庫
├── assets/
│   └── audio.js               # Web Audio API 戰術無線電與射擊音效合成器 (免載入 MP3)
└── docs/                      # 系統企劃案與教研規格設計文件
```