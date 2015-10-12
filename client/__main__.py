from socket import getfqdn
from getpass import getuser
from datetime import datetime
from os.path import expanduser
import os
from random import choice
from platform import system, mac_ver, win32_ver, uname
from subprocess import check_call, PIPE, CalledProcessError
from time import sleep
from pprint import PrettyPrinter

import netifaces
from netaddr import EUI
from netaddr.core import NotRegisteredError, AddrFormatError
from jinja2 import Environment, FileSystemLoader

from client.search import extensions, find_files


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
            interface["mfg"] = "Unknown"
        active.append(interface)

    return active


def get_random_files(root_path, n):
    paths = find_files(root_path, filter_extensions=extensions["documents"])
    selected_paths = []
    for i in range(n):
        selected_paths.append(choice(paths))

    return selected_paths


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
    args = [open_command]
    args.append(payload_args)
    try:
        check_call(args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    except CalledProcessError:
        success = False

    return success

sample_file_paths = "\n\n".join(get_random_files(home, 10))
contact_email_address = "security@example.com"

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('media.html')
template_output = template.render(sample_file_paths=sample_file_paths,
                                  contact_email_address=contact_email_address)
with open("warning.html", "w") as warning_file:
    warning_file.write(template_output)

payloads = ["warning.html"]

payload_results = []
for payload in payloads:
    if platform_name == "Windows":
        os.startfile(payload)
    else:
        payload_results.append(dict(args=payload, success=launch_payload(payload)))
    sleep(1)


info = dict(
    platform=dict(name=platform_name, version=platform_version),
    user=getuser(),
    local_time=datetime.now().isoformat(),
    fqdn=getfqdn(),
    active_interfaces=get_active_interfaces(),
    payloads=payload_results
)

pretty = PrettyPrinter()
pretty.pprint(info)
