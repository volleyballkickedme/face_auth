import face_recognition
from pathlib import Path

def face_authentication(user_image_path, known_encodings):
    # load in the user image
    unknown_image = face_recognition.load_image_file(user_image_path)

    # generate encoding of unknown image
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces(known_encodings, unknown_encoding)
    if any(results):
        print("face recognized")
        return results.index(True)
    else:
        print("face no match for database image")
        return -1

# return list of known encodings
def generate_database_encodings(database_dirpath):
    known_encodings= []
    # Iterate through each image file in the directory
    for file_path in database_dirpath.iterdir():
        # Check if it is a file and has a valid image extension
        if file_path.is_file() and file_path.suffix.lower() in {'.png', '.jpg', '.jpeg'}:
            known_image = face_recognition.load_image_file(file_path)
            known_encoding_array = face_recognition.face_encodings(known_image)
            
            if known_encoding_array:
                known_encodings.append(known_encoding_array[0])

    return known_encodings

if __name__ == "__main__":
    database_path = Path("./database")
    user_input_path = "./jonemun_test.jpeg"
    list_of_known_encodings = generate_database_encodings(database_path)
    match_index = face_authentication(user_input_path, list_of_known_encodings)

    if (match_index < 0):
        print("Failed")
    else:
        print(f"recognized person {match_index} in database")

