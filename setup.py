from setuptools import find_packages,setup
from typing import List

CONNECTOR="-e ."
def get_requirements(file_path:str)->List[str]:
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        
        if CONNECTOR in requirements:
            requirements.remove(CONNECTOR)
    
    return requirements


setup(
    name="SupplyChain_MLWorkflow Project",
    version="0.0.01",
    author="Subinoy Bera",
    author_email="subinoyberadgp@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)