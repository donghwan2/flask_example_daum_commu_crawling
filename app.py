from flask import Flask, render_template
import crawling

app = Flask(__name__)

@app.route('/')
def hello():

    list_daum, list_daum_href = crawling.daum_crawl()
    list_today, list_today_href = crawling.today_crawl()
    list_clien, list_clien_href = crawling.clien_crawl()

    return render_template('index.html', 
                            daum=list_daum,
                            today=list_today,
                            clien=list_clien, 
                            daum_href=list_daum_href,
                            daum_len = len(list_daum),
                            today_href=list_today_href,
                            today_len=len(list_today),
                            clien_href=list_clien_href,
                            clien_len = len(list_clien)
                            )

@app.route('/about')
def about():
    return "여기는 about 입니다"

if __name__ == '__main__':
    app.run()

