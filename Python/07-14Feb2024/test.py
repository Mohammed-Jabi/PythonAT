from typing import List


def getResponses(valid_auth_tokens, requests):
    """
  Parses and validates HTTP requests.

  Args:
    valid_auth_tokens: List of valid authentication tokens.
    requests: List of requests as [type, url] pairs.

  Returns:
    List of responses, one for each request.
  """
    responses: list[str] = []

    for req_type, url in requests:
        # Parse URL parameters
        params = {}
        try:
            url_parts = url.split("?")
            if len(url_parts) > 1:
                for param_pair in url_parts[1].split("&"):
                    key, value = param_pair.split("=")
                    params[key] = value
        except Exception as e:
            responses.append("INVALID")
            continue

        # Validate authentication token
        if params.get("token") not in valid_auth_tokens:
            responses.append("INVALID")
            continue

        # Validate CSRF token for POST requests
        if req_type == "POST":
            csrf_token = params.get("csrf")
            if not csrf_token or not csrf_token.isalnum() or len(csrf_token) < 8:
                responses.append("INVALID")
                continue

        # Build response string
        response_params = []
        for key, value in params.items():
            if key != "token" and key != "csrf":
                response_params.append(f"{key},{value}")
        response_str = "VALID,{}".join(response_params)

        responses.append(response_str)

    return responses


if __name__ == '__main__':
    arr_rows = int(input().strip())
    arr_columns = int(input().strip())
    arr = []
    for _ in range(arr_rows):  # Corrected indentation
        arr.append(list(map(int, input().rstrip().split())))

    # Call countNumbers function (assuming it's defined elsewhere)
    countNumbers(arr)
