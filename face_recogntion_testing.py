import face_recognition
from pathlib import Path

def face_authentication(user_image_path, known_encodings):
    # load in the user image
    unknown_image = face_recognition.load_image_file(user_image_path)

    # generate encoding of unknown image
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    # Ensure there is exactly one face in the image
    if len(unknown_encodings) != 1:
        raise ValueError(f"Image {user_image_path} contains {len(unknown_encodings)} faces. Only one face is allowed.")

    unknown_encoding = unknown_encodings[0]

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

def process_user_inputs(input_dir, known_encodings):
    """
    Process all images in the user input directory, authenticating each image.
    """
    input_dir_path = Path(input_dir)
    # checks for user_inputs existign
    if not input_dir_path.exists():
        raise FileNotFoundError(f"Input directory {input_dir} does not exist.")

    results = {}
    for file_path in input_dir_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in {'.png', '.jpg', '.jpeg'}:
            try:
                match_index = face_authentication(file_path, known_encodings)
                if match_index < 0:
                    results[file_path.name] = "No match found"
                else:
                    results[file_path.name] = f"Recognized person {match_index} in database"
            except ValueError as e:
                results[file_path.name] = str(e)

    return results

if __name__ == "__main__":
    database_path = Path("./database")
    user_input_path = "./user_inputs"
    list_of_known_encodings = generate_database_encodings(database_path)
    results = process_user_inputs(user_input_path, list_of_known_encodings)

    for image_name, result in results.items():
        print(f"{image_name}: {result}")

