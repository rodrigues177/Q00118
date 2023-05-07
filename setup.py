from setuptools import setup

REQUIREMENTS = []

with open('requirements.txt') as requirements:
    for requirement in requirements.readlines():
      REQUIREMENTS.append(requirement)

setup(     
    name="Q00118",
    author="rodrigues177",     
    version="3.9.7",     
    install_requires= REQUIREMENTS
)
