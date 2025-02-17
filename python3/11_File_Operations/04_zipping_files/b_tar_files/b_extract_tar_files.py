import os
import tarfile

os.makedirs("files", exist_ok=True)
os.chdir("files")

# Extracting a specific file from archive
with tarfile.open("tarFileOne.tar") as tF:
    tF.extract("fileThree.txt")

# NOTE:  The extract() method does not take care of several extraction issues.
#      In most cases you should consider using the extractall() method.


# Extracting all files in archive
def is_within_directory(directory, target):
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)

    prefix = os.path.commonprefix([abs_directory, abs_target])

    return prefix == abs_directory


def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    for member in tar.getmembers():
        member_path = os.path.join(path, member.name)
        if not is_within_directory(path, member_path):
            raise Exception("Attempted Path Traversal in Tar File")

    tar.extractall(path, members, numeric_owner=numeric_owner)


# Extracting all files in the archive
with tarfile.open("tarFileOne.tar") as tar_file:
    safe_extract(tar_file)
