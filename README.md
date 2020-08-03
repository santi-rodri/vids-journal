# YOUTUBE VIDEO-JOURNAL

The Youtube Video-Journal is a web app that let users store their **favourite youtube videos** in a personal video-journal.
Videos can be organized by **category** and **rating**.

## UX

This web app has been designed with a **mobile-first** approach in mind, as most people nowadays access the Internet by using their smart phones.

Special attention has been paid to make the app **responsive** to different screen sizes so the content can be viewed in a clear and well structured way.

## Features

The web app has been divided into 2 different areas, resulting in 2 vertical panels:

### Left Panel:
+ Video-Form with 4 main fields:
1. **Youtube Video URL**: here the user must copy and paste the youtube link they wish.
A field validator is in place to make sure the link has the right format.

2. **Category**: a category must be assigned to each video, so they can be easily found later.

3. **Comment**: the user may add any comments to the video up to 500 characters long.

4. **Rating**: a rating from 1 to 5 must be chosen for each video.

### Right Panel:
+ Upper area:
Left: An "**All Videos**" button let us retrieve all the videos we have stored in our video-journal.
Right: A **category search** option is provided so we can quickly retrieve our videos by category.

+ Main area:
This is where videos are displayed.
**Update** and **Delete** options are provided in case the user would like to modify the category, comments or rating.
  
## Technologies used
 
 - **HTML5** : Page structure
 
 - **CSS3** : Styling
 
 - **Materialize** : Responsiveness and form styling

 - **Python**, **Flask** framework and **Jinja2** : Backend operations

 - **Mongodb** : Document based database system
 
 - **Javascript** : Form validation
 
 - **jQuery** : Frontend effects


## Testing

- The website has been tested for **reponsiveness** for all different screen sizes, using the Google Chrome built-in Inspector tool.

- Tests were carried out for **form validation**.


## Deployment

The entire project has been uploaded to **Github**, and then, making use of the **GitPod** interface, it was deployed to **Heroku**, making sure that the mongodb database credentials are securely stored as config variables on Heroku.

## Media

 - **Videos**: all the videos stored in the personal video-journal are freely available youtube videos.


