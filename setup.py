from setuptools import setup
import sys

if not sys.version_info[0] == 3 and sys.version_info[1] < 5:
    sys.exit("Python < 3.5 is not supported")

version = "0.80"

setup(
    name="steampie",
    packages=[
        "steampy",
        "test",
        "examples",
    ],
    version=version,
    description="A Steam lib for trade automation",
    author="venoia",
    author_email="overutilization@gmail.com",
    license="MIT",
    url="https://github.com/venoia/steampie",
    download_url="https://github.com/venoia/steampie/tarball/" + version,
    keywords=[
        "steam",
        "trade",
    ],
    classifiers=[],
    install_requires=["requests", "beautifulsoup4", "rsa"],
)
