from aframe_app import app
from aframe_app.views.aframe_views import AFrameViews
from aframe_app.views.blog_views import BlogViews
from aframe_app.views.live2d_view import ProjectTestViews


@app.route('/', methods=['GET'])
def blog_index():
    return BlogViews.index()


# ------------------------------------------------------
# 測試 AFrame
# ------------------------------------------------------

@app.route('/aframe01', methods=['GET'])
def aframe01():
    return AFrameViews.aframe01()

@app.route('/aframe02', methods=['GET'])
def aframe02():
    return AFrameViews.aframe02()

@app.route('/test1', methods=['GET'])
def test1():
    return ProjectTestViews.proejctTeste01()



if __name__ == '__main__':
    app.run()
