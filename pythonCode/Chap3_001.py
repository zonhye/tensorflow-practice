#!/usr/bin
# -*- coding: utf-8 -*-
#tensor、session的概念和使用

import tensorflow as tf

a = tf.constant([1.0, 2.0], name = "a")
b = tf.constant([2.0, 3.0], name = "b")

result = a + b

print('tensor的三个属性'.encode('utf-8'))
print(result)
print('使用get_shape函数获取tensor的维度信息'.encode('utf-8'))
print(result.get_shape())

#建立session，并且执行定义好的计算
sess = tf.Session()
print(sess.run(result))
print(result.eval(session = sess))

#关闭session
sess.close()
