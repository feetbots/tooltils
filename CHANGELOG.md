# Version History

## 1.5.2 (16/11/2023)

Weird bug <br><br>

**Additions:**
- None

<br>

**Removals:**
- None

<br>

**Changes:**
- Modified `pyproject.toml` in hopes of fixing obscure bug where the contents of `src/` would be output into the main project file when installed

<br><br>

## 1.5.1 (16/11/2023)

Small update but I somehow always forget something<br><br>

**Additions:**
- Checker that will raise an error if `.requests.request.send()` is called again after it has already been called

<br>

**Removals:**
- `https` parameter from `.requests.ctx()` method

<br>

**Changes:**
- Modified the way all directory dependent files are accessed within `.info` to avoid errors

<br><br>

## 1.5.0 (15/11/2023)

The biggest update yet<br><br>

**Main Changes:**
- Added other system implementations of `.sys` modules (Windows and Linux)
- Fixed a shelf of `.requests` module bugs
- Implemented cache and config for global use
- Added the `interpreter()` project into the main module from version 1.0
- Added `NoHttpConnection` and `SSLCertificateFailed` exception classes for `.requests`
- Added the `requests.http` module implementing a bit more functionality but using the `http.client` module
- Adapted the way requests are sent in `.requests`, it now uses the initialise and send system (`.requests.request(url, method).send()`)
- Various optimisations

**Full Changelog:**

**Additions:**
- Linux implementation of `.sys.info` properties
- Windows and Linux implementation of `.sys.pID()` method
- Version history to `CHANGELOG.md` file
- Included `gzip.decompress()` function for the received data in `.requests` methods as the `gzip, deflate` header was provided, but not actually decoded, leading to substantial errors
- `verifiable()` method in `.requests` to determine whether requests can be verified with a valid ssl certificate on the current connection
- `.errors.SSLCertificateFailed` error class for `.requests` as it can be unclear to when a request couldn't be verified
- `.lower()` method to all string variables in tooltils for long term update stability
- Readded the mini interpreter module from version 1.0.0-beta into the main module, it was a cool small project that I'm still willing to continue
- Added `storage` folder containing `cache.json`, and `config.json`, two new features added to compliment new methods like `.requests.verifiable()`
- Documentation for the config on how to specify built-in Python and local tooltils methods as values for the settings
- `clearCache()`, `clearConfig()` and `clearData()` methods in `.info` to also compliment the two new features respectively
- Extensively tested each method and property to make sure there are no bugs before releasing
- Type check for `agent` property in `.requests` methods
- `install_opener(None)` method in `.requests.request` class to make sure that non tooltils requests using urllib aren't interfered with
- **"Accept: application/json"** header replacing **"\*/\*"** if the request method is POST or PUT
- Text describing the first method used to install tooltils in `README.md`
- Code using the `data` parameter in `.requests` methods were not using the type-checked version, this could have lead to unwanted errors, so it has been replaced
- Important note section in `README.md` to describe the current implementation of reading and writing to the cache and config
- Config feature for `.requests.connected()` for whether caching should be used
- Allow the `storage` folder to be deleted entirely or a file within and it being replaced with the default version. Essentially a force clear
- `location` property in `.info` for the path directory location
- Notes section in `CHANGELOG.md` versions starting now for anything that isn't important but is an oversight/limitation
- `getArrayValues()` method in the main module for recursively obtaining each base-level value from an array
- A potential feature could have allowed for a user to specify methods or variables as config values but I am too dumb right now to use my brain and figure out how to implement it. My first unfinished implementation is currently commented in `info.py`
- `getCurrentWifiName()` method in `.sys` as it was used in requests but would make more sense as a standalone function
- Stringify each cookie value before adding it to the request in `.requests`
- Code to catch `http.client.RemoteDisconnected` error in `.requests`
- More variable checking for what openers to use for the request in `.requests`, this also allows for none to be used, providing a small performance boost
- Ability to specify a message when raising the `.errors.TooltilsError` base class
- `requests.http` module implementation of `.requests` using the `http` Python library as a backend (alpha). This version boasts a nearly 2x speed increase in http requests and tiny boost with https used
- Docstrings to `cafile` and `capath` variables in `.requests.where()` `certifs` return class
- `NoHttpConnection` exception class for `.requests`
- Protocol set to **"https/1.1"** for `SSLContext` supplied to requests in `.requests.request()`
- Child baseclasses inheriting from `TooltilsException` in `.errors` to reflect the module an error is being raised from and similar
- Default error string to `TooltilsException` class in `.errors`
- Text showing what the parent class for each exception is in `.errors` in `API.md`
- `RequestError` exception for all package-specifc errors raised by `.requests.request()` method
- `SystemCallError` exception for all package-specifc errors raised by `.sys.system()` method
- `.read()` and `.readlines()` methods from `.requests.request()` into `API.md`
- `sent` variable to `.requests.request()` to determine whether the request has been used yet
- `timeTest()` method in the main module to test the average time taken to run two different methods 10 times (can be changed)
- `logger()` class method for tooltils only into `.info` as a wrapper for the `logging` module
- List of exception classes that methods may raise to `API.md`
- New properties to `.sys.system()` return class, being `list_text` and `clean_list_text`
- Parameter testing for all methods
- `print` parameter to `.sys.system()` method for if the output of the command/program should be written to stdout
- `varName()` method to the main module, allows you to obtain the name of a variable
 
