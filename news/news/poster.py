#-*- coding: utf-8 -*-

"""
Poster: 发布微博。
"""

#import re
import pickle
import urllib2
from time import sleep

import config
#from lib.weibopy.auth import OAuthHandler
#from weibopy.api import API
import weibopy
import Helper

import database

log = Helper.log
