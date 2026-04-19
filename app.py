from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
df, similarity = pickle.load(open("model.pkl", "rb"))

def recommend(movie):
    movie = movie.strip()
    
    if movie not in df["title"].values:
        return ["Movie not found"]
    
    idx = df[df["title"] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    return [df.iloc[i[0]]["title"] for i in scores[1:6]]

@app.route("/", methods=["GET", "POST"])
def home():
    recs = []
    
    if request.method == "POST":
        movie = request.form["movie"]
        recs = recommend(movie)
    
    return render_template("index.html", recommendations=recs)

if __name__ == "__main__":
    app.run(debug=True)