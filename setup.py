from setuptools import setup

setup(name='botchat',
      version='0.1',
      description='Let a bot chat on your behalf on whatsapp',
      url='https://github.com/lakshaykalbhor/Whatsapp-BotChat',
      author='Lakshay Kalbhor',
      author_email='lakshaykalbhor@gmail.com',
      license='MIT',
      packages=['botchat'],
      scripts=["bin/botchat"],
      install_requires=[
          'selenium',
          'bs4',
      ],
      zip_safe=False
      )