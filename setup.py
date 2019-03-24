from setuptools import setup, find_packages

setup(name='deadspeare',
      version='0.1',
      packages=find_packages(),
      description='deadspeare setup to run keras on gcloud ml-engine',
      author='Sam Farren',
      author_email='farren.19@osu.edu',
      license='MIT',
      install_requires=[
                        'keras==2.1.2',
                        'h5py'
                        ],
      zip_safe=False)
