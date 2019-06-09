
import os
import re


path = os.path.dirname(os.path.abspath(__file__))
ignore_dir = [".git", ".idea", "assets", ".gitignore"]


def _make_dir_list(dir_path, result=[]):
    """

    Args:
        dir_path: str abs path

    Returns: List[str]

    """
    if not result:
        result = []
    if not os.path.isdir(dir_path):
        result.append(dir_path)
    else:
        for file in sorted(os.listdir(dir_path)):
            file_path = os.path.join(dir_path, file)
            if file.endswith(".md"):
                result.append(file_path)
            if os.path.isdir(file_path):
                _make_dir_list(file_path)
    return result


def make_file_list(path):
    res = {}
    for file in sorted(os.listdir(path)):
        sub_path = os.path.join(path, file)
        if file not in ignore_dir and os.path.isdir(sub_path):
            file_list = _make_dir_list(sub_path)
            if file_list:
                res.update({file: file_list})
    return res


def get_contents(file_dict):
    """

    Args:
        file_list: Dict

    """
    contents = ""
    for title, file_list in file_dict.items():
        content = ""
        content += f"### {title}\n"
        for file in file_list:
            file_name = os.path.split(file)[-1]
            file_path = re.sub("/home/lanms/Desktop/github/learning-notes", '.', file)
            content += f"- [{file_name}]({file_path})\n"
        contents += content
    return contents


def main():
    file_dict = make_file_list(path)
    file_contents = get_contents(file_dict)
    readme = os.path.join(path, "README.md")
    with open(readme, "a", encoding="utf-8") as f:
        f.write(file_contents)


if __name__ == '__main__':
    main()
