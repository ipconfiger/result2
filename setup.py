from setuptools import setup

readme = open('README.md').read()

setup(name='result2',
            version='0.0.1',
            description='A Swift-Style result type for Python',
            author='Alexander Li',
            author_email='superpowerlee@gmail.com',
            url='https://github.com/ipconfiger/result2',
            packages=['result2'],
            zip_safe=True,
            include_package_data=True,
            license='MIT',
            keywords='swift result enum',
            long_description=readme,
            classifiers=[
                          'Development Status :: 1 - Beta',
                          'License :: OSI Approved :: MIT License',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 3',
                      ],
      )