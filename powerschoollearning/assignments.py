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


class Assignment:
    "Class for assignments in the portal"

    def __init__(
        self,
        name: str = None,
        url: str = None,
        class_name: str = None,
        points: int = None,
        description: str = None,
        posted: str = None,
        due: str = None,
        handed_in: bool = None,
        page: int = None,
        status: str = None,
    ):
        """
        :param name: the name of the Assignment.
        :type name: str
        :param url: url of the Assignment
        :type url: str
        :param class_name: name of the class that posted the assignment
        :type class_name: str
        :param points: the number of points the assignment is worth
        :type points: int
        :param description: description of the assignment
        :type description: str
        :param posted: string of the date powerschool gives for when the assignment was posted
        :type posted: str
        :param due: due date that powerschool gives you
        :type due: str
        :param handed_in: if the assignment has been handed in or not
        :type handed_in: bool
        :param page: page of the assignment
        :type page: int
        :param status: status of the assignment
        :type status: str
        """
        self.name = name
        self.url = url
        self.class_name = class_name
        self.points = points
        self.description = description
        self.posted = posted
        self.due = due
        self.handed_in = handed_in
        self.page = page
        self.status = status

    def __str__(self):
        return self.name
