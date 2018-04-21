# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


def init():
    # create the application instance :)
    app = Flask(__name__) 
    
     # load config from this file , flaskr.py
    app.config.from_object(__name__)

    # Usually, it is a good idea to load a separate, environment-specific 
    # configuration file. Flask allows you to import multiple configurations 
    # and it will use the setting defined in the last import. 
    # This enables robust configuration setups. from_envvar() can help achieve this.
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)
 