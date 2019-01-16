import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances
#from PIL import Image
#import requests
#from io import BytesIO
#import matplotlib.pyplot as plt

def image_urls(customer_input): 
    data=pd.read_csv("C:\\Users\\Himanshu Bansal\\Desktop\\datasets_reco\\flipkart_data\\flipkart_without_stop.csv")
    #customer_input=input("what is it that you desire?")
    customer_input=customer_input.lower()
    length=data.shape[0]
    x=pd.Series([0,0,0,0,0,0],index=data.columns)
    data=data.append(x,ignore_index=True)

    data['product_name'].iloc[length]=customer_input
    tdidf=TfidfVectorizer(min_df=0)
    results=tdidf.fit_transform(data['product_name'])
    dist=pairwise_distances(results[0:length],results[length])
    indexes=np.argsort(dist.flatten())[0:4]
    url_list=[]
    for x in indexes:
        url=(str(data['image'].iloc[x]).split()[0])
        url=url[2:-2]
        print(url)
        url_list.append(url)
    #url=''.join(url)
    #print(url)
    #response=requests.get(url)
    #img=Image.open(BytesIO(response.content))
    #print(type(data['uniq_id'].iloc[x]))
    #img.save("C:\\Users\\Himanshu Bansal\\Desktop\\datasets_reco\\flipkart_data\\images\\"+str(data['uniq_id'].iloc[x])+'.jpeg')
    #plt.imshow(img)
    #plt.show()
    return (url_list)
