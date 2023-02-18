from drf_yasg import openapi
from collections import OrderedDict

game_swagger_schema_properties =  {
    "id": openapi.Schema(type=openapi.TYPE_INTEGER, description='int'),
    "name": openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    "url": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI),
    "author": openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    "published_date": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='YYYY-MM-DD'),
    "created_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
    "modified_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
}


get_list_of_objs_swagger_response = {
    200: openapi.Schema(
                type = openapi.TYPE_OBJECT,
                properties=OrderedDict((
                    ('count', openapi.Schema(type=openapi.TYPE_INTEGER)),
                    ('next', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                    ('previous', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                    ('results', openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT, properties=game_swagger_schema_properties)),
                )))
                # {
                #         "count": openapi.Schema(type=openapi.TYPE_INTEGER),
                #         "results": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT, properties=game_swagger_schema_properties)),
                #     }
            )
    }


get_obj_swagger_responses = {
    200: openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties=game_swagger_schema_properties
                    )
            }
        ),
    404: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "message": openapi.Schema(type=openapi.TYPE_STRING),
                "data": openapi.Schema(type=openapi.TYPE_STRING, default=None)
            }
    )
}


post_obj_swagger_response = {
    201: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "message": openapi.Schema(type=openapi.TYPE_STRING),
            "data": openapi.Schema(type=openapi.TYPE_OBJECT, properties=game_swagger_schema_properties),
            # "data": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT, properties=game_swagger_schema_properties)),
            # "errors": ""
        }),
    422: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "message": openapi.Schema(type=openapi.TYPE_STRING),
            "errors": openapi.Schema(type=openapi.TYPE_OBJECT, properties= {
                "key": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
            })
        }
    )
}   

delete_obj_swagger_response = {
    202: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "message": openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    204: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "message": openapi.Schema(type=openapi.TYPE_STRING),
        }
    )
}