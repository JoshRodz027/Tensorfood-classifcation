from flask import Flask, render_template, url_for, jsonify, request
# from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
from waitress import serve
from werkzeug.utils import secure_filename
from src.inference import Model
import numpy as np
import logging 
import os 
import markdown.extensions.fenced_code

#control c to stop server
#set Flask_APP=flaskblog.py at the cd directory to set flask  #normal mode
# debugg mode : set FLASK_DEBUG=1 - does not require refreshing
#flask run to run this!
#cmd shift r hard refresh and clear cache

#logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("tensorfood")

#load flask
logger.info("***Instantiating Flask***")
app = Flask(__name__)  # instatiate Flask class
logger.info("***Flask instantiated***")

# Upload folder
if os.getcwd().endswith('src'):
    app.config["UPLOAD_FOLDER"] = "static/uploads/"
else:
    app.config["UPLOAD_FOLDER"] = "src/static/uploads/"


#load model
logger.info("***Instatiating model***")
m = Model()
logger.info("***Model instantiated***")



logger.info("***Loading homepage")
@app.route("/", methods=["GET"]) # what you type for about this page. "/" is home page/root page
def home():
    return render_template('index.html')




@app.route('/info', methods=['GET'])
def short_description():
    response = {
        "url":"/predict",
        "method": "Post",
        "model": "MobileNetv2",
        "input-size": "160x160x3",
        "num-classes": 12,
        "pretrained-on": "ImageNet"
    }
    return jsonify(response)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        response ={
            "probability": 0,
            "food ": "not implemented",
            "comment": "error"
            }
        
        #obtaining image file and save it 
        file = request.files['file']
        filename = secure_filename(file.filename)
        filename = 'temp.' + filename.split('.')[-1] # Change to default name to save memory
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        #make prediction
        pred_dish, max_proba, comment = m.predict_food(filepath)
        #output
        response ={
            "probability": f"{ np.round(max_proba*100,3) }%",
            "food ": pred_dish,
            "comment": comment
            }

    except Exception as e:
        logger.info(str(e))
        response["comment"] = str(e)

    return render_template("index.html" , food = pred_dish , probability = max_proba , comment = comment )

@app.route('/docs', methods=['GET'])
def render_readme():
    readme_file = open("README.md", "r")
    readme_txt = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return readme_txt


if __name__ == '__main__': #for python script run directly , otherwise name is name of module
    logger.info("***Starting session***")
    # app.run(debug=True)#runs via cmd python flaskblog.py
    # For production mode, comment the line above and uncomment below
    serve(app, host="0.0.0.0", port=8000)
    logger.info("***Session ended***")
