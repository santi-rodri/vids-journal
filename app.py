import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ['MONGO_DBNAME']
app.config['MONGO_URI'] = os.environ['MONGO_URI']
app.secret_key = os.environ['secret_key']

mongo = PyMongo(app)

@app.route('/')
def home():
    all_videos = mongo.db.videos.find()
    num_videos = all_videos.count()
    if num_videos == 0:
        return render_template('index.html', num_videos=num_videos)
    return render_template('videos.html', videos=all_videos, num_videos=1)

@app.route('/allvideos')
def allvideos():
    all_videos = mongo.db.videos.find()
    num_videos = all_videos.count()

    return render_template('videos.html', videos=all_videos, num_videos=num_videos)

@app.route('/add',methods=['GET','POST'])
def add():
    url = get_youtube_embed_link(request.form['url'].strip())
    category = request.form['category'].strip().replace(" ","")
    comment = request.form['comment'].strip()
    rating = request.form['rating']

    video_unique_verification = mongo.db.videos.find({'url': url})
    verification_result = video_unique_verification.count()
    if verification_result == 0:
        new_video = {'url': url, 'category': category, 'comment': comment, 'rating': rating}
        mongo.db.videos.insert(new_video)

        videos = mongo.db.videos.find()
        num_videos = videos.count()
        video_just_added = videos[num_videos-1]
        id = video_just_added['_id']
        video = mongo.db.videos.find({'_id': ObjectId(id)})
        return render_template('videos.html', videos=video, num_videos=1)
    else:
        flash("This video already existed","video_already_exists")
        return render_template('videos.html', videos=video_unique_verification, num_videos=1)

@app.route('/search_by_category', methods=['GET','POST'])
def search_by_category():
    videos = []
    if request.method=='POST':
        category = request.form['category'].strip()
        videos_on_category = mongo.db.videos.find({'category': category.lower()})
        num_videos_on_category = videos_on_category.count()
        if num_videos_on_category != 0:
            return render_template('videos.html', videos=videos_on_category, num_videos=num_videos_on_category)
        else:
            flash_message = "No videos found for category " + category.upper()
            flash(flash_message,"category_not_found")
            videos = mongo.db.videos.find();
            return render_template('videos.html', videos=videos, num_videos=1)

@app.route('/delete/<id>')
def delete(id):
    mongo.db.videos.remove({'_id': ObjectId(id)})
    flash("Video successfully deleted (!)","video_deleted")
    return redirect(url_for('home'))

@app.route('/update/<id>', methods=['GET','POST'])
def update(id):
    category = request.form['category'].strip().replace(" ","")
    comment = request.form['comment'].strip()
    rating = request.form['rating']

    mongo.db.videos.update_one({'_id': ObjectId(id)},{'$set': {'category': category,'comment': comment,'rating': rating}})
    flash("Successfully updated","video_updated")
    video = mongo.db.videos.find({'_id': ObjectId(id)})
    return render_template('videos.html', videos=video, num_videos=1)

def get_youtube_embed_link(youtube_link):
    return youtube_link[:23] + '/embed/' + youtube_link[32:]

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
