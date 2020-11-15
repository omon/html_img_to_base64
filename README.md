# html_img_to_base64
This is convenient when converting the html image spit out from Markdown to html converted to base64 format and distributing it as one file.

## How to use
```shell
python image_converter_to_base64.py [html file path] [output html file path] [encoding option]
```
'utf-8' is specified if nothing is entered in encoding option.

Or please use
```python
convert_html_img_to_base64 (html_file_name, encoding = None)
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
'''
