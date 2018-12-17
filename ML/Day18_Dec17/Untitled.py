
# coding: utf-8

# In[6]:


"""
   Q 1. Create a tensor of the shape [2, 3] with all elements set to zero.
"""

import tensorflow as tf
session = tf.Session()

a = tf.zeros([2,3])
print a
out = session.run(a)
print out

"""
   Q  2. Let X be a tensor of [[1,2,3], [4,5,6]].
    Create a tensor of the same shape and dtype as X with all elements set to zero
"""
b = tf.zeros_like([[1,2,3], [4,5,6]],tf.int32)
out1 = session.run(b)
print out1



# In[7]:


"""
    3. Create a tensor of shape [2, 3] with all elements set to one.
"""
c = tf.ones([2,3])
out2 = session.run(c)
print out2


# In[9]:


""" 
    4. Let X be a tensor of [[1,2,3], [4,5,6]].
    Create a tensor of the same shape and dtype as X with all elements set to one.
"""
d = tf.ones_like([[1,2,3], [4,5,6]], tf.int32)
out3 = session.run(d)
print out3



# In[13]:


"""
    5. Create a tensor of the shape [3, 2], with all elements of 5.
"""
e = tf.fill([3,2],value=5)
out4 = session.run(e)
print out4


# In[20]:


"""
    6. Create a constant tensor of [[1, 3, 5], [4, 6, 8]], with dtype=float32
"""
f = tf.constant([[1, 3, 5], [4, 6, 8]], dtype=tf.float32)
out5 = session.run(f)
print out5


# In[23]:


"""
    7. Create a constant tensor of the shape [2, 3], with all elements set to 4.
"""
h = tf.constant([[4,4,4],[4,4,4]], dtype=tf.float32)
out6 = session.run(h)
print out6


# In[28]:


"""
    8. Create a 1-D tensor of 50 evenly spaced elements between 5 and 10 inclusive.
"""
i = tf.linspace(5.0,10.0,50, name="l")
out7 = session.run(i)
print out7


# In[31]:


"""
    9. Create a random tensor of the shape [3, 2], with elements from a normal distribution of 
    mean=0, standard deviation=2.
"""
j = tf.random_normal([3,2],mean=0,stddev=2)


# In[32]:


out8 = session.run(j)
print out8


# In[35]:


"""
    10. Create a random tensor of the shape [3, 2], with all elements from a uniform distribution that
    ranges from 0 to 2 (exclusive).
"""
k = tf.random_uniform([3,2],minval=0,maxval=2)
out9 = session.run(k)
print out9
                      


# In[36]:


"""
    11. Let X be a tensor of [[1, 2], [3, 4], [5, 6]]. Shuffle X along its first dimension.
"""
l = tf.random_shuffle([[1, 2], [3, 4], [5, 6]])
out10 = session.run(l)
print out10


# In[39]:


"""
    12. Let X be a random tensor of the shape [10, 10, 3], with elements from a unit normal
    distribution. Crop X with the shape of [5, 5, 3]. (hint: 5, 3]) out = tf.random_crop(X, [5,5,3])
"""
m = tf.random_normal([10,10,3])
out11 = tf.random_crop(m, [5,5,3])
print (session.run(out11))


# In[42]:


"""
    13. Let X be a tensor [[-1, -2, -3], [0, 1, 2]] and Y be a tensor of zeros with the same shape as
    x. Return a boolean tensor that yields True if X does not equal Y elementwise. (hint : out
    = tf.not_equal(X, Y))
"""
x = tf.constant([[-1,-2,-3],[0,1,2]],dtype=tf.float32)
print session.run(x)
y = tf.zeros([2,3],dtype=tf.float32)
print session.run(y)
out = tf.not_equal(x,y)
print session.run(out)


# In[44]:


"""
    14. Add x and y element-wise. (hint: out = tf.add(x, y))
"""
x = tf.constant([1,2,3], name ="x")
y = tf.constant([1,1,1], name ="y")
z = tf.constant([5,6,7], name ="z")
out = tf.add(x,y)
print session.run(out)




# In[47]:


"""
    15. Subtract y from x element-wise.
"""
out = tf.subtract(y,x)
print session.run(out)


# In[48]:


"""
    16. Multiply x by y element-wise.
"""

out = tf.multiply(y,x)
print session.run(out)


# In[49]:


"""
    17. Multiply x by 5 element-wise.
"""
out = tf.multiply(y,5)
print session.run(out)
out = tf.multiply(x,5)
print session.run(out)


# In[50]:


"""
    18. Add x, y, and z element-wise.
"""
out = tf.add_n([x,y,z])
print session.run(out)


# In[56]:


"""
    19. View the output using tensorboard for random questions
"""
writer = tf.summary.FileWriter(logdir='./file1', graph=session.graph)
writer.close()

