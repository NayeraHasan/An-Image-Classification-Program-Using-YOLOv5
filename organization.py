import os
import requests


def organizer(objects: dict) -> None:
    """
    This function takes the dictionary from the image classification function and separates it into different files
    based on the objects, and adds the photo files to the object category files. This also uses a few for loops. The
    first cycles through the keys from the dictionary and makes files based on them. Then the nested for loop takes the
    image for that key and renames it. Then it changes the URL to a jpg and adds it to the file.
    """
    for key in objects:  # Goes through each key only
        path = './' + key  # Makes a file path
        if not os.path.exists(path):  # If that file doesn't exist yet...
            os.mkdir(path)  # Adds that file
        n = 0  # A counter for repeat images
        for image_url in objects[key]:  # Another for loop for each image URL under that key
            img_name = path + "/" + key + str(n) + '.jpg'  # Renames the file with numbers and adds to file
            img_data = requests.get(image_url).content  # Gets the content of the URL
            with open(img_name, 'wb') as handler:  # Opens new image files as .jpgs
                handler.write(img_data)  # Adds URL content to the file
                n += 1  # Adds one to the counter so another URL won't duplicate the file name


