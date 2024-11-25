from setuptools import find_packages,setup
from typing import List

hyphenedot='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if hyphenedot in requirements:
            requirements.remove('hyphenedot')
        return requirements
    
setup(
    name='DiamondPricePrediction',
    author='Bavadharani',
    author_email='bavadharani2536@gmail.com',
    version='0.0.1',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)
