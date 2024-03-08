# <span style="font-family: Trebuchet MS;">tooltils – api | v1.7.1</span>

*<b>NOTE:</b> If a variable has a star sign in front of it, it can have a value of none*

## <span style="font-family: Trebuchet MS;">Tooltils</span>

*General utility methods* <br><br>

**Properties:**

**`ANSI_colours`** dict[str, int] – List of major colours as ANSI integer codes

<br>

**Methods:**

**`length(file)`** <br>
Get the length of a wave file in seconds

Parameters:
- **`file`** str - Path to WAVE file

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect
- **`ValueError`** – Input parameter is invalid
- **`FileNotFoundError`** – Unable to locate input file

Example:
```py
>>> length = tooltils.length('song.wav') # song.wav is 5.15 seconds long
>>> length
5.15
```

Return type: **float** <br>
Returns: **Length of file in seconds** <br><br>

**`style(text)`** <br>
Create text in the specified colour and or style

Parameters:
- **`text`** str – Text to style
- **`colour`** str = ‘’ – Colour to use (uses list from ANSI_colours)
- **`bold`** bool = False – Whether to make the text bold
- **`italic`** bool = False – Whether to italicise the text
- **`fill`** bool = False – Whether to fill the text background with the specified colour
- **`crossed`** bool = False – Whether to cross the text
- **`underline`** bool = False – Whether to underline the text
- **`double_underline`** bool = False – Whether to double underline the text
- **`flush`** bool = True – Whether to apply a fix to the terminal because of a display bug

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect

Example:
```py
>>> text = tooltils.style('Hello World!', 'red', True, True, True)
>>> text # text value can be stored and doesn't have to be printed right away
'\u001b[41;1;3mHello World!\u001b[0m' # raw ANSI style text
```

Return type: **str** <br>
Returns: **Styled text** <br><br>

**`halve(array)`** <br>
Return the halves of a string or array

Parameters:
- **`array`** str | list | tuple | set | dict – Iterable to halve

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect

Example:
```py
>>> texts = tooltils.halve('Hello World!')
>>> texts
['Hello ', 'World!']
```

Return type: **list** <br>
Returns: **Either half of iterable** <br><br>

**`cipher(text, shift)`** <br>
A simple caeser cipher

Parameters:
- **`text`** str – Text to cipher
- **`shift`** int – Amount of letters to shift in the alphabet

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid

Example:
```py
>>> text = tooltils.cipher('Hello World!', 8)
>>> text
'PmttwvEwztlw'
```

Return type: **str** <br>
Returns: **Ciphered text** <br><br>

**`mstrip(text, values)`** <br>
Change some text from a dictionary pair of values

Parameters:
- **`text`** str – Text to be changed
- **`values`** dict – List of characters to change

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect

Example:
```py
>>> text = tooltils.mstrip('Hello World!', {'Hell': 'Heaven', 'World': 'Earth'})
>>> text
'Heaveno Earth!'
```

Return type: **str** <br>
Returns: **Changed text** <br><br>

**`date()`** <br>
Convert epoch to human formatted date

Parameters:
- **`epoch`** float = time.time() – Epoch in seconds to use
- **`timezone`** str = ‘local’ – Timezone offset to use (e.g. ‘+11:00’, ‘local’ means your current timezone, ‘gm’ means no offset time)
- **`format`** str = ‘standard’ – How to format the output date (‘standard’, ‘fancy’)

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid
- **`OverflowError`** – Epoch parameter value is too large to be used

Example:
```py
>>> date = tooltils.date(format='fancy')
>>> date
'11:52 AM on the 3rd of January, 2024'
```

Return type: **str** <br>
Returns: **Formatted date** <br><br>

**`epoch(date)`** <br>
Get epoch from a formatted string date

Parameters:
- **`date`** str – The formatted date to convert

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect
- **`ValueError`** – Input parameter type is invalid

Example:
```py
>>> epoch = tooltils.epoch('11:52 AM on the 3rd of January, 2024')
>>> epoch
1704243120
```

Return type: **int** <br>
Returns: **Epoch in seconds of the input date** <br><br>

**`squeeze(array)`** <br>
Remove empty or the specified item(s) from an array

Parameters:
- **`array`** list | tuple | set | dict – The array to change
- **`item`** Any = None – The item to remove

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect

Example:
```py
>>> array = tooltils.squeeze(['', 'Hello World!', 'a bug', '', 'test'])
>>> array
['Hello World!', 'a bug', 'test']
```

Return type: **list | tuple | set | dict** <br>
Returns: **Edited array of the same time as the input** <br><br>

**`reverseDictSearch(array, value)`** <br>
Find the unknown key(s) of a value in a dictionary

Parameters:
- **`array`** dict – The dictionary to search
- **`value`** Any – The value to find the key(s) for

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect

Example:
```py
>>> key = tooltils.reverseDictSearch({'hello': True, 'world': True, '!': False}, True)
>>> key
('hello', 'world')
```

Return type: **tuple** <br>
Returns: **Key(s) found** <br><br>

**`getArrayValues(array)`** <br>
Recursively obtain all of the values of any keys or items within an array

Parameters:
- **`array`** list | tuple | dict – The array to search

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect

Example:
```py
>>> values = tooltils.getArrayValues(['hello', ['world', {'hello world': ['hello']}, ['world']]])
>>> values
('hello', 'world', 'hello', 'world')
```

Return type: **tuple** <br>
Returns: **All base-level values in the array** <br><br>

**`timeTest(method)`** <br>
Run a method with optional kwargs {accuracy} amount of times, sum then divide by {accuracy} for precise run time

Parameters:
- **`method`** function – The method to test
- **`params`** dict = {} – Kwargs for the method
- **`accuracy`** int = 10 – The amount of times to test the method

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid

Example:
```py
>>> time = tooltils.timeTest(tooltils.requests.get, {'url': 'httpbin.org/get'}, 20)
>>> time
0.9137420050014043 # legitimate requests time test from feetbots' pc
```

Return type: **float** <br>
Returns: **Average run-time the input method based on the accuracy** <br><br>

**`varName(**vars)`** <br>
Get the namespace name of one or more variables

Parameters:
- **`**vars`** dict – The variables to get the name for

Example:
```py
>>> data = 'Hello World!'
>>> name = tooltils.varName(data=data)
>>> name
'data'
```

Raisable exceptions:
- None

Return type: **str | list[str]** <br>
Returns: **Names of variables input** <br><br>

**`tgzOpen(file)`** <br>
Open a gzipped tar file

Parameters:
- **`file`** str – The location of the .tar.gz or .tgz file
- **`output`** str = None – The file path and name of the output uncompressed file

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid
- **`FileExistsError`** – Output file exists already
- **`FileNotFoundError`** – Problem locating output file
- **`BadGzipFile`** (Python 3.8+) | **`OSError`** (Python 3.7) – The file was not a gzipped file

Example:
```py
>>> path = tgzOpen('tooltils-v1.7.0.tar.gz')
>>> path
'/Users/feetbots/Documents/projects/tooltils/tests/tooltils-v1.7.0'
```

Return type: **str** <br>
Returns: **File path of output folder/file** <br><br>

**`lengthSort(array)`** <br>
Sort an array by it's length

Parameters:
- **`array`** list | tuple | set | dict – The array object to sort
- **`fromLowest`** = True – Whether to return the sorted object starting from the shortest item
- **`sortByKey`** = False – Whether to sort by the keys of the array if it is a dictionary

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid

Example:
```py
>>> array = lengthSort(['11111', '5', '44', '333', '2222'])
>>> array
['5', '44', '333', '2222', '11111']
```

Return type: **list | tuple | set | dict** <br>
Returns: **Sorted input array** <br><br>

