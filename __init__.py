import ctypes
import os

def crc32(buffer, init):
    dll = ctypes.WinDLL(os.path.join(os.path.dirname(__file__), "crc32.dll"))
    
    return dll.crc32(ctypes.c_char_p(buffer), 
                          ctypes.c_size_t(len(buffer)), 
                          ctypes.c_uint32(init))
    
    
