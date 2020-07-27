import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'vid_vault'
app.config["MONGO_URI"] = "mongodb+srv://root:rootCode99@mycicluster-cecn6.mongodb.net/vid_vault?retryWrites=true&w=majority"
app.secret_key = "a1b2c3d4e5f6g7"

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/videos')
def videos():
    all_videos = mongo.db.videos.find()
    return render_template('videos.html', videos=all_videos)

@app.route('/add',methods=['GET','POST'])
def add():
    url = get_youtube_embed_link(request.form['url'])
    category = request.form['category']
    comment = request.form['comment']
    rating = request.form['rating']

    new_video = {'url': url, 'category': category, 'comment': comment, 'rating': rating}
    mongo.db.videos.insert(new_video)

    flash('Video added(!)')
    return redirect(url_for('home'))

@app.route('/search', methods=['GET','POST'])
def search():
    videos = []
    result = ""
    if request.method=='POST':
        category = request.form['category']
        videos = mongo.db.videos.find({'category': category.lower()})
        if videos.count() == 0:
            result = 'No videos found(!)'

    return render_template('search.html', videos=videos, result=result)

@app.route('/delete/<id>')
def delete(id):
    mongo.db.videos.remove({'_id': ObjectId(id)})
    flash("Video deleted")
    return redirect(url_for('home'))

@app.route('/edit/<id>')
def edit(id):
    video = mongo.db.videos.find_one({'_id': ObjectId(id)})
    return render_template('edit.html', video=video)

@app.route('/update/<id>', methods=['GET','POST'])
def update(id):
    category = request.form['category']
    comment = request.form['comment']
    rating = request.form['rating']

    mongo.db.videos.update_one({'_id': ObjectId(id)},{'$set': {'category': category,'comment': comment,'rating': rating}})
    flash('Video info updated(!)')
    return redirect(url_for('home'))

def get_youtube_embed_link(youtube_link):
    return youtube_link[:23] + '/embed/' + youtube_link[32:]

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
