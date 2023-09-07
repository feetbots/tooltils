# v1.4.4

## 1.4.4 (6/9/2023)

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
- Changed '(c)' to '©'
 in the `LICENSE` file in 1.4.1 but forgot to mention
- Tested all of the available methods to verify their function
- Changed `.date()` `format` parameter to use the instances of `'standard'` and `'fancy'` instead of `1` and `2`
- Reworded `.sys.info.bitsize` docstring
- Adapted the *`.date().fv()`* helper function to return multiple values
- Fixed an issue in `.sys.system()` (and child commands) where if the output was not checked, an error would be raised when creating the output property
- Changed `.style()` `style` parameter to `colour` as font styles were added as seperate parameters
- Made `.style()` `colour` parameter become a non required parameter so you don't need to add a colour to use font styles
- Added official keyword to the `.requests.status_codes` dictionary to indicate supported codes everywhere
- Reworded the main file docstring to have correct grammar
