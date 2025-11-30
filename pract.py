from flask import Flask,request,jsonify
from g import respond

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"

@app.route("/chat", methods =["POST"])
def chat_api():
    try:
        data = request.get_json(force=True)
        query = data.get("query")
        
        if not query:
            return jsonify({"success":False, "message":"Missing 'query' in request"}), 400
       
        reply = respond(query)
        return jsonify({"success":True, "message": reply}), 200
    
    except Exception as e:
        print("Error", e)
        return jsonify({"success": False, "message": "Internal Server Error"}), 500




if __name__ == '__main__':
    app.run(debug=True)