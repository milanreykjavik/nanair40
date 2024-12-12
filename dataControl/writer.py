import os
import tempfile
import json

def atomicWrite(fp, data):
    dirName = os.path.dirname(fp)
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dirName, encoding="utf-8") as tmpFile:
        json.dump(data, tmpFile, indent=4)
        tmpFileName = tmpFile.name
        tmpFile.flush()
        os.fsync(tmpFile.fileno()) # if you cut off the power of kernel panics

    os.replace(tmpFileName, fp)
