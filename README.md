# CSRFPoC - CSRF PoC Generator

CSRFPoC is a simple Python script that generates a CSRF Proof of Concept (PoC) HTML file from a Burp request file. It's designed to help security researchers and developers quickly create CSRF PoC files for testing and demonstration purposes.

## Features

- Parses request (file) to extract URL and form data
- Generates an HTML PoC file with a form that automatically submits upon page load

## Requirements

- Python 3.x

## Usage

1. Clone this repository or download the script `csrf_poc_generator.py`.
2. Use the following command to run the script:


Replace `<path_to_request_file>` with the path to your request file, and `<path_to_output_file>` with the desired path for the generated HTML PoC file.

### Arguments

- `-r`, `--request`: Path to the request file (required)
- `-o`, `--output`: Path to the output HTML PoC file (default: `PoC.html`)

## Example


This command generates a CSRF PoC HTML file named `CSRF_PoC.html` using the request file `change_email.req`.

```bash
python csrf_poc_generator.py -r change_email.req -o CSRF_PoC.html
```

## Disclaimer

This script is intended for educational purposes only. The author is not responsible for any misuse or damage caused by using this tool.

## License

MIT License
