#!/usr/bin/env python
# coding=utf-8
#
## Copyright 2013 mifan.tv

import time
from lib.query import Query

class HotModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "hot"
        super(HotModel, self).__init__()

    def add_new_hot(self, hot_info):
        return self.data(hot_info).add()

    def get_hot_posts(self, num = 10, current_page = 1):
        join = "LEFT JOIN post ON hot.post_id = post.id\
                LEFT JOIN user AS author_user ON post.author_id = author_user.uid"
        order = "post.created DESC, post.id DESC"
        field = "post.*, \
                author_user.username as author_username, \
                author_user.avatar as author_avatar"
        return self.order(order).join(join).field(field).pages(current_page = current_page, list_rows = num)