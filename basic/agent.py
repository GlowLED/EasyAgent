class Agent(object):
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
    
    def __call__(self, *args, **kwargs):
        raise NotImplementedError
