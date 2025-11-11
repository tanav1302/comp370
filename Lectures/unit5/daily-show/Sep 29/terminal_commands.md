
# Terminal commands to process the raw text file
```bash
grep "^[0-9]\+\. " imdb_funny_actors.raw.txt
```
to check count the number of lines
```bash
grep "^[0-9]\+\. " imdb_funny_actors.raw.txt | wc -l
```
to cut the number and dot from the beginning of each line

```bash
grep "^[0-9]\+\. " imdb_funny_actors.raw.txt |cut -d " " -f 2,3,4
```

since there are more male actors than female so we just take the first 74 male actors
```bash
grep "^[0-9]\+\. " imdb_funny_actors.raw.txt | head -n 74 | cut -d " " -f 2,3,4 > imdb_funny_actors_m.names
```


# add  src/ to the python path

```bash
tmux new -s comp370
```
so this is a tmux session
```bash
tmux attach -t comp370
```
to attach to the session

```bash
echo $PYTHONPATH
```
to check the python path
its empty right now
```bash
export PYTHONPATH=/home/tanavbansal/repos/comp370/Lectures/unit5/daily-show/src
```
it is telling python that whenever I run python if I mention comedic it should look in this directory
you can check by typing import comedic in python


```bash
export PYTHONPATH= 
```
now if I remove it and import comedic it won't find it

now this was in tmux so if I exit tmux and open python it won't find it
, I can create a protected session that
1:09:18
is configured the way that I want.
1:09:20
It's in the directories that I want.
1:09:22
The environment variables are set the way that I want
1:09:25
and that allows me to continue doing this work, not
1:09:28
just right now, but I can detach, I can reattach
1:09:32
and it'll still be there for me.

to add another path so that python looks into both directories just separate them by a colon
```bash
export PYTHONPATH=/home/tanavbansal/repos/comp370/Lectures/unit5/daily-show/src:/home/tanavbansal/repos/comp370/Lectures/unit5/daily-show/data
```
now if I do import comedic it will look in both places
