import configparser
import os

config = configparser.RawConfigParser()
config_file_path = 'C:\\Users\\AB\\PycharmProjects\\OpenCart_automation\\configurations\\config.ini'
config.read(config_file_path)


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url