<br>

**Removals:**
- `.requests.request()` headers were defined three times, and the last two were lazy only coming from the json response, so it would never work. Stripped the non-needed declarations
- `typing.MutableMapping` type anywhere as there is no way to convert a dict to MutableMapping, annoyingly
- Exclude `API.md`, `CHANGELOG.md` and `LICENSE` from the line counter in `.info` as they are not code
- `verified` and `unverified` properties from `.requests` as they were wifi dependent
- Cython package builder as it would require the `Cython` package which is not a standard module
- Awkward indentation before each line in the documentation, looked nicer but wasn't practical
- `cstrip()` method from the main file as you could do it easily with the `str.strip()` method
- `bytes` type hint from the `url` parameter in all `.requests` methods as there wasn't a reason to have it there in the first place
- All `__pycache__` folders each install so that the newest version is fresh without older optimisations taking up storage, though this will make the first run slower
- The ability to specify the URL as a file path in `.requests` `prep_url()` and `request()` methods
- Catch block code for `EOFError` and `KeyboardInterrupt` errors because they were non-request related
- `bytes` type hint from `.requests.request.raw` variable response class
- Easy access methods in the main module as they were unecessary performance decreasers
- `UnicodeDecodeError` from `.errors` because there is already an error in Python for this
- Error raising for `UnicodeDecodeError` because the message does not need to be changed in any way
- `createfile()` method from the main module as it was a useless wrapper

<br>