**`interpreter(file)`** <br>
Custom top-level Python interpreter to add useful typing features

Parameters:
- **`file`** str – The Python file to convert
- **`output`** str = ‘%(name)s.interpreted.py’ – The name of the converted Python file
- **`override`** bool = False – Whether to override the content of an existing output file with the same name
- **`ternary`** bool = True – Whether the ternary operater feature is enabled
- **`comments`** bool = True – Whether the Javscript comments feature is enabled

Return properties:
- **`file`** str – The full path of Python file that was converted
- **`output`** str – The full path of the converted Python file
- **`override`** bool – Whether an existing file was overrid

Return methods:
- **`.read()`** str – Read the output file and return the content as a string
- **`.readlines()`** list[str] – Read the output file and return the content as a list containing strings split at every newline

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid | function already called
- **`FileExistsError`** – Output file exists already
- **`FileNotFoundError`** – Problem locating output file

Current features:
- **Ternary Operations** – Javascript like ternary operators
- **JS Comments** – Javascript like comments using `//` as a prefix

Example:
- `test.py`
```py
def hello(windows: bool=False):
    // JS ternary operator
    name = windows ? 'Windows' : 'Anything'

    return name
```
- Python Interactive Shell
```py
>>> interpreter = tooltils.interpreter('test.py')
>>> interpreter
<Interpreter instance [test.py]>
>>> interpreter.file
'/Users/feetbots/Documents/projects/tooltils/tests/test.py'
>>> interpreter.output
'/Users/feetbots/Documents/projects/tooltils/tests/test.interpreted.py'
>>> interpreter.readlines()
['def hello(windows: bool=False):\n', '    # JS ternary operator\n', "    name = 'Windows' if windows else 'Anything'\n", '\n', '    return name\n']
```

Return type: **tooltils.interpreter** <br>
Returns: **Interpreter instance** <br><br>

## <span style="font-family: Trebuchet MS;">info</span>

*General installation information*

Properties:
- **`author`** str – The current owner of tooltils
- **`author_email`** str – The email of the current owner of tooltils
- **`maintainer`** str – The current sustainer of tooltils
- **`maintainer_email`** str – The email of the current sustainer of tooltils
- **`version`** str – The current installation version
- **`released`** str – The release date of the current installation
- **`release_description`** str – The description of the current release version
- **`*license`** str – The content of the currently used license
- **`description`** str – The short description of tooltils
- **`*long_description`** str – The long description of tooltils
- **`location`** str – The path of the current installation of tooltils
- **`lines`** int – The amount of lines of code in this tooltils installation
- **`homepage`** str – The current home website of tooltils
- **`homepage_issues`** str – The current issues directory of the home website of tooltils
- **`releases`** list[str] – All current versions of tooltils

Methods:

**`clearCache()`** <br>
Clear the file cache of tooltils or a specific module within

Parameters:
- **`module`** str = None – The name of module to clear the cache for

Raisable exceptions:
- **`ValueError`** – Input parameter is invalid

Example:
```py
>>> tooltils.info.clearCache()
None # cache json file in storage has been reset to default
```

Return type: **None** <br>
Returns: **Nothing** <br><br>

**`clearConfig()`** <br>
Revert the config of tooltils or a specific module within

Parameters:
- **`module`** str = None – The name of module to revert the settings for

Raisable exceptions:
- **`ValueError`** – Input parameter is invalid

Example:
```py
>>> tooltils.info.clearConfig()
None # config json file in storage has been reset to default
```

Return type: **None** <br>
Returns: **Nothing** <br><br>

**`clearData()`** <br>
Clear the cache and config of tooltils

Parameters:
- None

Raisable exceptions:
- None

Example:
```py
>>> tooltils.info.clearData()
None # the cache and config json files have been reset to the default
```

Return type: **None** <br>
Returns: **Nothing** <br><br>

**`deleteData()`** <br>
Delete the stored data for a specific python version of tooltils, a specific tooltils version, a combination of these or the entire tooltils storage directory

Parameters:
- **`pyv`** str = None – The Python version to be deleted
- **`tsv`** str = None – The Tooltils version to be deleted

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect
- **`ValueError`** – Input parameter is invalid
- **`FileNotFoundError`** – Unable to locate tootlils data files

Example:
```py
>>> tooltils.info.deleteData()
None # the .tooltils folder has been deleted
```

Return type: **None** <br>
Returns: **Nothing** <br><br>

**`logger()`** <br>
Create a logging instance for tooltils modules only

Parameters:
- **`module`** str = ‘ALL’ – The name of module to initiliase logging for
- **`level`** str | int | LoggingLevel = ‘ALL’ – The starting level of the logging range
- **`level2`** str | int | LoggingLevel = ‘ALL’ – The ending level of the logging range

Return properties:
- **`module`** str – The name of module logging is initiliased for
- **`level`** str | int | LoggingLevel – The starting level of the logging range
- **`level2`** str | int | LoggingLevel – The ending level of the logging range
- **`enabled`** bool – Whether the logging instance is enabled
- **`closed`** bool – Whether the logging instance has been closed

Return methods:
- **`enable()`** – Enable the logger instance
- **`disable()`** – Disable the logger instance
- **`close()`** – Close the logger instance

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter is invalid

Example:
```py
>>> logger = tooltils.info.logger()
[01:11:56] [tooltils.info/DEBUG]: Initiated logger for <tooltils> with range DEBUG -> CRITICAL
>>> logger
<Logger instance: [on] -> [TOOLTILS]>
>>> req = tooltils.requests.get('httpbin.org/get')
[01:14:01] [tooltils.requests/DEBUG]: Setting up https/1.1 GET request to <httpbin.org:443>
[01:14:01] [tooltils.requests/DEBUG]: Sending headers: {'Connection': 'close', 'User-Agent': 'Python-tooltils/1.7.0', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate'}
[01:14:02] [tooltils.requests/DEBUG]: Request response body was not gzipped
[01:14:02] [tooltils.requests/DEBUG]: Server replied with [200 OK]
[01:14:02] [tooltils.requests/DEBUG]: Connection to server has been discarded
>>> req
<GET httpbin.org [200]>
```

Return type: **tooltils.info.logger** <br>
Returns: **Logger instance** <br><br>

## <span style="font-family: Trebuchet MS;">os</span>

*Operating system specific methods, information and interaction*

Properties:
- **`info`** – Operating system information – *Details*:
  - **Properties**:
    - **`macOS_releases`** dict[str, str] – List of all current MacOS versions
    - **`python_version`** str – Current Python interpreter version
    - **`name`** str – The network and user name of the current operating system/computer
    - **`bitsize`** int – The bit limit of the current Python interpreter
    - **`interpreter`** str – Location of current Python interpreter
    - **`platform`** str – Name of current operating system
    - **`detailed_platform`** str – Version number and or name of your computer's current OS
    - **`cpu`** str – Name of the currently in use cpu of your computer
    - **`arch`** str – Computer architecture
    - **`platform_version`** tuple[str] – Version number and or name of current OS
    - **`model`** str – The model or manufacturer of your computer
    - **`cores`** int – The amount of cores in your computer's cpu
    - **`ram`** int – The amount of ram in megabytes in your computer
    - **`manufacturer`** str – The creator of your computer
    - **`*serial_number`** str – The identifiable code or tag string of your computer (This is unobtainable on Linux)
    - **`boot_drive`** str – The location of the disk currently being used on your computer
  - **Supported**:
    - **`MacOS`**
    - **`Windows`**
    - **`Linux`** – Some distributions may not work

Methods:

**`exit(details)`** <br>
Print some text and exit the current thread

Parameters:
- **`details`** str = ‘’ – Text to print before exiting
- **`code`** int = 0 – Exit code to use

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect

