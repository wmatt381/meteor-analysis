#!/usr/bin/env python3
import sqlite3

# Created for modular implementation of SQL manipulation functions.

# Function to create SQL table (Table name, column1 TYPE, column2 TYPE,...)
def createTable(*args):
    elements = list(args)
    parclose = ')' # Closing ) added because of error with attempting to use join
    command = 'CREATE TABLE IF NOT EXISTS ' +  ' ('.join(elements[0:2]) + ', ' + ', '.join(elements[2:])
    command = command + parclose
    return command