**Changes:**
- Edit link text in `README.md` as it did not work on github before
- Matched `info` property docstrings to that of the API's
- Reformatted older releases to match the most recent versions
- The way headers are processed in `.requests.request()`, now the `_UrlopenRet.getheaders()` method is used providing a reliable way of obtaining the request data
- Convert `license` property in `.info` to read from the license file instead of having direct text
- Rename 'Roadmap' in `README.md` to 'Planned Features'
- Reformatted the way the method is converted in `.requests` to make sure the correct headers are added depending on if it is post or put
- Reworded main module description in `API.md` to better describe it
- Convert `months` property in the main file to become an unusable constant because it only served as a helper variable
- Reword text in `README.md` describing the code block building tooltils using `!setup.py`
- Convert the installation methods in `README.md` to call the Python binary directly instead of Pip
- Use the `status_codes` property value from `.errors.StatusCodeError` instead of defining it again in `.requests`
- Updated `status_codes` property in `.requests` to the official list as specified by the [Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)
- Reworded `.requests.connected()` method docstring
- Compacted `.requests.request()` property testing to save around 20-30 lines
- Changed `.errors.StatusCodeError.status_codes` property to a dictionary as it would not return the correct value
- Encode the request JSON data before sending in `.requests`
- Reworded `.errors.StatusCodeError` exception docstring
- Change final line of code in the tooltils example in `README.md` to call the **'User-Agent'** header directly instead of the whole variable
- Update `pyproject.toml` Python versions to support 3.12 (possibly 3.13 in like nov or dec)
- Compacted each http method parameter list in `.requests` in `API.md` to save about 100 lines
- Correct the method called for `.requests.download()` as it would input **'FILE'** instead of **'DOWNLOAD'**
- `self.method` would be assigned to `rmethod` in `.requests.request()`, resulting in the download method not being used and **'GET'** taking its place
- Optimised the ways headers are added to the request in `.requests.request()`
- Renamed `Redirects` class in `.requests` to `NoRedirects`
- Optimised the way the request is setup in `.requests.request()`
- Reformatted the way requests are created in `.requests.request()`, you can initialise the host but you must call `.send(method=...)` to perform the request
- Optimisation on the way the arguments are processed in the `.style()` method in the main module
- Revert MacOS user agent header to the Intel version instead of M1 because it may not be recognised properly by some websites
- Reformatted the way the **"Content-Length"** and **"Content-Type"** headers are included in the request in `.requests.request()`
- Rename `colours` variable to `ANSI_colours` in the main module to reflect the content
- Adapted the way `self.text` is read to make sure it doesn't show up as nothing even when a response was returned
- The user agent has been updated to the correct version including the Python tag in `README.md`
- Implemented a new method of checking for different request outcomes in the `.requests` module, now using more specific exceptions
- Optimise `connected()` method in `.requests` to use httpbin.org, avoiding google's http errors
- Optimise the way the request data is read in `.requests.request()` to avoid re-encoding the text
- Make sure that the base request data in `.requests.request()` cookie is set back to zero when read from either `.read()` or `.readlines()` so it can be read multiple times
- Correct code example in the main module's docstring
- Reword `verified` variable docstring in `.requests` `API.md` module
- The port for connections with `.requests.connected()` has been changed to 80 because it was timing out before, stupid issue
- Reword `.requests` module docstring
- Converted `.sys.system()` method to a class
- Rename `output` variable from `.sys.system()` `shell_response` return to `text`
- The way some system programs are called from various methods, they should call the program directly instead of running a shell command
- Made sure the correct return type is present on every method in `API.md`
- Converted `clean` parameter from `.sys.system()` class to instead be a seperate property
- Made text property in `.sys.system()` become a string instead of a list

<br>

**Notes:**
- The current implementation of reading and writing to `cache.json` and `config.json` rely on the file staying open for the duration of the program to speed load times. Though there is no local Python way to call `.close()` on the TextIOWrapper when the program is ended. It is dependent on CPython's garbage collecter to do this for us.

<br><br>

## 1.4.4-1 (7/9/2023)

Forgot to change some things bruh<br><br>

**Additions:**
- Version release date in `info.py`
- `info` section in the API
- `str()` method on each `info.py` property so that pylance (python linter for vsc) doesn't recognise them as direct string literals

<br>

**Removals:**
- Build system as setuptools in `pyproject.toml` as having `setup.py` wouldn't work regardless
 
<br>

**Changes:**
- Updated README.md file request `__str__()` method variable to return the correct string
- Made sure the correct release date was present on every file
- Replaced '(c)' with '©' in license property in `info.py`
- Rename `setup.py` to `!setup.py` to avoid backend subprocess error when building package binaries

<br><br>

## 1.4.4 (7/9/2023)

Some needed features lacking in 1.4.3 (also bugfixes)<br><br>

