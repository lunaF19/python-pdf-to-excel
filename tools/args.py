
import sys
import os

from tools.files import is_directory, directory_have_content, create_dir


def get_source_ddl_files_path():
    args = sys.argv

    # Check the number of arguments
    if len(args) <= 1:
        raise Exception("No se ingreso el primer path")

    if (args[1] is None):
        raise Exception("No se ingreso el primer path")

    _source_path = os.path.join(args[1])
    if (not is_directory(_source_path)):
        raise Exception("El primer path no es un directorio")
    if (not directory_have_content(_source_path)):
        raise Exception("El primer path no tiene nada para leer")
    return _source_path


def get_final_path():
    args = sys.argv

    # Check the number of arguments
    if len(args) <= 2:
        raise Exception("No se ingreso el segundo path")

    if (args[2] is None):
        raise Exception("No se ingreso el segundo path")
    _filnal_path = os.path.join(args[2])

    print(_filnal_path)
    if (not is_directory(_filnal_path)):
        raise Exception("El segundo path no es un directorio")

    if (not os.path.exists(_filnal_path)):
        response_user = None
        response_count = 0
        while True:
            if (response_count > 3):
                raise Exception("Error con el directorio final")

            response_user = input("Deseas crear esta carpeta? Y/N:")

            if (response_user == "N"):
                raise Exception("Debes vaciar el directorio para continuar")

            if (response_user == "Y"):
                create_dir(_filnal_path)
                print("Se creo el directorio: " + _filnal_path)
                break

            response_count += 1
    else:
        final_path_have_content = directory_have_content(_filnal_path)
        if (final_path_have_content):
            raise Exception(f"Debes vaciar el directorio para continuar")

    return _filnal_path
