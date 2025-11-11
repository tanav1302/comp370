import os.path
mod_path = os.path.dirname(__file__)

COMEDIC_LIST_FILES = [
    os.path.join(mod_path, "..", "data", "imdb_funny_actors_f.names"),
    os.path.join(mod_path, "..", "data", "imdb_funny_actors_m.names")
]

def is_comedic_actor(name):
    for fname in COMEDIC_LIST_FILES:
        with open(fname,"r") as f:
            for line in f:
                if name.lower() == line.strip().lower():
                    return True
    return False

         

# Well, the first thing is we recognize something that we're
# doing something similar with female comic name, male comic name.
# We put it into a list so that we can
# iterate over it and do whatever it is that needs
# to happen to both of these things.