**Additions:**
- Added `status_codes` property to `.errors.StatusCodeError` to reflect the class name
- Created the `CHANGELOG` file for the update details, also added `COMMIT` file in 1.4.3 but forgot to mention (deleted this update)
- The ability to use the default certificate file location in `.requests.ctx()`
- Created `order` parameter in `.requests.prep_url()` for if the url items should be ordered alphabetically
- Created `errors` section in the API file
- Included the list of supported methods in the API file for `.requests.Request`
- Created a new method in the main directory, `reverseDictSearch()`, to find the unknown key(s) of a value in a dictionary
- Included the `url_response` class variables in the `requests` API methods
- Created unverified and verified default `SSLContext` variables in `.requests`
- Readded `shutil.copyfileobj()` as I had implemented it incorrectly
- Readded `.requests.header()` http method as it also had a broken impementation
- Included a few disclaimer messages and notes in the documentation for poorly described methods, classes or blocks of code
- Included disclaimer message in README.md about needed implementation of `.sys.info` linux version
- Added gm timezone in `.date()` for standard time
- Added `seconds` parameter in `.epoch()` for if the epoch should be returned in seconds or milliseconds
- Included `unverified` and `verified` properties in API.md
- Added `.requests.connected()` method to determine whether the system has a valid internet connection
- Added codeblocks, bolding, spaces, indentation, breaks and wide hyphens to improve the readability of the documentation in API.md

<br>

**Removals:**
- The use and ability to use the `FILE` parameter in `.requests.Request`, use `DOWNLOAD` instead
- Unecessary lines before each parameter list in the API.md methods, took up around 50 useless lines
- Exception `UnicodeEncodeError` from `.requests.Request` as the tryed code did not encode anything
- Cliche ending message when you reach the bottom of the API
- `COMMIT` file as it serves no technical purpose

<br>

**Changes:**
- Made the `reason` parameter in `.errors.StatusCodeError` to not be required because the reason will automatically be assumed by the method
- Renamed `.errors.TimeoutExpired` to `ConnectionTimeoutExpired` in spite of context naming
- Converted the `tooltils.requests.Request.__str__()` method to return in the format `<(method) (stripped url) [(code)]>` instead of `<Request (method) [(code)]>`
- Fixed a typo in the variable `interpreter` in `sys.info`
- Changed description of `flush` parameter in `.style()` to properly describe what it is actually doing
- Changed '(c)' to '©' in the `LICENSE` file in 1.4.1 but forgot to mention
- Tested all of the available methods to verify their function
- Changed `.date()` `format` parameter to use the instances of `'standard'` and `'fancy'` instead of `1` and `2`
- Reworded `.sys.info.bitsize` docstring
- Adapted the *`.date().fv()`* helper function to return multiple values
- Fixed an issue in `.sys.system()` (and child commands) where if the output was not checked, an error would be raised when creating the output property
- Changed `.style()` `style` parameter to `colour` as font styles were added as seperate parameters
- Made `.style()` `colour` parameter become a non required parameter so you don't need to add a colour to use font styles
- Added official keyword to the `.requests.status_codes` dictionary to indicate supported codes everywhere
- Reworded the main file docstring to have correct grammar

<br><br>

## 1.4.3 (15/8/2023)

Yet even more bloody fixes<br><br>

**Additions:**
- `italic`, `crossed`, `underline` and `double_underline` parameters in the `.style()` method
- A few comments to reflect pieces of code that may not be understood correctly
- `clean` parameter to `.sys.check()` and `.sys.system()` for if the result should be stripped of empty lines
- `capture` parameter to `.sys.system()` for if the command output should be recorded
- Solver to correct for variables when the request type is `file` in `.requests`

<br>

**Removals:**
- Font styles from the `styles` (now `colours`) variable in the main file as font styles were added to `tooltils.style()`
- The use of `shutil.copyfileobj()` in `.requests.request(method='file')` as it would not work sometimes
- `header` method from `tooltils.requests` as it would not work

