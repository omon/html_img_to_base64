#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup 
import base64
import re
import os.path

def decode_image(file):
    """
    read image file by binary and decode to base64
    
    Parameters
    ----------
    file : string
        input file path with directory path
    
    Returns
    -------
    string
        utf-8 string decoding binary.
    """
    with open(file, "rb") as img:
        data = base64.b64encode(img.read())
    return data.decode('utf-8')
    

def convert_html_img_to_base64(html_file_name, encoding=None):
    """
    get html that convert image to base64
    
    Parameters
    ----------
    html_file_name : string
        input file path
    encoding : string
        encoding option html file encoding.
    
    Returns
    -------
    string
        converted html string.
    """
    if encoding == None:
        encoding = 'utf-8'

    if filename.split('.')[-1] != 'html':
        print('input html file.(ext must be .html)')
        sys.exit(1)

    dir_path = os.path.dirname(filename)
    # print(dir_path)
    
    with open(filename, encoding=encoding) as f:
        html = f.read()
        pattern = r'<img(.+?)>'
        matchObj = re.finditer(pattern, html)

        if matchObj:
            for match in matchObj:
                soup = BeautifulSoup(match.group(), 'lxml')
                for img in soup.select('img'):
                    # print(img)                
                    # print('directory is = '.format(dir_path))
                    image_path = os.path.join(dir_path, str(img['src']))
                    # print(image_path)
                    b64 = decode_image(image_path)
                    # print(b64)
                    enc = "data:image/png;base64,{0}".format(b64)
                    img['src'] = enc
                    html = html.replace(match.group(), str(img))
                    # print('replace = {0} to {1}'.format(match.group(), str(img)))
    return html



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('input html file name like a => python image_converter_to_base64.py [html file path] [output html file path] [encoding option]')
        print('[encoding option] is html file encoding. default=\'utf-8\'')
        sys.exit(1)
    
    filename = sys.argv[1]
    output = sys.argv[2]
    
    if len(sys.argv) > 3:
        encoding = sys.argv[3]
    else:
        encoding = 'utf-8'

    with open(output, mode='w', encoding=encoding) as f:
        f.write(convert_html_img_to_base64(filename, encoding))
    
    