# <span style="font-family: Trebuchet MS;">tooltils – api</span>

*<b>NOTE:</b> If a property has a star sign in front of it, it can have a value of none*

## <span style="font-family: Trebuchet MS;">Tooltils</span>

*Broad methods that aren't big enough for their own module* <br><br>

Properties:
- **`ANSI_colours`** dict – List of the main colours as ANSI integer codes

<br>

Methods:

**`length(file)`** <br>
Get the length of a wave file in seconds

Parameters:
- **`file`** str - Path to WAVE file

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect
- **`ValueError`** – Input parameter is invalid
- **`FileNotFoundError`** – Unable to locate input file

Return type: **float** <br>
Returns: **Length of file in seconds** <br><br>

**`style(text)`** <br>
Create text in the specified colour and or style

Parameters:
- **`text`** str – Text to style
- **`colour`** str = ‘’ – Colour to use
- **`bold`** bool = False – Whether to make the text bold
- **`italic`** bool = False – Whether to italicise the text
- **`fill`** bool = False – Whether to fill the text background with the specified colour
- **`crossed`** bool = False – Whether to cross the text
- **`underline`** bool = False – Whether to underline the text
- **`double_underline`** bool = False – Whether to double underline the text
- **`flush`** bool = True – Whether to apply a fix to the terminal because of a display bug

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect

Return type: **str** <br>
Returns: **Styled text** <br><br>

**`halve(array)`** <br>
Return the halves of a string or array

Parameters:
- **`array`** str | list | tuple | set | dict – Iterable to halve

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect

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

Return type: **str** <br>
Returns: **Ciphered text** <br><br>

**`mstrip(text, values)`** <br>
Change some text from a dictionary pair of values

Parameters:
- **`text`** str – Text to be changed
- **`values`** dict – List of characters to change

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect

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

Return type: **str** <br>
Returns: **Formatted date** <br><br>

**`epoch(date)`** <br>
Get epoch from a formatted string date

Parameters:
- **`date`** str – The formatted date to convert

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect
- **`ValueError`** – Input parameter type is invalid

Return type: **int** <br>
Returns: **Epoch in seconds of the input date** <br><br>

**`squeeze(array)`** <br>
Remove empty or the specified item(s) from an array

Parameters:
- **`array`** list | tuple | set | dict – The array to change
- **`item`** Any = None – The item to remove

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect

Return type: **list | tuple | set | dict** <br>
Returns: **Edited array of the same time as the input** <br><br>

**`reverseDictSearch(array, value)`** <br>
Find the unknown key(s) of a value in a dictionary

Parameters:
- **`array`** dict – The dictionary to search
- **`value`** Any – The value to find the key(s) for

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect

Return type: **Any** <br>
Returns: **Key(s) found** <br><br>

**`getArrayValues(array)`** <br>
Recursively obtain all of the values of any keys or items within an array

Parameters:
- **`array`** list | tuple | dict – The array to search

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect

Return type: **tuple** <br>
Returns: **All base-level values in the array** <br><br>

**`timeTest(method, method2)`** <br>
Run two different methods x amount of times, sum then divide to estimate accurate run-time

Parameters:
- **`method`** function – The first method to test
- **`method2`** function – The second method to test
- **`params`** dict = {} – Kwargs for the first method
- **`params2`** dict = {} – Kwargs for the second method
- **`accuracy`** int = 10 – The amount of times to test each method

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid

Return type: **tuple[float]** <br>
Returns: **Average run-time for each method as a tuple** <br><br>

**`varName(**vars)`** <br>
Get the namespace name of one or more variables

Parameters:
- **`**vars`** dict – The variables to get the name for

Usage:
- Input a variable that has been declared earlier as the kward argument, then put that variable as the value of the argument. Example `varName(data=data) # data`

Raisable exceptions:
- None

Return type: **str | list[str]** <br>
Returns: **Names of variables input** <br><br>

**`tgzOpen(file)`** <br>
Open a gzipped tar file

Parameters:
- **`file`** str – The location of the .tar.gz or .tgz file
- **`output`** str – The location or file path and name of the output uncompressed file

Usage:
- For the output parameter, if you only want to specify the location it should be placed in, then add a slash or backslash to the end of the path to signify. If it shall include the name of the output file/folder, then don't include a terminating character at the end.

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid
- **`FileExistsError`** – Output file exists already
- **`FileNotFoundError`** – Problem locating output file

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

Return type: **list | tuple | set | dict** <br>
Returns: **Sorted input array** <br><br>

