from flask import Flask,render_template,request
from image_based_recommendation_api_1 import bottlebeck_features
from image_based_recommendation_api_2 import the_urls
from text_based_recommendation_api_1 import image_urls
import numpy as np
import os
app=Flask(__name__, template_folder= "C:\\Python35\\templates")
app.config['TEMPLATES_AUTO_RELOAD']=True
app.config['UPLOAD_FOLDER']=("C:\\Python35\\image\\subfolder\\")

@app.route('/')
def hello():
    return render_template('front_end.html')
@app.route('/result',methods = ['POST', 'GET'])
def hello1():
    if(request.method=='POST'):
        data = request.form['customer']
        url_list=image_urls(data)
        #return (str(url_list[0]))
        #return (type(url_list[0]))
        return render_template('fron_end2.html',url_list=url_list)
    else:
        return ("error")
@app.route('/img_res',methods=['POST','GET'])
def image_rec():
    if(request.method=='POST'):
        if 'ima' not in request.files:
            #return(len(request.files))
            return('No file part')
        #return((request.files))
        file =request.files['ima']
        if not file:
            return("no uploads")
        else:
            path= "C:\\Python35\\Upload_folder\\New folder\\"+str(file.filename)
            file.save(path)
            file.close()
            vector=bottlebeck_features(path)
            print("yes")
            #os.chmod(path, 0o777)
            #os.remove(path)
            #np.save("C:\\Python35\\Upload_folder\\user_img.npy",vector)
            #return(path)
            os.remove(path)
            url_list=the_urls(vector)
            print(url_list)
            return render_template('fron_end2.html',url_list=url_list)
            #return (path)
    else:
        return("no file uploaded")

if __name__=='__main__':
    app.run(threaded=False)