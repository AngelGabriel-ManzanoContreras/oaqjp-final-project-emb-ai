from flask import Flask, request, render_template
from EmotionDetection import emotion_detector
app = Flask(__name__)
@app.route("/")
def index():
    """Render the main HTML page."""
    return render_template("index.html")
@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Handle POST request for emotion detection.
    Returns:
        str: Formatted response string or error message.
    """
    text = request.form["text"]
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)