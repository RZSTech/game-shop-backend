import os
import re


def extract_endpoints(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    endpoints = []
    for i, line in enumerate(content):
        if '@products_crud.route' in line:
            pattern = r"@products_crud.route\('(.*?)'[,\)]"
            match = re.search(pattern, line)
            method_pattern = r"methods=\['(GET|POST|PUT|DELETE)'\]"
            method_match = re.search(method_pattern, line)

            if i + 1 < len(content):
                function_pattern = r"def (\w+)"
                function_match = re.search(function_pattern, content[i + 1])

            if match and method_match and function_match:
                endpoint = match.group(1)
                http_method = method_match.group(1)
                function_name = function_match.group(1)
                endpoints.append((endpoint, http_method, function_name))

    return endpoints


def main():
    directory = '.'
    endpoints = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                endpoints.extend(extract_endpoints(full_path))

    output_file = 'endpoints_summary.txt'
    with open(output_file, 'w') as file:
        for endpoint, method, function in set(endpoints):
            file.write(f"Endpoint: {endpoint}, Method: {method}, Function: {function}\n")

    print(f"Results saved in {output_file}")


if __name__ == "__main__":
    main()
