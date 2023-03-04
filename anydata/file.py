import pandas as pd
import os

def get_type(filename):
    return os.path.splitext(filename)[1]
    
def read(filename: str, chunk_size=-1, sep=","):
    file_type = get_type(filename)
    match(file_type):
        case ".csv":
            if chunk_size > 0:
                return pd.read_csv(filename, chunk_size)
            else:
                return pd.read_csv(filename)
        case ".txt":
            if chunk_size > 0:
                return pd.read_csv(filename, chunk_size,sep="\t")
            else:
                return pd.read_csv(filename,sep="\t")
        case _:
            print(f"No defined reader for file type {file_type}")
            exit()


def write(filename, chunks: pd.io.parsers.readers.TextFileReader):
    file_type = get_type(filename)
    match(file_type):
        case ".csv":
            header = True
            for chunk in chunks:
                chunk.to_csv(filename, header=header,  mode='a')
                header = False
        case _:
            print(f"No defined writer for file type {file_type}")


def write(filename, df: pd.DataFrame):
    file_type = get_type(filename)
    match(file_type):
        case "csv":
            df.to_csv(filename)
        case _:
            print(f"No defined writer for file type {file_type}")
