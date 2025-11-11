import os.path
mod_path = os.path.dirname(__file__)
COMEDIC_LIST_FILES = [
    os.path.join(mod_path, "..", "data", "imdb_funny_actors_f.names"),
    os.path.join(mod_path, "..", "data", "imdb_funny_actors_m.names")
]
def is_comedic_actor(name):
    # scan through all comedic list files and check for the name
    pass

# this is platform independent
# so it will work on Windows, Mac, Linux, etc.