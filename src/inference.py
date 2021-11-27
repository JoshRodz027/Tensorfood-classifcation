import sys
import os 
import argparse
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array,ImageDataGenerator

from PIL import Image

class Model :
    def __init__(self):
        # Load pre-trained model
        print("***Loading  model***")
        MODEL_FILE = "tensorfood.h5"
        if os.getcwd().endswith("all-assignments"):
            self.model_path = os.path.join("assignment7", MODEL_FILE)
        else:
            self.model_path = MODEL_FILE
        self.model = tf.keras.models.load_model(self.model_path)

        print("***Model loaded***")


        FOODS = ['chilli_crab',
                'curry_puff',
                'dim_sum',
                'ice_kacang',
                'kaya_toast',
                'nasi_ayam',
                'popiah',
                'roti_prata',
                'sambal_stingray',
                'satay',
                'tau_huay',
                'wanton_noodle']
        self.classes=FOODS


        COMMENTS = [
            "I'm 100 percent sure its ",
            "I think its most likely ",
            "Hmmm probably it is ",
            "Maybe it is ",
            "I'm guessing it might be "
        ]

        self.comments=COMMENTS

    def preproc_image(self,IMAGE_PATH):
        print("***Loading image***")
        self.target_size = (256, 256)
        image = load_img(path=IMAGE_PATH,
                        target_size=self.target_size,
                        color_mode="rgb")
        input_arr = img_to_array(image)
        input_arr = np.array([input_arr])
        return input_arr

    def get_comment(self,max_proba, pred_dish):
        choice = 0
        if max_proba==1.0:
            choice = 0
        elif max_proba > 0.85:
            choice = 1
        elif max_proba > 0.8:
            choice = 2
        elif max_proba > 0.75:
            choice = 3
        else :
            choice = 4
            
        comment = self.comments[choice]+ pred_dish
        return comment


    def predict_food(self,IMAGE_PATH):
        transformed_image = self.preproc_image(IMAGE_PATH)
        print("***predicting image***")
        prediction = self.model.predict(transformed_image)
        max_proba = np.max(prediction)
        pred_index = np.where(prediction == np.max(prediction))[1][0]
        pred_dish = self.classes[pred_index]
        comment = self.get_comment(max_proba,pred_dish)

        return pred_dish, max_proba, comment


if __name__ == "__main__":
    arglen = len(sys.argv)
    if (arglen > 1):
        print(f"preparing to classify: {sys.argv[1]} ")
        imagepath = sys.argv[1]

        m = Model()
        pred_dish, max_proba, comment = m.predict_food(imagepath)
        print(f"Probability : { max_proba } to be { pred_dish } for { imagepath }")
        print(comment)

