# *****************************COPYRIGHT******************************
# (C) Crown copyright Met Office. All rights reserved.
# For further details please refer to the file LICENCE.txt
# which you should have received as part of this distribution.
# *****************************COPYRIGHT******************************
#
# This file is part of the UM SST Pert library module.
#
# It is free software: you can redistribute it and/or modify it under
# the terms of the Modified BSD License, as published by the
# Open Source Initiative.
#
# Mule is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Modified BSD License for more details.
#
# You should have received a copy of the Modified BSD License
# along with this UM SST-pert module.
# If not, see <http://opensource.org/licenses/BSD-3-Clause>.
import os
import shutil
import setuptools
import numpy as np
from glob import glob


class CleanCommand(setuptools.Command):
    """
    Custom clean which gets rid of build files that the
    standard clean command does not
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for cleanpath in ["./build", "./dist", "./lib/*.egg-info",
                          "./lib/*/*.so"]:
            print("Removing: {0}...".format(cleanpath))
            cleanpath = glob(cleanpath)
            if cleanpath:
                if os.path.isfile(cleanpath[0]):
                    os.remove(cleanpath[0])
                elif os.path.isdir(cleanpath[0]):
                    shutil.rmtree(cleanpath[0])

setuptools.setup(
    name='um_sstpert',
    version='2019.01.1',
    description='Unified Model SST-perturbation extension and utility',
    author='UM Systems Team',
    url='https://code.metoffice.gov.uk/trac/um',
    cmdclass={'clean': CleanCommand},
    package_dir={'': 'lib'},
    packages=['um_sstpert'],
    features={
        'sstpert': setuptools.Feature(
            "UM SST-pert library (requires UM Licence)",
            standard=True,
            ext_modules=[
                setuptools.Extension(
                    'um_sstpert.um_sstpert',
                    ['lib/um_sstpert/um_sstpert.c'],
                    include_dirs=[np.get_include()],
                    libraries=["um_sstpert",
                               "shum_string_conv",
                               "shum_constants"])
                ])},
    entry_points={
        'console_scripts': [
            'mule-sstpert = um_sstpert:_main',
            ]})
