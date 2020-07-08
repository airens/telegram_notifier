from setuptools import setup
from os.path import join, dirname

setup(name='telegram-notifier',
      version='0.1',
      description='Simple telegram notifier',
      url='http://github.com/airens/telegram_notifier',
      author='Valeriy Chistyakov',
      author_email='airens@mail.ru',
      license='MIT',
      packages=['telegram_notifier'],
      install_requires=['requests'],
      zip_safe=False,
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      long_description_content_type="text/markdown"
      )
