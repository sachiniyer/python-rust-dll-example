# Python Rust DLL Example

I wanted to understand how easy it was to create interop between rust and python. It is actually super easy.

To run this example, just do the following:

``` sh
cargo build
python python.py
```

The only slightly complex part is how you deal with ctypes when bringing data into python, but even that is fairly easy.
