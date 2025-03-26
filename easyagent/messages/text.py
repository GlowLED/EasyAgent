from easyagent.core import Message

class TextMessage(Message):
    """
    文本消息类
    """
    
    __message_schema = {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "文本内容"
            }
        },
        "required": ["text"]
    }
    
    def __init__(self, text: str, source: str = "system"):
        """
        初始化文本消息
        :param text: 文本内容
        :param source: 消息来源
        """
        super().__init__()
        self.text = text
        self.source = source

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"<TextMessage: {self.text}>"