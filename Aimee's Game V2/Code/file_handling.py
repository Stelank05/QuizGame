import json
import os

def write_file(file_path: str, file_data: str) -> None:
    write_file = open(file_path, "w")
    write_file.write(file_data)
    write_file.close()

def append_file(file_path: str, append_data: str) -> None:
    append_file = open(file_path, "a")
    append_file.write(f"\n{append_data}")
    append_file.close()

def read_file(file_path: str) -> list[str]:
    return_list: list[str] = []

    open_file = open(file_path, "r")

    for line in open_file:
        return_list.append(line.replace("\n", "").replace("ï»¿", ""))

    return return_list

def delete_file(file_path: str) -> None:
    os.remove(file_path)

def relocate_file(old_path: str, new_path: str) -> None:
    file_data: list[str] = read_file(old_path)
    delete_file(old_path)
    write_file(new_path, file_data)

def write_json_file(file_path: str, file_data: dict) -> None:
    json_file = open(file_path, "w")
    json.dump(file_data, json_file)

def read_json_file(file_path: str) -> dict:
    with open(file_path) as json_file:
        file_data = json.load(json_file)

    return_dictionary: dict

    try:
        return_dictionary = file_data[0]
    except:
        return_dictionary = file_data

    return return_dictionary

def get_files_in_folder(folder: str) -> list[str]:
    pass

def file_exists(file_path: str) -> bool:
    return os.path.exists(file_path)