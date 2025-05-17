import setuptools
from typing import List

HYPHEN = '-e .'

with open("README.md", 'r', encoding='utf-8')as f:
    long_description = f.read()
__version__ = "0.0.0"


def get_requirements(file_path: str) -> List:
    requierments = []
    with open("requirements.txt", 'r', encoding='utf-8')as f:
        requierments = f.readlines()
        requierments = [req.replace('\n', ' ') for req in requierments]

        if HYPHEN in requierments:
            requierments.remove(HYPHEN)
    return requierments


REOP_NAME = 'End-to-end-Detecting-Card-Fraud'
AUTHER_USER_NAME = 'Mazenasag'
SRC_REPOS = 'CardFraud'
AUTHER_EMAIL = 'mezonabhy@gamil.com'


setuptools.setup(
    name=REOP_NAME,
    version=__version__,
    author=AUTHER_USER_NAME,
    auther_email=AUTHER_EMAIL,
    description="Card Fruad detection ",
    long_description=long_description,
    url=f"https://github.com/{AUTHER_USER_NAME}/{REOP_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHER_USER_NAME}/{REOP_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements('requirements.txt')
)
