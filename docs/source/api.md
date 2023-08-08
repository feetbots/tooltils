# Tooltils Interface

## Documentation

The docs are currently in heavy work this is just a temporary write over.

### Tooltils

Methods that dont need it's own directory

Properties:

- **styles** dict - List of supported coloured ASCII codes
- **months** list - List of months in the year
- **python_version** str - Current Python interpreter version

Methods:

length(file)
Get the length of a wave file in seconds

Parameters:

- **file** str - Path to WAVE file

Returns: Length of file in seconds
Return type: float

get(url)
Send a GET request

The same as tooltils.requests.get()

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

post(url)
Send a POST request

The same as tooltils.requests.post()

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Encoded in the request data)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

download(url)
Download a file onto the disk

The same as tooltils.requests.download()

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **file_name** str = None - Path to download the file(Will use URL file name if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

style(text)
Return text in the specified style

Parameters:

- **text** str - Text to style
- **style** str = 'white' - Colour or font to use
- **bold** bool = False - Whether to make the text bold
- **flush** bool = True - Whether to call '' in the shell to make sure the text shows properly

Returns: Styled text
Return type: str

halve(text)
Return the halves of a string

Parameters:

- **text** str - Text to halve

Returns: Both halves of text
Return type: list

cipher(text, shift)
A simple caeser cipher

Parameters:

- **text** str - Text to cipher
- **shift** int - Amount of letters to shift in the alphabet

Returns: Ciphered text
Return type: str

call(cmds)
Call a system command and return the exit code

The same as tooltils.sys.call()

Parameters:

- **cmds** list | str - Commands/program/arguments to call
- **shell** bool = False - Whether to use the shell
- **timeout** int = 10 - How long the subprocess should last
- **check** bool = False - Whether to raise an error if the returncode is not 0

Returns: Exit code of command
Return type: int

cstrip(text, chars)
Strip a string or list of characters from some text

Parameters:

- **text** str - Text to be replaced
- **chars** str | list - List of characters to strip

Returns: Stripped text
Return type: str

mstrip(text, charlist)
Strip/change a dictionary of string pairs from some text

Parameters:

- **text** str - Text to be replaced
- **chars** dict - List of characters to strip/change

Returns: Changed text
Return type: str

date()
Convert epoch to human formatted date

Parameters:

- **epoch** float = time.time() - Epoch in seconds to use
- **timezone** str = 'local' - Timezone offset to use (e.g. '+11:00', local means your current timezone)
- **format** int = 1 - How to format the output date (1 = compact, 2 = fancy)

Returns: Formatted date
Return type: str

epoch(date)
Convert a formatted date to an epoch value

Parameters:

- **date** str - The formatted date to convert

Returns: Converted date
Return type: int

createfile(name)
Create a file with the specified name

Parameters:

- **name** str - The name and or extension of the file
- **extension** str = None - The extension of the file
- **data** str = None - The data to write to the file
- **keep** bool = False - Whether to keep the file open and return the TextIOWrapper class

Returns: Nothing or the file class
Return type: None | TextIOWrapper

squeeze(array)
Remove empty or the specified item(s) from an array

Parameters:

- **array** list | tuple | set | dict - The array to change
- **item** Any | None - The item to remove

Returns: Edited array
Return type: Same as input type (list | tuple | set | dict)

### Sys

System specific methods and information

exit(details)
Exit the current thread with details

Parameters:

- **details** *str - String(s) to print before exiting
- **code** int = 0 — Exit code to use
- **sep** str = ' ' - Detail string(s) seperator
- **end** str = '\n' - Detail string(s) end character(s)
  
Returns: Nothing
Return type: NoReturn

clear()
OS independent terminal clearing

No parameters

Returns: None
Return type: NoneType

system(cmds)
Call a system program and return some information

Parameters:

- **cmds** list | str - Commands to call
- **shell** bool = False - Whether to use the shell(terminal)
- **timeout** int = 10 - How long the process should last
- **check** bool = False - Whether to raise an error if the returncode is not 0

shell_response:

- **args** list | str - Arguments that were called
- **code** int - Exit code of command
- **raw** bytes - Raw byte text of stdout output
- **text** list - A list containing each line of output as a string

Returns: Response Class
Return type: tooltils.sys.shell_response

check(cmds)
Call a system program and return the output

Parameters:

- **cmds** list | str - Commands to call
- **shell** bool = False - Whether to use the shell(terminal)
- **timeout** int = 10 - How long the process should last
- **check** bool = False - Whether to raise an error if the returncode is not 0
- **raw** bool = False - Whether to return raw bytes output

Returns: List or bytes of stdout output
Return type: list | bytes

call(cmds)
Call a system program and return the exit code

Parameters:

- **cmds** list | str - Commands to call
- **shell** bool = False - Whether to use the shell(terminal)
- **timeout** int = 10 - How long the process should last
- **check** bool = False - Whether to raise an error if the returncode is not 0

Returns: Exit code of command
Return type: int

pID(name)
Get the process ID of an app or binary by name

May return a list if multiple processes are found.

Parameters:

- **name** str - Name of app or binary

Returns: Process ID or list of found IDs
Return type: list | int

### Sys.info

Identifying system information

Some variables may be None or empty if the value could not be determined.

Properties:

- **macOS_releases** dict[str, str] - List of all current MacOS versions
- **python_version** str - Current Python interpereter version
- **python_version_tuple** tuple - Current Python interpereter version seperated into major, minor, patch
- **name** str - The network name of computer
- **bitsize** int - Determine if your computer is 32 or 64-bit
- **interperter** str - Location of current Python interpereter
- **platform** str - Name of current operating system
- **detailed_platform** str - Detailed name of current operating system
- **cpu** str - Name of the currently in use cpu of your computer
- **arch** str - Computer architecture
- **platform_version** tuple[str] - Version number and or name of current OS
- **model** str - The model or manufacturer of your computer
- **cores** int - The amount of cores in your computer cpu
- **ram** int - The amount of ram in megabytes in your computer
- **serial_number** str - The identifiable code or tag string of your computer
- **boot_drive** str - The location of the boot drive currently being used on your computer

### Requests

Properties:

- **status_codes** dict - List of status codes and corresponding reasons

Methods:

ctx()
Create a custom SSLContext instance

Parameters:

- **verify** bool = True - Whether to check hostname and verify SSL request
- **cert** str = None - Location of certificate.pem file

Returns: An SSLContext instance
Return type: ssl.SSLContext

prep_url(url)
Configure a URL making it viable for requests

Parameters:

- **url** str | bytes - URL to configure
- **data** dict = {} - Data to include in the URL
- **https** bool = True - Whether to guess https as the protocol if not specified

Returns: Corrected URL
Return type: str

where()
Return default certificate file and path locations used by Python

No parameters

Returns: Class method
Return type: tooltils.requests.certifs

Redirects()
A handler to stop redirects in urllib

You can install this as an opener to use in urllib

request(url, method)
Prepare and send a http request

Parameters:

- **url** str | bytes - URL to send the request to
- **method** str - Http method to use
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **file_name** str = None - Path to download the file(Will use URL file name if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.request

get(url)
Send a GET request

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

post(url)
Send a POST request

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

post(url)
Send a POST request

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

download(url)
Download a file onto the disk

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **file_name** str = None - Path to download the file(Will use URL file name if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

put(url)
Send a PUT request

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

patch(url)
Send a PATCH request

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

header(url)
Send a HEADER request

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

delete(url)
Send a DELETE request

Parameters:

- **url** str | bytes - URL to send the request to
- **auth** tuple = None - Authentication in a username password pair
- **data** dict = None - JSON data to send with the request(Added to url)
- **headers** dict = None - Headers to add to the request(Overwrites defaults if the same are present)
- **cookies** dict = None - Cookies to include in the headers
- **cert** str = None - Path to certificate.pem file(Will use default if None)
- **timeout** int = 10 - When to terminate the request
- **encoding** str = 'utf-8' - Codec used to decode the response text
- **mask** bool = False - Decide whether to use an anonymous user agent header
- **agent** str = None - Overwrite for the agent header
- **verify** bool = True - Whether to check the hostname and verify the request
- **redirects** bool = True - Whether to allow redirects

Returns: A class method
Return type: tooltils.requests.url_response

Welp, looks like you've reached the end!
