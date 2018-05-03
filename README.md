# SQL Reporting Tool
A tool created for the Udacity Logs Analysis Project
The tool takes sql server data and answers the following questions:
1) What are the most popular three articles of all time?
2) Who are the most popular article authors of all time?
3) On which days did more than 1% of requests lead to errors? 

## Getting Started
Move the project folder to a folder accessible by your vagrant machine
ssh into your vagrant machine with 'vagrant ssh'
cd into the folder
run python reporting_tool.py

## Prerequisites
Python 2
psycopg2
The vargrant machine provided by Udacity
The news SQL database provided by Udacity

## Notes
Views are created for this tool, however the views are added and dropped
from within the python code
