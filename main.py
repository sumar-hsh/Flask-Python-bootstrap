from flask import Flask, render_template

app = Flask(__name__)



image_data = {
        "kate": {"title": "Kate", "description": "A portrait of Kate.", "img_url": "static/img/kate.jpg"},
        "Morgan": {"title": "Morgan", "description": "A portrait of Morgan.", "img_url": "static/img/Morgan.jpg"},
        "Slavic": {"title": "Slavic", "description": "A portrait of Slavic.", "img_url": "static/img/Slavic.jpg"}
    }

    # Pass image details to the template
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/image/<image_name>')
def image_detail(image_name):
    image = image_data.get(image_name)
    if image is None:
        return "Image not found", 404
    return render_template('image_detail.html', image=image)

if __name__ == '__main__':
    app.run()


