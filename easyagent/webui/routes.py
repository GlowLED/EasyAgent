# webui/routes.py
from flask import Blueprint, jsonify, render_template
from utils.monitor import SystemMonitor  # 自定义监控工具

web_bp = Blueprint('webui', __name__)
# EXAMPLE
@web_bp.route("/dashboard")
def control_panel():
    return render_template("dashboard.html")

@web_bp.route("/api/agent/status")
def get_agent_status():
    # 返回所有Agent运行状态
    return jsonify(SystemMonitor.get_agents_status())

@web_bp.route("/api/model/update", methods=["POST"])
def update_model_params():
    # 处理模型参数修改请求
    pass
