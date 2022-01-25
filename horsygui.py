import argparse
import os
import sys
import modules.gui as gui
import modules.tui as tui
from modules.console import cls
from modules.manager import install, uninstall, apps_list
from modules.virustotal import add_to_cfg
from modules.uploader import upload
from modules.source import get_source
from modules.search import search, info
import modules.vars as horsy_vars


