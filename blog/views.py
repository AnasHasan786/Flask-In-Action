from . import blog_bp

@blog_bp.route('/posts')
def posts():
    return "Welcome to the Blog Posts Page"

@blog_bp.route('/new_post')
def new_post():
    return "Create a New Blog Post"



