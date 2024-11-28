
import os

#FullPage Screenshot extension for Chrome - no need for now
extension_path = r"D:\Work 2024\NETPALM\MVP test\Main\Test\FDPOHAOCAECHIFIFMBBBBBKNOALCLACL_8_3_0_0.crx"

def install_extension(chrome_options, extension_path):
    try:
        if not os.path.exists(extension_path):
            raise FileNotFoundError(f"Extension file not found: {extension_path}")
        chrome_options.add_extension(extension_path)
        print(f"Extension added from: {extension_path}")
    except Exception as e:
        print(f"Error installing extension: {e}")