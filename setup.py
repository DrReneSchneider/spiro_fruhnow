from setuptools import setup, find_packages
setup(name = 'spiro',
      version = '1.0b2',
      packages = find_packages(),
      scripts = ['bin/spiro'],
      install_requires = ['picamera==1.13', 'RPi.GPIO==0.7.1', 'Flask==2.2.5', 'waitress==2.1.2', 'numpy', 'Werkzeug==2.2.3'],
      author = 'Jonas Ohlsson adapted by René Schneider, Ulrike Lehmann, and Felix Ruhnow',
      author_email = 'jonas.ohlsson@slu.se and rene.schneider@uni-potsdam.de',
      description = 'Control software for the SPIRO imaging system adapted for IR dark growth imaging',
      url = 'https://github.com/drreneschneider/spiro_fruhnow',
      include_package_data = True,
      zip_safe = False,
      )
