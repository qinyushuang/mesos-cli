# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import, print_function

import json

from .. import cli, completion_helpers
from ..master import CURRENT as MASTER

parser = cli.parser(
    description="Fetch the JSON encoded state for either the master " +
                "or a specific slave."
)

parser.add_argument(
    "slave", nargs="?",
    help="Slave ID filter to retrieve state for. " +
    	 "May match multiple slaves (or all if unspecified)"
).completer = completion_helpers.slave


@cli.init(parser)
def main(args):
    if not args.slave:
        print(json.dumps(MASTER.state, indent=4))
    else:
        print(json.dumps(
            [s.state for s in MASTER.slaves(args.slave)], indent=4))
