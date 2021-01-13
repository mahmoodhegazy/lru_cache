''' Test LRUCache funcctionality'''
import unittest
from LRUCache import LRUCache

class LRUCacheTest(unittest.TestCase):

    def setUp(self):
        """ Initial setup """
        self.lru_cache = LRUCache(3)
        
    def test_put(self):
        """ Test LRU Cache put functionality """
        self.lru_cache.put('1', 1)
        self.lru_cache.put('2', 2)
        self.lru_cache.put('3', 3)
        assert self.lru_cache.curr_size() == 3, f'Curr size of cache is {lru_cache.curr_size()}'
    
    def test_get(self):
        """ Test LRU Cache get functionality """
        self.lru_cache.put('3', 3)
        assert self.lru_cache.get('3') == 3
    
    def test_lru_policy(self):
        """ Test LRU Eiction Policy by adding 2 items over capacity """
        self.lru_cache.put('1', 1)
        self.lru_cache.put('2', 2)
        self.lru_cache.put('3', 3)
        self.lru_cache.put('4', 2)
        self.lru_cache.put('5', 3)
        # assert that nodes 1, and 2 have been be evicted
        self.assertFalse(self.lru_cache.get('1'))
        self.assertFalse(self.lru_cache.get('2'))
    
    def test_priority(self):
        """ Test LRU Cache prioritzation """
        self.lru_cache.put('2', 2)
        self.lru_cache.put('3', 3)
        self.lru_cache.put('6', 6)
        assert self.lru_cache.most_recently_used() == '6',f'Curr mru {self.lru_cache.most_recently_used()}'

    def test_delete(self):
        """ Test LRU Cache delete functionality """
        self.lru_cache.put('2', 2)
        self.lru_cache.put('3', 3)
        self.lru_cache.delete('3')
        self.assertFalse(self.lru_cache.get('3'))
    
    def test_reset(self):
        """ Test LRU Cache reset functionality"""
        self.lru_cache.put('2', 2)
        self.lru_cache.put('3', 3)
        self.lru_cache.reset()
        assert self.lru_cache.is_empty()

if __name__ == '__main__':
    unittest.main()