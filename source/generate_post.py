from markdownmaker.document import Document
from markdownmaker.markdownmaker import *
import frontmatter
import argparse
import os
from pprint import pprint


def default_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", type=str, default="default.md")
    parser.add_argument("--tags", type=str, nargs="+")
    parser.add_argument("--result-folder-path", type=str, default="_posts/leetcode/")
    args = parser.parse_args()
    return args


def generate_md():
    data = frontmatter.load("_posts/leetcode/template.md")
    data["title"] = args.title
    data["tags"] = args.tags
    return frontmatter.dumps(data)


def save(str):
    _filename = "".join(args.title.split())
    _filename = _filename.replace(".", "_")
    with open(os.path.join(args.result_folder_path, _filename + ".md"), "w") as f:
        f.write(str)


if __name__ == "__main__":
    args = default_argument_parser()
    save(generate_md())
