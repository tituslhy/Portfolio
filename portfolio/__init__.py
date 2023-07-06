#%%
from flask import Flask, render_template, abort

app = Flask(__name__)

#%%
projects = [
    {
        "name": "You only edit once (YOEO)",
        "thumb": "imgs/YOEO.png",
        "hero":"imgs/YOEO.png",
        "categories": ["computer vision", "video and image processing"],
        "slug": "YOEO",
        "prod": "https://github.com/teyang-lau/you-only-edit-once"
    },
    {
        "name": "A Song for Singapore",
        "thumb": "imgs/Singapore.jpeg",
        "hero":"imgs/Singapore.jpeg",
        "categories": ["natural language processing", "variational autoencoder"],
        "slug": "a-song-for-singapore",
        "prod": "https://github.com/quekhyg/NLP-Lyric-Generator"
    },
    {
        "name": "Barista Board: The Coffee Recommender",
        "thumb": "imgs/coffee.jpeg",
        "hero":"imgs/coffee.jpeg",
        "categories": ["recommender systems", "natural language processing"],
        "slug": "coffee-recommender-system",
        "prod": "https://github.com/teyang-lau/Coffee_Joint_Recommender_System"
    },
    {
        "name": "The AI Backdoor Catcher",
        "thumb": "imgs/backdoor.png",
        "hero":"imgs/backdoor.png",
        "categories": ["computer vision", "AI systems evaluation"],
        "slug": "ai-security",
        "prod": "https://github.com/spencerkmarley/cs612-ai-sys-eval-project"
    },
    {
        "name": "Skimlit: Making summaries skimmable",
        "thumb": "imgs/skimlit.png",
        "hero":"imgs/skimlit.png",
        "categories": ["natural language processing","streamlit"],
        "slug": "skimlit",
        "prod": "https://github.com/tituslhy/Skimlit"
    },
    {
        "name": "Facemask classification",
        "thumb": "imgs/facemask.jpeg",
        "hero":"imgs/facemask.jpeg",
        "categories": ["computer vision","machine learning engineering"],
        "slug": "facemask",
        "prod": "https://github.com/tituslhy/Face-mask-classification"
    }
]

slug_to_project = {project['slug']: project for project in projects}
#%%
@app.route("/")
def home():
    return render_template('home.html', projects = projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html",
                           project = slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404