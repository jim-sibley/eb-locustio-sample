# Copyright 2015-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.

import os
from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):

    @task()
    def get_home_page(self):
        self.client.get("/")


class MyLocust(HttpLocust):
    host = os.getenv('TARGET_URL', "http://localhost")
    task_set = MyTaskSet
    min_wait = 100
    max_wait = 300
