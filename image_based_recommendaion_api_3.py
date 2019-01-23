import pickle

def image_hirarchy(vec):
    model=pickle.load(open("C:\\Users\\Himanshu Bansal\\Desktop\\datasets_reco\\flipkart_data\\svm_labels_model",'rb'))
    res=model.predict(vec)
    return res