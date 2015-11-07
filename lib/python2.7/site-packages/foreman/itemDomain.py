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

import base64
from string import Template
from foreman.item import ForemanItem
from foreman.subItemInterface import SubItemInterface
from foreman.subItemSubnet import SubItemSubnet
from foreman.subItemParameter import SubItemParameter
from foreman.subDict import SubDict


class ItemDomain(ForemanItem):
    """
    ItemHost class
    Represent the content of a foreman hostgroup as a dict
    """

    objName = 'domains'
    payloadObj = 'domain'

    def enhance(self):
        """ Function enhance
        Enhance the object with new item or enhanced items
        """
        self.update({'parameters':
                     SubDict(self.api, self.objName,
                             self.payloadObj, self.key,
                             SubItemParameter)})
        self.update({'interfaces':
                     SubDict(self.api, self.objName,
                             self.payloadObj, self.key,
                             SubItemInterface)})
        self.update({'subnets':
                    SubDict(self.api, self.objName,
                            self.payloadObj, self.key,
                            SubItemSubnet)})

    def __setitem__(self, key, attributes):
        """ Function __setitem__
        Set a parameter of a foreman object as a dict

        @param key: The key to modify
        @param attribute: The data
        @return RETURN: The API result
        """
        if key in ['parameters', 'interfaces', 'subnets']:
            print('Can not assign {} directly, use .append()'.format(key))
            return False
        else:
            return ForemanItem.__setitem__(self, key, attributes)
