from enum import Enum

# a set of error codes used by the backend code
class ErrorCodes(Enum):

    SUCCESS = "successful"
    UPLOAD_INVALID_CONTENTS_ERROR = "invalid risk factor contents for upload"
    DELETE_ERROR = "issue with deleting risk factors"
    INVALID_QUERY_ERROR = "invalid query"
    DATABASE_CONNECTION_ERROR = "issue with connecting to database"