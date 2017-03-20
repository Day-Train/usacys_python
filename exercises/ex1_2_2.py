"""

"""
import argparse

from hashlib import sha1
from Evtx.Evtx import Evtx
from Evtx.Views import evtx_file_xml_view
from lxml import etree


def main(filename):
    with Evtx(filename) as evtx:
        parse_file(evtx)


def parse_file(evtx):
    ns = "{http://schemas.microsoft.com/win/2004/08/events/event}"
    for xml, record in evtx_file_xml_view(evtx.get_file_header()):
        tree = etree.fromstring('<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>{}'.format(xml))
        sys = tree.find("{}System".format(ns))
        event = sys.find("{}EventID".format(ns)).text
        record_id = sys.find("{}EventRecordID".format(ns)).text
        time = sys.find("{}TimeCreated".format(ns)).get('SystemTime', '')
        print(sha1(record_id).hexdigest())
        break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EVTX File Viewing Tool')
    parser.add_argument('filename', type=str, help='EVTX File to parse')
    args = parser.parse_args()
    main(args.filename)