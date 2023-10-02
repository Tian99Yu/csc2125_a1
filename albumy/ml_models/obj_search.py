from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import os

subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def get_objects_in_img(img_path):
    img = open(img_path, "rb")

    tags_result_remote = computervision_client.tag_image_in_stream(img)
    # Return tags with confidence score higher than 0.7
    results = [tags_result_remote.tags[i].name for i in range(len(tags_result_remote.tags)) if tags_result_remote.tags[i].confidence > 0.9]
    return results

if __name__ == "__main__":
    print(get_objects_in_img("./uploads/2c34708eed284e82b8c6ef9aa196e75e.JPG"))