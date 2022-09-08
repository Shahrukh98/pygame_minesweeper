from dataclasses import dataclass
from typing import Set

@dataclass
class Clickable:
  callbacks: Set[callable]
  
  def on_click(self, callback: callable) -> None:
    self.callbacks.add(callback)


@dataclass
class Button(Clickable):

  name: str

btn = Button(name='button',callbacks=set())
# btn.on_click(lambda x: print('callback 1'))
# btn.on_click(lambda x: print('callback 2'))



@btn.on_click
def callback() -> None:
    print(1231245)


print(btn.callbacks)
