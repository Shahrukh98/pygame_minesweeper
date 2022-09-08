# from dataclasses import dataclass
# from functools import wraps
# from types import FunctionType
# from typing import Set

# def shappater(func):
#     @wraps(func)
#     def shappar(*args, **kwargs):
#           func(*args, **kwargs)
#     return shappar


# @dataclass
# class Clickable:
#     callbacks: Set[FunctionType]
#     def on_click(self) -> None:
#         for fun in self.callbacks:
#             fun()

#     def add_on_click(self,func) -> None:
#         self.callbacks.add(func)
        