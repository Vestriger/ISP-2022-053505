from setuptools import setup

setup(
    name='custom_serialize',
    packages=[
        'custom_serialize',
        'custom_serialize/Serializer',
        'custom_serialize/Serializer/json',
        'custom_serialize/Serializer/toml',
        'custom_serialize/Serializer/yaml',
    ],
    version='1.0.0',
    author='vestriger',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.3'],
    test_suite='tests',
    scripts=['custom_serialize/serializer_cmd.py']
)