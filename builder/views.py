from django.shortcuts import render

from django.http import HttpResponse

import subprocess
from subprocess import call


def fly(request):
    call(['rm', '-rf', 'durputtbuilder/operation-mr-putt-putt'])



    call(['git', 'clone', '-b', 'dev', 'https://github.com/jwitcig/operation-mr-putt-putt'])

    subprocess.Popen(['fastlane', 'ios', 'fly'], cwd='~/operation-mr-putt-putt')

    return HttpResponse()
