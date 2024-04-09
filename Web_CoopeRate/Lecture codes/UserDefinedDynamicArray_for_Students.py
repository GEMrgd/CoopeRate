import ctypes


class UserDefinedDynamicArray:
    def __init__(self,I=None):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self,x):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=x
        self._n+=1

    def _resize(self,newsize):
        A=self._make_array(newsize)
        self._capacity=newsize
        for i in range(self._n):
            A[i]=self._A[i]
        self._A=A

    def _make_array(self,size):
        return (size*ctypes.py_object)()

    def __getitem__(self,i):
        if isinstance(i,slice):
            A=UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)): # * operator was used to unpack the slice tuple
                A.append(self._A[j])
            return A
        if i<0:
            i=self._n+i
        return self._A[i]

    def __delitem__(self,i):  # Remove by index
        # >>> l = [1, 2, 3, 4] (Example)
        # >>> del l[0]
        # >>> del l[0]
        # >>> l
        # [3, 4]
        # Task 8
        # Current version __delitem__ does not shrink the array capacity.
        #
        # We want to shrink the array capacity by half if total number of
        # actual elements reduces to one fourth of the capacity.

        if isinstance(i,slice):
            #A=UserDefinedDynamicArray()
            for j in reversed(range(*i.indices(self._n))):
                 del self[j]
        else:
            if i<0:
                i=self._n+i
            for j in range(i,self._n-1):
                self._A[j]=self._A[j+1]
            self[-1]=None        # Calls __setitem__
            self._n-=1
            # TODO
            # Missing some code for Task 8, shrink the size.


    def __str__(self):
        return "[" \
               +"".join( str(i)+"," for i in self[:-1]) \
               +(str(self[-1]) if not self.is_empty() else "") \
               +"]"

    def is_empty(self):
        return self._n == 0

    def __iter__(self):
        for x in range(self._n):
            yield self._A[x]

    def __setitem__(self,i,x):
        if i <0:
            i += self._n
        if i >= self._n or i <0:
            raise IndexError
        self._A[i] = x

    def extend(self,I):
        for x in I:
            self.append(x)

    def reverse(self):
        for x in range(len(self)//2):
            temp = self[x]
            self[x] = self[-x-1]
            self[-x-1] = temp


    def __contains__(self,x):
        for el in range(self._n):
            if self._A[el] == x:
                return True
        return False

    def index(self,x):
        for i in range(self._n):
            if self[i] == x:
                return i
        return None

    def count(self,x):
        cnt = 0
        for el in self:
            if el == x:
                cnt+=1
        return cnt

    def __add__(self,other):
        result = UserDefinedDynamicArray
        for x in self:
            result.append(x)
        for x in other:
            result.append(x)
        return result

    def __mul__(self,times):
        res = UserDefinedDynamicArray()
        for _ in range(times):
            res.extend(self)
        return res

    __rmul__=__mul__

    def pop(self,i=-1):
        res = self[i]
        del self[i]
        return res

    def remove(self,x):     # Remove by value
        # Task 7
        # remove element x from the list, we will delete the first occurrence of element x from the list
        # at first find out the index of element x, then call __del__(self, i) to delete it
        # Your code
        ind = self.index(x)
        del self[ind]

    def max(self):
        max = self[0]
        for x in self:
            if x > max:
                max = x
        return max


    def min(self):
        min = self[0]
        for x in self:
            if x < min:
                min = x
        return min

    def sort(self, order = "asc"):
        # Task 10
        # Sort self._A in ascending order if order == "asc"
        # otherwise sort in descending order if order = 'desc'
        # if order parameter value is wrong, do nothing.
        # Your code
        pass

lst = UserDefinedDynamicArray()
for x in range(10):
    lst.append(x)
lst.reverse()
print(lst)
lst.append(8)



