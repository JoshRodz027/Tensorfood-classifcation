import os
import unittest
from PIL import Image
import tensorflow as tf
from src.inference import Model

TEST_IMG_PATH = "test_img.jpg"
TEST_MODEL_PATH = "tensorfood.h5"


class TestModule(unittest.TestCase):
    def setUp(self):
        if os.getcwd().endswith("all-assignments"):
            self.img_path = os.path.join("assignment7", TEST_IMG_PATH)
            self.model_path = os.path.join("assignment7", TEST_MODEL_PATH)
        else:
            self.img_path = TEST_IMG_PATH
            self.model_path = TEST_MODEL_PATH

    def model_import_test(self):

        m = Model()
        import_weights = tf.keras.models.load_model(self.model_path)
        import_weights = import_weights.weights[-1].numpy()
        trained_weights = m.model.weights[-1].numpy()
        assert import_weights==trained_weights, "imported wrong model weights"
 

    def test_preproc_image(self):
        #check if image processes correctly
        m = Model()
        input_arr = m.preproc_image(self.img_path)
        
        assert input_arr.shape == (
            1, 256, 256, 3), "transformed image is not shape of (1,256,256,3)"

    def test_predict_food(self):
        # check prediction of test img
        m = Model()
        pred_dish , max_proba, comment = m.predict_food(self.img_path)
        assert pred_dish == "ice_kacang", f"Expecting ice_kacang, got {pred_dish} instead"




if __name__ == "__main__":
    unittest.main()
