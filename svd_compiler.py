import xml.etree.ElementTree as ET

svd_output_name = 'svd_me14.svd' 

doc = ET.parse('gpio_reva_me14.svd')

root = doc.getroot()


periph = root.find('peripherals')

block = ET.tostring(periph)

print(block)