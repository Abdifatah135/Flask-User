

from flaskblog import app

app = create_app('production')
if __name__ == '__main__':
    app.run(debug=True)