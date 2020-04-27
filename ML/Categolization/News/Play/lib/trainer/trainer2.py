import os
import numpy as np

from config import conf
from lib.utility import utils
from lib.model.dlnn_karal import Dlnn as dlnn


def main():
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
    #
    np.random.shuffle(train)
    label = train[:, 0]
    data = train[:, 1]
    n_batch = len(label)
    n_categories = len(meta.categories)
    predict_label = test[:, 0].tolist()
    predict_data = test[:, 1].tolist()

    model = dlnn()
    model.set_model(n_batch, conf.NUM_UNITS1, n_categories)

    print(np.array([label]).shape)
    print(np.array([label]).shape)
    print(n_categories)
    model.fit(np.array([data]), np.array([label]))

if __name__ == '__main__':
    main()

