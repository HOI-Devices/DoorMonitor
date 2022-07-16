from unittest import IsolatedAsyncioTestCase
from unittest import TestCase
from main import Main
import config
import json
import console_logging

'''
General Note:

These tests and this software in general assumes:

1.The matching server follows the correct protocol
2.There are no network interruptions
'''

class AsyncTests(IsolatedAsyncioTestCase):

    async def test_successful_authentication(self):
        main = Main()
        websocket = main.establish_connection()
        response = main.send_connection_credentials(websocket)
        self.assertEqual("success",response)

    async def test_successful_configuration(self):
        test_data = {"host":"test1","port":"test2","name":"test3","interval":1}

        config_maker = config.ConfigMaker()
        config_maker.write_config(test_data)
        actual_config = config.DoorMonitorConfig()

        self.assertEqual("test1",actual_config.host)
        self.assertEqual("test2",actual_config.port)
        self.assertEqual("test3",actual_config.name)
        self.assertEqual(1,actual_config.door_check_interval)

class SyncTests(TestCase):

    def test_console_logger_row(self):
        logger = console_logging.ConsoleLogger()
        self.assertEqual(0,logger.row_number)
        logger.log_generic_row("test","green")
        self.assertEqual(1,logger.row_number)