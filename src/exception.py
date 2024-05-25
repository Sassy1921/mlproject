import sys 
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #exc_info() returns a tuple of three values: the exception type, the exception value, and the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error)) #format() method returns a formatted version of a string using values supplied in the positional argument list
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): #error_message is the error message and error_detail is the sys.exc_info()
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    
