from flask import Flask, request, jsonify, render_template
import requests # needed to connect to external apis

app = Flask(__name__)

base_url = "https://vpic.nhtsa.dot.gov/api/" # holds api link

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pokemon/")
def get_pokemon_info():
    name = request.args.get("name") # fetches name
    url = f"{base_url}/pokemon/{name}" # modifies url with input
    response = requests.get(url) # calls api and saves response
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon = {
            "name": pokemon_data["name"],
            "id": pokemon_data["id"],
            "height": pokemon_data["height"]
        }

        return render_template("index.html", pokemon=pokemon)
    else:
        return render_template("index.html", error="Pokemon not found.")
    

if __name__ == "__main__":
    app.run(debug=True)