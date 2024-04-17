- executable uniq reads from stdin, prints to stdout
- every input: if seen, don't output anything
    - if not seen, repeat it to stdout
- case sensitive


future goals:
- logger
- packaging
- os compatibility

scope:
- testing
- functional + clean


# edgecase of empty string
# unordered text input 
# executable


issues w/ this:
- memory (RAM)

- write something to disk
    - how often?  -->  batch writes
    - how to save on disk  -->  pickle
    - how to lookup from a save
- sorted segment files
- which values to keep in cache

read -> cache hit -> return
read -> cache miss -> check on-disk
    -> hit -> return
    -> miss -> write to cache

max # entries for in-memory: 100
    - most recently used / least recently used
    - 101: --> n least recently used items --> store on-disk

log
- most recent log, check in there
-> miss -> next most recent log
-> first find, you just return

- multiple files of a limited size
- don't load entire object, load each line at a time


- one on-disk file to save items that are least used
- line: (input, # times seen)
- if cache miss, then read on-disk file line by line until find it; if miss, then total miss
    - add to cache

- if cache is full, then we flush part of it (1 item)