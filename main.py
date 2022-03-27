from typing import Iterable

def solution(liste):
  for i in liste:
    if isinstance(i, Iterable) and not isinstance(i, (str,bytes)):
      for sub_i in solution(i):
        yield sub_i
    else:
      yield i


def reverse_list(_items):
  for i in _items:
    i.reverse()
  _items.reverse()