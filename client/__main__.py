import sys
from socket import getfqdn
from getpass import getuser
from datetime import datetime
from os.path import expanduser
import os
from platform import system, mac_ver, win32_ver, uname
from subprocess import check_call, PIPE, CalledProcessError
from time import sleep
from pprint import PrettyPrinter

import netifaces
from netaddr import EUI
from netaddr.core import NotRegisteredError, AddrFormatError
from jinja2 import Environment, FileSystemLoader

from client.search import get_extentions_by_type, find_files, get_recent_files, basename_paths


def get_active_interfaces():
    active = []
    interfaces = netifaces.interfaces()
    for iface_name in interfaces:
        inet_addresses = netifaces.ifaddresses(iface_name)
        if netifaces.AF_LINK not in inet_addresses:
            continue
        if netifaces.AF_INET not in inet_addresses:
            continue
        interface = inet_addresses[netifaces.AF_INET][0]
        interface["name"] = iface_name
        if interface["addr"].startswith("127.") or interface["addr"].startswith("169.254."):
            continue
        interface["mac"] = inet_addresses[netifaces.AF_LINK][0]["addr"]
        try:
            registration = EUI(interface["mac"]).oui.registration()
            interface["mfg"] = registration.org
        except (NotRegisteredError, AddrFormatError):
            interface["mfg"] = ""
        active.append(interface)

    return active


platform_name = system()
if platform_name == "Darwin":
    platform_name = "Mac OS"
    open_command = "open"
    platform_version = mac_ver()[0]
    home = expanduser("~")
elif platform_name == "Windows":
    platform_version = win32_ver()[1]
    home = os.environ['USERPROFILE']
elif platform_name == "Linux":
    platform_version = uname()[3]
    home = expanduser("~")
    open_command = "xdg-open"
    home = expanduser("~")
else:
    platform_name = "Other"
    platform_version = ""
    open_command = ["xdg-open"]


def launch_payload(payload_args):
    success = True
    args = [open_command, payload_args]
    try:
        check_call(args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    except CalledProcessError:
        success = False

    return success

paths = find_files(home, filter_extensions=get_extentions_by_type(["documents", "audio", "video"]))
recent_files = "\n\n".join(basename_paths(get_recent_files(paths, 10)))
contact_email_address = "security@example.com"
if getattr(sys, 'frozen', None):
    base_dir = sys._MEIPASS
else:
    basedir = os.path.dirname(os.path.realpath(__file__))
templates_path = os.path.join(base_dir, 'templates')
print(templates_path)
env = Environment(loader=FileSystemLoader(templates_path))
template = env.get_template('media.html')
template_output = template.render(logo="logo.png",
                                  file_names=recent_files,
                                  contact_email_address=contact_email_address)

warning_path = os.path.join(base_dir, "warning.html")
with open(warning_path, "w") as warning_file:
    warning_file.write(template_output)

payloads = [warning_path]

payload_results = []
for payload in payloads:
    if platform_name == "Windows":
        os.startfile(payload)
        payload_results.append(dict(args=payload, success=True))
    else:
        payload_results.append(dict(args=payload, success=launch_payload(payload)))
    sleep(.5)


info = dict(
    platform=dict(name=platform_name, version=platform_version),
    user=getuser(),
    local_time=datetime.now().isoformat(),
    hostname=getfqdn().split(".")[0],
    active_interfaces=get_active_interfaces(),
    payloads=payload_results
)

pretty = PrettyPrinter()
pretty.pprint(info)
