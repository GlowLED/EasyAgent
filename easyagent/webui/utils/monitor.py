# webui/utils/monitor.py
import psutil
from easyagent.agents import agent_registry  # 假设已实现Agent注册机制
# EXAMPLE
class SystemMonitor:
    @staticmethod
    def get_system_status():
        return {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent
        }
    
    @staticmethod
    def get_agents_status():
        return [agent.stats() for agent in agent_registry.values()]  # 假设Agent有stats()方法
