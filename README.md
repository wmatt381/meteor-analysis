# MeteorAnalysis
A simple project to download and analyze meteor landing data.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)

## General info
This project is a simple program to download meteor landing information from a JSON located at [NASA's Open Data Portal](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh), create an SQL database and analyze the data to extract information.

## Technologies
Project is created with:
* Python 3.9.2
* SQLite 3.35.5

## Setup
To run this project, download files and execute 'meteor_download.py' from command line. The program will ask for a URL to download from, if no URL is specified it will default to [NASA's Open Data Portal-Meteor Landings](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh). An SQLite database named 'nasaMeteor' will be created in the working directory.

## Status
2021-06-7 Completed: JSON download and database creation functionally complete.

Work in Progress: Add functions for analysis of data and continue to refine existing code.
