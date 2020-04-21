from queue import Queue 
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
    output = []

    if path is None or len(path) == 0:
        return []
    
    if os.path.isfile(path):
        if path.endswith(suffix):
            output.append(path)
        return output

    q = Queue()
    q.put(path)

    while not q.empty():
        p = q.get()
        
        if os.path.isdir(p):
            subdirs = os.listdir(p)
            for d in subdirs:
                d = os.path.join(p, d)
                if os.path.isdir(d):
                    q.put(d)
                else:
                    if d.endswith(suffix):
                        output.append(d)

    return output



# Test case 1
print(find_files('.c', './testdir'))

#Test case 2
print(find_files('.c', './testdir/t1.c'))

#Test case 3
print(find_files('.c', '.'))

#Test case 4
print(find_files('.c', ''))

#Test case 5
print(find_files('.c', './testdir/subdir2'))
