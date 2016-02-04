########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

"""
Tests 'cfy ssh'
"""

from cloudify_cli import utils
from cloudify_cli.tests.commands.test_cli_command import CliCommandTest


class LogsTest(CliCommandTest):

    def test_no_prior_init(self):
        self._assert_ex('cfy logs get', 'Cannot find .cloudify')

    def test_with_empty_config(self):
        settings = utils.CloudifyWorkingDirectorySettings()
        self._create_cosmo_wd_settings(settings)
        self._assert_ex('cfy logs get',
                        'Management Key is not set '
                        'in working directory settings')

    def test_with_no_key(self):
        settings = utils.CloudifyWorkingDirectorySettings()
        settings.set_management_user('test')
        settings.set_management_server('127.0.0.1')
        self._create_cosmo_wd_settings(settings)
        self._assert_ex('cfy logs get',
                        'Management Key is not set '
                        'in working directory settings')

    def test_with_no_user(self):
        settings = utils.CloudifyWorkingDirectorySettings()
        settings.set_management_server('127.0.0.1')
        settings.set_management_key('/tmp/test.pem')
        self._create_cosmo_wd_settings(settings)
        self._assert_ex('cfy logs get',
                        'Management User is not set '
                        'in working directory settings')

    def test_with_no_server(self):
        settings = utils.CloudifyWorkingDirectorySettings()
        settings.set_management_user('test')
        settings.set_management_key('/tmp/test.pem')
        self._create_cosmo_wd_settings(settings)
        self._assert_ex('cfy logs get', 'Must either first run')
