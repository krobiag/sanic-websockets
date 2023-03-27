from sanic.response import json

def api_response_serializer(retval, request, status):
    return json(
        {
            "success": status == 200,
            "request_id": str(request.id),
            "status": status,
            "data": retval,
        },
        status=status,
    )
    
# def responseSerializer(data): 
    