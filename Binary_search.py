class BinarySearch(list):
    def __init__(self, a, b, *args):
        #Init list
        list.__init__(self, *args)
        self.list_length = a
        self.step = b
        end = self.list_length * self.step
        for i in range(self.step, end + 1, self.step):
            self.append(i)
    @property
    def length(self):
      return len(self)        
    def search(self, element, bottom=0, top=None, count=0):
        if not top:
            top = self.length - 1
        if element == self[bottom]:
            return {'index': bottom, 'count': count}
        elif element == self[top]:
            return {'index': top, 'count': count}
        mid = (bottom + top) // 2
        if element == self[mid]:
            return {'index': mid, 'count': count}
        elif element > self[mid]:
            bottom = mid + 1
        elif element < self[mid]:
            top = mid - 1
        if bottom >= top:
            return {'index': -1, 'count': count}
        count += 1  
        return self.search(element, bottom, top, count)