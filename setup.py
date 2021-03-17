import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
prjurl = "https://github.com/tirtharajsinha/bostas/"


setuptools.setup(
    name="bostas",
    version="0.0.2",
    author="Tirtharaj Sinha",
    author_email="sinhatirtharaj@gmail.com",
    description="Tool for social media automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=prjurl,
    project_urls={
        "Bug Tracker": prjurl+"issues",
        "Quick StarterPlate":prjurl+"docu/guide.html/",
    },
    keywords=(
        "bostas python social-Media instagram automation marketing promotion bot selenium "
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Topic :: Software Development :: Build Tools",
    ],
    packages=setuptools.find_packages(),
    install_requires=["beautifulsoup4==4.9.3","requests==2.25.1","selenium==3.141.0"],
    python_requires=">=3.6",
)
