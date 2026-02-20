import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certification')
def certification():
    return render_template('certification.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    basedir = os.path.abspath(os.path.dirname(__file__)) 
    blog_path = os.path.join(basedir, 'data', 'blog.json')  
    
    with open(blog_path, 'r') as f:
        blog_posts = json.load(f)

    return render_template('blog.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
