import numpy as np

from config import conf
from lib.utility import utils
from lib.model import double_layer_nn as dlnn


def main():
    print('start...')
    print(conf.METADATA_FILE)
    meta = utils.pickle_load(conf.METADATA_FILE)
    label_and_data = utils.pickle_load(conf.DATA_FILE)
    np.random.shuffle(label_and_data)
    length = len(label_and_data)
    boundary = int(length * conf.TRAINING_DATA_RATIO)
    test = label_and_data[boundary:]
    train = label_and_data[0:boundary - 1]
    print(len(test))
    print(len(train))
    print(meta.categories)
    num_categories = len(meta.categories)
    predict_label = test[:, 0].tolist()
    predict_data = test[:, 1].tolist()

    nn = dlnn.DoubleLayerNetwork(conf.LEARNING_RATE,
                                 conf.NUM_UNITS1, conf.NUM_UNITS2,
                                 conf.NUM_UNITS3, conf.NUM_UNITS4,
                                 conf.PCA_DIMENSION, num_categories,
                                 conf.LOG_FILE)

    for step in range(conf.TOTAL_STEP):

        np.random.shuffle(train)
        batch_label = train[:conf.BATCH_SIZE, 0].tolist()
        batch_data = train[:conf.BATCH_SIZE, 1].tolist()

        nn.sess.run(nn.train_step, feed_dict={
            nn.x: batch_data, nn.t: batch_label,
            nn.keep_prob: conf.KEEP_PROB})

        if step % 100 == 0:
            stdout_log(
                step=step,
                curModel=nn,
                data=predict_data,
                label=predict_label
            )

def stdout_log(step, curModel, data, label):
    summary, loss_val, acc_val = curModel.sess.run(
        [curModel.summary, curModel.loss, curModel.accuracy],
        feed_dict={curModel.x: data, curModel.t: label, curModel.keep_prob: 1.0}
    )
    print('Step: %d, Loss: %f, Accuracy: %f' % (step, loss_val, acc_val))
    curModel.writer.add_summary(summary, step)

if __name__ == '__main__':
    main()