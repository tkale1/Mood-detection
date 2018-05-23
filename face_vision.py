import argparse
from geopy.geocoders import Nominatim
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

#get the address of the user based on the lat/lng position of the device
def getLocation(latlng):
    geolocator = Nominatim()
    location = geolocator.reverse(latlng)
    print(location.address)


# [START def_detect_face]
def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of Face objects with information about the picture.
    """
    # [START get_vision_service]
    client = vision.ImageAnnotatorClient()

    #fetch the contents of the image
    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations
# [END def_detect_face]


# [START def_highlight_emotions]
def highlight_emotions(image, faces):
    """Draws a polygon around the faces, then saves to output_filename.
    Args:
      image: a file containing the image with the faces.
      faces: a list of faces found in the file. This should be in the format
          returned by the Vision API.
    """
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Emotions detected : ')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        print('sad: {}'.format(likelihood_name[face.sorrow_likelihood]))

# [END def_highlight_emotions]


# [START def_main]
def main(input_filename, max_results,):
    latlng = "37.400054,-121.990476"
    print "Users current location address is: "
    getLocation(latlng)

    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        print('\nFound {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))

        # Reset the file pointer, so we can read the file again
        image.seek(0)
        highlight_emotions(image, faces)
# [END def_main]


if __name__ == '__main__':
    main('happy.jpeg', 4)