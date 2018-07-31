import tensorflow as tf
from tensorflow.contrib.keras.api.keras.losses import mean_absolute_error, mean_absolute_percentage_error
from metrics import calculate_metrics

a = tf.constant([[4.0, 4.0, 4.0], [3.0, 3.0, 3.0], [1.0, 1.0, 1.0]])
b = tf.constant([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [2.0, 2.0, 2.0]])

with tf.Session() as sess:
    # print(sess.run(tf.reshape(a, [-1])))
    #mae = mean_absolute_error(tf.reshape(a, [-1]), tf.reshape(b, [-1]))

    mmae = tf.reduce_mean(tf.abs(tf.reshape(a, [-1]) - tf.reshape(b, [-1])))
    print(sess.run(mmae))

    mae,mape, rmse = calculate_metrics(tf.reshape(a, [-1]), tf.reshape(b, [-1]))
    print(sess.run(mae))
    print(sess.run(mape))
    print(sess.run(rmse))