Example:
```py
>>> tooltils.os.exit('Goodbye!')
Goodbye! # current thread code execution stops
```

Return type: **NoReturn** <br>
Returns: **Nothing** <br><br>

**`clear()`** <br>
Clear the terminal history

Parameters:
- None

Raisable exceptions:
- None

Example:
```py
>>> tooltils.os.clear() # terminal history cleared
```

Return type: **None** <br>
Returns: **None** <br><br>

**`system(cmds)`** <br>
Call a system program and return some information

Parameters:
- **`cmds`** str | list | tuple – Commands/program to call
- **`shell`** bool = False – Whether to use the shell
- **`timeout`** int | float = 10 – How long the command/program should last before cancelling
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`capture`** bool = True – Whether to capture the output of the command/program
- **`print`** bool = True – Whether command/program can print to stdout

Return properties:
- **`cmds`** str | list | tuple – Command/programs that were called
- **`shell`** bool – Whether shell was used to call the command/program
- **`timeout`** int | float – How long the command/program should last before cancelling
- **`check`** bool – Whether to raise an error if the returncode is not 0
- **`capture`** bool – Whether to capture the the output of the command/program
- **`print`** bool – Whether command/program can print to stdout
- **`code`** int – Exit code of command/program
- **`raw`** bytes – Raw bytes text of stdout output
- **`text`** str – String containing text of stdout output
- **`list_text`** list[str] – List containing text of stdout output split at every newline
- **`clean_list_text`** list[str] – List containing text of stdout output split at every newline but with the empty items removed

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid
- **`tooltils.errors.SubprocessExecutionError`** – Child process execution failed
- **`tooltils.errors.SubprocessCodeError`** – Child process execution returned non-zero exit code
- **`tooltils.errors.SubprocessTimeoutExpired`** – Child process execution timed out
- **`tooltils.errors.SubprocessLookupNotFound`** – Unable to locate program or shell command
- **`tooltils.errors.SubprocessPermissionError`** — Denied access to program or shell command

Example:
```py
>>> shell_info = tooltils.os.system('echo Hello World!', shell=True)
>>> shell_info
<System instance [0x1794e5378f0]>
>>> shell_info.raw
b'Hello World!\r\n'
>>> shell_info.text
Hello World!

>>> shell_info.list_text
['Hello World!']
```

Return type: **tooltils.os.system** <br>
Returns: **A system class** <br><br>

**`check(cmds)`** <br>
Call a system program and return the output

Parameters:
- **`cmds`** str | list | tuple – Commands/program to call
- **`shell`** bool = False – Whether to use the shell (sh)
- **`timeout`** int | float = 10 – How long the process should last
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`clean`** bool = False – Whether to remove empty values from the output as a list
- **`listify`** bool = True – Whether to convert the stdout output to a list (.list_text)
- **`raw`** bool = False – Whether to return raw bytes output

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid
- **`tooltils.errors.SubprocessExecutionError`** – Child process execution failed
- **`tooltils.errors.SubprocessCodeError`** – Child process execution returned non-zero exit code
- **`tooltils.errors.SubprocessTimeoutExpired`** – Child process execution timed out
- **`tooltils.errors.SubprocessLookupNotFound`** – Unable to locate program or shell command
- **`tooltils.errors.SubprocessPermissionError`** — Denied access to program or shell command

Example:
```py
>>> tooltils.os.check('echo Hello World!', shell=True, raw=True)
b'Hello World!\r\n'
>>> tooltils.os.check('echo"Hello World!', shell=True, listify=False)
Hello World!

>>> tooltils.os.check('echo Hello World!', shell=True)
['Hello World"']
```

Return type: **str | bytes | list[str]** <br>
Returns: **List of lines or bytes containing stdout output** <br><br>

**`call(cmds)`** <br>
Call a system program and return the exit code

Parameters:
- **`cmds`** str | list | tuple – Commands to call
- **`shell`** bool = False – Whether to use the shell (sh)
- **`timeout`** int | float = 10 – How long the process should last
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`print`** bool = True – Whether command/program can print to stdout

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid
- **`tooltils.errors.SubprocessExecutionError`** – Child process execution failed
- **`tooltils.errors.SubprocessCodeError`** – Child process execution returned non-zero exit code
- **`tooltils.errors.SubprocessTimeoutExpired`** – Child process execution timed out
- **`tooltils.errors.SubprocessLookupNotFound`** – Unable to locate program or shell command
- **`tooltils.errors.SubprocessPermissionError`** — Denied access to program or shell command

Example:
```py
>>> tooltils.os.call('echo Hello World!', shell=True)
0
```

Return type: **int** <br>
Returns: **Exit code of program call** <br><br>

**`pID(name)`** <br>
Get the process ID of an app or binary by name

Parameters:
- **`name`** str – Name of app or binary
- **`strict`** bool = False – Whether the input name has to be an exact match to the process found

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid

Supported:
- **`MacOS`**
- **`Linux`** – Some distributions don't have the -i or -x arguments required for the `pgrep` command
- **`Windows`**

Example:
```py
>>> ids = tooltils.os.pID('chrome')
>>> ids
(30716, 22172, 4884, 3696, 26024, 29140)
>>> ids = tooltils.os.pID('chrome', strict=True)
>>> ids
()
```

Return type: **tuple[int] | None** <br>
Returns: **List of found process IDs** <br><br>

**`getCurrentWifiName()`** <br>
Get the currently connected wifi name

*Will return None if not connected or nothing was found*

Parameters:
- None

Raisable exceptions:
- None

Supported:
- **`MacOS`**
- **`Linux`**
- **`Windows`**

Example:
```py
>>> name = tooltils.os.getCurrentWifiName()
>>> name
'NetComm 9055'
```

Return type: **str | None** <br>
Returns: **Wifi Name** <br><br>

## <span style="font-family: Trebuchet MS;">requests</span>

*HTTP/1.1 simple interface*

Properties:
- **`status_codes`** dict – List of official HTTP response status codes
- **`defaultVerificationMethod`** bool – The config value for the verify parameter in request methods
- **`redirectLimit`** – The config value for the redirectLimit parameter in request methods

Methods:

**`ctx()`** <br>
Create a custom SSLContext instance

Parameters:
- **`verify`** bool = True – Whether to check hostname and verify SSL request
- **`cert`** str = None – Location of certificate.pem file

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`FileNotFoundError`** – Cannot find input parameter file

Example:
```py
>>> ctx = tooltils.requests.ctx()
>>> ctx
<ssl.SSLContext object at 0x00000206D4E30FD0>
```

Return type: **ssl.SSLContext** <br>
Returns: **An SSLContext instance** <br><br>

**`connected()`** <br>
Get the connectivity status of the currently connected wifi network

*When caching is enabled, it will used the cached value 20 times by default and then create a new one and cache that instead.*

Parameters:
- None

Raisable exceptions:
- None

Example:
```py
>>> status = tooltils.requests.connected()
>>> status
True
```

Return type: **bool** <br>
Returns: **The result of the internet test** <br><br>

**`prep_url(url)`** <br>
Configure a URL making it viable for requests

Parameters:
- **`url`** str | bytes – URL to configure
- **`data`** dict = {} – Data to include in the URL
- **`https`** bool = True – Whether to guess https as the protocol if not specified
- **`order`** bool = False – Whether to alphabetically order the url items

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid

Example:
```py
>>> url = tooltils.requests.prep_url('httpbin.org/get/')
>>> url
'https://httpbin.org/get'
```

Return type: **str** <br>
Returns: **Corrected URL** <br><br>

**`where()`** <br>
Return default certificate file and path locations used by Python

*This function will use the openssl cert locations if the normal ones are None*

