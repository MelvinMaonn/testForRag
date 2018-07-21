

import os


def statistics(root_dir):
    for categories in os.listdir(root_dir):

        path = os.path.join(root_dir, categories)

        for categories in os.listdir(path):
    print path
        if os.path.isdir(path):
            Test2(path)