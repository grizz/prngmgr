# Copyright 2016-2017 Workonline Communications (Pty) Ltd. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Management command module for prngmgr."""

from django.core.management.base import BaseCommand
from prngmgr import models
from prngmgr.settings import *


class Command(BaseCommand):
    help = 'Displays infomation from our PDB record'
    def handle(self, *args, **options):
        net = models.Network.objects.get(asn=MY_ASN)
        self.stdout.write( "Name: %s" % net.name )
        self.stdout.write( "ASN: AS%s" % net.asn )