**`interpreter(file)`** <br>
Custom top-level Python interpreter to add niche features from other languages

Parameters:
- **`file`** str – The Python file to convert
- **`output`** str = ‘%(name)s.interpreted.py’ – The name of the converted Python file
- **`override`** bool = False – Whether to override the content of an existing output file with the same name

Return properties:
- **`file`** str – The Python file that was converted
- **`output`** str – The name of the converted Python file
- **`full_output`** str – The full file path of the convert Python file
- **`override`** bool – Whether an existing file was overrid

Return methods:
- **`.read()`** str – Read the output file and return the content as a string
- **`.readlines()`** list[str] – Read the output file and return the content as a list containing strings split at every newline

Current features:
- **Ternary Operations** – Javascript like ternary operators
- **JS Comments** – Javascript like comments using `//` as a prefix

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid | function already called
- **`FileExistsError`** – Output file exists already
- **`FileNotFoundError`** – Problem locating output file

Return type: **tooltils.interpreter** <br>
Returns: **Interpreter instance** <br><br>

## <span style="font-family: Trebuchet MS;">sys</span>

*System specific methods and information*

**`exit(details)`** <br>
Print some text and exit the current thread

Parameters:
- **`details`** str = ‘’ – Text to print before exiting
- **`code`** int = 0 – Exit code to use

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect

Return type: **NoReturn** <br>
Returns: **Nothing** <br><br>

**`clear()`** <br>
Clear the terminal history

Parameters:
- None

Raisable exceptions:
- None

Return type: **None** <br>
Returns: **None** <br><br>

**`system(cmds)`** <br>
Call a system program and return some information

Parameters:
- **`cmds`** str | list – Commands/program to call
- **`shell`** bool = False – Whether to use the shell
- **`timeout`** int = 10 – How long the command/program should last before cancelling
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`capture`** bool = True – Whether to capture the output of the command/program
- **`print`** bool = True – Whether command/program can print to stdout

Return properties:
- **`cmds`** str | list – Command/programs that were called
- **`shell`** bool – Whether shell was used to call the command/program
- **`timeout`** bool – How long the command/program should last before cancelling
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
- **`tooltils.errors.ShellCodeError`** – Shell code returncode is not zero
- **`tooltils.errors.ShellTimeoutExpired`** – Self explanatory
- **`tooltils.errors.ShellCommandNotFound`** – Cannot locate shell program
- **`tooltils.errors.ShellCommandPermissionError`** — Access denied to shell program
- **`tooltils.errors.ShellCommandError`** – General shell program error

Return type: **tooltils.sys.system** <br>
Returns: **A system class** <br><br>

**`check(cmds)`** <br>
Call a system program and return the output

Parameters:
- **`cmds`** str | list – Commands/program to call
- **`shell`** bool = False – Whether to use the shell (sh)
- **`timeout`** int = 10 – How long the process should last
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`clean`** bool = False – Whether to remove empty values from the output as a list
- **`listify`** bool = True – Whether to convert the stdout output to a list (.list_text)
- **`raw`** bool = False – Whether to return raw bytes output
- **`print`** bool = True – Whether command/program can print to stdout

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid
- **`tooltils.errors.ShellCodeError`** – Shell code returncode is not zero
- **`tooltils.errors.ShellTimeoutExpired`** – Self explanatory
- **`tooltils.errors.ShellCommandNotFound`** – Cannot locate shell program
- **`tooltils.errors.ShellCommandPermissionError`** — Access denied to shell program
- **`tooltils.errors.ShellCommandError`** – General shell program error

Return type: **str | bytes | list[str]** <br>
Returns: **List of lines or bytes containing stdout output** <br><br>

**`call(cmds)`** <br>
Call a system program and return the exit code

Parameters:
- **`cmds`** str | list – Commands to call
- **`shell`** bool = False – Whether to use the shell (sh)
- **`timeout`** int = 10 – How long the process should last
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`print`** bool = True – Whether command/program can print to stdout

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid
- **`tooltils.errors.ShellCodeError`** – Shell code returncode is not zero
- **`tooltils.errors.ShellTimeoutExpired`** – Self explanatory
- **`tooltils.errors.ShellCommandNotFound`** – Cannot locate shell program
- **`tooltils.errors.ShellCommandPermissionError`** — Access denied to shell program
- **`tooltils.errors.ShellCommandError`** – General shell program error

Return type: **int** <br>
Returns: **Exit code of program call** <br><br>

