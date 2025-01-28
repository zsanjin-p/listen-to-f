from flask import Flask, request, jsonify
from flask_cors import CORS
import pyautogui
import logging
import traceback

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 完全禁用CORS
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "methods": ["*"]}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/trigger-f', methods=['POST', 'OPTIONS'])
def trigger_f_key():
    if request.method == 'OPTIONS':
        return '', 204
        
    try:
        logger.info(f"收到请求 Headers: {dict(request.headers)}")
        logger.info(f"收到请求 Data: {request.get_data(as_text=True)}")
        
        data = request.get_json()
        
        if not data:
            logger.error("没有收到数据")
            return jsonify({'status': 'error', 'message': '没有接收到数据'}), 400
            
        if data.get('action') == 'press_f':
            logger.info("收到F键信号，模拟按键...")
            pyautogui.press('f')
            return jsonify({
                'status': 'success',
                'message': 'F键已按下',
                'timestamp': data.get('timestamp')
            })
        else:
            logger.warning(f"收到无效的action: {data.get('action')}")
            return jsonify({
                'status': 'error',
                'message': '无效的action参数'
            }), 400
            
    except Exception as e:
        logger.error(f"处理请求时发生错误: {traceback.format_exc()}")
        return jsonify({
            'status': 'error',
            'message': f'服务器错误: {str(e)}'
        }), 500

if __name__ == '__main__':
    logger.info("Flask服务器启动在 http://localhost:2716")
    app.run(host='localhost', port=2716, debug=False)