Parameters:
- None

Raisable exceptions:
- None

Example:
```py
>>> certs = tooltils.requests.where()
>>> certs
('C:\\Program Files\\Common Files\\SSL\\certs', 'C:\\Program Files\\Common Files\\SSL\\cert.pem')
```

Return type: **tuple** <br>
Returns: **Python used certificates in the format (path, file)** <br><br>

**`verifiable()`** <br>
Determine whether requests can be verified with a valid ssl certificate on the current connection

*This function will use the cached value 20 times by default and then create a new one and cache that instead.*

Parameters:
- None

Raisable exceptions:
- None

Example:
```py
>>> status = tooltils.requests.verifiable()
>>> status
True # connected to a normal private home wifi
```

Return type: **bool** <br>
Returns: **Whether requests can use a valid ssl certificate** <br><br>

**`advancedContext()`** <br>
Create an advanced context instance intended to be used for extended functionality with requesting

Parameters:
- **`redirectLimit`** int = `config.requests.redirectLimit` – How many times the url can redirect the request before an exception is raised
- **`extraLogs`** bool = False – Whether extra more detailed logs should be output
- **`SSLContext`** SSLContext = `tooltils.requests.ctx()` – A custom SSLContext instance to override the one created by the request

Return properties:
- **`redirectLimit`** int – How many times the url can redirect the request before an exception is raised
- **`extraLogs`** bool – Whether extra more detailed logs should be output
- **`SSLContext`** SSLContext – A custom SSLContext instance to override the one created by the request class

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid

Example:
```py
>>> advancedContext = tooltils.requests.advancedContext()
>>> advancedContext
<tooltils.requests.advancedContext object at 0x00000249B35617F0>
```

Return type: **tooltils.requests.advancedContext** <br>
Returns: **Advanced requesting context class** <br><br>

**`tooltilsResponse()`** <br>
Create a tooltils style http response class using the HTTPResponse return class

Parameters:
- **`data`** http.client.HTTPResponse – A http.client response class to extract the data from
- **`url`** str – The URL of the request
- **`method`** str – The http method to use for request data determination (GET, POST, DOWNLOAD, HEAD, PUT, PATCH, OPTIONS, TRACE, DELETE)
- **`encoding`** str | tuple = (‘utf-8’, ‘ISO-8859-1’) – Codec(s) to use to decode the response text
- **`_agent`** = None – The user agent for the request, passed from requesting methods
- **`_headers`** = None – The headers that were sent in the request, passed from requesting methods
- **`_clog`** = None – Whether `openConnection()` or `request()` is calling the class constructor, passed from requesting methods
- **`_rID`** = None – The request ID, passed from requesting methods

Return properties:
- **`data`** http.client.HTTPResponse – The http.client response class the data was extracted from
- **`code`** int – The http status code that the request returned
- **`reason`** str – The reason of the http status code that the request returned
- **`status_code`** str – The http status code and reason combined
- **`headers`** dict[str, str] – The headers that the request returned
- **`end_url`** str – The final url that was requested, can be used to find out where a request was redirected
- **`*end_agent`** str – The final User-Agent header that was sent in the request
- **`*raw`** bytes – The raw byte content of the request response body
- **`*text`** str – The decoded content of the request response body
- **`*json`** dict – The converted Python JSON of the request response body (if applicable)
- **`end_data**`** class – Information that was sent in the request but not returned – *Properties*:
  - **`url`** str – The url that was requested
  - **`*sent_headers`** dict[str, str] – The headers that were sent in the request
  - **`*agent`** str – The User-Agent of the request headers that were sent

Return methods:
- **`.read(amt: int=None)`** bytes – Read the request response body or up to amt bytes – *Raisable Exceptions*:
  - **`TypeError`** – Input parameter type is incorrect
  - **`ValueError`** – The input amt was bigger than the length of the request response body
- **`.readlines(amt: int=None)`** list[str] - Read the request response body or up to amt bytes and return as a list split at every newline – *Raisable Exceptions*:
  - **`TypeError`** – Input parameter type is incorrect
  - **`ValueError`** – The input amt was bigger than the length of the request response body

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid
- **`tooltils.errors.RequestCodecError`** – None of the specified codecs were able to decode the response received from the server

Example:
```py
>>> import http
>>> conn = http.client.HTTPSConnection('httpbin.org')
>>> conn.send('GET', '')
>>> data = conn.getresponse()
>>> resp = tooltils.requests.tooltilsResponse(data, 'httpbin.org', 'GET')
>>> resp.status_code
'200 OK'
```

Return type: **tooltils.requests.tooltilsResponse** <br>
Returns: **A tooltils requests style http response class** <br><br>

**`openConnection(host)`** <br>
Open a re-usable connection to a URL