**`pID(name)`** <br>
Get the process ID of an app or binary by name

*May return a list if multiple processes are found*

Parameters:
- **`name`** str – Name of app or binary

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid

Return type: **int | list[int]** <br>
Returns: **Process ID or list of found IDs** <br><br>

**`getCurrentWifiName()`** <br>
Get the currently connected wifi name

*Will return None if not connected or nothing was found*

Parameters:
- None

Raisable exceptions:
- None

Return type: **str | None** <br>
Returns: **Wifi Name** <br><br>

## <span style="font-family: Trebuchet MS;">sys.info</span>

*Identifying system information*

Properties:
- **`macOS_releases`** dict[str, str] – List of all current MacOS versions
- **`python_version`** str – Current Python interpreter version
- **`name`** str – The network name of computer
- **`bitsize`** int – The bit limit of the current Python interpreter
- **`interpreter`** str – Location of current Python interpreter
- **`platform`** str – Name of current operating system
- **`detailed_platform`** str – Detailed name of current operating system
- **`cpu`** str – Name of the currently in use cpu of your computer
- **`arch`** str – Computer architecture
- **`platform_version`** tuple[str] – Version number and or name of current OS
- **`model`** str – The model or manufacturer of your computer
- **`cores`** int – The amount of cores in your computer cpu
- **`ram`** int – The amount of ram in megabytes in your computer
- **`manufacturer`** str – The organisation or company that created your computer
- **`serial_number`** str – The identifiable code or tag string of your computer (This is unobtainable on Linux)
- **`boot_drive`** str – The location of the boot drive currently being used on your computer

<br><br>

## <span style="font-family: Trebuchet MS;">requests</span>

*Internet requesting access methods*

Properties:
- **`status_codes`** dict – List of official valid HTTP response status codes (100-511)
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

Return type: **ssl.SSLContext** <br>
Returns: **An SSLContext instance** <br><br>

**`connected()`** <br>
Get the connectivity status of the currently connected wifi network

*When caching is enabled, it will used the cached value 20 times by default and then create a new one and cache that instead.*

Parameters:
- None

Raisable exceptions:
- None

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

Return type: **str** <br>
Returns: **Corrected URL** <br><br>

**`where()`** <br>
Return default certificate file and path locations used by Python

Parameters:
- None

Raisable exceptions:
- None

Return type: **tooltils.requests.certifs** <br>
Returns: **Certificate class** <br><br>

**`verifiable()`** <br>
Determine whether requests can be verified with a valid ssl certificate on the current connection

*This function will use the cached value 20 times by default and then create a new one and cache that instead.*

Parameters:
- None

Raisable exceptions:
- None

Return type: **bool** <br>
Returns: **Whether requests can use a valid ssl certificate** <br><br>

**`advancedContext()`** <br>
Create an advanced context intended to be used for extended functionality with requesting

Parameters:
- **`redirectLimit`** int = `config.redirectLimit` – How many times the url can redirect the request before an exception is raised
- **`extraLogs`** bool = False – Whether extra more detailed logs should be output
- **`SSLContext`** SSLContext = tooltils.requests.ctx() – A custom SSLContext instance to override the one created by the request class

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid

Return type: **tooltils.requests.advContext** <br>
Returns: **Advanced context class** <br><br>

**`request(url, method)`** <br>
Initiate and send a request to a url

