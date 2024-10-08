from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path) -> List[str]:
    requirements = []
    with open(file_path) as obj:
        req = obj.readlines()
        requirements = [r.replace("\n", "") for r in req]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Abinanthan',
    author_email='abinanthankaruppusamy@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)