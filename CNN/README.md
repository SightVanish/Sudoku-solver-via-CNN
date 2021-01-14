## Sudoku solver with cnn
### How to run

```python train.py```

Currently, it is modified to load pre_trained model (my_model.h5) to predict a sample for 1000 times.

You can use 

```
model.fit(x_train, y_train, batch_size=32, epochs=5)
model.save("my_model.h5")
```

to train you model.

You can use 

```
model = load_model('my_model.h5')
print("Testing accuracy:")
print(test_accuracy(x_test[:50000], y_test[:50000]))
```

to load pre_trained model and test it.

### Note

There is something wrong with Tensorflow. Currently, I am using Tensorflow 2 to train the model and it works well, but I have met error with Tensorflow2. So if you met such problem, try python3.6+tensorflow1.14.

### Reference

https://github.com/shivaverma/Sudoku-Solver
https://github.com/Kyubyong/sudoku
https://blog.csdn.net/zdy0_2004/article/details/74736656

