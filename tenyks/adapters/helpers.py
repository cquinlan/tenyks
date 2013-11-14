import importlib


def get_adapter_class(adapter_module):
    module = adapter_module.split('.')[:-1]
    class_name = adapter_module.split('.')[-1:].pop()
    module = importlib('.'.join(module))
    class_def = getattr(module, class_name)
    return class_def
