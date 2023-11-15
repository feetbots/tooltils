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

Returns: **Length of file in seconds** <br>
Return type: **float** <br><br>

**`style(text)`** <br>
Create text in the specified colour and or style

Parameters:
- **`text`** str – Text to style
- **`colour`** str = '' – Colour to use
- **`fill`** bool = False – Whether to fill the text background with the specified colour
- **`bold`** bool = False – Whether to make the text bold
- **`italic`** bool = False – Whether to italicise the text
- **`crossed`** bool = False – Whether to cross the text
- **`underline`** bool = False – Whether to underline the text
- **`double_underline`** bool = False – Whether to double underline the text
- **`flush`** bool = True – Whether to apply a fix to the terminal because of a display bug

Returns: **Styled text** <br>
Return type: **str** <br><br>

**`halve(object)`** <br>
Return the halves of a string or list

Parameters:
- **`text`** str | list – Object to halve

Returns: **Either half of object** <br>
Return type: **list** <br><br>

**`cipher(text, shift)`** <br>
A simple caeser cipher

Parameters:
- **`text`** str – Text to cipher
- **`shift`** int – Amount of letters to shift in the alphabet

Returns: **Ciphered text** <br>
Return type: **str** <br><br>

**`mstrip(text, values)`** <br>
Change some text from a dictionary pair of values

Parameters:
- **`text`** str – Text to be changed
- **`values`** dict – List of characters to change

Returns: **Changed text** <br>
Return type: **str** <br><br>

**`date()`** <br>
Convert epoch to human formatted date

Parameters:
- **`epoch`** float = time.time() – Epoch in seconds to use
- **`timezone`** str = ‘local’ – Timezone offset to use (e.g. ‘+11:00’, local means your current timezone, gm means no offset time)
- **`format`** str = ‘standard’ – How to format the output date ('standard', 'fancy')

Returns: **Formatted date** <br>
Return type: **str** <br><br>

**`epoch(date)`** <br>
Get epoch from a formatted date (`strftime` etc.)

Parameters:
- **`date`** str – The formatted date to convert

Returns: **Epoch in seconds of the input date** <br>
Return type: **int | float** <br><br>

**`squeeze(array)`** <br>
Remove empty or the specified item(s) from an array

Parameters:
- **`array`** list | tuple | set | dict – The array to change
- **`item`** Any | None – The item to remove

Returns: **Edited array** <br>
Return type: **Same as input type** <br><br>

**`reverseDictSearch(array, value)`** <br>
Find the unknown key(s) of a value in a dictionary

Parameters:
- **`array`** dict – The dictionary to search
- **`value`** Any – The value to find the key(s) for

Returns: **Key(s) found | Raise an error if no key is found** <br>
Return type: **Any** <br><br>

**`getArrayValues(array)`** <br>
Recursively obtain all of the values of any keys or items within an array

Parameters:
- **`array`** list | tuple | dict – The array to search

Returns: **All base-level values in the array (recursed)** <br>
Return type: **tuple** <br><br>

**`timeTest(method, method2)`** <br>
Run two different methods x amount of times, sum then divide to estimate accurate run-time

Parameters:
- **`method`** function – The first method to test
- **`method2`** function – The second method to test
- **`params`** dict = {} – Kwargs for the first method
- **`params2`** dict = {} – Kwargs for the second method
- **`accuracy`** int = 10 – The amount of times to test each method

Returns: **Average run-time for each method (method, method2)** <br>
Return type: **tuple** <br><br>

**`varName(**vars)`** <br>
Get the namespace name of one or more variables

Parameters:
- **`**vars`** dict – The variables to get the name for

Usage:
- Input a variable that has been declared earlier as the kward argument, then put that variable as the value of the argument. Example `varName(data=data)`

Returns: **Names of variables input** <br>
Return type: **str | list[str]** <br><br>

**`interpreter(file)`** <br>
Custom top-level Python interpereter to add niche features from other languages

Parameters:
- **`file`** str – The Python file to convert
- **`output`** str = ‘%(name)s.interpereted.py’ – The name of the converted Python file
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

Returns: **Interpreter instance** <br>
Return type: **tooltils.interpreter** <br><br>

## <span style="font-family: Trebuchet MS;">Sys</span>

*System specific methods and information*

**`exit(details)`** <br>
Exit the current thread with details

Parameters:
- **`details`** str = ‘’ – Text to print before exiting
- **`code`** int = 0 – Exit code to use

