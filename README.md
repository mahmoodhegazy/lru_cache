# lru_cache
This is a python 3 implementation of an LRU Cache.  The LRU Cache stores items and allows for constant time access. It utilises the LRU policy for cache eviction.

# installation
Follow these steps to install the package to your local python environment
```bash
git clone git@github.com:mahmoodhegazy/lru_cache.git
pip install -e lru_cache
```

# Usage

```python
from LRUCache import LRUCache

# initialize the LRU
lru_cache = LRUCache(capacity=3)

# insert nodes
lru_cache.put('1', 1)
lru_cache.put('2', 2)
lru_cache.put('3', 3)
print(lru_cache.curr_size())
>>> 3

# the cache evicts the least recently used node
lru_cache.put('4', 4)
assert not lru_cache.get('1') #assertion succeeds

# to get a node
value = lru_cache.get('4')
print(value)
>>> 4

# you can delete a node directly by
lru_cache.delete('4')
assert not lru_cache.get('4') #assertion succeeds

# to reset the cache
lru_cache.reset()
print(lru_cache.is_empty())
>>> True
```

# Unit Tests
to run unit tests
```bash
python lru_cache/LRUCache_test.py
```