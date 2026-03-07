class Rails:
    cache = {} 
    def __init__(self):
        pass

    def count_rails_recursive(self, length: int) -> int:
        if length < 0:
            return 0
        if length <= 1:
            return 1
        if cached := self.cache.get(length):
            return cached
        count = self.count_rails_recursive(length -1) + self.count_rails_recursive(length - 2) + self.count_rails_recursive(length - 3) 
        self.cache[length] = count
        return count        

    def count_rails_iterative(self, length: int) -> int:
        if length < 0:
            return 0
        if length <= 1:
            return 1
        if length == 2:
            return 2
        if cached := self.cache.get(length):
            return cached
        
        # Start from smallest known values
        # l(0) = 1, l(1) = 1, l(2) = 2
        l_0 = 1
        l_1 = 1
        l_2 = 2
        
        for current_lenght in range(3, length + 1):
            current_count = sum((l_0, l_1, l_2))
            l_0, l_1, l_2 = l_1, l_2, current_count
            self.cache[current_lenght] = current_count
            
        return self.cache[length]
