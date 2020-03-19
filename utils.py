# -*- coding: utf-8 -*-
import shelve
from random import shuffle

from telebot import types

from SQLighter import SQLighter
from config import  database_name


def get_question():
    db = SQLighter(database_name)
    question = db.select_all_question()
    return question





