from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'#this is just the indicator of the ending of requirements.txt
def get_requirements(file_path) -> List[str]:
    '''
    this function is going to return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

    


setup(
    name='mlProject reference',
    version='1.0.0',
    author='Vinayak',
    author_email='vinayak912002@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)