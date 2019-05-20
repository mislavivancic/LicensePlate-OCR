import tensorflow as tf

W = tf.Variable([.3])
b = tf.Variable([-.3])
x= tf.placeholder(tf.float32)
#Model
linear_model = W*x + b 
#Calculate Loss
y = tf.placeholder(tf.float32)

squaredelta = tf.square(linear_model - y)
loss = tf.reduce_sum(squaredelta)

optimize = tf.train.GradientDescentOptimizer(0.01)
train = optimize.minimize(loss)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(1000):
    sess.run(train,{x:[1,2,3],y:[0,-1,-2]})


print(sess.run([W,b]))
print(sess.run(loss,{x:[1,2,3],y:[0,-1,-2]})) 


#print(sess.run(squaredelta,{x:[1,2,3],y:[0,-1,-2]}))




