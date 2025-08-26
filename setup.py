from setuptools import setup, find_packages
from cerberus import __version__

setup(
    name="cerberus-profiler",
    version=__version__,
    description="CERBERUS – Advanced User Password Profiler",
    author="Yashraj Sharma",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cerberus=cerberus.cli:cli",
        ],
    },
    install_requires=["colorama", "tabulate"],
    extras_require={
        "dev": ["pytest"],
    },
)
