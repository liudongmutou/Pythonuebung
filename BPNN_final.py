from __future__ import print_function
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
#Tensorflow的图必须在一个会话(Session)中来计算。Session提供了Operation执行和Tensor求值的环境。
from sklearn.utils import shuffle
from sklearn import preprocessing
#使用tf.InteractiveSession()来构建会话的时候，我们可以先构建一个session然后再定义操作（operation），如果我们使用tf.Session()来构建会话我们需要在会话构建之前定义好全部的操作（operation）然后再构建会话。
sess = tf.InteractiveSession()
flags = tf.app.flags
FLAGS = flags.FLAGS


#conduct 3 layers ANN
def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    # add one more layer and return the output of this layer
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name + '/weights', Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
            tf.summary.histogram(layer_name + '/biases', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)   #tf.matmul是矩阵乘法
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b, )
        tf.summary.histogram(layer_name + '/outputs', outputs)
    return outputs

def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, y_: v_ys})
    return result

data = pd.read_excel(r"F:\mat\CluRhoM1P51.xlsx")
X=data[data.columns[1:3]].values
y=data[data.columns[3]].values
Y = tf.one_hot(indices=y, depth=5, on_value=1., off_value=0., axis=
1, name="label_onehot").eval()  # 把输出变成one_hot类型,只用0 1表示类别
X, Y = shuffle(X, Y) #打乱顺序
scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(X)  #数据归一化
#c=X.shape[0];
Xtr = X[0:220, :]
Ytr = Y[0:220, :]
Xt = X[221:442, :]
Yt = Y[221:442, :]
Xtr, Ytr = shuffle(Xtr, Ytr, random_state=0)  # 为什么要打乱2次
# batch_xs, batch_ys = mnist.train.next_batch(100)
batch_xs, batch_ys = Xtr, Ytr

# Define loss and optimizer
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 2], name='x_input')
    y_ = tf.placeholder(tf.float32, [None, 5], name='output')
l1 = add_layer(xs, 2, 3, n_layer=1,activation_function=tf.nn.relu) #从输入到隐藏层，输入2个节点，隐藏层3个节点，激励函数为relu
t = add_layer(l1, 3, 5, n_layer=2,activation_function=tf.nn.softmax)  #从隐藏层到输出层，隐藏层3个节点，输入5个节点,激励函数为softmax
prediction=t

with tf.name_scope('cross_entropy'):
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(t),
                                                  reduction_indices=[1]))  # 应该是一个交叉熵算法，这里就相当于cost function了.平均误差
    tf.summary.scalar('cross_entropy', cross_entropy)
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
# Train


sess = tf.Session()
merged = tf.summary.merge_all()

init = tf.global_variables_initializer()
sess.run(init)
writer = tf.summary.FileWriter('C:/logfile', tf.get_default_graph())
writer.close()
for i in range(1000):  #训练100次
    sess.run(train_step, feed_dict={xs: batch_xs, y_: batch_ys})   #传入数据
    if i % 100 == 0:  #每隔50步记录一下result
        result = sess.run(merged, feed_dict={xs: batch_xs, y_: batch_ys})
        writer.add_summary(result, i) #i记录步数
        #print(sess.run(cross_entropy, feed_dict={xs: batch_xs, y_: batch_ys}))
        print(compute_accuracy(batch_xs, batch_ys))
        plt.pause(0.1)

fig = plt.figure()   #生成一个图片框
ax = fig.add_subplot(1,1,1)
plt.ion()
plt.show()
