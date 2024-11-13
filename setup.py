# good if u want to publish as pypi package
import setuptools

#initilize readme file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ ="0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "avaniPatle"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "avanipatle07@gmail.com"

# local package setup - it will look for every folders constructor file and install it 
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple python package for NLP text summarizer app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)


    