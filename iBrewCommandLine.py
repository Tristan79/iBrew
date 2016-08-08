# -*- coding: utf8 -*

import sys
from iBrewProtocol import *
from iBrewVersion import *
from iBrewClient import *
from iBrewMonitor import *
from iBrewConsole import *

#------------------------------------------------------
# iBrew COMMAND LINE
#
# Command line access for iKettle 2.0 or Smarter Coffee
# Device
#------------------------------------------------------

class iBrewCommandLine:

    def is_valid_ipv4_address(self,address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:  # not a valid address
            return False

        return True

    def is_valid_ipv6_address(self,address):
        try:
            socket.inet_pton(socket.AF_INET6, address)
        except socket.error:  # not a valid address
            return False
        return True
    
    def help(self):
        iBrewPrintAppVersion()
        print 'Usage:'
        print '  iBrew [option] (host)'
        print
        print "[options]"
        print "  console             start console¹"
        print "  monitor             start monitor"
        print
        print "  iKettle 2.0 & Smarter Coffee Commands"
        print "  info                Device info"
        print "  status              Show status"
        print "  raw [data]          Send raw data to device"
        print
        print "  iKettle 2.0 Commands"
        print "  formula             Heat kettle formula mode"
        print "  heat                Heat kettle"
        print "  stop                Stop heating kettle"
        print
        print "  Smarter Coffee Commands"
        print "  brew                Brew coffee"
        print "  cups [number]       Set number of cups [1..12]"
        print "  grinder             Toggle grinder"
        print "  hotplate off        Turn hotplate off"
        print "  hotplate on         Turn hotplate on"
        print "  strength [strength] Set strength coffee [weak, medium or strong]"
        print
        print "  Help Commands"
        print "  protocol            Show protocol"
        print
        print "  ¹console grants access to advanced options"
        print
        print "(host) ip4 format, ip6 format or host name"
        print

    def __init__(self,host):
        
        # Lower Case Arguments
        arguments = len(sys.argv) - 1
        if arguments >= 1:
            arg1 = sys.argv[1].lower()
        if arguments >= 2:
            arg2 = sys.argv[2].lower()
        if arguments >= 3:
            arg3 = sys.argv[3].lower()

        # No arguments display help
        if arguments == 0:
            self.help()
            sys.exit()

        if arguments > 0:
            if self.is_valid_ipv4_address(sys.argv[arguments]) or self.is_valid_ipv6_address(sys.argv[arguments]):
                host = sys.argv[arguments]
      
        # Preform action!
        if arguments >= 1:
            if arg1 == "heat":
                iBrewClient(host).heat()
            elif arg1 == "stop":
                iBrewClient(host).stop()
            elif arg1 == "formula":
                iBrewClient(host).formula()
            elif arg1 == "status":
                iBrewClient(host).print_status()
            elif arg1 == "info":
                client = iBrewClient(host)
                client.info()
                client.print_info()
                pass
            elif arg1 == "grinder":
                iBrewClient(host).grinder()
            elif arg1 == "brew":
                iBrewClient(host).brew()
            elif arg1 == "protocol":
                iBrewProtocol().all()
            elif arg1 == "monitor":
                iBrewMonitor(host)
            elif arg1 == "console":
                iBrewConsole(host)
            elif arguments >= 2:
                if arg1 == "raw":
                    iBrewClient(host).raw(arg2)
                elif arg1 == "hotplate" and arg2 == "on":
                    iBrewClient(host).hotplate_on()
                elif arg1 == "hotplate" and arg2 == "off":
                    iBrewClient(host).hotplate_off()
                elif arg1 == "strength":
                    iBrewClient(host).coffee_strength(arg2)
                elif arg1 == "cups":
                    print "iBrew: Not Implemented"
                    # FIX WRONG IP{UT
                    #iBrewClient(host).coffee_cups(arg2)
                else:
                    self.help()
                    print 'iBrew: Invalid option: ',arg1
                    print
            else:
                self.help()
                print 'iBrew: Invalid option: ',arg1
                print