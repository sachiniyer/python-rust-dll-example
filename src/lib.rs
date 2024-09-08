use std::ffi::CString;
use std::os::raw::c_char;

#[no_mangle]
pub extern "C" fn add(left: u64, right: u64) -> u64 {
    left + right
}

#[no_mangle]
pub extern "C" fn hello() -> *const c_char {
    let c_string = CString::new("Hello World!").unwrap();
    c_string.into_raw()
}
