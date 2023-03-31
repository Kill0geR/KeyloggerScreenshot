import subprocess
import sys

def get_working_ports():
    if sys.platform != "linux":
        cmd = subprocess.check_output(["netstat", "-ano"])
        all = cmd.split()

        working_ports = []
        zahlen = [str(zahl) for zahl in range(0, 11)]

        for each in all:
            str_each = str(each)
            if ":" in str_each:
                switch = str_each[::-1]
                this_port = ""
                for port in switch:
                    if port not in zahlen: pass
                    if port == ":": break
                    this_port += port

                another_switch = this_port[::-1]
                if "'" in another_switch: another_switch = another_switch.replace("'", "")

                if len(another_switch) == 4:
                    working_ports.append(another_switch)
        return working_ports
    return None
