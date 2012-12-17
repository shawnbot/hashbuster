hashbuster
==========

A tool for updating cache-busting query strings from git commit hashes.

Usage: 

```
hashbuster.py \
    (--version VERSION | --git) \
    [--query-key KEY] \
    --path[s] (PATH1[,PATH2[,PATH3]] | "GLOB1[,GLOB2[,GLOB3]]") \
    FILES

Update the URLs of the specified path(s) in one or more files to include
version information in the query string.


Options:
  -h, --help            show this help message and exit
  -p PATH, --path=PATH, --paths=PATH
                        one or more comma-separated paths (or shell globs) of
                        filenames to replace
  -v VERSION, --version=VERSION
                        the version string (if not using the git commit hash)
  --git                 use the git commit hash of the last commit that
                        touched each path (`git log -n 1 --format=%h path`)
  -q QUERY_KEY, --query-key=QUERY_KEY
                        the key to use in the cache-busting query string URLs
```
