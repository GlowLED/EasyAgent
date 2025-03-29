from easyagent.core import Model
from easyagent.messages import TextMessage, ImageMessage

from typing import List, Dict, Any, Text
from openai import OpenAI

class OpenAILLM(Model):
    """
    OpenAI接口标准的LLM模型
    """
    
    def __init__(self, model_name: str, api_key: str, base_url: str = "https://api.openai.com/v1"):
        """
        初始化OpenAI接口标准的LLM模型
        :param model_name: 模型名称
        :param api_key: API密钥
        :param api_base: API基础URL
        """
        super().__init__()
        self.model_name = model_name
        self.api_key = api_key
        self.base_url = base_url
        
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        
        
    def call(self,
                prompts: List[TextMessage, ImageMessage, str] | TextMessage | ImageMessage | str,
                max_tokens: int = 1024,
                temperature: float = 0.7,
                top_p: float = 1.0,
                n: int = 1,
                stop: List[str] = None,
                stream: bool = False,
                logprobs: int = None,
                echo: bool = False,
                presence_penalty: float = 0.0,
                frequency_penalty: float = 0.0,
                best_of: int = 1,
                logit_bias: Dict[str, float] = None,
                user: str = None    ) -> List[TextMessage]:
        """
        调用OpenAI接口进行文本生成
        :param prompts: 提示词， 允许传入文本消息或图像消息
        :type prompts: List[TextMessage, ImageMessage, str] | TextMessage | ImageMessage | str
        :param max_tokens: 最大token数
        :param temperature: 温度
        :param top_p: top_p采样
        :param n: 生成的文本数量
        :param stop: 停止词
        :param stream: 是否流式返回
        :param logprobs: 返回logprobs
        :param echo: 是否回显提示词
        :param presence_penalty: 出现惩罚
        :param frequency_penalty: 频率惩罚
        :param best_of: 最佳选择
        :param logit_bias: token偏置
        :param user: 用户ID
        :param kwargs: 其他参数
        :return: 生成的文本消息列表
        """
        
        # 把prompt参数都转换为OpenAI要求的JSON格式
        if isinstance(prompts, str):
            prompts = [prompts]
        elif isinstance(prompts, (TextMessage, ImageMessage)):
            prompts = [prompts]
        
        message = {}
        
        for prompt in prompts:
            if isinstance(prompt, TextMessage):
                message["text"] = prompt.text
            elif isinstance(prompt, ImageMessage):
                message["image"] = prompt.img_url
            else:
                message["text"] = prompt
        
        
        
        
                 
        