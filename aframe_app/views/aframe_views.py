from flask import render_template, request



class AFrameViews():
    def aframe01():
        return render_template("aframe/test01.html")

    def aframe02():
        return render_template("aframe/test02.html")