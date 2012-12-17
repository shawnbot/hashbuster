# hashbuster

hashbuster is a tool for adding cache-busting query strings to URLs in your HTML files.

If you make lots of changes to live web sites, browser and proxy caches are probably
the bane of your existence. If you've ever had to tell a client to clear their browser
cache to see your latest code push, then hashbuster is for you.

## Examples

Update all instances of "foo.css" in your HTML files to point to a cache-busting URL
"foo.css?v=fixed":

```
hashbuster.py --path foo.css --version fixed *.html
```

Update the URLs of all your CSS files in all of your HTML files to include the hash of
the most recent git commit that touched them:

```
hashbuster.py --paths "css/*.css" --git *.html
```

## Usage

To install hashbuster, just copy `hashbuster.py` to somewhere in your `$PATH` (or alias
it to your git checkout).

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
