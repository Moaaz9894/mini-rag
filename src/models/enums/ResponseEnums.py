from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATED_SUCCESS = "File validated successfully_moaaz"
    FILE_TYPE_NOT_SUPPORTED = "Invalid file type"
    FILE_SIZE_EXCEEDED = "File size exceeds the limit"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    PROCESSING_SUCCESS = "File processed successfully"
    PROCESSING_FAILED = "File processing failed"
    NO_FILES_ERROR = "not_found_files"
    FILE_ID_ERROR = "no_file_found_eith_id"