#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from six.moves import http_client

from keystone.tests.unit import rest


class HealthCheckTestCase(rest.RestfulTestCase):
    def test_get_healthcheck(self):
        with self.test_client() as c:
            resp = c.get('/healthcheck', expected_status_code=http_client.OK)
            # healthcheck is not supposed to return any data
            self.assertEqual(0, resp.content_length)
