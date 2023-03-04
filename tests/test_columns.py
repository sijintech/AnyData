from anydata import columns
import filecmp
import os
import errno

def test_drop():
    try:
        os.mkdir("./data/generated")
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
    file_in = "./data/original/wide.txt"
    file_answer= "./data/answer/wide.txt"
    file_out = "./data/generated/wide.txt"
    columns.drop(file_in,["JobId"],file_out)
    assert filecmp.cmp(file_in, file_out)
    os.remove(file_out)