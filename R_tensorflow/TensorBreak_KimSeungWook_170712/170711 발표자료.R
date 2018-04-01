#170711 kaggle_2
#reticulate = python numpy같은거 다 쓸수 있음

rm(list=ls())
gc() #컴퓨터 메모리리


library(tensorflow)

tf$reset_default_graph()
datasets = tf$contrib$learn$datasets
mnist = datasets$mnist$read_data_sets("MNIST-data", one_hot = TRUE)

sess = tf$InteractiveSession() # 뭔차이? - tensor 유연하게 다루려고 ㅎ..

#Softmax Regression - 숫자분류 (명목형 로지스틱 회귀)
#sess$close()


x  = tf$placeholder(tf$float32, shape(NULL, 784L)) #픽셀 28*28 / L - 명목화 
y_ = tf$placeholder(tf$float32, shape(NULL,  10L))

W <- tf$Variable(tf$zeros(shape(784L, 10L)))
b <- tf$Variable(tf$zeros(shape(10L)))

sess$run(tf$global_variables_initializer()) #전역변수 초기화/ 준비단계!


#Prediction & Loss Function
y = tf$nn$softmax(tf$matmul(x,W) + b) #x: input image W: weight matrix b: bias matmul(): Multiplies matrix a by matrix b, producing a * b.
cross_entropy = tf$reduce_mean(-tf$reduce_sum(y_ * tf$log(y), reduction_indices = 1L)) #reduce 가 약간 aggregate 함수랑 비ㅅ슷
cross_entropy

optimizer = tf$train$GradientDescentOptimizer(0.5)
train_step = optimizer$minimize(cross_entropy)
train_step

for(i in 1:1000){
  batches = mnist$train$next_batch(100L)
  batch_xs = batches[[1]]
  batch_ys = batches[[2]]
  sess$run(train_step,
           feed_dict = dict(x = batch_xs, y_ = batch_ys))

}

correct_prediction = tf$equal(tf$argmax(y, 1L), tf$argmax(y_, 1L))
accuracy = tf$reduce_mean(tf$cast(correct_prediction, tf$float32))
accuracy$eval(feed_dict = dict(x  = mnist$test$images,
                               y_ = mnist$test$labels))

sess$close()
# [Part 2]
# Multilayer ConvNet
# Weight Initialization

sess=tf$InteractiveSession()

weight_variable = function(shape){
  initial = tf$truncated_normal(shape, stddev = 0.1) #양쪽끝이 조금 잘린 정규분포 (양끄무한방지..)
  tf$Variable(initial)
}

bias_variable = function(shape){
  initial = tf$constant(0.1, shape = shape)
  tf$Variable(initial)
}

#Convolution and Pooling

conv2d = function(x, W){
  tf$nn$conv2d(x, W, strides=c(1L, 1L, 1L, 1L), padding = "SAME")
}

max_pool_2x2 = function(x){
  tf$nn$max_pool(x, 
                 ksize   = c(1L, 2L, 2L, 1L),
                 strides = c(1L, 2L, 2L, 1L), 
                 padding = "SAME")
}

#First Convolution Layer
W_conv1 = weight_variable(shape(5L, 5L, 1L, 32L))
b_conv1 = bias_variable(shape(32L))
x_image = tf$reshape(x, shape(-1L, 28L, 28L, 1L)) #-1 1 은 테두
h_conv1 = tf$nn$relu(conv2d(x_image, W_conv1) + b_conv1) #relu- 활성함수 (sigmoid function느낌)
h_pool1 = max_pool_2x2(h_conv1)

#Second Convolution Layer
W_conv2 = weight_variable(shape = shape(5L, 5L, 32L, 64L))
b_conv2 = bias_variable(shape = shape(64L))

h_conv2 = tf$nn$relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

#Densely Connected Layer
W_fc1 = weight_variable(shape(7L * 7L * 64L, 1024L))
b_fc1 = bias_variable(shape(1024L))

h_pool2_flat = tf$reshape(h_pool2, shape(-1L, 7L * 7L * 64L))
h_fc1 = tf$nn$relu(tf$matmul(h_pool2_flat, W_fc1) + b_fc1)


#dropout - overfitting 방지 ->일부러 노이즈 넣음 (overfitting 공부한거만 맞)
keep_prob = tf$placeholder(tf$float32)
h_fc1_drop = tf$nn$dropout(h_fc1, keep_prob)

#Readout Layer
W_fc2 = weight_variable(shape(1024L, 10L))
b_fc2 = bias_variable(shape(10L))

y_conv = tf$nn$softmax(tf$matmul(h_fc1_drop, W_fc2) + b_fc2)

#Train and Evaluate the Model
cross_entropy = tf$reduce_mean(-tf$reduce_sum(y_ * tf$log(y_conv), reduction_indices = 1L))
train_step = tf$train$AdamOptimizer(1e-4)$minimize(cross_entropy)
correct_prediction = tf$equal(tf$argmax(y_conv, 1L), tf$argmax(y_, 1L))
accuracy = tf$reduce_mean(tf$cast(correct_prediction, tf$float32))
sess$run(tf$global_variables_initializer())

for(i in 1:500){
  batch = mnist$train$next_batch(50L)
  if(i %% 100 == 0){
    train_accuracy = accuracy$eval(feed_dict = dict(x  = batch[[1]],
                                                    y_ = batch[[2]],
                                                    keep_prob = 1.0))
    cat(sprintf("step %d, training accuracy %g\n", i, train_accuracy))
  }
  train_step$run(feed_dict = dict(x  = batch[[1]],
                                  y_ = batch[[2]],
                                  keep_prob = 0.5))
}

test_accuracy = accuracy$eval(feed_dict = dict(x  = mnist$test$images, 
                                               y_ = mnist$test$labels,
                                               keep_prob = 1.0))
cat(sprintf("test accuracy %g", test_accuracy))

