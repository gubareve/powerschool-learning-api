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


class LoginFailed(Exception):
    """
    This is throwed when the client attempts to log in and fails.
    """

    def __init__(self):
        super().__init__("Logging into powerschool failed (check your session id).")


class AuthFailed(Exception):
    """
    The previously correct session id become expired or was invalidated.
    """

    def __init__(self):
        super().__init__("AuthFailed (check your session id).")
