import json
import pickle
import sys
import os
from configuration.scraper_config import STORAGE_PATH


def create_path_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)


def store_as_json(var_name, var):
    create_path_if_not_exist(STORAGE_PATH)
    filename = STORAGE_PATH + var_name + ".json"
    with open(filename, "w") as fp:
        json.dump(var, fp, indent=2)


def retrieve_json(var_name):
    filename = STORAGE_PATH + var_name + ".json"
    with open(filename, "r") as fp:
        var = json.load(fp)
    return var


def store_as_bin(var_name, var):
    create_path_if_not_exist(STORAGE_PATH)
    sys.setrecursionlimit(10000)
    filename = STORAGE_PATH + var_name + ".bin"
    with open(filename, "wb") as fp:
        pickle.dump(var, fp)


def retrieve_bin(var_name):
    sys.setrecursionlimit(10000)
    filename = STORAGE_PATH + var_name + ".bin"
    with open(filename, "rb") as fp:
        var = pickle.load(fp)
    return var


def read_file(filename):
    fp = open(filename, "r")
    text = fp.read()
    return text


def load_or_if_not_exits_create_json_file(json_file):
    try:
        stored_data = retrieve_json(json_file)
    except FileNotFoundError:
        print("Creating new data file")
        empty_file = []
        store_as_json(json_file, empty_file)
        stored_data = retrieve_json(json_file)
    return stored_data
