import argparse
import xml.etree.ElementTree as ET
from argparse import RawTextHelpFormatter
import readline

descText = "Compile SVD per peripheral to one file describing entire MCU"
parser = argparse.ArgumentParser(description=descText, formatter_class=RawTextHelpFormatter)

svd_output_name = 'svd_me14.svd' 

doc = ET.parse('gpio_reva_me14.svd')

root = doc.getroot()


periph = root.find('peripherals')

block = ET.tostring(periph)

print(block)