#ONE HOT ENCODING




























'''
import tensorflow as tf
import numpy as np
a = [.2, 1, 0, 3, -2]
sigmoid_Activation = tf.sigmoid(a)
tanh_Activation = tf.tanh(a)
relu_Activation = tf.nn.relu(a)
with tf.Session() as sess:
    output1 = sess.run(sigmoid_Activation)
    output2 = sess.run(tanh_Activation)
    output3 = sess.run(relu_Activation)
    print("sigmoid_Activation:", output1)
    print("tanh_Activation:", output2)
    print("relu_Activation:", output3)





Scores = [12, 8, .3]
import numpy as np
def softmax(x):
    return np.exp(x)/np.sum(np.exp(x), axis = 0)
print(softmax(Scores))
print(sum(softmax(Scores)))




import numpy as np
def relu_(a):
    return np.maximum(0,a)
relu_(.3)
a = [-4,-2,2,-4]
for i in a:
    print(relu_(i))

    

Scores = [12, 8, .3]
import numpy as np
def softmax(x):
    return np.exp(x)
print(softmax(Scores))
print(sum(softmax(Scores)))




import numpy as np
#tanh(a) = (e^a - e^-a)/e^a + e^-a
def tanh_(a):
    return np.tanh(a)
tanh_(.3)
a = [-4,-2,0,2,4]
for i in a:
    print(tanh_(i))




import numpy as np
def sigmoid_(a):
    return 1/(1+np.exp(-a))
sigmoid_(.3)
a = [1,2,4,0,5,-6,7]
for i in a:
    print(sigmoid_(i))


#TENSORFLOW MATH

import tensorflow as tf
x = tf.add(5, 2)
print(x)

y = tf.subtract(10, 4)
print(y)

z = tf.multiply(2, 5)
print(z)

#Converting data types

with tf.Session() as sess:
    print(sess.run(tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))))

#Tensorflow devide
x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.divide(x,y),tf.cast(tf.constant(1),tf.float64))

with tf.Session() as sess:
    output = sess.run(z)
    print(output)







#Tensorflow Variable
import tensorflow as tf
W1 = tf.Variable([.5], tf.float32)
init =  tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(W1))

W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.9], tf.float32)
x = tf.placeholder(tf.float32)

linear_model =  W*x + b
init =  tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(linear_model,{x:[1,2,3,4,5,7]}))




import tensorflow as tf
p = tf.placeholder(tf.float32)
q = tf.placeholder(tf.float32)
r = p+q
sess = tf.Session()
print(sess.run(r,feed_dict={p:[1,7,6], q:[3,20,2]}))

import tensorflow as tf
z = r * 5
print(sess.run(z,{p: [[1,2,3],
    [2,3,4],
    [3,2,1]], q: [[10,2,3],
    [2,3,4],
    [3,2,1]]}))


import tensorflow as tf
m = tf.constant(3.0, tf.float32)
n = tf.constant(4.0)
print(m,n)

sess = tf.Session()
print(sess.run([m,n]))
sess.close()




import tensorflow as tf
hello_constant = tf.constant('Hello World!')
print(hello_constant)
with tf.Session() as sess:
    b = sess.run(hello_constant)
print(b)


import tensorflow as tf
a = tf.constant(4.0)
b = tf.constant(3.0)
c = a * b
print(c)
sess = tf.Session()
print(sess.run(c))
sess.close()

'''
