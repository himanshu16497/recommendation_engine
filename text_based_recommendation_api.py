from flask import Flask,render_template,request
from text_based_recommendation_api_1 import image_urls

app=Flask(__name__, template_folder= "C:\\Python35\\templates")
app.config['TEMPLATES_AUTO_RELOAD']=True

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

if __name__=='__main__':
    app.run()