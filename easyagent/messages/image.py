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
    
    def __init__(self, img_url: str, source: str = "system") -> None:
        """
        初始化图像消息
        :param img_url: 图像URL, 可以是本地路径或网络URL
        :param source: 消息来源
        """
        super().__init__()
        self.img_url = img_url
        self.source = source
    
    def __str__(self) -> str:
        return self.img_url
    
    def __repr__(self) -> str:
        return f"<ImageMessage: {self.img_url}>"
    
    def show(self) -> None:
        """
        显示图像消息
        :return: None
        """
        from PIL import Image
        if self.img_url.startswith("http"):
            import requests
            from io import BytesIO
            response = requests.get(self.img_url)
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(self.img_url)
        img.show()
        
    def __eq__(self, other: "ImageMessage") -> bool:
        """
        重载等于运算符
        :param other: 另一个图像消息对象
        :return: 是否相等
        """
        return self.img_url == other.img_url and self.source == other.source
    
    
    def __ne__(self, other: "ImageMessage") -> bool:
        """
        重载不等于运算符
        :param other: 另一个图像消息对象
        :return: 是否不相等
        """
        return not self.__eq__(other)
    