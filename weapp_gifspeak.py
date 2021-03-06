'''
Flask webapp for gif speak
'''

from flask import Flask
import os
from flask import render_template, request, send_from_directory
from extractor import Extractor
from get_gif import Get_Giffer

HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
PORT = int(os.environ.get('PORT', 5000))

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def starting_page(top_story1=None):
    top_story1 = text_input(url1=None,url2=None,url3=None,url4=None,url5=None)
    return render_template('newHome.html', top_story1=top_story1)

@app.route('/test')
def test():
    return render_template('newHome.html')

@app.route('/about_us')
def about_team():
    return render_template('about_us.html')

@app.route('/about_project')
def about_project():
    return render_template('about_project.html')

@app.route('/the_app', methods=['GET','POST'])
def the_app(url=None):
    if request.method == 'POST':
        return redirect('home.html')
    return render_template('find_text_2_gif.html', url=url)


@app.route('/text_input', methods=['GET', 'POST'])
def text_input(url1=None, url2=None, url3=None, url4=None, url5=None):
    if request.method == 'POST':
        result = request.form
        for key, val in result.items():
            if key == 'url':
                urlNews = val
                print(urlNews)
        if request.form['GIF!'] and request.form['url']:
            #this is where the code would go to call sams function
            result = request.form['url']
            search_list = Get_Giffer(result)
            Gif_list = Get_Giffer.get_json(search_list)
            sentiment = Get_Giffer.output_sentiment(search_list)
            giffy = Extractor(Gif_list,sentiment)
            url_list = Extractor.running_gifs(giffy)
            url1 = url_list[0]
            url2 = url_list[1]
            url3 = url_list[2]
            url4 = url_list[3]
            url5 = url_list[4]
            return render_template('gif_results.html', urlNews=urlNews, url1=url1,url2=url2, url3=url3,url4=url4,url5=url5)
        else:
            return render_template('find_text_2_gif.html')

    else:
        return render_template('home.html')

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(port=5001)
=======

    #app.run(port=5002)

    app.run(app.run(host=HOST, port=PORT))
>>>>>>> 2bf3b5f2193f96b73a6fbd74750f8087f4e4fa25
