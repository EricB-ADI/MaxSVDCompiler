import argparse
import xml.etree.ElementTree as ET
from argparse import RawTextHelpFormatter
import readline

descText = "Compile SVD per peripheral to one file describing entire MCU"
parser = argparse.ArgumentParser(description=descText, formatter_class=RawTextHelpFormatter)
parser.add_argument('device',help='MCU Part Number (e.g MAX32665')
parser.add_argument('series',help='Chip Series (e.g  ME14)')
parser.add_argument('cpu',help='Main Processor for Device (e.g Cortex-M4 = CM4')
parser.add_argument('-p', '--path', default="",help='Path to search for SVDs in Default is current path')


def discoverSvds(basepath):
    svdfiles = []

    return svdfiles
    

svd_output_name = 'svd_me14.svd' 

doc = ET.parse('gpio_reva_me14.svd')

root = doc.getroot()


periph = root.find('peripherals')

block = ET.tostring(periph)

print(block)