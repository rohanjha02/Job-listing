def _json(status_code:int,message:string,data:[]):
    """
    Helper function to send clean similarly formattted data .
    """
    return '''{
    "status_code": {},
    "message": {},
    "data": {}
    }'''.format(status_code,message,data)