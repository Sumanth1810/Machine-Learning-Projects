from setup import find_packages,setup
setup(  
    name='ML Project',
    version='0.01',
    author='Sumanth Gowda R',
    author_email='sumanthgowdaramesh@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn']  
)