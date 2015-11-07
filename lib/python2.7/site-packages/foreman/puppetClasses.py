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

from foreman.objects import ForemanObjects
from foreman.itemPuppetClass import ItemPuppetClass


class PuppetClasses(ForemanObjects):
    """
    OperatingSystems class
    """
    objName = 'puppetclasses'
    payloadObj = 'puppetclass'
    itemType = ItemPuppetClass
    searchLimit = 100000

    def load(self):
        """ Function load
        Get the list of all objects

        @return RETURN: A ForemanItem list
        """
        cl_tmp = self.api.list(self.objName, limit=self.searchLimit).values()
        cl = []
        for i in cl_tmp:
            cl.extend(i)
        return {x[self.index]: ItemPuppetClass(self.api, x['id'],
                                               self.objName, self.payloadObj,
                                               x)
                for x in cl}
