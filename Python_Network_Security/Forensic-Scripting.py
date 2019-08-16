import _winreg

try:
    keyname = 'myKey'
    key = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, 'Software\\' + keyname)
    _winreg.SetValueEx(key, 'myVal', 0, _winreg.REG_SZ, 'This is a value')
except Exception as e:
    print(e)