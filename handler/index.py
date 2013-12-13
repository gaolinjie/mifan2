#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2013 mifan.tv

import uuid
import hashlib
import Image
import StringIO
import time
import json
import re
import urllib2
import tornado.web
import lib.jsonp
import pprint
import math
import datetime 

from base import *
from lib.variables import *
from form.topic import *
from lib.variables import gen_random
from lib.xss import XssCleaner
from lib.utils import find_mentions
from lib.reddit import hot
from lib.utils import pretty_date

from lib.utils import find_video_id_from_url

class IndexHandler(BaseHandler):
    def get(self, template_variables = {}):
    	page = int(self.get_argument("page", "1"))
    	template_variables["head1"] = self.head1_model.get_head1_post()
    	template_variables["head2"] = self.head2_model.get_head2_post()
    	template_variables["stds"] = self.std_model.get_std_posts(current_page = page)
    	template_variables["hots"] = self.hot_model.get_hot_posts(current_page = page)
        self.render("index.html", **template_variables)