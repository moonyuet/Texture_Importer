# STYLE ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

# original: logging.init.py

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    curr_frame = currentframe()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if curr_frame is not None:
        curr_frame = curr_frame.f_back
    rv = "(unknown file)", 0, "(unknown function)"
    while hasattr(curr_frame, "f_code"):
        frame_code = curr_frame.f_code
        filename = os.path.normcase(frame_code.co_filename)
        if filename == _srcfile:
            curr_frame = curr_frame.f_back
            continue
        rv = (frame_code.co_filename, curr_frame.f_lineno, frame_code.co_name)
        break
    return rv

# How can we make this code better?
# Instead of using f as a varaible for function, dubbing the function with more concise variable such as current_frame, curr_frame
