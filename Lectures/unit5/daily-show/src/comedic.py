import os.path
mod_path = os.path.dirname(__file__)
COMEDIC_LIST_FILES = [
    os.path.join(mod_path, "..", "data", "imdb_funny_actors_f.names"),
    os.path.join(mod_path, "..", "data", "imdb_funny_actors_m.names")
]
def is_comedic_actor(name):
    # scan through all comedic list files and check for the name
    for comedic_file in COMEDIC_LIST_FILES:
        if is_name_in_file(name, comedic_file):
            return True
    return False        
    pass

def is_name_in_file(name, filename):
    with open(filename,"r") as f:
        for line in f:
            if name.lower() == line.strip().lower():
                return True
    return False