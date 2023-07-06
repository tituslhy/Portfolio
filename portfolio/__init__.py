from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "You only edit once (YOEO)",
        "thumb": "imgs/YOEO.png",
        "hero":"imgs/YOEO.png",
        "categories": ["computer vision", "streamlit"],
        "slug": "YOEO"
    },
    {
        "name": "A Song for Singapore",
        "thumb": "imgs/Singapore.jpeg",
        "hero":"imgs/Singapore.jpeg",
        "categories": ["natural language processing", "variational autoencoder"],
        "slug": "a-song-for-singapore"
    },
    {
        "name": "The Coffee Recommender System",
        "thumb": "imgs/coffee.jpeg",
        "hero":"imgs/coffee.jpeg",
        "categories": ["recommender systems", "natural language processing"],
        "slug": "coffee-recommender-system"
    },
    {
        "name": "The AI Backdoor Catcher",
        "thumb": "imgs/backdoor.png",
        "hero":"imgs/backdoor.png",
        "categories": ["computer vision", "AI security"],
        "slug": "ai-security"
    },
    {
        "name": "Skimlit",
        "thumb": "imgs/skimlit.png",
        "hero":"imgs/skimlit.png",
        "categories": ["natural language processing","streamlit"],
        "slug": "skimlit"
    },
    {
        "name": "Facemask classification",
        "thumb": "imgs/facemask.jpeg",
        "hero":"imgs/facemask.jpeg",
        "categories": ["computer vision","machine learning engineering", "google cloud platform"],
        "slug": "facemask"
    }
]

@app.route("/")
def home():
    return render_template('home.html', projects = projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")