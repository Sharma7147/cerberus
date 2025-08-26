from setuptools import setup, find_packages

setup(
    name="cerberus-profiler",
    version="0.1.0",  # directly hardcoded, avoids import issues
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
