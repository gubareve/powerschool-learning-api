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


class Grade:
    "Grade class."

    def __init__(self, earned_points: float, total_points: float, letter_grade: str, name: str, url: str):
        """
        :param percentage: grade percentage (0.97) is 97%
        :type name: str

        """
        self.earned_points = earned_points
        self.total_points = total_points
        self.letter_grade = letter_grade
        self.name = name
        self.url = url

    def __str__(self):
        return self.url
