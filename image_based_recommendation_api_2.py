import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances

def the_urls(image_vector):
    url_list=[]
    data=pd.read_csv("C:\\Users\\Himanshu Bansal\\Desktop\\datasets_reco\\flipkart_data\\flipkart_com.csv")
    bottleneck_features_train = np.load('C:\\Users\\Himanshu Bansal\\Desktop\\datasets_reco\\flipkart_data\\reshaped_16k_data_cnn_features.npy')
    asins = np.load('C:\\Users\\Himanshu Bansal\\Desktop\\datasets_reco\\flipkart_data\\16k_data_cnn_feature_asins.npy')
    asins=list(asins)
    #print(asins)
    #df_asins = list(data['asin'])
    #doc_id=12566
    #doc_id=asins.index(df_asins[doc_id])
    dista=pairwise_distances(bottleneck_features_train,image_vector.reshape(1,-1))
    indices=np.argsort(dista.flatten())[0:10]
    list_df=[]
    for i in indices:
        print(i)
        list_df.append(asins[i][7:])
    print(list_df)
    for x in list_df:
        try:
            print(x)
            print(type(x))
            url=(data.loc[(data['uniq_id'])==x,'image'].item()).split()[0]
            url=url[2:-2]
            url_list.append(url)
            print(url)
        except:
            pass
    print(url_list)
    return(url_list)