Returns: **Nothing** <br>
Return type: **NoReturn** <br><br>

**`clear()`** <br>
OS independent terminal clearing

No parameters

Returns: **None** <br>
Return type: **None** <br><br>

**`system(cmds)`** <br>
Call a system program and return some information

Parameters:
- **`cmds`** str | list – Commands/program to call
- **`shell`** bool = False – Whether to use the shell (sh)
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

Returns: **A system class** <br>
Return type: **tooltils.sys.system** <br><br>

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

Returns: **List of lines or bytes containing stdout output** <br>
Return type: **str | bytes | list[str]** <br><br>

**`call(cmds)`** <br>
Call a system program and return the exit code

Parameters:
- **`cmds`** str | list – Commands to call
- **`shell`** bool = False – Whether to use the shell (sh)
- **`timeout`** int = 10 – How long the process should last
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`print`** bool = True – Whether command/program can print to stdout

Returns: **Exit code of program call** <br>
Return type: **int** <br><br>

**`pID(name)`** <br>
Get the process ID of an app or binary by name

*May return a list if multiple processes are found*

Parameters:
- **`name`** str – Name of app or binary

Returns: **Process ID or list of found IDs** <br>
Return type: **int | list[int]** <br><br>

**`getCurrentWifiName()`** <br>
Get the currently connected wifi name

*Will return None if not connected or nothing was found*

Parameters:
- None

Returns: **Wifi Name** <br>
Return type: **str | None** <br><br>

## <span style="font-family: Trebuchet MS;">Sys.info</span>

*Identifying system information*

Properties:
- **`macOS_releases`** dict[str, str] – List of all current MacOS versions
- **`python_version`** str – Current Python interpereter version
- **`python_version_tuple`** tuple – Current Python interpereter version seperated into major, minor, patch
- **`name`** str – The network name of computer
- **`bitsize`** int – Whether the current Python interpreter computer is 32 or 64-bit
- **`interpreter`** str – Location of current Python interpereter
- **`platform`** str – Name of current operating system
- **`detailed_platform`** str – Detailed name of current operating system
- **`cpu`** str – Name of the currently in use cpu of your computer
- **`arch`** str – Computer architecture
- **`platform_version`** tuple[str] – Version number and or name of current OS
- **`model`** str – The model or manufacturer of your computer
- **`cores`** int – The amount of cores in your computer cpu
- **`ram`** int – The amount of ram in megabytes in your computer
- **`manufacturer`** str – The organisation or company that created your computer
- **`serial_number`** str – The identifiable code or tag string of your computer (This is unobtainable without sudo on Linux)
- **`boot_drive`** str – The location of the boot drive currently being used on your computer

<br>

## <span style="font-family: Trebuchet MS;">Requests</span>

*Internet requesting access methods*

Properties:
- **`status_codes`** dict – List of official valid HTTP response status codes (100-511)

Methods:

**`ctx()`** <br>
Create a custom SSLContext instance

Parameters:
- **`verify`** bool = True – Whether to check hostname and verify SSL request
- **`cert`** str = None – Location of certificate.pem file

Returns: **An SSLContext instance** <br>
Return type: **ssl.SSLContext** <br><br>

**`connected()`** <br>
Get the connectivity status of the currently connected wifi network

*When caching is enabled, it will used the cached value 50 times by default and then create a new one and cache that instead.*

No Parameters

Returns: **The result of the internet test** <br>
Return type: **bool** <br><br>

**`prep_url(url)`** <br>
Configure a URL making it viable for requests

Parameters:
- **`url`** str | bytes – URL to configure
- **`data`** dict = {} – Data to include in the URL
- **`https`** bool = True – Whether to guess https as the protocol if not specified
- **`order`** bool = False – Whether to alphabetically order the url items

Returns: **Corrected URL** <br>
Return type: **str** <br><br>

**`where()`** <br>
Return default certificate file and path locations used by Python

No parameters

Returns: **Class method** <br>
Return type: **tooltils.requests.certifs** <br>

**`verifiable()`** <br>
Determine whether requests can be verified with a valid ssl certificate on the current connection

*This function will use the cached value 50 times by default and then create a new one and cache that instead.*

No parameters

Returns: **Whether requests can use a valid ssl certificate** <br>
Return type: **bool** <br>

**`NoRedirects()`** <br>
An opener to prevent redirects in urllib requests

