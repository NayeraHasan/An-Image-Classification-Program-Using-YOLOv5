import torch

def model_loader():
    """
    This function is only responsible for loading YOLO, packaging it as a variable, and then returning it. This means
    that the model only is loaded once, making the runtime much faster.
    """
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # Calling the model per their instructions
    # Notably, we have pretrained on so we are using their database of images
    return model


def detect(model, images: list) -> dict:
    """
    This function takes the model as one of its inputs and a list of images as the other. The result is a dictionary,
    which has the objects as the keys and the image links as its values. The basis of the code is a for loop. It goes
    through the list of images and for each one, runs YOLO on them and makes a table of results with a lot of
    information in it. The function sorts this out and returns the relevant objects as a list. This list then goes
    through another for loop, which checks if each object found in a single image is already in the output dictionary.
    This lets either a new key be created to add an image or add it to the key if it's already there.
    """
    objects_and_images: dict = {}  # The output dictionary
    for photo in images:  # This for loop sorts through each file
        results = model(photo)  # Running the preloaded model handed to it from the previous function
        # results.show()  # This is only if you want to see the physical boxes and confidence on the picture itself
        raw_output = list(results.pandas().xyxy[0]["name"])  # Reformats the table, getting just the objects as list
        # The pandas and xyxy are again suggested by YOLO and came with the code
        for item in raw_output:  # This sorts through the objects in a single image
            if item not in objects_and_images:  # If the object is not in the dictionary...
                objects_and_images[item] = [photo]  # add it.
            else:
                objects_and_images[item].append(photo)  # Otherwise just add the link to the existing key.
    return objects_and_images  # Returns dictionary

detect(model_loader(), 'https://www.zooplus.co.uk/magazine/wp-content/uploads/2018/03/cat_bird_cohabitation.jpg')