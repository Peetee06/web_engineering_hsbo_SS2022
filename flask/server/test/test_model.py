from cgi import test
from pathlib import Path
import pytest

from tnyml import model

# TODO get model instance


def test_make_prediction():
    """
    Test for make_prediction
    """

    image_path = Path(__file__).parent.parent / "public" / "user" / "uploads" / "Uploads_cat_dog" / "image_to_predict.jpg"
    model_name = "cat_dog_model"
    prediction = model.make_prediction(model_name, image_path)
    assert prediction.prediction == "cat"
    assert prediction.confidence == 0.998
