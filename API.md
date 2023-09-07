# &nbsp;<span style="font-family: Trebuchet MS;">tooltils – api</span>

## &nbsp;<span style="font-family: Trebuchet MS;">Tooltils</span>

&nbsp; *Methods that don't need their own directory* <br><br>

&nbsp; Properties:
- **`colours`** dict – List of the main colours as ANSI integer codes
- **`months`** list – List of months in the year
- **`python_version`** str – Current Python interpreter version
- **`platform`** str – Name of current operating system

<br>

&nbsp; Methods:

&nbsp; **`length(file)`** <br>
&nbsp; Get the length of a wave file in seconds

&nbsp; Parameters:
- **`file`** str - Path to WAVE file

&nbsp; Returns: **Length of file in seconds** <br>
&nbsp; Return type: **float** <br><br>

&nbsp; **`get(url)`** <br>
&nbsp; Send a GET request

&nbsp; *The same as `tooltils.requests.get()`*

&nbsp; Parameters:
- **`url`** str | bytes – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request(Added to url)
- **`headers`** dict = None – Headers to add to the request(Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file(Will use default if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`post(url)`** <br>
&nbsp; Send a POST request

&nbsp; *The same as `tooltils.requests.post()`*

&nbsp; Parameters:
- **`url`** str | bytes – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request(Encoded in the request data)
- **`headers`** dict = None – Headers to add to the request(Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file(Will use default if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`download(url)`** <br>
&nbsp; Download a file onto the disk

&nbsp; *The same as `tooltils.requests.download()`*

&nbsp; Parameters:
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
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A class method** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`style(text)`** <br>
&nbsp; Create text in the specified colour and or style

&nbsp; Parameters:
- **`text`** str – Text to style
- **`colour`** str = '' – Colour to use
- **`fill`** bool = False – Whether to fill the text background with the specified colour
- **`bold`** bool = False – Whether to make the text bold
- **`italic`** bool = False – Whether to italicise the text
- **`crossed`** bool = False – Whether to cross the text
- **`underline`** bool = False – Whether to underline the text
- **`double_underline`** bool = False – Whether to double underline the text
- **`flush`** bool = True – Whether to apply a fix to the terminal because of a display bug

&nbsp; Returns: **Styled text** <br>
&nbsp; Return type: **str** <br><br>

&nbsp; **`halve(text)`** <br>
&nbsp; Return the halves of a string

&nbsp; Parameters:
- **`text`** str – Text to halve

&nbsp; Returns: **Both halves of text** <br>
&nbsp; Return type: **list** <br><br>

&nbsp; **`cipher(text, shift)`** <br>
&nbsp; A simple caeser cipher

&nbsp; Parameters:
- **`text`** str – Text to cipher
- **`shift`** int – Amount of letters to shift in the alphabet

&nbsp; Returns: **Ciphered text** <br>
&nbsp; Return type: **str** <br><br>

&nbsp; **`call(cmds)`** <br>
&nbsp; Call a system command and return the exit code

&nbsp; *The same as `tooltils.sys.call()`*

&nbsp; Parameters:
- **`cmds`** list | str – Commands/program/arguments to call
- **`shell`** bool = False – Whether to use the shell
- **`timeout`** int = 10 – How long the subprocess should last
- **`check`** bool = False – Whether to raise an error if the returncode is not 0

&nbsp; Returns: **Exit code of command** <br>
&nbsp; Return type: **int** <br><br>

&nbsp; **`cstrip(text, chars)`** <br>
&nbsp; Strip a string or list of characters from some text

&nbsp; Parameters:
- **`text`** str – Text to be replaced
- **`chars`** str | list – List of characters to strip

&nbsp; Returns: **Stripped text** <br>
&nbsp; Return type: **str** <br><br>

&nbsp; **`mstrip(text, charlist)`** <br>
&nbsp; Strip/change a dictionary of string pairs from some text

&nbsp; Parameters:
- **`text`** str – Text to be replaced
- **`chars`** dict – List of characters to strip/change

&nbsp; Returns: **Changed text** <br>
&nbsp; Return type: **str** <br><br>

&nbsp; **`date()`** <br>
&nbsp; Convert epoch to human formatted date

&nbsp; Parameters:
- **`epoch`** float = time.time() – Epoch in seconds to use
- **`timezone`** str = ‘local’ – Timezone offset to use (e.g. ‘+11:00’, local means your current timezone, gm or '00:00' means no offset time)
- **`format`** str = ‘standard’ – How to format the output date ('standard', 'fancy')

&nbsp; Returns: **Formatted date** <br>
&nbsp; Return type: **str** <br><br>

&nbsp; **`epoch(date)`** <br>
&nbsp; Convert a formatted date to an epoch value

&nbsp; Parameters:
- **`date`** str – The formatted date to convert
- **`seconds`** bool = True – Whether to return the epoch in seconds or milliseconds

&nbsp; Returns: **Epoch in seconds or milliseconds of the input date** <br>
&nbsp; Return type: **int** <br><br>

&nbsp; **`createfile(name)`** <br>
&nbsp; Create a file with the specified name

&nbsp; Parameters:
- **`name`** str – The name and or extension of the file
- **`extension`** str = None – The extension of the file
- **`data`** str = None – The data to write to the file
- **`keep`** bool = False – Whether to keep the file open and return the TextIOWrapper class

&nbsp; Returns: **Nothing or the file class** <br>
&nbsp; Return type: **None | TextIOWrapper** <br><br>

&nbsp; **`squeeze(array)`** <br>
&nbsp; Remove empty or the specified item(s) from an array

&nbsp; Parameters:
- **`array`** list | tuple | set | dict – The array to change
- **`item`** Any | None – The item to remove

&nbsp; Returns: **Edited array** <br>
&nbsp; Return type: **Same as input type** <br><br>

&nbsp; **`reverseDictSearch(array, value)`** <br>
&nbsp; Find the unknown key(s) of a value in a dictionary

&nbsp; Parameters:
- **`array`** dict – The dictionary to search
- **`value`** Any – The value to find the key(s) for

&nbsp; Returns: **Key(s) found | Raise an error if no key is found** <br>
&nbsp; Return type: **Any** <br><br>

## &nbsp; <span style="font-family: Trebuchet MS;">Sys</span>

&nbsp; *System specific methods and information*

&nbsp; **`exit(details)`** <br>
&nbsp; Exit the current thread with details

&nbsp; Parameters:
- **`details`** str = ‘’ – Text to print before exiting
- **`code`** int = 0 – Exit code to use

&nbsp; Returns: **Nothing** <br>
&nbsp; Return type: **NoReturn** <br><br>

&nbsp; **`clear()`** <br>
&nbsp; OS independent terminal clearing

&nbsp; No parameters

&nbsp; Returns: **None** <br>
&nbsp; Return type: **NoneType** <br><br>

&nbsp; **`system(cmds)`** <br>
&nbsp; Call a system program and return some information

&nbsp; Parameters:
- **`cmds`** list | str – Commands to call
- **`shell`** bool = False – Whether to use the shell(terminal)
- **`timeout`** int = 10 – How long the process should last
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`clean`** bool = False – Whether to remove empty values from the output as a list
- **`capture`** bool = True – Whether to capture the output of the program/command

&nbsp; shell_response:
- **`args`** list | str – Arguments that were called
- **`code`** int – Exit code of command
- **`raw`** bytes – Raw byte text of stdout output
- **`output`** list[str] – A list containing each line of output as a string

&nbsp; Returns: **Response Class** <br>
&nbsp; Return type: **tooltils.sys.shell_response** <br><br>

&nbsp; **`check(cmds)`** <br>
&nbsp; Call a system program and return the output

&nbsp; Parameters:
- **`cmds`** list | str – Commands to call
- **`shell`** bool = False – Whether to use the shell(terminal)
- **`timeout`** int = 10 – How long the process should last
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`raw`** bool = False – Whether to return raw bytes output
- **`clean`** bool = False – Whether to remove empty values from the output as a list

&nbsp; Returns: **List or bytes containing stdout output** <br>
&nbsp; Return type: **list | bytes** <br><br>

&nbsp; **`call(cmds)`** <br>
&nbsp; Call a system program and return the exit code

&nbsp; Parameters:
- **`cmds`** list | str – Commands to call
- **`shell`** bool = False – Whether to use the shell(terminal)
- **`timeout`** int = 10 – How long the process should last
- **`check`** bool = False – Whether to raise an error if the returncode is not 0
- **`clean`** bool = False – Whether to remove empty values from the output as a list

&nbsp; Returns: **Exit code of command** <br>
&nbsp; Return type: **int** <br><br>

&nbsp; **`pID(name)`** <br>
&nbsp; Get the process ID of an app or binary by name

&nbsp; *May return a list if multiple processes are found*

&nbsp; Parameters:
- **`name`** str – Name of app or binary

&nbsp; Returns: **Process ID or list of found IDs** <br>
&nbsp; Return type: **list | int** <br><br>

## &nbsp; <span style="font-family: Trebuchet MS;">Sys.info</span>

&nbsp; *Identifying system information*

&nbsp; <u>*Note: Some variables may be None or empty if the value could not be determined*</u>

&nbsp; Properties:
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
- **`serial_number`** str – The identifiable code or tag string of your computer
- **`boot_drive`** str – The location of the boot drive currently being used on your computer

<br>

## &nbsp; <span style="font-family: Trebuchet MS;">Requests</span>

&nbsp; *If a property has a star sign in front of it, it can have a value of none*

&nbsp; url_response:
- **`verified`** bool – Whether the request used https or http
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
- **`code`** int – The status code of the request
- **`reason`** str – The reason of the request's status code
- **`status_code`** str – The status code and reason of the requets combined
- **`*text`** str – The text of the request response
- **`*raw`** bytes – The encoded text of the request response
- **`*html`** str – The html of the request url (if applicable)
- **`*path`** str – The output path of the file if the download method was used
- **`*json`** dict – The json of the request response containing all the data
- **`_rdata`** urllib.request._Urlopenret – The urllib base response class

&nbsp; Properties:
- **`status_codes`** dict – List of official valid HTTP response status codes (100-505)
- **`unverified`** SSLContext – An unverified default SSLContext instance to use in `urlopen`
- **`verified`** SSLContext – A verified default SSLContext instance to use in `urlopen`

&nbsp; Methods:

&nbsp; **`ctx()`** <br>
&nbsp; Create a custom SSLContext instance

&nbsp; Parameters:
- **`verify`** bool = True – Whether to check hostname and verify SSL request
- **`cert`** str = None – Location of certificate.pem file

&nbsp; Returns: **An SSLContext instance** <br>
&nbsp; Return type: **ssl.SSLContext** <br><br>

&nbsp; **`connected()`** <br>
&nbsp; Return whether the system has a valid internet connection

&nbsp; No Parameters

&nbsp; Returns: **The result of the internet test** <br>
&nbsp; Return type: **bool** <br><br>

&nbsp; **`prep_url(url)`** <br>
&nbsp; Configure a URL making it viable for requests

&nbsp; Parameters:
- **`url`** str | bytes – URL to configure
- **`data`** dict = {} – Data to include in the URL
- **`https`** bool = True – Whether to guess https as the protocol if not specified
- **`order`** bool = False – Whether to alphabetically order the url items

&nbsp; Returns: **Corrected URL** <br>
&nbsp; Return type: **str** <br><br>

&nbsp; **`where()`** <br>
&nbsp; Return default certificate file and path locations used by Python

&nbsp; No parameters

&nbsp; Returns: **Class method** <br>
&nbsp; Return type: **tooltils.requests.certifs** <br>

&nbsp; **`Redirects()`** <br>
&nbsp; A handler to stop redirects in urllib

&nbsp; You can install this as an opener to use in urllib <br>
&nbsp; to prevent redirects by the requested url <br><br>

&nbsp; **`request(url, method)`** <br>
&nbsp; Prepare and send a http request

&nbsp; Parameters:
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
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`get(url)`** <br>
&nbsp; Send a GET request

&nbsp; Parameters:
- **`url`** str | bytes – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request(Added to url)
- **`headers`** dict = None – Headers to add to the request(Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file(Will use default if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`post(url)`** <br>
&nbsp; Send a POST request

&nbsp; Parameters:
- **`url`** str | bytes – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request(Added to url)
- **`headers`** dict = None – Headers to add to the request(Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file(Will use default if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`download(url)`** <br>
&nbsp; Download a file onto the disk

&nbsp; Parameters:
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
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`header(url)`** <br>
&nbsp; Send a HEADER request

&nbsp; Parameters:
- **`url`** str | bytes – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request(Added to url)
- **`headers`** dict = None – Headers to add to the request(Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file(Will use default if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`put(url)`** <br>
&nbsp; Send a PUT request

&nbsp; Parameters:
- **`url`** str | bytes – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request(Added to url)
- **`headers`** dict = None – Headers to add to the request(Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file(Will use default if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`patch(url)`** <br>
&nbsp; Send a PATCH request

&nbsp; Parameters:
- **`url`** str | bytes – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request(Added to url)
- **`headers`** dict = None – Headers to add to the request(Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file(Will use default if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

&nbsp; **`delete(url)`** <br>
&nbsp; Send a DELETE request

&nbsp; Parameters:
- **`url`** str | bytes – URL to send the request to
- **`auth`** tuple = None – Authentication in a username password pair
- **`data`** dict = None – JSON data to send with the request(Added to url)
- **`headers`** dict = None – Headers to add to the request(Overwrites defaults if the same are present)
- **`cookies`** dict = None – Cookies to include in the headers
- **`cert`** str = None – Path to certificate.pem file(Will use default if None)
- **`timeout`** int = 10 – When to terminate the request
- **`encoding`** str = ‘utf-8’ – Codec used to decode the response text
- **`mask`** bool = False – Decide whether to use an anonymous user agent header
- **`agent`** str = None – Overwrite for the agent header
- **`verify`** bool = True – Whether to check the hostname and verify the request
- **`redirects`** bool = True – Whether to allow redirects

&nbsp; Returns: **A request class** <br>
&nbsp; Return type: **tooltils.requests.url_response** <br><br>

## &nbsp; <span style="font-family: Trebuchet MS;">Errors</span>

&nbsp; *Package specific exceptions*

&nbsp; **`TooltilsError`** <br>
&nbsp; Base class for tooltils specific errors <br><br>

&nbsp; **`ShellCodeError`** <br>
&nbsp; Shell command return non-zero exit code

&nbsp; Parameters:
- **`code`** int = -1 – The non-zero error code returned
- **`message`** str = ‘’ – The message to print instead of the code message

&nbsp; Return type: **str** <br>
&nbsp; Returns:
- Default Message: **"Shell command returned non-zero exit code"**
- Message with code: **"Shell command returned non-zero exit code <i>[code]</i>"**
- Specified Message <br><br>

&nbsp; **`ShellTimeoutExpired`** <br>
&nbsp; Shell command timed out

&nbsp; Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

&nbsp; Return type: **str** <br>
&nbsp; Returns:
- Default Message: **"Shell command timed out"**
- Specified Message <br><br>

&nbsp; **`ShellCommandError`** <br>
&nbsp; Shell command exited while in process

&nbsp; Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

&nbsp; Return type: **str** <br>
&nbsp; Returns:
- Default Message: **"Shell command exited while in process"**
- Specified Message <br><br>

&nbsp; **`ShellCommandNotFound`** <br>
&nbsp; Unable to locate shell command or program

&nbsp; Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

&nbsp; Return type: **str** <br>
&nbsp; Returns:
- Default Message: **"Unable to locate shell command or program"**
- Specified Message <br><br>

&nbsp; **`ConnectionError`** <br>
&nbsp; Connection to URL failed

&nbsp; Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

&nbsp; Return type: **str** <br>
&nbsp; Returns:
- Default Message: **"Connection to URL failed"**
- Specified Message <br><br>

&nbsp; **`ConnectionTimeoutExpired`** <br>
&nbsp; Request read timeout expired

&nbsp; Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

&nbsp; Return type: **str** <br>
&nbsp; Returns:
- Default Message: **"Request read timeout expired"**
- Specified Message <br><br>

&nbsp; **`StatusCodeError`** <br>
&nbsp; URL response returned non 200s status code

&nbsp; Parameters:
- **`code`** int = 0 – The status code returned by the response
- **`reason`** str = ‘’ – The reason paired with the status code

&nbsp; Return type: **str** <br>
&nbsp; Returns:
- Default Message: **"URL response returned non 200s status code"**
- Specified Message <br><br>

&nbsp; **`UnicodeDecodeError`** <br>
&nbsp; Unable to decode text input

&nbsp; *Even though there is a class for this in python already, it requires more details so this simplified version is convenient*

&nbsp; Parameters:
- **`message`** str = ‘’ – The text to print instead of the default message

&nbsp; Return type: **str** <br>
&nbsp; Returns:
- Default Message: **"Unable to decode text input"**
- Specified Message
