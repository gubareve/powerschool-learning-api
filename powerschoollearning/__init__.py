# All Rights Reserved. You are not allowed to redistribute this software, or use
# the software to build derivative works based upon without prior written permission.

# Permission is hereby granted, free of charge, to any person obtaining a verbatim
# copy of this software and associated documentation files (the "Software").

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import logging

import aiohttp
import lxml.html

from .assignments import Assignment
from .classes import Eclass
from .errors import AuthFailed, LoginFailed

logger = logging.getLogger("powerschoollearning")


class ps:
    """Powerschool Class"""

    def __init__(self, session_id: str, url_base: str):
        """
        Powerschool client class.
        :param session_id: current sesion id
        :type session_id: str
        :param url_base: url base for all api calls
        :type url_base: str
        :param fetch_classes: (optional) load and store classes on login (defualts to true)
        :type fetch_classes: bool
        """
        self.session_id = session_id
        self.url_base = url_base
        logger.info(f"PowerSchool Classs initialized with base url {url_base}.")

    async def login(self, fetch_classes: bool = True):
        """
        Tests if login info is correct by sending a get request to the /do/account endpoint.
        :param fetch_classes: (optional) load and store classes on login (defualts to true)
        :type fetch_classes: bool
        """
        login_url = f"https://{self.url_base}/do/account"
        cookies = {"_session_id": self.session_id}
        async with aiohttp.ClientSession(cookies=cookies) as session:
            async with session.get(login_url) as response:
                response_code = int(response.status)
                if response_code == 200:
                    response_string = await response.text()
                    document = lxml.html.fromstring(response_string)
                    title = document.xpath("//title/text()")[0]
                    if "PowerSchool Learning : My Account" == title:
                        text_rows = document.xpath("//tr[@valign='top']/td/text()")
                        self.full_name = [x for x in text_rows if "\n" not in x][0]
                        self.email = document.xpath('//*[@id="user_login_txt"]/text()')[
                            0
                        ]
                        self.username = self.email.split("@")[0]
                        if fetch_classes:
                            await self.fetch_classes()
                            logger.info("Fetched classes.")
                    else:
                        logger.warn("Incorrect title found, failing.")
                        raise LoginFailed
                else:
                    logger.warn("Non 200 error code recieved. Failing")
                    raise LoginFailed

    async def fetch_classes(self):
        """
        Fetches all the classes the user is in and stores them.
        """
        homepage_url = f"https://{self.url_base}/u/{self.username}/portal"
        cookies = {"_session_id": self.session_id}
        async with aiohttp.ClientSession(cookies=cookies) as session:
            async with session.get(homepage_url) as response:
                response_code = int(response.status)
                if response_code == 200:
                    response_string = await response.text()
                    document = lxml.html.fromstring(response_string)
                    title = document.xpath("//title/text()")[0]
                    if "PowerSchool Learning : Portal" in title:
                        class_rows = document.xpath(
                            "//div[@class='eclass_list']/ul/li/div[@data-alt-tip='true']"
                        )
                        self.classes = []
                        for row in class_rows:
                            a_link = row.xpath("./a")[0]
                            x = Eclass(
                                name=row.get("atitle"),
                                url=a_link.get("href").replace("/cms_page/view", ""),
                                teacher=a_link.get("href").split("/")[1],
                            )
                            self.classes.append(x)
                            logger.debug(f"Got new class {x.name}.")
                    else:
                        logger.warn("Incorrect title recieved, failing.")
                        raise AuthFailed
                else:
                    logger.warn("Non 200 error code recieved, failing.")
                    raise AuthFailed

    async def fetch_assignments(self, class_to_fetch: Eclass):
        """
        Returns a list of all the assignments in a class.
        :param relative_class_url: relative url of the class
        :type relative_class_url: Eclass
        """
        assignments_url = f"https://{self.url_base}/{class_to_fetch.url}/assignment"
        cookies = {"_session_id": self.session_id}
        async with aiohttp.ClientSession(cookies=cookies) as session:
            async with session.get(assignments_url) as response:
                response_code = int(response.status)
                if response_code == 200:
                    response_string = await response.text()
                    document = lxml.html.fromstring(response_string)
                    title = document.xpath("//title/text()")[0]
                    if (
                        f"PowerSchool Learning : {class_to_fetch.name} : Assignments"
                        == title
                    ):
                        assignment_list = document.xpath(
                            "//div[@id='assignment_list']/table/tr"
                        )[1:100]
                        result = []
                        for assignment in assignment_list:
                            assignment_tds = assignment.xpath("./td")
                            assignment_url = (
                                assignment_tds[0]
                                .xpath("./a")[0]
                                .get("onclick")
                                .replace("TB_show('", "")
                                .replace("')", "")
                            )
                            class_name = class_to_fetch.url.split("/")[1]
                            assignment_name = assignment_tds[0].xpath("./a/text()")[0]
                            assignment_status = assignment_tds[1].xpath("./text()")[0]
                            assignment_due = assignment_tds[2].xpath("./text()")[0]
                            assignment_page = assignment_tds[3].xpath("./text()")[0]
                            if assignment_page == "n/a":
                                assignment_page = 0
                            assignment_turnedin = bool(assignment_tds[4].xpath("./i"))
                            assignment = Assignment(
                                name=assignment_name,
                                url=assignment_url,
                                class_name=class_name,
                                due=assignment_due,
                                page=assignment_page,
                                handed_in=assignment_turnedin,
                                status=assignment_status,
                            )
                            result.append(assignment)
                        return result
                    else:
                        logger.warn("Incorrect title recieved, failing.")
                        raise AuthFailed
                else:
                    logger.warn("Non 200 error code recieved, failing.")
                    raise AuthFailed

    async def get_grades(self, eclass: Eclass):
        """
        Returns a updated assignment object that has more details.
        :param assignment: assignment object that will be updated, must contain url.
        :type assignment: Assignment
        """
        grades_url = f"https://{self.url_base}{eclass.url}/grades/index3"
        cookies = {"_session_id": self.session_id}
        async with aiohttp.ClientSession(cookies=cookies) as session:
            async with session.get(grades_url) as response:
                response_code = int(response.status)
                if response_code == 200:
                    response_string = await response.text()
                    document = lxml.html.fromstring(response_string)
                    title = document.xpath("//title/text()")[0]
                    if "Gradebooks" in title:
                        print(response_string)
                    else:
                        logger.warn("Incorrect title found, failing.")
                        raise LoginFailed
                else:
                    logger.warn("Non 200 error code recieved. Failing")
                    raise LoginFailed