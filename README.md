# listen-to-f
为了适老化设计，用于配合自动全屏的油猴JS脚本，当油猴JS脚本post时，本程序将按下F，以绕过浏览器的策略

## 使用方式
1. 克隆仓库或下载项目文件  
   ```
   git clone https://github.com/zsanjin-p/listen-to-f
   ```
2. 安装python和pip，所有版本应该都通用  
3. 安装所需的python库  
   ```
   pip install Flask Flask-CORS pyautogui
   ```
4. 运行listen-to-f.py  
5. 安装油猴脚本  
   https://greasyfork.org/zh-CN/scripts/525029
6. 访问当前脚本设定的网页，或者自行增加需要自动全屏的网址  
   https://xiaoxintv.cc/index.php/vod/play/id/*
   https://www.bilibili.com/video/*等，理论所有网址都可以
7. 无需操作即可自动进入全屏，方便老人小孩