You can install this as an opener to use in urllib to prevent redirects by the requested url <br><br>

**`request(url, method)`** <br>
Prepare and send a http[s] request

Parameters:
- **`url`** str – URL to send the request to
- **`method`** str – The http method to make the request with
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request (Added to url)
- **`headers`** dict = None – Headers to add to the request (Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file (Will use default if None)
- **`file_name`** str = None – Path to download the file (Will use URL file name if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

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
- **`sent`** bool – Whether the request has been used
- **`code`** int – The status code of the request
- **`reason`** str – The reason of the request's status code
- **`status_code`** str – The status code and reason of the requets combined
- **`*text`** str – The text of the request response
- **`*raw`** bytes – The encoded text of the request response
- **`*html`** str – The html of the request url (if applicable)
- **`*path`** str – The output path of the file if the download method was used
- **`*json`** dict – The json of the request response containing all the data
- **`rdata`** http.client.HTTPResponse – The http base response class containing all the data read

Return methods:
- **`.read()`** – Read the request file and return the raw data
- **`.readlines()`** list – Read the request file and return the data as a list split at every newline

Returns: **A request class** <br>
Return type: **tooltils.requests.request** <br><br>

**`get(url)`** <br>
Send a GET request

*Calls `.requests.request(method='GET', ...).send()` and returns the result*

**`post(url)`** <br>
Send a POST request

*Calls `.requests.request(method='POST', ...).send()` and returns the result*

**`download(url)`** <br>
Download a file onto the disk

*Calls `.requests.request(method='DOWNLOAD', ...).send()` and returns the result*
*This uses the `file_name` parameter aswell as any request ones*

Parameters:
- **`file_name`** str = None – Path to download the file (Will use URL file name if None)

**`head(url)`** <br>
Send a HEAD request

*Calls `.requests.request(method='HEAD', ...).send()` and returns the result*

**`put(url)`** <br>
Send a PUT request

*Calls `.requests.request(method='PUT', ...).send()` and returns the result*

**`patch(url)`** <br>
Send a PATCH request

*Calls `.requests.request(method='PATCH', ...).send()` and returns the result*

**`delete(url)`** <br>
Send a DELETE request

*Calls `.requests.request(method='DELETE', ...).send()` and returns the result*

## <span style="font-family: Trebuchet MS;">requests.http</span>

*Internet requesting access methods - http.client version (alpha)*

***Note: This version of the requests module has a few different features than the urllib implementation***

**`request(url)`** <br>
Prepare and send a http[s] request

Parameters:
- **`url`** str | bytes – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request (Added to url)
- **`headers`** dict = None – Headers to add to the request (Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file (Will use default if None)
- **`file_name`** str = None – Path to download the file (Will use URL file name if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to use SSL in the request
- **`redirects`** bool = True – Whether to allow redirects
- **`https`** bool = True – Whether https should be used in the request
- **`port`** int – The port to send the request from

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
- **`agent`** str – The user agent to send in the headers of the request
- **`headers`** dict – The data sent as the configuration of the request
- **`encoding`** str – The text encoding to use when decoding the response text
- **`url`** str – The configured url used to sent the request to
- **`sent`** bool – Whether the request has been used
- **`code`** int – The status code of the request
- **`reason`** str – The reason of the request's status code
- **`status_code`** str – The status code and reason of the requets combined
- **`*text`** str – The text of the request response
- **`*raw`** bytes – The encoded text of the request response
- **`*html`** str – The html of the request url (if applicable)
- **`*path`** str – The output path of the file if the download method was used
- **`*json`** dict – The json of the request response containing all the data
- **`rdata`** http.client.HTTPResponse – The http base response class containing all the data read

Return methods:
- **`.read()`** – Read the request file and return the raw data
- **`.readlines()`** list – Read the request file and return the data as a list split at every newline

Returns: **A request class** <br>
Return type: **tooltils.requests.http.request** <br><br>

**`get(url)`** <br>
Send a GET request

*Calls `.requests.http.request(method='GET', ...).send()` and returns the result*

**`post(url)`** <br>
Send a POST request

*Calls `.requests.http.request(method='POST', ...).send()` and returns the result*

**`download(url)`** <br>
Download a file onto the disk

*Calls `.requests.http.request(method='DOWNLOAD', ...).send()` and returns the result*
*This uses the `file_name` parameter aswell as any request ones*

Parameters:
- **`file_name`** str = None – Path to download the file (Will use URL file name if None)

**`head(url)`** <br>
Send a HEAD request

*Calls `.requests.http.request(method='HEAD', ...).send()` and returns the result*

**`put(url)`** <br>
Send a PUT request

*Calls `.requests.http.request(method='PUT', ...).send()` and returns the result*

**`patch(url)`** <br>
Send a PATCH request

*Calls `.requests.http.request(method='PATCH', ...).send()` and returns the result*

**`delete(url)`** <br>
Send a DELETE request

*Calls `.requests.http.request(method='DELETE', ...).send()` and returns the result*

## <span style="font-family: Trebuchet MS;">Errors</span>

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

Return type: **str** <br>
Returns:
- Default Message: **"Shell command returned non-zero exit code"**
- Message with code: **"Shell command returned non-zero exit code <i>[code]</i>"**
- Specified Message <br><br>

**`ShellTimeoutExpired`** <br>
Shell command timed out

Parent class: `SystemCallError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

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

**`NoHttpConnection`** <br>
No valid wifi connection could be found for the request

Parent class: `RequestError` <br>

Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

Return type: **str** <br>
Returns:
- Default Message: **"No valid wifi connection could be found for the request"**
- Specified Message <br><br>

## <span style="font-family: Trebuchet MS;">Info</span>

*General installation information*

Properties:
- **`author`** str – The creator of tooltils
- **`version`** str – The current installation version
- **`released`** str – The release date of the current installation
- **`lines`** lines – How many lines of code in this installation
- **`license`** str – The content of the currently used license
- **`description`** str – The short description of tooltils
- **`long_description`** str – The long description of tooltils (README.md)
- **`location`** str – The path of the current installation of tooltils

Methods:

**`clearCache`** <br>
Clear the file cache of tooltils or a specific module within

Parameters:
- **`module`** str = None – The name of module to clear the cache for

Returns: **Nothing** <br>
Return type: **None** <br><br>

**`clearConfig`** <br>
Revert the config of tooltils or a specific module within

Parameters:
- **`module`** str = None – The name of module to revert the settings for

Returns: **Nothing** <br>
Return type: **None** <br><br>

**`clearData`** <br>
Clear the cache and config of tooltils

No Parameters

Returns: **Nothing** <br>
Return type: **None** <br><br>

**`logger`** <br>
Create a logging instance for tooltils modules only

Parameters:
- **`module`** str = 'ALL' – The name of module to initiliase logging for
- **`level`** str | int | LoggingLevel = 'ALL' – The starting level of the logging range
- **`level2`** str | int | LoggingLevel = 'ALL' – The ending level of the logging range

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

Raiseable exceptions:
- **`TypeError`** – Input parameter types are incorrect
- **`ValueError`** – Input parameter is invalid

Returns: **Logger instance** <br>
Return type: **tooltils.info.logger** <br><br>

## <span style="font-family: Trebuchet MS;">Config</span>

*My smart thought process converted to text*

**Default Settings**

The default structure for the config is as follows:

```json
"errors": {},
"global": {},
"info": {},
"main": {
    "easyAccessMethods": true
},
"requests": {
    "verifiableCachingCheck": 50,
    "connectedCachingCheck": 50,
    "verifiableCaching": false,
    "connectedCaching": false
},
"sys.info": {},
"sys": {}
```

**Note: The text below was going to be for a feature to specify methods as config values but I am too dumb to lazy to implement it. Hopefully one day I am bothered.**

<br>

**Specifying methods**

To set a setting value as a method, you first need to set the value to a string, then add the **`$function`** keyword, afterwards insert a space and the method. You may not use tooltils methods/properties as circular imports will not work. Built-in Python functions will work but not those from the standard library. But you may use methods or properties from the same module that you are editing the config for:

```json
"requests": {
    "defaultVerificationMethod": "$function .verifiable()"
},
```

The above example sets the verify parameter default in `requests` methods to the result of `.requests.verifiable()`, automatically preventing any kind of SSL error. Though this is not good practice as the certificate should be verified by default for security purposes. See as to why implementing a config to have the option of doing this is a good idea for people who seek this capability.

**Note: As a limitation to prevent tooltils from being slowed or broken, two parameters in the global config have been added, `runConfigMethodAlways: false` and `checkMethodForSafety: true`. Only change these values if you really know what you are doing!**
