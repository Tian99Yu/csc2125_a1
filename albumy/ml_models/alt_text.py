from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
def get_alt_text(img):
    """
    returns both alternative text and the confidence if API is available. otherwise, return None
    :param img: The path to image
    :return: Alternative text and model confidence, or None if API is busy
    """
    with open(img, "rb") as image_stream:
        try:
            description_result = computervision_client.describe_image_in_stream(image_stream)
            caption = description_result.captions[0]
            return caption.text, caption.confidence
        except:
            return None, None


if __name__ == "__main__":
    print(get_alt_text("./test/cat.jpeg"))