Parameters:
- **`url`** str – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request
- **`headers`** dict = None – Headers to add to the request (Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file (Will use default if None)
- **`file_name`** str = None – Path to download the file (Will use URL file name if None)
- **`write_binary`** bool – Whether to write the downloaded file as binary
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str | tuple = (‘utf-8’, ‘ISO-8859-1’) – Codec(s) used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = `config.defaultVerificationMethod` – Whether to use SSL in the request
- **`redirects`** bool = True – Whether to allow redirects
- **`https`** bool = True – Whether https should be used in the request
- **`port`** int = (443 if https else 80) – The port to send the request on
- **`override`** bool = False – Whether the output file should be overrid if the request method is **"DOWNLOAD"**
- **`advContext`** tooltils.requests.advancedContext = None – A tooltils advanced context class

Return properties:
- **`verified`** bool – Whether the request was verified with SSL
- **`port`** int – The port used to send the request on
- **`https`** bool - Whether https was used for the request
- **`redirects`** bool – Whether url redirects are enabled
- **`mask`** bool – Whether the user agent header should be replaced with a more conventional one (firefox browser)
- **`method`** str – The method used in the request
- **`*data`** dict – Data to send with the request
- **`*cookies`** dict – Cookies to include in the request header
- **`cert`** str – The location of the certificate used in the request
- **`*auth`** tuple – The authentication of the request [user pass tuple pair] (none if not specified)
- **`timeout`** int – The amount of seconds the request should last for before being terminated
- **`*file_name`** str – The name and directory of the file if the download method is being used
- **`write_binary`** bool – Whether to write the downloaded file as binary
- **`agent`** str – The user agent to send in the headers of the request
- **`sent_headers`** dict – The headers sent as the configuration of the request
- **`resp_headers`** dict – The headers that the server responded with from the request
- **`encoding`** str | tuple – The text encoding(s) to use when decoding the response text
- **`url`** str – The configured url used to sent the request to
- **`override`** bool – Whether the output file was overrid if the request method was **"DOWNLOAD"**
- **`sent`** bool – Whether the request has been used
- **`code`** int – The status code of the request
- **`reason`** str – The reason of the request's status code
- **`status_code`** str – The status code and reason of the requets combined
- **`text`** str – The text of the request response
- **`raw`** bytes – The encoded text of the request response
- **`*path`** str – The output path of the file if the download method was used
- **`*json`** dict – The json of the request response containing all the data
- **`rdata`** http.client.HTTPResponse – The http base response class containing all the data read
- **`*advContext`** tooltils.requests.advancedContext – A tooltils advanced context class
- **`redirectLimit`** int – The amount of redirects the url can make before an exception is raised
- **`extraLogs`** bool – If extra detailed logs should be output
- **`*SSLContext`** ssl.SSLContext – A custom SSLContext instance

Return methods:
- **`.read()`** – Read the request file and return the raw data
- **`.readlines()`** list – Read the request file and return the data as a list split at every newline

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter types are invalid
- **`FileNotFoundError`** – Unable to locate input parameter file argument
- **`FileExistsError`** – Output file already exists
- **`tooltils.errors.ConnectionError`** – General connection failed error
- **`tooltils.errors.SSLCertificateFailed`** – Unable to verify SSL certificate
- **`tooltils.errors.StatusCodeError`** – HTTP error status code response
- **`tooltils.errors.InvalidWifiConnection`** – No valid internet connection present
- **`tooltils.errors.ConnectionTimeoutExpired`** – Connection timed out
- **`tooltils.errors.RequestRedirectError`** – Requested url redirected too many times or entered a redirect loop
- **`tooltils.errors.RequestCodecError`** – None of the specified codecs were able to decode the response received from the server

Return type: **tooltils.requests.request** <br>
Returns: **A request class** <br><br>

**`get(url)`** <br>
Send a GET request

*Calls `.requests.request(method='GET', ...).send()` and returns the result*

<br><br>

**`post(url)`** <br>
Send a POST request

*Calls `.requests.request(method='POST', ...).send()` and returns the result*

<br><br>

**`download(url)`** <br>
Download a file onto the disk

*Calls `.requests.request(method='DOWNLOAD', ...).send()` and returns the result*
*This uses the `file_name`, `write_binary` and `override` parameters aswell as any request ones*

<br><br>

**`head(url)`** <br>
Send a HEAD request

*Calls `.requests.request(method='HEAD', ...).send()` and returns the result*

<br><br>

**`put(url)`** <br>
Send a PUT request

*Calls `.requests.request(method='PUT', ...).send()` and returns the result*

<br><br>

**`patch(url)`** <br>
Send a PATCH request

*Calls `.requests.request(method='PATCH', ...).send()` and returns the result*

<br><br>

**`delete(url)`** <br>
Send a DELETE request

*Calls `.requests.request(method='DELETE', ...).send()` and returns the result*

<br><br>

## <span style="font-family: Trebuchet MS;">requests.urllib</span>

*Internet requesting access methods - `urllib.request` version (deprecated)*

***Note: This version of the requests module is deprecated and may be removed in a future release***

Properties:
- **`status_codes`** dict – List of official valid HTTP response status codes (100-511)
- **`defaultVerificationMethod`** bool – The config value for the verify parameter in request methods

Methods:

**`ctx()`** <br>
Create a custom SSLContext instance

Parameters:
- **`verify`** bool = True – Whether to check hostname and verify SSL request
- **`cert`** str = None – Location of certificate.pem file

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`FileNotFoundError`** – Cannot find input parameter file

Return type: **ssl.SSLContext** <br>
Returns: **An SSLContext instance** <br><br>

**`connected()`** <br>
Get the connectivity status of the currently connected wifi network

*When caching is enabled, it will used the cached value 20 times by default and then create a new one and cache that instead.*

Parameters:
- None

Raisable exceptions:
- None

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

Return type: **str** <br>
Returns: **Corrected URL** <br><br>

**`where()`** <br>
Return default certificate file and path locations used by Python

Parameters:
- None

Raisable exceptions:
- None

Return type: **tooltils.requests.urllib.certifs** <br>
Returns: **Certificate class** <br><br>

**`verifiable()`** <br>
Determine whether requests can be verified with a valid ssl certificate on the current connection

*This function will use the cached value 20 times by default and then create a new one and cache that instead.*

Parameters:
- None

Raisable exceptions:
- None

Return type: **bool** <br>
Returns: **Whether requests can use a valid ssl certificate** <br><br>

**`NoRedirects()`** <br>
An opener to prevent redirects in urllib requests

**You can install this as an opener to use in urllib to prevent redirects by the requested url** <br><br>

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
- **`cert`** str – The location of the certificate used in the request
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
- **`.read()`** – Read the request file and return the raw data
- **`.readlines()`** list – Read the request file and return the data as a list split at every newline

Raisable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter type is invalid
- **`FileNotFoundError`** – Unable to locate input parameter file argument
- **`FileExistsError`** – Output file already exists
- **`tooltils.errors.ConnectionError`** – General connection failed error
- **`tooltils.errors.SSLCertificateFailed`** – Unable to verify SSL certificate
- **`tooltils.errors.StatusCodeError`** – HTTP error status code response
- **`tooltils.errors.InvalidWifiConnection`** – No valid internet connection present
- **`tooltils.errors.ConnectionTimeoutExpired`** – Connection timed out

Return type: **tooltils.requests.http.request** <br>
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

*Calls `.requests.urllib.request(method='DOWNLOAD', ...).send()</a> and returns the result*
*This uses the `file_name` parameter aswell as any request ones*

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

Return type: **str** <br>
Returns:
- Default Message: **"A Tooltils error occured"**
- Specified Message <br><br>

**`TooltilsMainError`** <br>
Base class for tooltils main module specific errors

Parent class: `TooltilsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A Tooltils main module error occured"**
- Specified Message <br><br>

**`TooltilsRequestsError`** <br>
Base class for tooltils.requests module specific errors

Parent class: `TooltilsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.requests error occured"**
- Specified Message <br><br>

**`TooltilsSysError`** <br>
Base class for tooltils.sys module specific errors

Parent class: `TooltilsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.sys error occured"**
- Specified Message <br><br>

**`TooltilsInfoError`** <br>
Base class for tooltils.info module specific errors

Parent class: `TooltilsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.info error occured"**
- Specified Message <br><br>

**`SystemCallError`** <br>
Base class for tooltils.sys.system() specific errors

Parent class: `TooltilsSysError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.sys.system() error occured"**
- Specified Message <br><br>

**`RequestError`** <br>
Base class for tooltils.requests.request() specific errors

Parent class: `TooltilsRequestsError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"A tooltils.requests.request() error occured"**
- Specified Message <br><br>

**`ShellCommandError`** <br>
Shell command exited while in process

Parent class: `SystemCallError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

**`ShellCodeError`** <br>
Shell command return non-zero exit code

Parent class: `SystemCallError` <br>

Parameters:
- **`code`** int = -1 – The non-zero error code returned
- **`message`** str = ‘’ – The message to print instead of the code message

Return properties:
- **`code`** int – The non-zero error code returned

Return type: **str** <br>
Returns:
- Default Message: **"Shell command returned non-zero exit code"**
- Message with code: **"Shell command returned non-zero exit code <i>[code]</i>"**
- Specified Message <br><br>

**ShellTimeoutExpired`** <br>
Shell command timed out

Parent class: `SystemCallError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`timeout`** int = -1 – The timeout of the command that raised an error

Return properties:
- **`timeout`** int – The timeout of the command that raised an error

Return type: **str** <br>
Returns:
- Default Message: **"Shell command timed out"**
- Specified Message <br><br>

**`ShellCommandError`** <br>
Shell command exited while in process

Parent class: `SystemCallError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"Shell command exited while in process"**
- Specified Message <br><br>

**`ShellCommandNotFound`** <br>
Unable to locate shell command or program

Parent class: `SystemCallError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"Unable to locate shell command or program"**
- Specified Message <br><br>

**`ShellCommandPermissionError`** <br>
Denied access to system command or program

Parent class: `SystemCallError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"Denied access to system command or program"**
- Specified Message <br><br>

**`ConnectionError`** <br>
Connection to URL failed

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"Connection to URL failed"**
- Specified Message <br><br>

**`ConnectionTimeoutExpired`** <br>
Request read timeout expired

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message
- **`timeout`** int = -1 – The timeout of the request that raised an error

Return properties:
- **`timeout`** int – The timeout of the request that raised an error

Return type: **str** <br>
Returns:
- Default Message: **"Request read timeout expired"**
- Specified Message <br><br>

**`StatusCodeError`** <br>
The URL response returned an impassable status code

Parent class: `RequestError` <br>

Parameters:
- **`code`** int = 0 – The status code returned by the response
- **`reason`** str = ‘’ – The reason paired with the status code

Return type: **str** <br>
Returns:
- Default Message: **"The URL response returned an impassable status code"**
- Specified Message <br><br>

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
- **`limit`** int = -1 – The redirect limit of the request that raised an error

Return properties:
- **`limit`** int – The redirect limit of the request that raised an error

Return type: **str** <br>
Returns:
- Default Message: **"Request redirected too many times or entered a redirect loop"**
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
- Specified Message <br><br>

## <span style="font-family: Trebuchet MS;">info</span>

*General installation information*

Properties:
- **`author`** str – The current owner of tooltils
- **`author_email`** str – The email of the current owner of tooltils
- **`maintainer`** str – The current sustainer of tooltils
- **`maintainer_email`** str – The email of the current sustainer of tooltils
- **`version`** str – The current installation version
- **`released`** str – The release date of the current installation
- **`license`** tuple[str] – The name and content of the currently used license in a tuple pair (name, content)
- **`description`** str – The short description of tooltils
- **`long_description`** str – The long description of tooltils
- **`location`** str – The path of the current installation of tooltils
- **`lines`** int – The amount of lines of code in this tooltils installation
- **`classifiers`** list[str] – The list of PyPi style tooltils classifiers
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

Return type: **None** <br>
Returns: **Nothing** <br><br>

**`clearConfig()`** <br>
Revert the config of tooltils or a specific module within

Parameters:
- **`module`** str = None – The name of module to revert the settings for

Raisable exceptions:
- **`ValueError`** – Input parameter is invalid

Return type: **None** <br>
Returns: **Nothing** <br><br>

**`clearData()`** <br>
Clear the cache and config of tooltils

Parameters:
- None

Return type: **None** <br>
Returns: **Nothing** <br><br>

**`deleteData()`** <br>
Delete the data file for a specific tooltils version or all present

Parameters:
- **`version`** str = None – The version to be erased

Raisable exceptions:
- **`TypeError`** – Input parameter type is incorrect
- **`ValueError`** – Input parameter is invalid
- **`FileNotFoundError`** – Unable to locate input parameter file

Return type: **None** <br>
Returns: **Nothing** <br><br>

**`logger`** <br>
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

Return type: **tooltils.info.logger** <br>
Returns: **Logger instance** <br><br>

## <span style="font-family: Trebuchet MS;">Config</span>

**Default Settings**

The default structure for the config is as follows:

```json
"errors": {},
"global": {
    "config": {
         "runConfigMethodAlways": false,
         "configMethodCheck": 20
    } 
},
"info": {},
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

To set a setting value as a method, you first need to set the value to a string, then add the **"`$f`"** keyword, afterwards insert a space and the method. If an error was raised or the function did not execute properly the config value will become None. Keyword arguments are not supported as of yet. If you wish to use the keyword without insitigating a method, you can backslash each character (**"`\$\f`"**). To use a tooltils method follow the below example with each module.. You may use any tooltils method available. Built-in Python functions will work but not those from the standard library:

```json
"requests": {
    "defaultVerificationMethod": "$f tooltils.requests.verifiable()"
},
```

The above example sets the verify parameter default in `requests` methods to the result of `tooltils.requests.verifiable()`, automatically preventing any kind of SSL error. Though this is not good practice as the certificate should be verified by default for security purposes. See as to why implementing a config to have the option of doing this is a good idea for people who seek this capability.

```jsonc
"requests": {
    "defaultHttpVerificationMethod": "$f any()", // builtin function any
    "defaultVerificationMethod": "$f tooltils.sys.getCurrentWifiName()" // tooltils function
}
```

**Note: As a limitation to prevent tooltils from being slowed, the parameter `runConfigMethodAlways: false` exists in the global config.**