Parameters:
- **`host`** str – The host to connect to
- **`port`** int = (443 if https else 80) – The port to send the request on
- **`https`** bool = True – Whether https should be used in the request
- **`verify`** bool = `config.requests.defaultVerificationMethod` – Whether to verify the request using a certificate
- **`redirects`** bool = True – Whether to allow redirects
- **`redirect_loops`** bool = False – Whether to allow redirect looping
- **`auth`** tuple = None – Authentication in a username password tuple format
- **`data`** dict = None – JSON data to send with the request
- **`headers`** dict = None – Headers to add to the request (Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file (Will use default if None)
- **`file_name`** str = None – Path to download the file (Will use URL file name if None)
- **`write_binary`** bool = False – Whether to write the downloaded file as binary
- **`override`** bool = False – Whether the output file should be overrid
- **`timeout`** int | float = 15 – How long the request should last in seconds before it should be terminated
- **`encoding`** str | tuple = (‘utf-8’, ‘ISO-8859-1’) – Codec(s) to use to decode the response text
- **`mask`** bool = False – Whether to use an anonymous user agent header (firefox's user agent)
- **`agent`** str = None – Overwrite for the agent header
- **`proxy`** str = None – The proxy to send the request on
- **`advContext`** tooltils.requests.advancedContext = None – A tooltils advanced context class

Return properties:
- **`host`** str – The host that was connected to
- **`port`** int – The port the request was sent on
- **`https`** bool – Whether https was used with the request
- **`verify`** bool – Whether the request was verified with a certificate
- **`redirects`** bool – Whether the requested URL was allowed to redirect the request
- **`redirect_loops`** bool = False – Whether the requested URL was allowed to loop redirects recursively
- **`*auth`** tuple – Authentication used in the request
- **`*data`** dict – JSON data that was sent with the request
- **`headers`** dict – The headers sent as the configuration of the request
- **`cookies`** dict – Cookies that were sent with the request
- **`cert`** str – Path to certificate.pem file (Will use default if None)
- **`*file_name`** str – Path to download the file (Will use URL file name if None)
- **`write_binary`** bool – Whether to write the downloaded file as binary
- **`override`** bool – Whether the output file should be overrid
- **`timeout`** int | float – How long the request lasts in seconds before it should be terminated
- **`encoding`** str | tuple – Codec(s) used to decode the response text
- **`mask`** bool – Whether the user agent header was anonymised
- **`*agent`** str – The overwritten agent header for the request
- **`*proxy`** str – The proxy that was used to send the request on
- **`*advContext`** tooltils.requests.advancedContext – A tooltils advanced context class
- **`state`** str – The current state of the connection
- **`rID`** int – The ID for the current connection
- **`redirectLimit`** int – The amount of redirects the url can make before an exception is raised
- **`extraLogs`** bool – If extra detailed logs should be output
- **`*SSLContext`** ssl.SSLContext – A custom SSLContext instance

Return methods:
- **`.open()`** – Open the connection – *Raisable Exceptions*:
  - **`tooltils.errors.InvalidRequestURL`** – The specificed URL could not be used to make a valid request
  - **`tooltils.errors.ConnectionError`** – General connection failed error or connection is not in the right state to open
  - **`tooltils.errors.ActiveRequestError`** – The request returned malformed data
  - **`tooltils.errors.SSLCertificateFailed`** – Unable to verify SSL certificate
  - **`tooltils.errors.StatusCodeError`** – HTTP error status code response
  - **`tooltils.errors.InvalidWifiConnection`** – No valid internet connection present
  - **`tooltils.errors.ConnectionTimeoutExpired`** – Connection timed out
- **`.close()`** – Close the connection – *Raisable Exceptions*:
  - **`tooltils.errors.ConnectionError`** – Connection is not in the right state to close
- **`.change()`** – Change the data being sent for requests succeeding this call – *Details*:
  - **Parameters** (Must be passed as kwargs):
    - **`redirects`** bool – Whether to allow redirects
    - **`redirect_loops`** bool – Whether to allow redirect looping
    - **`auth`** tuple – Authentication in a username password tuple format
    - **`data`** dict – JSON data to send with the request
    - **`headers`** dict – Headers to add to the request (Overwrites defaults if the same are present)
    - **`cookies`** dict– Cookies to include in the headers
    - **`file_name`** str – Path to download the file (Will use URL file name if None)
    - **`write_binary`** bool – Whether to write the downloaded file as binary
    - **`override`** bool – Whether the output file should be overrid
    - **`encoding`** str | tuple – Codec(s) to use to decode the response text
    - **`mask`** bool – Whether to use an anonymous user agent header (firefox's user agent)
    - **`agent`** str – Overwrite for the user agent header
  - **Raisable Exceptions**:
    - **`TypeError`** – Input parameter types are incorrect
    - **`ValueError`** – Input parameter types are invalid
    - **`FileNotFoundError`** – Unable to locate input parameter file argument
    - **`FileExistsError`** – Output file already exists
- **`.send()`** – Send the request to the specified page – *Details*:
  - **Parameters**:
    - **`method`** str = ‘GET’ – The http method to use in the request (GET, POST, DOWNLOAD, HEAD, PUT, PATCH, OPTIONS, TRACE, DELETE)
    - **`page`** str = ‘’ – The subpage of the host to send the request to
    - **`close`** bool = False – Whether to close the connection after the request
    - **`**params`** dict – Any kwargs that the `.change()` method accepts to pass single use values for a specific request
  - **Return Properties**:
    - **`data`** http.client.HTTPResponse – The http.client response class the data was extracted from
    - **`code`** int – The http status code that the request returned
    - **`reason`** str – The reason of the http status code that the request returned
    - **`status_code`** str – The http status code and reason combined
    - **`headers`** dict[str, str] – The headers that the request returned
    - **`*raw`** bytes – The raw byte content of the request response body
    - **`*text`** str – The decoded content of the request response body
    - **`*json`** dict – The converted Python JSON of the request response body (if applicable)
    - **`*path`** str – The path of the downloaded file (if the method was DOWNLOAD)
    - **`redirected`** bool – Whether the request was redirected
    - **`rdata`** http.client.HTTPResponse – The http base response class containing all the data read
    - **`end_data**`** class – Information that was sent in the request but not returned – *Properties*:
      - **`url`** str – The url that was requested
      - **`*sent_headers`** dict[str, str] – The headers that were sent in the request
      - **`*agent`** str – The User-Agent of the request headers that were sent
  - **Return Methods**:
    - **`.read()`** bytes – Read the request response body or up to amt bytes – *Details*:
      - **Parameters**:
        - **`amt`** int = None – The length of data to read (will read whole body if None)
      - **Raisable Exceptions**:
        - **`TypeError`** – Input parameter type is incorrect
        - **`ValueError`** – The input amt was bigger than the length of the request response body
    - **`.readlines()`** list[str] - Read the request response body or up to amt bytes and return as a list split at every newline – *Details*:
      - **Parameters**:
        - **`amt`** int = None – The length of data to read (will read whole body if None)
      - **Raisable Exceptions**:
        - **`TypeError`** – Input parameter type is incorrect
        - **`ValueError`** – The input amt was bigger than the length of the request response body
    - **`.seek(pos)`** None - Read the request response body or up to amt bytes and return as a list split at every newline – *Details*:
      - **Parameters**:
        - **`pos`** int = None – The position of the request response body to go to
      - **Raisable Exceptions**:
        - **`TypeError`** – Input parameter type is incorrect
        - **`ValueError`** – The input pos was bigger than the length of the request response body or it was smaller than zero
    - **`.close()`** None - This method does nothing and only exists for cross compatibility
  - **Raisable Exceptions**:
    - **`TypeError`** – Input parameter types are incorrect
    - **`ValueError`** – Input parameter types are invalid
    - **`FileNotFoundError`** – Unable to locate input parameter file argument
    - **`FileExistsError`** – Output file already exists
    - **`tooltils.errors.InvalidRequestURL`** – The specificed URL could not be used to make a valid request
    - **`tooltils.errors.ConnectionError`** – General connection failed error
    - **`tooltils.errors.ActiveRequestError`** – The request returned malformed data
    - **`tooltils.errors.SSLCertificateFailed`** – Unable to verify SSL certificate
    - **`tooltils.errors.StatusCodeError`** – HTTP error status code response
    - **`tooltils.errors.InvalidWifiConnection`** – No valid internet connection present
    - **`tooltils.errors.ConnectionTimeoutExpired`** – Connection timed out
    - **`tooltils.errors.RequestRedirectError`** – Requested url redirected too many times or entered a redirect loop
    - **`tooltils.errors.RequestCodecError`** – None of the specified codecs were able to decode the response received from the server

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid
- **`FileNotFoundError`** – Unable to locate input parameter file argument
- **`FileExistsError`** – Output file already exists
- **`tooltils.errors.InvalidRequestURL`** – The specificed URL could not be used to make a valid request
- **`tooltils.errors.ConnectionError`** – General connection failed error
- **`tooltils.errors.ActiveRequestError`** – The request returned malformed data
- **`tooltils.errors.SSLCertificateFailed`** – Unable to verify SSL certificate
- **`tooltils.errors.StatusCodeError`** – HTTP error status code response
- **`tooltils.errors.InvalidWifiConnection`** – No valid internet connection present
- **`tooltils.errors.ConnectionTimeoutExpired`** – Connection timed out
- **`tooltils.errors.RequestRedirectError`** – Requested url redirected too many times or entered a redirect loop
- **`tooltils.errors.RequestCodecError`** – None of the specified codecs were able to decode the response received from the server

Example:
```py
>>> conn = tooltils.requests.openConnection('httpbin.org', proxy='localhost:12345') # this assumes you have a server set up on localhost at port 12345
>>> conn
<Connection httpbin.org [Connected]>
>>> data = conn.send('GET', '/basic-auth/user/pass', close=True, auth=('user', 'pass'), mask=True) # close the connection after use with close=True, anything else is kwargs that can be passed to `.change()`, you can also use the .send method with a context manager (with statement)
>>> conn
<Connection httpbin.org [Closed]>
>>> data
'<Request httpbin.org/basic-auth/user/pass [200 OK]>'
>>> data.redirected
False
>>> data.status_code
'200 OK'
>>> data.reason
'OK'
>>> data.code
200
>>> data.json
{'authenticated': True, 'user': 'user', ...}
>>> data.rdata
<http.client.HTTPResponse object at 0x0000016E67467A60>
```

Return type: **tooltils.requests.openConnection** <br>
Returns: **A requestable connection class** <br><br>

**`request(url, method)`** <br>
Open a single-use connection to a URL

Parameters:
- **`url`** str – URL to send the request to
- **`method`** str – The http method to use in the request (GET, POST, DOWNLOAD, HEAD, PUT, PATCH, OPTIONS, TRACE, DELETE)
- **`port`** int = (443 if https else 80) – The port to send the request on
- **`https`** bool = True – Whether https should be used in the request
- **`verify`** bool = `config.defaultVerificationMethod` – Whether to verify the request using a certificate
- **`redirects`** bool = True – Whether to allow redirects
- **`redirect_loops`** bool = False – Whether to allow redirect looping
- **`auth`** tuple = None – Authentication in a username password tuple format
- **`data`** dict = None – JSON data to send with the request
- **`headers`** dict = None – Headers to add to the request (Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file (Will use default if None)
- **`file_name`** str = None – Path to download the file (Will use URL file name if None)
- **`write_binary`** bool = False – Whether to write the downloaded file as binary
- **`override`** bool = False – Whether the output file should be overrid
- **`timeout`** int | float = 15 – How long the request should last in seconds before it should be terminated
- **`encoding`** str | tuple = (‘utf-8’, ‘ISO-8859-1’) – Codec(s) to use to decode the response text
- **`mask`** bool = False – Whether to use an anonymous user agent header (firefox's user agent)
- **`agent`** str = None – Overwrite for the agent header
- **`proxy`** str = None – The proxy to send the request on
- **`advContext`** tooltils.requests.advancedContext = None – A tooltils advanced context class

Return properties:
- **`url`** str – The URL that the request was sent to
- **`method`** str – The http method used in the request
- **`port`** int – The port the request was sent on
- **`https`** bool – Whether https was used with the request
- **`verify`** bool – Whether the request was verified with a certificate
- **`redirects`** bool – Whether the requested URL was allowed to redirect the request
- **`redirect_loops`** bool = False – Whether the requested URL was allowed to loop redirects recursively
- **`*auth`** tuple – Authentication used in the request
- **`*data`** dict – JSON data that was sent with the request
- **`headers`** dict – The headers sent as the configuration of the request
- **`cookies`** dict – Cookies that were sent with the request
- **`cert`** str – Path to certificate.pem file (Will use default if None)
- **`*file_name`** str – Path to download the file (Will use URL file name if None)
- **`write_binary`** bool – Whether to write the downloaded file as binary
- **`override`** bool – Whether the output file should be overrid
- **`timeout`** int | float – How long the request lasts in seconds before it should be terminated
- **`encoding`** str | tuple – Codec(s) used to decode the response text
- **`mask`** bool – Whether the user agent header was anonymised
- **`*agent`** str – The overwritten agent header for the request
- **`*proxy`** str – The proxy that was used to send the request on
- **`*advContext`** tooltils.requests.advancedContext – A tooltils advanced context class
- **`sent`** bool – Whether the request has been sent
- **`rID`** int – The ID for the current connection
- **`redirected`** bool – Whether the request was redirected
- **`redirectLimit`** int – The amount of redirects the url can make before an exception is raised
- **`extraLogs`** bool – If extra detailed logs should be output
- **`*SSLContext`** ssl.SSLContext – A custom SSLContext instance

Return methods:
- **`.send()`** – Send the request to the url – *Details*:
  - **Return Properties**:
    - **`code`** int – The status code of the request
    - **`reason`** str – The reason of the request's status code
    - **`status_code`** str – The status code and reason of the request combined
    - **`*text`** str – The text of the request response
    - **`*raw`** bytes – The raw, encoded text of the request response
    - **`*json`** dict – The json of the request response containing all the data
    - **`*path`** str – The path of the downloaded file (if the method was DOWNLOAD)
    - **`rdata`** http.client.HTTPResponse – The http base response class containing all the data read
    - **`end_data**`** class – Information that was sent in the request but not returned – *Properties*:
      - **`url`** str – The url that was requested
      - **`*sent_headers`** dict[str, str] – The headers that were sent in the request
      - **`*agent`** str – The User-Agent of the request headers that were sent
    - **`.read()`** bytes – Read the request file and return the raw data
    - **`.readlines()`** list[str] – Read the request file and return the data as a list split at every newline
  - **Return Methods**:
    - **`.read()`** bytes – Read the request response body or up to amt bytes – *Details*:
      - **Parameters**:
        - **`amt`** int = None – The length of data to read (will read whole body if None)
      - **Raisable Exceptions**:
        - **`TypeError`** – Input parameter type is incorrect
        - **`ValueError`** – The input amt was bigger than the length of the request response body
    - **`.readlines()`** list[str] - Read the request response body or up to amt bytes and return as a list split at every newline – *Details*:
      - **Parameters**:
        - **`amt`** int = None – The length of data to read (will read whole body if None)
      - **Raisable Exceptions**:
        - **`TypeError`** – Input parameter type is incorrect
        - **`ValueError`** – The input amt was bigger than the length of the request response body
    - **`.seek(pos)`** None - Read the request response body or up to amt bytes and return as a list split at every newline – *Details*:
      - **Parameters**:
        - **`pos`** int = None – The position of the request response body to go to
      - **Raisable Exceptions**:
        - **`TypeError`** – Input parameter type is incorrect
        - **`ValueError`** – The input pos was bigger than the length of the request response body or it was smaller than zero
    - **`.close()`** None - This method does nothing and only exists for cross compatibility
  - **Raisable Exceptions**:
    - **`tooltils.errors.InvalidRequestURL`** – The specificed URL could not be used to make a valid request
    - **`tooltils.errors.ConnectionError`** – General connection failed error
    - **`tooltils.errors.ActiveRequestError`** – The request returned malformed data
    - **`tooltils.errors.SSLCertificateFailed`** – Unable to verify SSL certificate
    - **`tooltils.errors.StatusCodeError`** – HTTP error status code response
    - **`tooltils.errors.InvalidWifiConnection`** – No valid internet connection present
    - **`tooltils.errors.ConnectionTimeoutExpired`** – Connection timed out
    - **`tooltils.errors.RequestRedirectError`** – Requested url redirected too many times or entered a redirect loop
    - **`tooltils.errors.RequestCodecError`** – None of the specified codecs were able to decode the response received from the server

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid
- **`FileNotFoundError`** – Unable to locate input parameter file argument
- **`FileExistsError`** – Output file already exists
- **`tooltils.errors.InvalidRequestURL`** – The specificed URL could not be used to make a valid request
- **`tooltils.errors.ConnectionError`** – General connection failed error
- **`tooltils.errors.ActiveRequestError`** – The request returned malformed data
- **`tooltils.errors.SSLCertificateFailed`** – Unable to verify SSL certificate
- **`tooltils.errors.StatusCodeError`** – HTTP error status code response
- **`tooltils.errors.InvalidWifiConnection`** – No valid internet connection present
- **`tooltils.errors.ConnectionTimeoutExpired`** – Connection timed out
- **`tooltils.errors.RequestRedirectError`** – Requested url redirected too many times or entered a redirect loop
- **`tooltils.errors.RequestCodecError`** – None of the specified codecs were able to decode the response received from the server

Example:
```py
>>> req = tooltils.requests.request('httpbin.org/basic-auth/user/pass', 'GET', auth=('user', 'pass'),
                                    mask=True, proxy='localhost:12345') # this assumes you have a server set up on localhost at port 12345
>>> req
<GET httpbin.org [Unsent]>
>>> data = req.send()
>>> req
<GET httpbin.org [200]>
>>> req.redirected
False
>>> data.status_code
'200 OK'
>>> data.reason
'OK'
>>> data.code
200
>>> data.json
{'authenticated': True, 'user': 'user', ...}
>>> data.rdata
<http.client.HTTPResponse object at 0x0000016E67467A60>
```

Return type: **tooltils.requests.request** <br>
Returns: **A request class** <br><br>

*The http method functions do not include the `file_name`, `write_binary` or `override` parameters unless otherwise specified*

<br>

**`get(url)`** <br>
Send a GET request

*Calls `request(method='GET', ...).send()` and returns the result*

<br>

**`post(url)`** <br>
Send a POST request

*Calls `request(method='POST', ...).send()` and returns the result*

<br>

**`download(url)`** <br>
Download a file onto the disk

*Calls `request(method='DOWNLOAD', ...).send()` and returns the result* <br>
*This uses the `file_name`, `write_binary` and `override` parameters aswell as any request ones*

<br>

**`head(url)`** <br>
Send a HEAD request

*Calls `request(method='HEAD', ...).send()` and returns the result*

<br>

**`put(url)`** <br>
Send a PUT request

*Calls `request(method='PUT', ...).send()` and returns the result*

<br>

**`patch(url)`** <br>
Send a PATCH request

*Calls `request(method='PATCH', ...).send()` and returns the result*

<br>

**`options(url)`** <br>
Send an OPTIONS request

*Calls `request(method='OPTIONS', ...).send()` and returns the result*

<br>

**`trace(url)`** <br>
Send a TRACE request

*Calls `request(method='TRACE', ...).send()` and returns the result* <br>
*This function does not use the `data` or `cookies` arguments, see [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-trace)*

<br>

**`delete(url)`** <br>
Send a DELETE request

*Calls `request(method='DELETE', ...).send()` and returns the result*

<br><br>

## <span style="font-family: Trebuchet MS;">requests.urllib</span>

*Internet requesting access methods - `urllib.request` version*

Properties:
- **`status_codes`** dict – List of official valid HTTP response status codes (100-511)
- **`defaultVerificationMethod`** bool – The config value for the verify parameter in request methods

Methods:

**`NoRedirects()`** <br>
An opener to prevent redirects in urllib requests

**You can install this as an opener to use in urllib to prevent redirects by the requested url**

Example:
- *See lines 197-201 in `tooltils.requests.urllib.py`*

<br>

**`request(url, method)`** <br>
Initiate and send a request to a url

Parameters:
- **`url`** str – URL to send the request to
- **`method`** str – The http method to make the request with
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request
- **`headers`** dict = None – Headers to add to the request (Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file (Will use default if None)
- **`file_name`** str = None – Path to download the file (Will use URL file name if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = `config.defaultVerificationMethod` – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects
- **`override`** bool – Whether the output file should be overrid if the request method is **"DOWNLOAD"**

Return properties:
- **`verified`** bool – Whether the request was verified with SSL
- **`port`** int = 443 – The port used to send the request on
- **`https`** bool = True - Whether https was used for the request
- **`redirects`** bool – Whether url redirects are enabled
- **`mask`** bool – Whether the user agent header should be replaced with a more conventional one (firefox browser)
- **`method`** str – The method used in the request
- **`*data`** dict – Data to send with the request
- **`*cookies`** dict – Cookies to include in the request header
- **`*cert`** str – The location of the certificate used in the request
- **`*auth`** tuple – The authentication of the request [user pass tuple pair] (none if not specified)
- **`timeout`** int – The amount of seconds the request should last for before being terminated
- **`*file_name`** str – The name and directory of the file if the download method is being used
- **`agent`** str – The user agent to send in the headers of the request
- **`headers`** dict – The data sent as the configuration of the request
- **`encoding`** str – The text encoding to use when decoding the response text
- **`url`** str – The configured url used to sent the request to
- **`override`** bool – Whether the output file was overrid if the request method was **"DOWNLOAD"**
- **`sent`** bool – Whether the request has been used
- **`code`** int – The status code of the request
- **`reason`** str – The reason of the request's status code
- **`status_code`** str – The status code and reason of the requets combined
- **`*text`** str – The text of the request response
- **`*raw`** bytes – The encoded text of the request response
- **`*html`** str – The html of the request url
- **`*path`** str – The output path of the file if the download method was used
- **`*json`** dict – The json of the request response containing all the data
- **`rdata`** http.client.HTTPResponse – The http base response class containing all the data read

Return methods:
- **`.send()`** <i>self</i> – Send the request to the url
- **`.read()`** – Read the request file and return the raw data
- **`.readlines()`** list – Read the request file and return the data as a list split at every newline

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid
- **`FileNotFoundError`** – Unable to locate input parameter file argument
- **`FileExistsError`** – Output file already exists
- **`tooltils.errors.InvalidRequestURL`** – The specificed URL could not be used to make a valid request
- **`tooltils.errors.ConnectionError`** – General connection failed error
- **`tooltils.errors.SSLCertificateFailed`** – Unable to verify SSL certificate
- **`tooltils.errors.StatusCodeError`** – HTTP error status code response
- **`tooltils.errors.InvalidWifiConnection`** – No valid internet connection present
- **`tooltils.errors.ConnectionTimeoutExpired`** – Connection timed out

Example:
- There is not another example for this method because the simplistic request interface is the same

Return type: **tooltils.requests.urllib.request** <br>
Returns: **A request class** <br><br>

**`get(url)`** <br>
Send a GET request

*Calls `.requests.urllib.request(method='GET', ...).send()` and returns the result*

<br><br>

**`post(url)`** <br>
Send a POST request

*Calls `.requests.urllib.request(method='POST', ...).send()` and returns the result*

<br><br>

**`download(url)`** <br>
Download a file onto the disk

*Calls `.requests.urllib.request(method='DOWNLOAD', ...).send()` and returns the result* <br>
*This uses the `file_name` and `override` parameters aswell as any request ones*

<br><br>

**`head(url)`** <br>
Send a HEAD request

*Calls `.requests.urllib.request(method='HEAD', ...).send()` and returns the result*

<br><br>

**`put(url)`** <br>
Send a PUT request

*Calls `.requests.urllib.request(method='PUT', ...).send()` and returns the result*

<br><br>

**`patch(url)`** <br>
Send a PATCH request

*Calls `.requests.urllib.request(method='PATCH', ...).send()` and returns the result*

<br><br>

**`delete(url)`** <br>
Send a DELETE request

*Calls `.requests.urllib.request(method='DELETE', ...).send()` and returns the result*

<br><br>

## <span style="font-family: Trebuchet MS;">errors</span>

*Package specific exceptions*

**`TooltilsError`** <br>
Base class for tooltils specific errors

Parent class: `Exception` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return properties:
- **`message`** str – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A Tooltils error occured"**
- Specified Message <br><br>

**`TooltilsMainError`** <br>
Base class for tooltils main module specific errors

Parent class: `TooltilsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return properties:
- **`message`** str – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A Tooltils main module error occured"**
- Specified Message <br><br>

**`TooltilsInfoError`** <br>
Base class for tooltils.info module specific errors

Parent class: `TooltilsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return properties:
- **`message`** str – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.info error occured"**
- Specified Message <br><br>

**`TooltilsOSError`** <br>
Base class for tooltils.os module specific errors

Parent class: `TooltilsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return properties:
- **`message`** str – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.os error occured"**
- Specified Message <br><br>

**`SubprocessError`** <br>
Base class for tooltils.os.system() specific errors

Parent class: `TooltilsOSError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return properties:
- **`message`** str – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.os.system() error occured"**
- Specified Message <br><br>

**`RequestError`** <br>
Base class for tooltils.requests.request() specific errors

Parent class: `TooltilsRequestsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return properties:
- **`message`** str – The message to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.requests.request() error occured"**
- Specified Message <br><br>

**`SubprocessExecutionError`** <br>
Child process execution failed

Parent class: `SubprocessError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return properties:
- **`message`** str – The message to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"Child process execution failed"**
- Specified Message <br><br>

**`SubprocessCodeError`** <br>
Child process execution returned non-zero exit code

Parent class: `SubprocessError` <br>

Parameters:
- **`code`** int = 0 – The non-zero error code raised
- **`message`** str = ‘’ – The message to print instead of the default message

Return properties:
- **`code`** int – The non-zero error code returned
- **`message`** str – The message to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"Child process execution returned non-zero exit code"**
- Message with code: **"Child process execution returned non-zero exit code <i>[code]</i>"**
- Specified Message <br><br>

**SubprocessTimeoutExpired`** <br>
Child process execution timed out

Parent class: `SubprocessError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`timeout`** int = 0 – The timeout in whole seconds of the program that timed out

Return properties:
- **`message`** str – The text to print instead of the default message
- **`timeout`** int – The timeout in whole seconds of the program that timed out

Return type: **str** <br>
Returns:
- Default Message: **"Child process execution timed out"**
- Message with timeout: **"Child process execution timed out at <i>[timeout]</i> seconds"**
- Specified Message <br><br>

**`SubprocessLookupNotFound`** <br>
Unable to locate program or shell command

Parent class: `SubprocessError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`name`** str = ‘’ – The name or arguments that were initiated to find the program or shell command

Return properties:
- **`message`** str – The text to print instead of the default message
- **`name`** str – The name or arguments that were initiated to find the program or shell command

Return type: **str** <br>
Returns:
- Default Message: **"Unable to locate program or shell command"**
- Message with name: **"Unable to locate program or shell command '<i>[name]</i>'"**
- Specified Message <br><br>

**`SubprocessPermissionError`** <br>
Denied access to program or shell command

Parent class: `SubprocessError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`name`** str = ‘’ – The name or arguments that were initiated to find the program or shell command

Return properties:
- **`message`** str – The text to print instead of the default message
- **`name`** str – The name or arguments that were initiated to find the program or shell command

Return type: **str** <br>
Returns:
- Default Message: **"Denied access to program or shell command"**
- Message with name: **"Unable to locate program or shell command '<i>[name]</i>'"**
- Specified Message <br><br>

**`TooltilsOSInfoError`** <br>
Base class for tooltils.os.info module specific errors

Parent class: `TooltilsOSError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return properties:
- **`message`** str – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.os.info error occured"**
- Specified Message <br><br>

**`TooltilsRequestsError`** <br>
Base class for tooltils.requests module specific errors

Parent class: `TooltilsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return properties:
- **`message`** str – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.requests error occured"**
- Specified Message <br><br>

**`ActiveRequestError`** <br>
Request to the URL failed

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`url`** str = ‘’ – The URL that failed the request

Return properties:
- **`message`** str – The text to print instead of the default message
- **`url`** str – The URL that failed the request

Return type: **str** <br>
Returns:
- Default Message: **"Request to the URL failed"**
- Message with url: **"Request to <i>[url]</i> failed"**
- Specified Message <br><br>

**`InvalidRequestURL`** <br>
URL cannot be used to make a valid request

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`url`** str = ‘’ – The URL that failed

Return properties:
- **`message`** str – The text to print instead of the default message
- **`url`** str – The URL that failed

Return type: **str** <br>
Returns:
- Default Message: **"URL cannot be used to make a valid request"**
- Message with url: **"URL '<i>[url]</i>' cannot be used to make a valid request"**
- Specified Message <br><br>

**`ConnectionError`** <br>
Connection to URL failed

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`url`** str = ‘’ – The URL that failed the request

Return properties:
- **`message`** str – The text to print instead of the default message
- **`url`** str – The URL that failed the request

Return type: **str** <br>
Returns:
- Default Message: **"Connection to URL failed"**
- Message with url: **"Connection to <i>[url]</i> failed"**
- Specified Message <br><br>

**`ConnectionTimeoutExpired`** <br>
Request connection timeout expired

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`timeout`** int = 0 – The timeout of the request that raised an error

Return properties:
- **`message`** str – The text to print instead of the default message
- **`timeout`** int – The timeout of the request that raised an error

Return type: **str** <br>
Returns:
- Default Message: **"Request connection timeout expired"**
- Message with timeout: **"Request connection timeout expired at <i>[timeout]</i> seconds"**
- Specified Message <br><br>

**`StatusCodeError`** <br>
The URL response returned an impassable status code

Parent class: `RequestError` <br>

Parameters:
- **`code`** int = 0 – The status code returned by the response
- **`reason`** str = ‘’ – The reason paired with the status code

Return properties:
- **`code`** int – The status code returned by the response
- **`reason`** str – The reason paired with the status code

Return type: **str** <br>
Returns:
- Default Message: **"The URL request response returned an impassable HTTP status code"**
- Message with code and reason: **"<i>[code] [reason]</i>"**
- Message with code: **"<i>[code] [reason guessed from .status_codes]</i>"**
- Message with reason: **"<i>[code guessed from .status_codes] [reason]</i>"**
- If the code or reason aren't successfully guessed, the message will revert back to the default <br><br>

**`SSLCertificateFailed`** <br>
The currently used SSL certificate could not be used to verify requests

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"The currently used SSL certificate could not be used to verify requests"**
- Specified Message <br><br>

**`InvalidWifiConnection`** <br>
No valid wifi connection could be found for the request

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"No valid wifi connection could be found for the request"**
- Specified Message <br><br>

**`RequestRedirectError`** <br>
Request redirected too many times or entered a redirect loop

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`limit`** int = 0 – The redirect limit of the request that raised an error

Return properties:
- **`limit`** int – The redirect limit of the request that raised an error

Return type: **str** <br>
Returns:
- Default Message: **"Request redirected too many times or entered a redirect loop"**
- Message with limit: **"Request redirected too many times at <i>[limit]</i> redirects"**
- Specified Message <br><br>

**`RequestCodecError`** <br>
Unable to decode request body

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`encoding`** str | tuple = (‘utf-8’, ‘ISO-8859-1’) – The codecs that were tried

Return properties:
- **`encoding`** str | tuple – The codecs that were tried

Return type: **str** <br>
Returns:
- Default Message: **"Unable to decode request body"**
- Message with encoding: **"Unable to decode request body from codec(s): <i>[encoding]</i>"**
- Specified Message <br><br>

## <span style="font-family: Trebuchet MS;">Config</span>

**Default Settings**

The default structure for the config is as follows:

```json
"errors": {},
"global": {
    "disableConfigMethodValues": false,
    "configMethodCheck": 20
},
"info": {
    "disableOnlineContentFetch": false,
},
"main": {},
"requests": {
    "defaultVerificationMethod": true,
    "verifiableCachingCheck": 20,
    "connectedCachingCheck": 20,
    "verifiableCaching": false,
    "connectedCaching": false,
    "redirectLimit": 20
},
"sys.info": {},
"sys": {}
```

<br>

**Specifying methods**

To set a setting value as a method, you first need to set the value to a string, then add the **"`$f`"** keyword, afterwards insert a space and the method. If an error was raised or the function did not execute properly the config value will become None. Keyword arguments are not supported as of yet. To use a tooltils method follow the below example with each module. You may use any tooltils method available. Built-in Python functions will work but not those from the standard library:

```json
"requests": {
    "defaultVerificationMethod": "$f tooltils.requests.verifiable()"
},
```

The above example sets the verify parameter default in `requests` methods to the result of `tooltils.requests.verifiable()`, automatically preventing any kind of SSL error. Though this is not good practice as the certificate should be verified by default for security purposes. See as to why implementing a config to have the option of doing this is a good idea for people who seek this capability.

```jsonc
"requests": {
    "defaultVerificationMethod": "$f tooltils.sys.getCurrentWifiName()" // tooltils function
}
```
