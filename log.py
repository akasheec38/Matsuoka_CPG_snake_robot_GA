# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:39:25 2019

@author: MOC817
"""


import datetime
import os
import pandas as pd

class Logger:
    """
    Class for storing global logging related variables
    """
    log_file = None
    log_dir = None
    log_flag = True
    datetime_str = None

    def __init__(self, log_dir, log_flag=True):
        """
        Function to initialize the logging variables and to create a log file
        :param log_dir: The directory to save log files
        :param log_flag: If True, print on console and also save to file, else only save to file
        """
        print('log_dir: ', log_dir)
        if not os.path.exists(log_dir):
            raise ValueError('Log directory ' + log_dir + ' does not exist')

        # Find the datetime string
        datetime_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        Logger.datetime_str = datetime_str

        # Set the static global variables
        Logger.log_dir = os.path.join(log_dir, datetime_str)
        Logger.log_flag = log_flag

        # Create directory
        os.makedirs(Logger.log_dir)

        # Create log file name
        filename = 'log_' + datetime_str + '.txt'

        # Set in Globals
        Logger.log_file = os.path.join(Logger.log_dir, filename)

        # Create the log file
        open(Logger.log_file, 'a').close()

def excel_logger(df, file_txt):
    if not os.path.exists('Excel_files'):
        os.mkdir('Excel_files')
    file_name = './Excel_files/' + file_txt +  '.xlsx'
    writer = pd.ExcelWriter(file_name)
    df.to_excel(writer)
    writer.save()
    log(' [GA] Excel file saved at:' + os.path.abspath(file_name))
    #print('Excel file saved at: ' + os.path.abspath(file_name))
    #print('Excel file saved by name'+file_txt+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    
    
def log(logstr):
    """
    Print logstr with a timestamp to the console and store in the log file
    :param logstr: String to print
    :return:
    """

    logstr_fmt = ("[%s] %s \n" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], logstr))

    if Logger.log_flag:
        print (logstr_fmt)

    fh = open(Logger.log_file, 'a')
    fh.write(logstr_fmt)
    fh.close()