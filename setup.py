from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    
    if "-e ." in requirements:
        requirements.remove("-e .")

    return requirements

setup(name='ml_pipeline', 
      version='0.0.1', 
      packages=find_packages(), 
      author='Shailendra Singh',
      author_email='shailendra24.singh@gmail.com',
      description='ML Pipeline',
      url='https://github.com/shailendra24/ml_pipeline',
      license='MIT',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      install_requires= get_requirements()
      )