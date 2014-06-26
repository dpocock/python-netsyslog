
#
# This is a very trivial demo of how to write a syslog collector
# that receives messages from the wire and prints them on
# the screen.
#
# To run it, specify the port number as the first command line
# argument, e.g.
#
#     python simple_server.py 10514
#


import logging
import netsyslog
import sys

class MyHandler(netsyslog.SyslogTCPHandler):

    def handle_message(self, frame):
        """Handle parsed Syslog frames.

        Applications should override this method.

        This default implementation prints some data from each frame.

        """
        print "severity: " + str(frame.pri.severity)
        print "facility: " + str(frame.pri.facility)
        print "tag: " + str(frame.msg.tag)
        print "pid: " + str(frame.msg.pid)
        print "content: " + str(frame.msg.content)
        print "host: " + str(frame.header.hostname)
        print "ts: " + str(frame.header.timestamp)
        print ""

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    c = netsyslog.Collector(int(sys.argv[1]), MyHandler)
    c.run()

# Copyright (C) 2010, Daniel Pocock http://danielpocock.com
#
# This module is free software, and you may redistribute it and/or modify
# it under the same terms as Python itself, so long as this copyright message
# and disclaimer are retained in their original form.
#
# IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
# SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF
# THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.
#
# THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS,
# AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
# SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

