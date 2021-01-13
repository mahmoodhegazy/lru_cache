#This class is a python 3 implementation of an LRU Cache.  The LRU Cache stores items and allows for constant time access. It utilises the LRU policy for cache eviction.

class DLNode(object):
    def __init__(self):
        """
        :type capacity: int
        This objext is a node implemenatation for a Doubly Linked List. We use a DLL to hold the items that our cache has.
        The DL data structure satisfies the constraint for fast addition/removals since any doubly linked list item can be added or removed in O(1) time with proper references.
        """
        self.key = None
        self.value = None
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        We will implement our LRU Cache utilising a DLL for fast constant time addition/removals and a Set (hashset) for fast constant time lookups
        The init constructor will
         - set the max capacity
         - Initialize our doubly linked list with dummy head and tail
         - define items_in_cache so that we keep track and know when capacity is reached
        """
        self.__cap = capacity
        self.__cache = {} # Using a Set for item storage will give us fast access to any item in the doubly linked list items to avoid O(n) search for items and the LRU entry (which will always be at the tail of the doubly linked list).
        self.__items_in_cache = 0 #keep track of current size to know when capacity is reached
        self.__head , self.__tail = DLNode(),DLNode() #Init our DLL wih a dummy head/tail and wire them together
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        Given a key this function will retrive value stored for that key if exists.
        If the key does not exist, return Null/None as would a normal Set behave
        """
        if (not self.__cache) or (key not in self.__cache): #cache is empty/key does not exist
            return None
        node = self.__cache[key]  # Retrieve item from set: O(1) operation
        self.__move_to_head(node) # Move Node to front of DLL as it is now the most recently used.
        return node.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        Given a Key, value pair this function will either:
            - update key with new value if key exists already
            - add new key,value pair to our LRU Cache 
        """     
        if key in self.__cache: #If Key already exists, we only need to update the value and move key to front
            node = self.__cache[key]
            node.value = value #Update value
            self.__move_to_head(node) #Move to front(most recently used)
        else: #If Key does not exist, we need to creat a new node and put infront of list
            new_node = DLNode() 
            new_node.key,new_node.value = key,value
            self.__cache[key] = new_node #add new node to Set for quick access
            self.__addNode(new_node)     #add to DLL for quick removal
            self.__items_in_cache += 1   #increment to keep track of current cache size
            if self.__items_in_cache > self.__cap: # if cache size exceeds capacity, we need to evict the LRU node.
                self.__evictLRU()
    
    def delete(self, key):
        """
        :type key: int
        :rtype: None
        Given a key this function will delete/remove a key from LRUCache
        Attempting to delete a key that does not exist is a no-op
        """
        if key in self.cache:
            self.removeNode(self.cache[key])
            del self.cache[key]        
            self.items_in_cache -= 1
    
    def reset(self):
        """
        :rtype: None
        This function will reset the cache 
        """
        self.__init__(self.__cap)
    
    def curr_size(self):
        """
        :rtype: int
        This function return current cache size 
        """
        return self.__items_in_cache
    
    def is_empty(self):
        """
        :rtype: bool
        This function will return true if cache is empty
        """
        return self.__items_in_cache == 0
    
    def most_recently_used(self):
        """
        :rtype: key
        This function will return the most recently used node (head of the DLL)
        """
        return self.__head.key
    
    def least_recently_used(self):
        """
        :rtype: key
        This function will return the least recently used node (tail of the DLL)
        """
        return self.__tail.key
    
    def __move_to_head(self,node):
        """
        :type node: object
        :rtype: None
        Helper function (private) to update LRUCache with the most recently used item after an operation is done
        """     
        self.__removeNode(node)
        self.__addNode(node)
    
    def __addNode(self,node):
        """
        :type node: object
        :rtype: None
        Helper function (private) to add new node into DLL 
        """    
        #Should be directly after the head
        node.prev = self.__head
        node.next = self.__head.next
        self.__head.next.prev = node #head's old next
        self.__head.next = node #rewrite head
    
    def __removeNode(self,node):
        """
        :type node: object
        :rtype: None
        Helper function (private) to remove specified Node from DLL
        """           
        prev = node.prev
        new_nxt = node.next
        prev.next = new_nxt
        new_nxt.prev = prev
    
    def __evictLRU(self):
        curr_tail = self.__tail.prev
        self.__removeNode(curr_tail)
        del self.__cache[curr_tail.key]        
        self.__items_in_cache -= 1
        