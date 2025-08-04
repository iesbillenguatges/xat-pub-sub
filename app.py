from flask import Flask, render_template, request, Response
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    message = request.form["message"]
    r.publish("chat", message)
    return "", 204

@app.route("/stream")
def stream():
    def event_stream():
        pubsub = r.pubsub()
        pubsub.subscribe("chat")
        for message in pubsub.listen():
            if message["type"] == "message":
                yield f"data: {message['data'].decode()}\n\n"
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
