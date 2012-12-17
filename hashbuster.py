#!/usr/bin/env python
import re, glob
import subprocess

def hashbust(text, path, version, query_key="version"):
    pat = re.compile("\\b%s(\?%s=\w*)?" % (re.escape(path), query_key), re.MULTILINE)
    url = "%s?%s=%s" % (path, query_key, version)
    return re.sub(pat, url, text)

def get_git_hash(path):
    p = subprocess.Popen(['git', 'log', '-n', '1', '--format=%h', path], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out.strip()

def expand_paths(paths):
    expanded = []
    for path in paths:
        if "*" in path or "?" in path:
            expanded.extend(glob.glob(path))
        else:
            expanded.append(path)
    return expanded

if __name__ == "__main__":
    import optparse, sys

    """
    ./hashbust.py --git --path foo.css *.html
    """

    parser = optparse.OptionParser("""%prog --version VERSION --path PATH [dest1 [dest2 [...]]]""")
    parser.add_option("--git", dest="git", action="store_true",
        help="use the git hash relevant to the provided PATH")
    parser.add_option("-v", "--version", dest="version", default="1",
        help="the version string (hint: `git log -n 1 --format=%h filename`)")
    parser.add_option("-p", "--path", "--paths", dest="path", default=None,
        help="the path to replace")
    parser.add_option("-q", "--query-key", dest="query_key", default="v",
        help="the key to use in the cache-busting query string URLs")

    options, args = parser.parse_args()

    paths = map(lambda s: s.strip(), options.path.split(","))
    paths = expand_paths(paths)

    print >> sys.stderr, "paths: %s" % paths

    def replace(text):
        for path in paths:
            if options.git:
                version = get_git_hash(path)
                print >> sys.stderr, "got git version: '%s' for path '%s'" % (version, path)
            else:
                version = options.version
            text = hashbust(text, path, version, options.query_key)
        return text

    if len(args) > 0 and args[0] != "-":
        for filename in args:
            fp = open(filename, "r")
            text = fp.read()
            fp.close()
            output = replace(text)
            fp = open(filename, "w")
            fp.write(output)
            fp.close()
    else:
        text = sys.stdin.read()
        output = replace(text)
        sys.stdout.write(output)
