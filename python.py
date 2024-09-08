"""
This is a Python script that tests the Rust DLL.

Run this script with make test
"""

import ctypes
import os
import random


dll = ctypes.CDLL("./target/release/librust_dll.so")

if os.name == "nt":
    dll = ctypes.CDLL("./target/release/rust_dll.dll")
elif os.name == "darwin":
    dll = ctypes.CDLL("./target/release/librust_dll.dylib")

dll.hello.restype = ctypes.c_char_p

x = random.randint(0, 100)
y = random.randint(0, 100)
print(f"Calling Rust to add {x} and {y}: {x}+{y} = {dll.add(x, y)}")

print(f"Calling Rust to say hi: {dll.hello().decode('utf-8')}")
