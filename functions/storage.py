import json
import pickle
import sys
from configuration.scraper_config import STORAGE_PATH


def store_as_json(var_name, var):
    filename = STORAGE_PATH + var_name + ".json"
    with open(filename, "w") as fp:
        json.dump(var, fp)


def retrieve_json(var_name):
    filename = STORAGE_PATH + var_name + ".json"
    with open(filename, "r") as fp:
        var = json.load(fp)
    return var


def store_as_bin(var_name, var):
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
