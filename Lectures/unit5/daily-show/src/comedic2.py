import os.path
mod_path = os.path.dirname(__file__)
COMEEDIC_LIST_FILES = [
    mod_path + "../data/imdb_comedic_actors.txt",
]
def is_comedic_actor(name):
    # scan through all comedic list files and check for the name
    pass

#     This will work, but remember how we talked about relative
# 1:12:14
# paths in these slashes?
# 1:12:15
# That is super uck like.
# 1:12:17
# That is that is definitely not the way we want
# 1:12:19
# it to be.