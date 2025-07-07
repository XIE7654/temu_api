from typing import TypeVar

T = TypeVar("T")


def action(path, method="POST"):

    def decorator(function: T) -> T:
        def wrapper(*args, **kwargs):
            kwargs.update({"path": path, "method": method})
            return function(*args, **kwargs)

        wrapper.__doc__ = function.__doc__
        return wrapper
    return decorator


def filter_none(obj):
    """
    递归过滤 dict/list 中所有值为 None 的项。
    """
    if isinstance(obj, dict):
        return {k: filter_none(v) for k, v in obj.items() if v is not None}
    elif isinstance(obj, list):
        return [filter_none(v) for v in obj if v is not None]
    else:
        return obj