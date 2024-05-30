from setuptools import setup,find_packages

setup(
    name="sphui",
    version="0.3",
    author="Zhang Zhi Peng",
    author_email="3571669089@qq.com",
    url="https://github.com/ZZP-DMU/SPHUI",
    description="sphui is ui lib for sphlib",
    packages=find_packages(),
    install_requires=[
        "numpy"
    ]
)
print(find_packages())