<br>

**Changes:**
- Made `.style()` method to use only colours in the `style`` parameter
- The way the certificate is processed in `.requests.ctx()` to avoid incorrect processing
- Fixed the way gm time (00:00) is processed in the `.date()` method
- Converted `.sys.pID()` results to be only integer
- Changed platform names for `.sys.clear()` to match the updated values in `v1.4.0`
- Changed `.sys.exit()` to use only a single string as the details parameter instead of `*args`
- Increased `.requests.request()` timeout to 15 seconds instead of 10 as it would timeout a lot
- Reworded docstrings of some variables and methods

<br><br>

## 1.4.2 (10/8/2023)

I am very unorganised <br><br>

**Additions:**
- None

<br>

**Removals:**
- Removed `docs/source/` from the line counter in `.info` to avoid startup issues

<br>

**Changes:**
- Fixed `.epoch()` method to produce the correct date instead of 14 hours behind
- Configured how `.epoch()` reads `.date(format=2)` to be compatible with `'August'` as the month

<br><br>

## 1.4.1 (10/8/2023)

Quick fixes cause I can't be bothered to test stuff <br><br>

**Additions:**
- `API.md` file in homepage to replace `/docs`

<br>

**Removals:**
- `/docs` for the documentation configuration because it required a third party module (myst-parser)

<br>

**Changes:**
- None

<br><br>

## 1.4.0 (9/8/2023)

It's been a while since the last update, hopefully this one is better <br><br>

**Additions:**
- A fully kitted requests module including get, post, download and more
- `.sys.info` for system variables (similar to platform but with more, no linux implementation unfortunately because of testing limitations)
- Documentation for every method and property in the form of html at `/docs`

<br>

**Removals:**
- A majority of the modules and compacted them into the main file
- Audio player is no longer in the road map due to required dependencies

<br>

**Changes:**
- Optimised existing code

<br><br>

## 1.3.0 (9/3/2023)

I needed to release some features for my [other project](https://github.com/feetbots/ezmusic/) so here's one last update for a bit <br><br>

**Additions:**
- A `sys` class for system variables and methods
- Error throwing for some methods

<br>

**Removals:**
- Underscores from the start of method and class parameters
- `json` class because it was a simple wrapper that didn't serve much purpose
- Use of `os.system()` anywhere as it is a deprecated method according to [the python docs](https://docs.python.org/3.7/library/os.html#:~:text=The%20subprocess%20module%20provides%20more%20powerful%20facilities%20for%20spawning%20new%20processes%20and%20retrieving%20their%20results%3B%20using%20that%20module%20is%20preferable%20to%20using%20this%20function.)

<br>

**Changes:**
- Updated `.requests` with a `verify` parameter (like the actual requests library), certificate and timeout parameter
- Updated `.requests` with better errors and status codes
- Reworded some of the doc strings on all available classes and methods
- Separated each class into its own file to allow for singular function imports
- Fixed methods in `string` class to return a string instead of a list

<br><br>

## 1.2.0 (2/3/2023)

Yet another small release <br>

**Note:**
This will probably be the last release for a while so I can focus on my [other](https://github.com/feetbots/ezmusic/) project 

<br>

**Additions:**
- Doc strings for each method and class for easier use

<br>

**Removals:**
- None

<br>

**Changes:**
- Fixed main file doc string so it will show up while using pylinters
- Completely rewrote `.date()` method allowing for timezone offsets

<br><br>

## 1.1.0 (18/2/2023)

1.0.0 version 2 <br><br>

**Additions:**
- New methods and classes

<br>

**Removals:**
- None

<br>

**Changes:**
- Completely rewrote the majority of methods available for optimisation
- Simplified the main file directory

<br><br>

## 1.0.0-beta (20/1/2023)

Idk what to say
