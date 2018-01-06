
# coding: utf-8

# In[1]:


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))


# In[2]:


x = 3
print(type(x)) # Prints "<class 'int'>"
print(x)       # Prints "3"
print(x + 1)   # Addition; prints "4"
print(x - 1)   # Subtraction; prints "2"
print(x * 2)   # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y)) # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"


# In[3]:


t = True
f = False
print (type(t))
print (t and f)
print (t or f)
print (not t)
print (t!= f)


# In[4]:


hello = 'hello'
world = 'world'
print (hello)
print (world)
print (len(hello))
print (hello + ' ' + world)
hw = '%s %s %d' %(hello, world, 12)
print hw


# In[9]:


s = "hello"
print (s.capitalize())
print (s.upper())
print (s.rjust(7))
print (s.ljust(7))
print (s.center(7))
print (s.replace('l', 'o'))
print ('   world   '.strip())


# In[12]:


xs = [3, 1, 2]
print (xs, xs[2])
print (xs[-1])
xs[2] = 'foo'
print (xs)
xs.append('bar')
print (xs)


# In[14]:


nums = list(range(5))
print (nums)
print (nums[2:4])
print (nums[2:])
print (nums[:2])
print (nums[:])
print (nums[:-1])
nums[2:4] = [8,9]
print (nums)


# In[19]:


animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print (animal)


# In[20]:


nums = [0, 1,2,3,4]
square = []
for x in nums:
    square.append(x**2)
print (square)


# In[21]:


nums = [0, 1, 2, 3, 4]
square = [x ** 2 for x in nums]
print (square)


# In[2]:


d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print(d['cat'])       # Get an entry from a dictionary; prints "cute"
print('cat' in d)     # Check if a dictionary has a given key; prints "True"
d['fish'] = 'wet'     # Set an entry in a dictionary
print d
print(d['fish'])      # Prints "wet"
# print(d['monkey'])  # KeyError: 'monkey' not a key of d
print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"
del d['fish']         # Remove an element from a dictionary
print(d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"


# In[10]:


d = {'person': 2, 'cat': 4, 'spider':8}
for animal, leg in d.items():
    print ('%s %d' %(animal, leg))


# In[9]:


nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  # Prints "{0: 0, 2: 4, 4: 16}"


# In[7]:


animals = {'cat', 'dog'}
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))       # Number of elements in a set; prints "3"
animals.add('cat')        # Adding an element that is already in the set does nothing
print(len(animals))       # Prints "3"
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Prints "2"


# In[11]:


animals = ['cat', 'dog', 'fish']
for idx, animal in enumerate(animals):
    print ('#%d: %s' %(idx, animal))


# In[14]:


from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print (nums)


# In[18]:


d = {(x, x+1): x for x in range(10)}
t = (5,6)
print (type(t))
print (d[t])
print (d[1,2])
print d


# In[19]:


def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))


# In[21]:


def hello(name, loud = False):
    if loud:
        print ('HELLO, %s!' %name.upper())
    else:
        print ('Hello, %s' %name)
hello('Bob')
hello('Fred', loud = True)

