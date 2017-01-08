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


    call(['fastlane', 'ios', 'fly'], cwd=os.path.realpath(__file__)+'/../operation-mr-putt-putt')

    return HttpResponse()
