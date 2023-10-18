from image_classification import model_loader
from image_classification import detect
from organization import organizer

photos = []


# https://www.zooplus.co.uk/magazine/wp-content/uploads/2018/03/cat_bird_cohabitation.jpg'  # A sample link

def ui() -> None:
    """
    This is the overall function that combines all the parts. First it loops through inputs and adds each one to a link.
    Once the user presses enter, it will run the organization function on the detection function of the list of photos.
    """
    print("WELCOME TO A PHOTO RECOGNITION PROGRAM CREATED BY DARSHAN, NAYERA AND TIMOTHY")
    print("Continue adding photos or press return to run detection")
    image = input('Please Enter the Address of the Image to be Identified: ')  # This first input kickstarts the loop
    photos.append(image)
    while image != '':  # Until they press enter...
        image = input('Please Enter the Address of the Image to be Identified: ')  # This is the looping input
        if image != '':
            photos.append(image)  # It should only add the image if it's not "enter"
    print(photos)  # Prints the list just to confirm it's what the user wanted
    organizer(detect(model_loader(), photos))  # Runs detection on the photos, which then has organization run on that


if __name__ == "__main__":
    ui()
