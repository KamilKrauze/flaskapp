import requests
import json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# Custom modules
import modules.data.globals as glb
import modules.utils.html_items as htmlItems

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    
    response = requests.get(glb.URL_CATEGORIES)    
    JSON_CATEGORIES = response.json()
    CATEGORIES = [item['category'] for item in JSON_CATEGORIES]
    
    list = ""
    for item in CATEGORIES:
        list += '<li><a class="dropdown-item" href="./">' +str(item).capitalize()+ '</a></li>\n'
    
    src = "http://" + glb.IP_NGINX + "/pics/bbb-th.png"
    
    carousel_imgs = ""
    for i in range(10):
        carousel_imgs += htmlItems.carouselItem(src, "Big Buck Bunny", (i==0))
        
    carousel_indicators = ""
    for i in range(10):
        carousel_indicators += htmlItems.carouselIndicator("video-carousel-1", i, (i==0))
    
    return render_template('index.html', categories=list, th_imgs=carousel_imgs, th_img_btns=carousel_indicators)

@app.route('/Test/')
def hello_page():

    
    response = requests.get(glb.URL_VIDEOS)
    print(response)
    JSON_VIDEOS = response.json()
    VIDEOS = [item['video']['Name'] for item in JSON_VIDEOS]
    
    list = ""
    for item in VIDEOS:
        list += "<li>" +str(item).capitalize()+ "</li>\n"
        
    return render_template('index.html', items=list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)