import os
from django.shortcuts import render

from django.http import HttpResponse

import subprocess
from subprocess import call


def fly(request):
    call(['ls'])

    call(['rm', '-rf', 'operation-mr-putt-putt'])
    call(['ls'])


    call(['git', 'clone', '-b', 'dev', 'https://github.com/jwitcig/operation-mr-putt-putt'])
    call(['ls'])


    project = grandparent_dir = os.path.abspath(  # Convert into absolute path string
        os.path.join(  # Current file's grandparent directory
            os.path.join(  # Current file's parent directory
                os.path.dirname(  # Current file's directory
                    os.path.abspath(__file__)  # Current file path
                ),
                os.pardir
            ),
            os.pardir
        )
    )
    print project

    call(['fastlane', 'ios', 'fly'], cwd=project+'operation-mr-putt-putt')

    return HttpResponse()
