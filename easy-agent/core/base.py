from abc import ABC, abstractmethod
from typing import Dict, List, Any

class Tool(ABC):
    """工具基类，所有工具应继承此类"""
    
    @property
    def schema(self) -> Dict[str, Any]:
        """返回工具的schema定义"""
        if hasattr(self, "__tool_schema"):
            return self.__tool_schema
        raise NotImplementedError("Tool schema not defined")
    
    @abstractmethod
    def call(self, *args, **kwargs):
        """调用工具的方法，必须由子类实现"""
        raise NotImplementedError("Tool call method not implemented")

class Message(ABC):
    """消息基类，所有消息类型应继承此类"""
    
    @property
    def schema(self) -> Dict[str, Any]:
        """返回消息的schema定义"""
        if hasattr(self, "__message_schema"):
            return self.__message_schema
        raise NotImplementedError("Message schema not defined")

class Model(ABC):
    """模型基类，所有模型应继承此类"""
    
    @property
    def schema(self) -> Dict[str, Any]:
        """返回模型的schema定义"""
        if hasattr(self, "__model_schema"):
            return self.__model_schema
        raise NotImplementedError("Model schema not defined")
    
    @abstractmethod
    def call(self, *args, **kwargs):
        """调用模型的方法，必须由子类实现"""
        raise NotImplementedError("Model call method not implemented")

class SDK(ABC):
    """SDK基类，所有SDK应继承此类"""
    
    @property
    def schema(self) -> Dict[str, Any]:
        """返回SDK的schema定义"""
        if hasattr(self, "__sdk_schema"):
            return self.__sdk_schema
        raise NotImplementedError("SDK schema not defined")

class Service(ABC):
    """服务基类，所有服务应继承此类"""
    
    @property
    def schema(self) -> Dict[str, Any]:
        """返回服务的schema定义"""
        if hasattr(self, "__service_schema"):
            return self.__service_schema
        raise NotImplementedError("Service schema not defined")
    
    @abstractmethod
    def call(self, *args, **kwargs):
        """调用服务的方法，必须由子类实现"""
        raise NotImplementedError("Service call method not implemented")

class Agent(ABC):
    """Agent基类，所有Agent应继承此类"""
    
    @property
    def schema(self) -> Dict[str, Any]:
        """返回Agent的schema定义"""
        if hasattr(self, "__agent_schema"):
            return self.__agent_schema
        raise NotImplementedError("Agent schema not defined")
    
    @abstractmethod
    def call(self, *args, **kwargs):
        """调用Agent的方法，必须由子类实现"""
        raise NotImplementedError("Agent call method not implemented")
    