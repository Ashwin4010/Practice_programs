def http_response(status):
    match status:
        case 400 | 401 | 402 | 403:
            return "Client side error"
        case 500 | 501 | 503:
            return "Server Side error"
        case _:
            return f"exception {status}"


print(http_response(400))
