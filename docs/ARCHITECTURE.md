# Project: EasyAgent

## 设计理念
- 简单，灵活，易用，更加符合python使用者的习惯（pythonic）
  
## 方案：
### Core元素
---

**Model**
- 模型，支持使用api-key、base-url进行创建。
- Model是一个基类，会继承实现OpenAILLM，QwenLLM等。

```python
model = OpenAILLM(base_url="xxx", api_key="xxx")
```

---

**Message**
- 信息，可以有多种模态。
- Message是一个基类，会继承实现TextMessage，ImageMessage，AudioMessage等

```python
text_message = TextMessage(content="Hello, world!")
image_message = ImageMessage(img_url="xxx")
```

---

**Tool**
- 工具，agent可以帮助model使用的接口。
- Tool是一个基类，会继承实现SearchEngine，Calculator等。
```python
search_engine = SearchEngine(engine="google")
calculator = Calculator()
```

---

**SDK**
- 工具的集合，方便进行管理。
- SDK是一个基类，会继承实现ChatSDK，MathSDK等。
```python
chatsdk = ChatSDK()
mathsdk = MathSDK()
```

---

**Service**
- 服务，如上下文管理，长中短期记忆管理
- Service是一个基类，会继承实现ContextManager，MemoryManager等。
```python
context_manager = ContextManager(max_length=4096)
memory_manager = MemoryManager(...) #参数没想好，到时候再说吧。
```

---

**Agent**
- AI Agent的核心，调用model，并帮助model行动，来增强model的能力，解决问题。
- Agent是一个基类，会继承实现ChatAgent，SearchAgent等。
```python
model = OpenAILLM(base_url="xxx", api_key="xxx")
sdk1 = ChatSDK()
sdk2 = SDK(SearchEngine(engine="google"))
agent1 = ChatAgent(model=model, sdk=sdk1)
agent2 = SearchAgent(model=model, sdk=sdk2)

```

---
### 构想的示例
```python
from easyagent.models import OpenAILLM, StableDiffusion
from easyagent.messages import TextMessage, ImageMessage
from easyagent.agents import ChatAgent
from easyagent.sdks import ChatSDK
from easyagent.core import Tool

class GetPaint(Tool):
    """
    对Tool基类进行二次开发
    实现了从文本生成图片
    """

    __tool_schema = {
        "name": "get_paint",
        "decription": "get a paint about a string 'query'.",
        "parameters": [
            {
                "name": "query",
                "type": "str",
                "description": "the paint's theme."
            }
        ]
    }

    def __init__(self, model):
        # model is a stable diffusion.
        super().__init__()
        self.model = model
    
    def call(self, query: str) -> ImageMessage:
        return model(query)


paint_model = StableDiffusion(...)  # 参数到时候再说
language_model = OpenAILLM(base_url="xxx", api_key="xxx", 
                           temperature=0.7, max_token=1024)

paint_tool = GetPaint(model=paint_model)
sdk = ChatSDK()
sdk.append(paint_tool)

agent = ChatAgent(model=language_model, sdk=sdk)

response = agent("Give me a picture about a cat girl, but in today's weather.")
# 实际上应该传入agent一个TextMessage类型，但我们会在内部兼容字符串。
# the agent will call the tool "weather_search", then call the tool "get_paint".

response.save("cat_girl.jpg")   # response: ImageMessage, and we will implement the method "save".

```
