import os

STATIC_FILES_DIR = 'static-files'


def handler(event, context):
    path = event["path"]
    method = event["httpMethod"]

    # https://stackoverflow.com/a/1945930/1459079
    # if path is absolute, make it relative
    if os.path.isabs(path):
        path = "".join(os.path.split(path)[1:])

    if method != 'GET':
        status_code = 400
        body = 'Invalid request'
        content_type = "text/plain;charset=UTF-8"

    else:
        file_path = os.path.join(STATIC_FILES_DIR, path)
        print(f"File path = {file_path}")
        try:
            with open(file_path, "r") as f:
                body = "".join(f.readlines())
            status_code = 200
            content_type = "text/plain;charset=UTF-8"
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            body = 'Invalid requeest'
            status_code = 400
            content_type = "text/plain;charset=UTF-8"

    return {
        "statusCode": status_code,
        "body": body,
        "headers": {"Content-Type": content_type},
    }
