from flask import render_template, request



class BlogViews():
    def index():
        return render_template("blog/index.html")