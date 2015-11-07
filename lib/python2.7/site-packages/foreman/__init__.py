#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Authors:
# @author: David Blaisonneau <david.blaisonneau@orange.com>
# @author: Arnaud Morin <arnaud1.morin@orange.com>

from foreman.api import Api
from foreman.objects import ForemanObjects
from foreman.smartProxies import SmartProxies
from foreman.operatingsystems import OperatingSystems
from foreman.hostgroups import HostGroups
from foreman.hosts import Hosts
from foreman.domains import Domains
from foreman.architectures import Architectures
from foreman.subnets import Subnets
from foreman.puppetClasses import PuppetClasses
from foreman.computeResources import ComputeResources
from foreman.smartClassParameters import SmartClassParameters
from foreman.environments import Environments
from foreman.configTemplates import ConfigTemplates


class Foreman:
    """
    HostGroup class
    """
    def __init__(self, password, login='admin', ip='127.0.0.1'):
        """ Function __init__
        Init the API with the connection params
        @param password: authentication password
        @param password: authentication login - default is admin
        @param ip: api ip - default is localhost
        @return RETURN: self
        """
        self.api = Api(login=login, password=password, ip=ip,
                       printErrors=False)
        self.domains = Domains(self.api)
        self.smartProxies = SmartProxies(self.api)
        self.puppetClasses = PuppetClasses(self.api)
        self.operatingSystems = OperatingSystems(self.api)
        self.architectures = Architectures(self.api)
        self.subnets = Subnets(self.api)
        self.hostgroups = HostGroups(self.api)
        self.hosts = Hosts(self.api)
        self.computeResources = ComputeResources(self.api)
        self.environments =  Environments(self.api)
        self.configTemplates =  ConfigTemplates(self.api)
        self.smartClassParameters = SmartClassParameters(self.api)
        self.settings =  ForemanObjects(self.api, 'settings', 'setting')
        self.ptables =  ForemanObjects(self.api, 'ptables', 'ptable')
        self.media =  ForemanObjects(self.api, 'media', 'medium')
