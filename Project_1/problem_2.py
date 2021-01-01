#------------------------------------------------------#
#   problem 2 - File Recursion
#------------------------------------------------------#

# imports
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # list to store the path of the files with suffix
    suffix_files = list()

    # if path does not exists, print a error massage and return an empty list
    if not os.path.exists(path):
        print("Provided path does not exist")
        return suffix_files

    # if no suffix is provided, print a error massage and return an empty list
    if suffix == "":
        print("No suffix provided")
        return suffix_files

    # if provided path is a file, check if file has the right suffix
    if os.path.isfile(path):
        if '.' + suffix in path:
            suffix_files.append(path)
        return suffix_files

    # get a list of items that are in the directory
    items = os.listdir(path)

    # loop over items
    for item in items:
        # convert item name to a path
        current_path = os.path.join(path, item)
        # if current path is a directory, call function recursivly
        if os.path.isdir(current_path):
            suffix_files.extend(find_files(suffix, current_path))
        # if current path is a file and has the suffix then add it to the list
        elif os.path.isfile(current_path) and len(current_path) > len(suffix):
            if '.' + suffix in current_path:
                suffix_files.append(current_path)

    return suffix_files


# standard test cases
print("--------------------------------------------")
print("Call function: find_files('c','./testdir'):")
print(find_files("c","./testdir"))
# ['./testdir/subdir3/subsubdir1/b.c', './testdir/subdir1/a.c', './testdir/t1.c', './testdir/subdir5/a.c']

print("--------------------------------------------")
print("Call function: find_files('c','./testdir/subdir1/a.c'):")
print(find_files("c","./testdir/subdir1/a.c"))
# ['./testdir/subdir1/a.c']

# edge test cases
print("--------------------------------------------")
print("Call function: find_files('c','./test'):")
print(find_files("c","./test"))
# []

print("--------------------------------------------")
print("Call function: find_files('','./testdir'):")
print(find_files("","./testdir"))
# []

print("--------------------------------------------")
print("Call function: find_files('',''):")
print(find_files("",""))
# []
