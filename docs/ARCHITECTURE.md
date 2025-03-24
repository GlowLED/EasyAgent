# Project: EasyAgent

## 设计理念
- 简单，灵活，易用，更加符合python使用者的习惯（pythonic）
  
## 方案：
### Basic元素
---
- **Agent**: 作为一个AI Agent SDK的基本元素，提供了直接调用方法（就像python函数那样调用它）：
```python
# a example of Agent using in EasyAgent.
a = Agent(url="your model url here")
response = a(messages)  # get the response of Agent like a Python function.
```

- 用户可以在Agent上进行二次开发，就像python的继承那样：
```python
# a example of Agent Inheritance in EasyAgent.
class MyAgent(Agent):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # implement your idea here.
        # ...
    
    def call(self, *args, **kwargs):
        # implement your idea here.
        # ...
```

- 我们会提供LLMAgent（实现文本生成），StableDiffusionAgent（实现绘图）等基本二次开发Agent类型。

---
- **Message**: 是一个代表信息的基类，允许多种模态（文本，图像...），Agent的开发即信息流的处理：
```python
# a example of Message using in EasyAgent.
msg = Message(content)
print(msg)

msg_input = TextMessage(content="Hello, world!")
a = LLMAgent(url="your model url here")
msg_output = a(msg_input)
print(msg_output)   # msg_output: TextMessage

```

- 用户可以在Message上进行二次开发，方法与Agent相同，略。
- 我们会提供TextMessage（文本信息），ImageMessage（图片信息），AudioMessage（音频信息）等基本二次开发Message类型。
---
- **Tool**: 是一个代表可与Agent互动的工具基类，是Agent开发中必不可少的部分，大致逻辑上是模型向一个东西输入action，这个东西返回给模型内容的东西都可以是Tool类（如记忆数据库，搜索API等），你也可以像python函数一样去调用它：
```python
tool = SearchEngine(engine="google")    # SearchEngine is a Tool Inheritance.
a = LLMAgent(url="your model url here")
msg_input = TextMessage(content="How's the weather today?")
msg_list = [msg_input,]     # to save the context

action = a(msg_list)   # Attention: action is a TextMessage
tool_output = tool(action)  # in EasyAgent, Action == Message

msg_list.append(action)
msg_list.append(tool_output)

msg_output = a(msg_list)
print(msg_output)   # Output: Fine!

```

