import os


def get_filename_of_path(_file_path):
    return _file_path.split("\\")[-1]


def is_directory(_path):  # is directory
    return os.path.isfile(_path) == False


def directory_have_content(_dir):
    return (len(os.listdir(_dir)) > 0)


def create_dir(_new_dir):
    if not os.path.exists(_new_dir):
        os.makedirs(_new_dir)


def get_filename(_filepath):
    if (is_directory(_filepath)):
        return None, None

    path_file, file_extension = os.path.splitext(_filepath)
    filename = get_filename_of_path(path_file)
    return filename, file_extension


def get_path(_dir, _filename):
    return os.path.join(_dir, _filename)


def get_files_of_dir(_from_dir):
    _files = []
    # Verify if is directory
    if not (is_directory(_from_dir)):
        return

    # list all content of folder
    for path_file_dir in os.listdir(_from_dir):
        path_dir = os.path.join(_from_dir, path_file_dir)
        if not (is_directory(path_dir)):   # is file
            filename, file_ext = get_filename(path_dir)
            print(f'{filename} - {file_ext}')
            _files.append({
                "dir": path_dir,
                "ext": file_ext,
                "name": filename
            })
    return _files
