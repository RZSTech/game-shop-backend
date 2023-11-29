import os
import re


def extract_endpoints(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    endpoints = []
    for i, line in enumerate(content):
        pattern = r"@(\w+)\.route\('(.*?)'[,\)]"
        match = re.search(pattern, line)
        method_pattern = r"methods=\['(GET|POST|PUT|DELETE)'\]"
        method_match = re.search(method_pattern, line)

        if i + 1 < len(content):
            function_pattern = r"def (\w+)"
            function_match = re.search(function_pattern, content[i + 1])

        if match and method_match and function_match:
            blueprint = match.group(1)
            endpoint = match.group(2)
            http_method = method_match.group(1)
            function_name = function_match.group(1)
            endpoints.append((blueprint, http_method, endpoint, function_name))

    return sorted(endpoints)


def format_endpoints(endpoints):
    formatted_endpoints = ""
    last_blueprint = None

    for blueprint, method, endpoint, function in endpoints:
        if blueprint != last_blueprint:
            if last_blueprint is not None:
                formatted_endpoints += "\n"
            formatted_endpoints += f"Blueprint: {blueprint}\n"
            last_blueprint = blueprint
        formatted_endpoints += f"  - Method: {method}, Endpoint: {endpoint}, Function: {function}\n"

    return formatted_endpoints


def main():
    directory = '.'
    endpoints = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                endpoints.extend(extract_endpoints(full_path))

    formatted_endpoints = format_endpoints(endpoints)

    output_file = 'endpoints_summary.txt'
    with open(output_file, 'w') as file:
        file.write(formatted_endpoints)

    print(f"Results saved in {output_file}")


if __name__ == "__main__":
    main()
