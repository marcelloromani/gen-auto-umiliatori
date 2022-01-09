import os

STATIC_FILES_DIR = 'static-files'


def read_static_file(url_path) -> str:
    # https://stackoverflow.com/a/1945930/1459079
    # if path is absolute, make it relative
    if os.path.isabs(url_path):
        url_path = "".join(os.path.split(url_path)[1:])

    file_path = os.path.join(os.getenv('LAMBDA_TASK_ROOT') or "", STATIC_FILES_DIR, url_path)
    with open(file_path, "r") as f:
        file_content = "".join(f.readlines())
    return file_content


def handler(event, context):
    url_path = event["path"]
    method = event["httpMethod"]

    if method != 'GET':
        status_code = 400
        body = 'Invalid request'
        content_type = "text/plain;charset=UTF-8"

    else:

        if url_path == '/favicon.ico':
            status_code = 404
            body = 'Not found'
            content_type = "text/plain;charset=UTF-8"
        else:
            try:
                body = read_static_file(url_path)
                status_code = 200
                content_type = "text/plain;charset=UTF-8"
            except Exception as e:
                print(f"Error reading {url_path}: {e}")
                body = 'Invalid requeest'
                status_code = 400
                content_type = "text/plain;charset=UTF-8"

    return {
        "statusCode": status_code,
        "body": body,
        "headers": {"Content-Type": content_type},
    }


if __name__ == "__main__":
    res = handler({
        "path": "/robots.txt",
        "httpMethod": "GET",
    }, {})
    print(res)
