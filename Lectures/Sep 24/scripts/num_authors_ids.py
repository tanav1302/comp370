
'''
Count the number of unique author IDs in a dataset
'''
import argparse
import os.path as osp
parser = argparse.ArgumentParser()

parser.add_argument("datafile",type = str,help = "path to the data file")

#focus on this part
blacklist_fname = osp.join("..","data","author_id_blacklist.json")
#focus on this part
#rest is same need to change rest of code for it to work

# What you.
# 1:03:17
# Can do though is you can go import  dot
# 1:03:25
# path OSP and OSP has a function called join.
# 1:03:32
# That allows you to put.
# 1:03:34
# All the different elements of your path together using in
# 1:03:39
# a way that works for your operating system, whatever operating
# 1:03:46
# system Python is running in here.
# 1:04:07
# And then we end up with the same result.
# 1:04:24
# But the crucial thing is we've referenced our files in
# 1:04:28
# a way that is platform independent.
# 1:04:30
# All right?

def main():
    args = parser.parse_args()
    author_ids = set()
    author_id_blacklist = set()
    if args.blacklist:
        with open(args.blacklist,'r') as bl_fh:
            import json
            author_id_blacklist=set(json.load(bl_fh))


    fh = open(args.datafile,'r')
    line_iterator = iter(fh)
    line_iterator.__next__()
    for line in line_iterator:
        parts = line.strip().split(",")
        if len(parts)>1:
            author_id= parts[0]#Assuming author id is the first column
            if author_id not in author_id_blacklist:
                author_ids.add(author_id)
    print(f"Number of unique author IDs: {len(author_ids)}")

if __name__ =="__main__":
    main()

