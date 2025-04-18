from flask import Flask, request, jsonify, render_template
import requests # needed to connect to external apis

app = Flask(__name__)

base_url = "https://api.breakingbadquotes.xyz/" # holds api link

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/v1/quotes")
def get_pokemon_info():
    # name = request.args.get("name") # fetches name
    # url = f"{base_url}/pokemon/{name}" # modifies url with input
    url = "https://api.breakingbadquotes.xyz/v1/quotes"
    response = requests.get(url) # calls api and saves response
    
    if response.status_code == 200:
        # pokemon_data = response.json()
        # pokemon = {
        #     "name": pokemon_data["name"],
        #     "id": pokemon_data["id"],
        #     "height": pokemon_data["height"]
        # }
        breakbad_data = response.json()
        quote_info = breakbad_data[0]
        breakbad = {
            "quote": quote_info["quote"],
            "author": quote_info["author"]
        }

        return render_template("index.html", quote=breakbad)
    else:
        return render_template("index.html", error="quote error")
    

if __name__ == "__main__":
    app.run(debug=True)