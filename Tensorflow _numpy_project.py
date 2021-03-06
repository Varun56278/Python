import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(0,10,10) + np.random.uniform(-1.5,1.5,10)
print(x_data)

y_label = np.linspace(0,10,10) + np.random.uniform(-1.5,1.5,10)
print(y_label)

#plt.plot(x_data,y_label,'*')
#plt.show()

print(np.random.rand(2))

m = tf.Variable(0.98)
b = tf.Variable(0.85)

#cost function
error = 0
for x,y in zip(x_data,y_label):
    y_hat = m*x + b
    error += (y-y_hat)**2


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(error)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    epochs = 1

    for i in range(epochs):
        sess.run(train)

    final_slope, final_intercept = sess.run([m,b])

print(final_slope)
print(final_intercept)

x_test = np.linspace(-1,11,10)
y_pred_plot = final_slope*x_test + final_intercept

plt.plot(x_test,y_pred_plot,'g')
plt.plot(x_data,y_label,'*')
plt.show()

