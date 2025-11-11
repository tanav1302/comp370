import os.path
mod_path = os.path.dirname(__file__)

def is_comedic_actor(name):
    # scan through the female comic names
    f_comic_fname = os.path.join(mod_path, "..", "data", "imdb_funny_actors_f.names")
   with open(f_comic_fname,"r") as f:
        for line in f:
            if name.lower() == line.strip().lower():
                return True
    return False

    # scan through the male comic names
    m_comic_fname = os.path.join(mod_path, "..", "data", "imdb_funny_actors_m.names")
   with open(m_comic_fname,"r") as f:
        for line in f:
            if name.lower() == line.strip().lower():
                return True
    return False

# now this is a block of code that has a healthy amount of
# redundant code it is fully functional but harder to maintain