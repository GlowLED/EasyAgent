from easyagent.core import Message
from typing import Optional, List, Dict, Any


class ImageMessage(Message):
    """
    图像消息类
    """
    
    __message_schema = {
        "type": "object",
        "properties": {
            "img_url": {
                "type": "string",
                "description": "图像URL"
            }
        },
        "required": ["image"]
    }
    
    def __init__(self, img_url: str, source: str = "system"):
        """
        初始化图像消息
        :param img_url: 图像URL
        :param source: 消息来源
        """
        super().__init__()
        self.img_url = img_url
        self.source = source
    
    def __str__(self):
        return self.img_url
    
    def __repr__(self):
        return f"<ImageMessage: {self.img_url}>"
    