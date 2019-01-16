import numpy as np
from keras.preprocessing.image import ImageDataGenerator
#from keras.models import Sequential
#from keras.layers import Dropout, Flatten, Dense
from keras import applications
from keras import backend as K
img_width, img_height = 224, 224
import os
top_model_weights_path = 'bottleneck_fc_model.h5'
#train_data_dir = 'C:\\Users\\Himanshu Bansal\\Desktop\\image'
nb_train_samples = 1
epochs = 50
batch_size = 1


def bottlebeck_features(path):
    K.clear_session()
    print("here2.............")
    #Function to compute VGG-16 CNN for image feature extraction.
    train_data_dir=path[0:26]
    print(train_data_dir)
    #asins = []
    datagen = ImageDataGenerator(rescale=1. / 255)
    # build the VGG16 network
    print("here1.............")
    model = applications.VGG16(include_top=False, weights='imagenet')
    generator = datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode=None,
        shuffle=False)
    print("here3.............")
    #for i in generator.filenames:
        #asins.append(i[0:-5])
    
    bottleneck_features_train = model.predict_generator(generator, nb_train_samples // batch_size)
    #np.save(open('/content/gdrive/My Drive/Colab Notebooks/16k_data_cnn_features.npy', 'wb'), bottleneck_features_train
    #bottleneck_features_train = bottleneck_features_train.reshape((19959,25088))
    print("here4.............")
    #np.save(open('/content/gdrive/My Drive/Colab Notebooks/16k_data_cnn_features.npy', 'wb'), bottleneck_features_train)
    #np.save(open('/content/gdrive/My Drive/Colab Notebooks/16k_data_cnn_feature_asins.npy', 'wb'), np.array(asins))
    print(bottleneck_features_train.shape)
    print (bottleneck_features_train)
    bottleneck_features_train = bottleneck_features_train.reshape((1,25088))
    print(bottleneck_features_train.shape)
    print (bottleneck_features_train)
    K.clear_session()
    print("yes1....")
    
    
    return(bottleneck_features_train)
#bottlebeck_features("C:\\Python35\\image")