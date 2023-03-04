import pandas as pd
import anydata.file as file
import copy
from multipledispatch import dispatch


def drop_by_chunk(chunk_reader: pd.io.parsers.readers.TextFileReader, columns_to_be_dropped: list[str], override=True):
    if override:
        out_reader = chunk_reader
    else:
        out_reader = copy.deepcopy(chunk_reader)
    for chunk in out_reader:
        drop(chunk, columns_to_be_dropped, True)
    if override:
        return out_reader


def drop_by_df(data: pd.core.frame.DataFrame, columns_to_be_dropped: list[str], override=True):
    if override:
        data.drop(columns_to_be_dropped, axis=1, inplace=True)
    else:
        return data.drop(columns_to_be_dropped, axis=1)


def drop(filename: str, columns_to_be_dropped: list[str], out_file: str | None = None, chunk_size=-1):
    reader = file.read(filename, chunk_size)
    if chunk_size > 0:
        drop_by_chunk(reader, columns_to_be_dropped, True)
    else:
        drop_by_df(reader, columns_to_be_dropped, True)
    if out_file == None:
        out_file = filename
    file.write(out_file, reader)


def keep(file: str, columns_to_keep):
    pass


def keep(data: pd.DataFrame, columns_to_keep):
    pass
