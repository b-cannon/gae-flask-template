#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from flask import Flask, request, render_template, url_for, redirect
from flask_cache import Cache

app = Flask(__name__)

@app.route('/')
def hello():
    msg = 'Hello World'
    return render_template('home.html', msg=msg)

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, nothing here', 404

