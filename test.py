from pathlib import Path


HYPHEN = '-e .'

# with open("README.md", 'r', encoding='utf-8')as f:
#     long_description = f.read()
__version__ = "0.0.0"


def get_requirements(file_path: str):
    requierments = []
    with open("requirements.txt", 'r', encoding='utf-8')as f:
        requierments = f.readlines()
        requierments = [req.replace('\n', ' ') for req in requierments]

        if HYPHEN in requierments:
            requierments.remove(HYPHEN)
    return requierments


f = Path('E:\Mlop\End to end\End-to-end-Detecting-Card-Fraud\requirements.txt')
print(get_requirements(f))
