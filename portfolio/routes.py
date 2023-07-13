#%%
from flask import Blueprint, render_template, abort

pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)

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
    },
    {
        "name": "Videomaker",
        "thumb": "imgs/AI_gift.png",
        "hero":"imgs/AI_gift.png",
        "categories": ["automatic speech recognition","natural language processing"],
        "slug": "AI_gift",
        "prod": "https://github.com/tituslhy/VideoMaker"
    },
    {
        "name": "Watchlist",
        "thumb": "imgs/movie.png",
        "hero":"imgs/movie.png",
        "categories": ["Full Stack Web Development","Hashing", "MongoDB"],
        "slug": "Watchlist",
        "prod": "https://github.com/tituslhy/watchlist"
    }
]

slug_to_project = {project['slug']: project for project in projects}
#%%
@pages.route("/")
def home():
    return render_template('home.html', projects = projects)

@pages.route("/about")
def about():
    return render_template("about.html")

@pages.route("/contact")
def contact():
    return render_template("contact.html")

@pages.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html",
                           project = slug_to_project[slug])

@pages.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404