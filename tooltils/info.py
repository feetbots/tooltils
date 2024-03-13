"""General installation information"""


version: str = str('1.7.2')
"""The current installation version"""

class _bm:
    from logging import (getLogger, Formatter, StreamHandler, DEBUG, 
                         INFO, WARN, ERROR, CRITICAL)
    from os.path import exists, abspath, expanduser
    from sys import platform, version as pyv
    from os import listdir, remove, mkdir
    from time import localtime, mktime
    from typing import Union, List
    from datetime import datetime
    from json import load, dumps
    from shutil import rmtree

    from ._external import run

    class LoggingLevel:
        pass

    defaultCache:  dict = {
        "errors": {},
        "global": {
            "configMethodValues": {}
        },
        "info": {
            "licenseContent": None,
            "readmeContent": None
        },
        "main": {},
        "os": {},
        "requests": {
            "verifiableTimesChecked": 0,
            "verifiableNetworkList": {},
            "connectedTimesChecked": 0,
            "connectedNetworkList": {}
        }
    }
    defaultConfig: dict = {
        "errors": {},
        "global": {
            "disableConfigMethodValues": True,
            "configMethodCheck": 20
        },
        "info": {
            "disableOnlineContentFetch": False,
        },
        "main": {},
        "os": {},
        "requests": {
            "defaultVerificationMethod": True,
            "verifiableCachingCheck": 20,
            "connectedCachingCheck": 20,
            "verifiableCaching": True,
            "connectedCaching": False,
            "redirectLimit": 20
        }
    }

    openCache          = None
    openConfig         = None
    actualConfig: dict = defaultConfig
    split:         str = '\\' if platform.lower().startswith('win') else '/'
    home:          str = expanduser('~')

    if not home:
        home: str = split.join(__file__.split(split)[:3])

    if not home:
        home: str = ''

    baseDir: str = home + split + '.tooltils' + split
    pyDir:   str = baseDir + 'py' + pyv.split('(')[0].strip() + split
    tDir:    str = pyDir + 'ts' + version + split

    class levelFilter(object):
        def __init__(self, level):
            self.level = level

        def filter(self, logRecord):
            return logRecord.levelno <= self.level

    class lFormatter(Formatter):
        def formatTime(self, record, datefmt):
            return _bm.datetime.fromtimestamp(
                   _bm.mktime(_bm.localtime(record.created))).strftime(datefmt)
    
    def closeFiles() -> None:
        _bm.openCache.close()
        _bm.openConfig.close()

        _bm.openCache  = False
        _bm.openConfig = False


def _makeFunc(module: str, func: str) -> str:
    if '.' not in module:
        return func
    else:
        return '.'.join(func.split('.')[1:])

def _logger(module: str):
    logger = _bm.getLogger('tooltils' + module)

    logger._debug    = lambda msg, func: logger.debug(msg, extra={"caller": _makeFunc(module, func)})
    logger._info     = lambda msg, func: logger.info(msg, extra={"caller": _makeFunc(module, func)})
    logger._warning  = lambda msg, func: logger.warning(msg, extra={"caller": _makeFunc(module, func)})
    logger._error    = lambda msg, func: logger.error(msg, extra={"caller": _makeFunc(module, func)})
    logger._critical = lambda msg, func: logger.critical(msg, extra={"caller": _makeFunc(module, func)})

    return logger


_bm.logger = _logger('.info')

author:              str = str('feetbots')
"""The current owner of tooltils"""
author_email:        str = str('pheetbots@gmail.com')
"""The email of the current owner of tooltils"""
maintainer:          str = str('feetbots')
"""The current sustainer of tooltils"""
maintainer_email:    str = str('pheetbots@gmail.com')
"""The email of the current sustainer of tooltils"""
released:            str = str('13/3/2024')
"""The release date of the current version"""
release_description: str = str('Infinite Bugs')
"""The description of the current release version"""
description:         str = str('A lightweight python utility package built on the standard library')
"""The short description of tooltils"""
homepage:            str = str('https://github.com/feetbots/tooltils')
"""The current home website of tooltils"""
homepage_issues:     str = str('https://github.com/feetbots/tooltils/issues')
"""The current issues directory of the home website of tooltils"""
location:            str = str(_bm.split.join(__file__.split(_bm.split)[:-1]) + _bm.split)
"""The path of the current installation of tooltils"""
releases:  _bm.List[str] = ['1.0.0-beta', '1.1.0', '1.2.0', '1.3.0', '1.4.0', '1.4.1', '1.4.2',
                            '1.4.3', '1.4.4', '1.4.4-1', '1.5.0', '1.5.1', '1.5.2', '1.5.3',
                            '1.6.0', '1.7.0', '1.7.1', '1.7.2']
"""All current versions of tooltils"""

def _checkLoaded():
    if not _bm.openCache and not _bm.openConfig:
        raise FileExistsError('The tooltils data files have been deleted, please rerun your program ' +
                              'to create them again')

def _getCache():
    if not _bm.openCache:
        _bm.openCache = open(_bm.tDir + 'cache.json', 'r+')

    return _bm.openCache

def _getConfig():
    if _bm.openConfig:
        return _bm.openConfig

    _f  = _bm.openConfig = open(_bm.tDir + 'config.json', 'r+')
    _f2 = _getCache()

    # locate and config method values and convert them

    config: dict = _bm.load(_f)
    cache:  dict = _bm.load(_f2)
    funcs:  dict = cache['global']['configMethodValues']

    _f.seek(0)
    _f2.seek(0)

    if config['global']['disableConfigMethodValues']:
        return _f
 
    for k, v in config.items():
        for k2, v2 in v.items():
            if type(v2) is str and '$f ' in v2:
                try:
                    statement: str = v2.split(' ')[1].split('(')
                    funcName:  str = statement[0]
                    args:      str = '[' + statement[1][:-1] + ']'

                    if funcName in funcs.keys() and funcs[funcName][1] < config['global']['configMethodCheck']:
                        funcs[funcName] = (funcs[funcName][0], funcs[funcName][1] + 1)
                        _editCache('global', {"configMethodValues": funcs})
                    else:
                        value = _bm.run(funcName, args)

                        funcs.update({funcName: (value, 1)})
                        _editCache('global', {"configMethodValues": funcs})
                except Exception:
                    value = None
            else:
                value = v2

            _bm.actualConfig[k][k2] = value
    
    return _f

def _loadCache(module: str='') -> dict:
    _f = _getCache()
    data: dict = _bm.load(_f)
    _f.seek(0)

    if module == '':
        return data
    else:
        return data[module]

def _editCache(module: str, option: dict, subclass: str='') -> None:
    _checkLoaded()

    _f = _getCache()
    data = _bm.load(_f)

    if subclass:
        data[module][subclass].update(option)
    else:
        data[module].update(option)

    _f.seek(0)
    _f.truncate()
    _f.write(_bm.dumps(data, indent=4))
    _f.seek(0)

def _deleteCacheKey(module: str, key: str, subclass: str='') -> None:
    _checkLoaded()

    _f = _getCache()
    data = _bm.load(_f)

    if subclass:
        keys = data[module][subclass].keys()
    else:
        keys = data[module].keys()

    for i in list(keys):
        if key == i:
            if subclass:
                data[module][subclass].pop(i)
            else:
                data[module].pop(i)

    _f.seek(0)
    _f.truncate()
    _f.write(_bm.dumps(data, indent=4))
    _f.seek(0)

def _loadConfig(module: str='') -> dict:
    # make sure _getConfig() is called otherwise _bm.actualConfig will not be set

    _getConfig()

    if module == '':
        return _bm.actualConfig
    else:
        return _bm.actualConfig[module]

def clearCache(module: str=None) -> None:
    """Clear the file cache of tooltils or a specific module within"""

    _checkLoaded()

    module: str = str(module).lower()
    _f          = _getCache()
    data:  dict = _bm.load(_f)

    if module == 'none':
        data: dict = _bm.defaultCache
    else:
        try:
            data.update(_bm.defaultCache[module])
        except KeyError:
            raise FileNotFoundError('Cache module not found')

    _f.seek(0)
    _f.truncate(0)
    _f.write(_bm.dumps(data, indent=4))
    _f.seek(0)

    _bm.logger._debug('User cache was cleared', 'info.clearCache')

def clearConfig(module: str=None) -> None:
    """Revert the config of tooltils or a specific module within"""

    _checkLoaded()

    module: str = str(module).lower()
    _f          = _getConfig()
    data:  dict = _bm.load(_f)

    if module == 'none':
        data: dict = _bm.defaultConfig
    else:
        try:
            data.update(_bm.defaultConfig[module])
        except KeyError:
            raise FileNotFoundError('Config module not found')

    _f.seek(0)
    _f.truncate(0)
    _f.write(_bm.dumps(data, indent=4))
    _f.seek(0)

    _bm.logger._debug('User config was reset', 'info.clearConfig')

def clearData() -> None:
    """Clear the cache and config of tooltils"""

    _checkLoaded()

    _f  = _getCache()
    _f2 = _getConfig()

    _f.truncate(0)
    _f.write(_bm.dumps(_bm.defaultCache, indent=4))
    _f.seek(0)

    _f2.truncate(0)
    _f2.write(_bm.dumps(_bm.defaultConfig, indent=4))
    _f2.seek(0)

    _bm.logger._debug('User cache and config was cleared and reset', 'info.clearData')

def deleteData(pyv: str=None, tsv: str=None) -> None:
    """Delete the stored data for a specific python version of tooltils, a specific tooltils version, 
    a combination of these or the entire tooltils storage directory"""

    _checkLoaded()

    if type(pyv) is not str and pyv:
        raise TypeError('Pyv must be a valid \'str\' instance')
    if type(tsv) is not str and tsv:
        raise TypeError('Tsv must be a valid \'str\' instance')

    if not _bm.exists(_bm.baseDir):
        raise FileNotFoundError('The tooltils storage directory does not exist')
    
    if not _bm.exists(_bm.tDir):
        raise FileNotFoundError('The current tooltils version storage directory does not exist')

    if not pyv and not tsv:
        _bm.closeFiles()

        _bm.rmtree(_bm.baseDir)

        _bm.logger._debug('User storage directory was deleted', 'info.deleteData')
    elif pyv and tsv:
        if not ('py' + pyv) in _bm.listdir(_bm.baseDir):
            raise FileNotFoundError('Python version not found in tooltils data files')
        
        if not ('ts' + tsv) in _bm.listdir(_bm.pyDir):
            raise FileNotFoundError('Tooltils version not found in tooltils data files')

        _bm.closeFiles()

        _bm.rmtree(_bm.tDir)

        _bm.logger._debug(f'User storage data for Python version {pyv} and Tooltils version {tsv} was deleted', 
                          'info.deleteData')
    elif pyv:
        if not ('py' + pyv) in _bm.listdir(_bm.baseDir):
            raise FileNotFoundError('Python version not found in tooltils data files')

        _bm.closeFiles()

        _bm.rmtree(_bm.pyDir)

        _bm.logger._debug(f'User storage data for Python version {pyv} was deleted', 'info.deleteData')
    elif tsv:
        for i in [i for i in _bm.listdir(_bm.baseDir) if 'temp' not in i and \
                                                         '.DS_Store' not in i]:
            for i2 in _bm.listdir(_bm.baseDir + i):
                try:
                    if ('ts' + tsv) in i2:
                        if _bm.openCache:
                            _bm.closeFiles()
                        
                        _bm.rmtree(_bm.baseDir + i + _bm.split + i2)
                except FileNotFoundError:
                    continue
                
        if _bm.openCache:
            raise FileNotFoundError('Tooltils version not found in tooltils data files')

        _bm.logger._debug(f'User storage data for Tooltils version {tsv} was deleted', 'info.deleteData')

class logger():
    """Create a logging instance for tooltils modules only"""

    def enable(self) -> None:
        """Enable the logger instance"""

        if self.closed:
            raise ValueError('The logger has already been closed')
        elif self.enabled:
            raise ValueError('The logger is already enabled')
        else:
            self.enabled:    bool = True
            self._logger.disabled = False

    def disable(self) -> None:
        """Disable the logger instance"""

        if self.closed:
            raise ValueError('The logger has already been closed')
        elif not self.enabled:
            raise ValueError('The logger is already disabled')
        else:
            self.enabled:    bool = False
            self._logger.disabled = True
    
    def close(self) -> None:
        """Close the logger instance"""

        if self.closed:
            raise ValueError('The logger has already been closed')
        else:
            self.closed:    bool = True
            self.enabled:   bool = False
            self._logger.disabled = True
            self._logger.close()

    def __init__(self, 
                 module: str='ALL', 
                 level: _bm.Union[str, int, _bm.LoggingLevel]='ALL',
                 level2: _bm.Union[str, int, _bm.LoggingLevel]='ALL'
                 ) -> None:
        if type(level) is str: level = level.upper()
        if type(level2) is str: level2 = level2.upper()
        
        if type(module) is not str:
            raise TypeError('Module must be a valid \'str\' instance')
        elif module.upper() not in ('', 'ALL', 'MAIN', 'REQUESTS', 'OS'):
            raise ValueError('Unknown module \'{}\''.format(module))
        else:
            self.module: str = module.upper()

            if module == '' or module == 'ALL' or module == 'MAIN':
                self.module: str = 'tooltils'
            else:
                self.module: str = 'tooltils.' + module.lower()

        for i in (('level', level), ('level2', level2)):
            if not isinstance(i[1], (str, int, _bm.DEBUG, _bm.INFO, _bm.WARN, _bm.ERROR, _bm.CRITICAL)):

                raise TypeError(f'{i[0]} must be a valid \'str\', \'int\' or \'logging\' level instance')
            
            elif i[1] not in ('ALL', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL', 10, 20, 30, 40, 50):

                raise ValueError('Invalid level \'{}\''.format(i[1]))
            else:
                if i[0] == 'level':
                    if level == 'ALL':
                        self.level = _bm.DEBUG
                    else:
                        self.level = level
                else:
                    if level2 == 'ALL':
                        self.level2 = _bm.CRITICAL
                    else:
                        self.level2 = level2
        
        self._logger = _bm.getLogger(self._module)

        handler = _bm.StreamHandler()
        handler.  setFormatter(_bm.lFormatter(
                               '[%(asctime)s] [%(name)s.%(caller)s()/%(levelname)s]: %(message)s', '%H:%M:%S'))

        self._logger.setLevel(self._level)
        self._logger.addFilter(_bm.levelFilter(self._level2))
        self._logger.addHandler(handler)

        self.closed:  bool = False
        self.enabled: bool = True

        for k, v in {10: "DEBUG", 20: "INFO", 30: "WARN", 40: "ERROR", 50: "CRITICAL"}.items():
            if self._level == k:
                r1 = v
            elif self._level2 == k:
                r2 = v
        
        if '.' not in self._module:
            caller = 'info.logger'
        else:
            caller = 'logger'

        self._logger.debug(f'Initiated logger for <{self._module}> with range {r1} -> {r2}', extra={"caller": caller})

    def __str__(self) -> str:
        module: str = 'ALL' if not self.module else self.module.upper()
        state:  str = 'on' if self.enabled else 'off'

        return f'<Logger instance: [{state}] -> [{module}]>'


# necessary startup code

_cache = _config = True

if not _bm.exists(_bm.baseDir):
    _bm.mkdir(_bm.baseDir)
    _bm.mkdir(_bm.baseDir + 'temp')
if not _bm.exists(_bm.pyDir):
    _bm.mkdir(_bm.pyDir)
if not _bm.exists(_bm.tDir):
    _bm.mkdir(_bm.tDir)

if _bm.exists(_bm.tDir + 'cache.json'):
    _cache: bool = False
if _bm.exists(_bm.tDir + 'config.json'):
    _config: bool = False

if _cache:
    with open(_bm.tDir + 'cache.json', 'a+') as _f:
        _f.write(_bm.dumps(_bm.defaultCache, indent=4))

if _config:
    with open(_bm.tDir + 'config.json', 'a+') as _f:
        _f.write(_bm.dumps(_bm.defaultConfig, indent=4))

_data = _loadConfig()

for i in (('global', 'configMethodCheck'), ('requests', 'verifiableCachingCheck'), 
          ('requests', 'connectedCachingCheck'), ('requests', 'redirectLimit')):
    if type(_data[i[0]][i[1]]) is not int:
        raise RuntimeError(f'Config value {i[0]}.{i[1]} is not an instance of type \'int\', ' +
                           'please change it or reset the config')

# try to get license and long_description

_check:              bool = not _data['info']['disableOnlineContentFetch']
license, long_description = 0, 0

if _check and _loadCache('info')['licenseContent'] == None: # check if it is already cached
    from ssl import create_default_context, CERT_NONE
    from http.client import HTTPSConnection
    from zipfile import ZipFile

    try:
        # make testing easier
        verOverride = releases[-2] if len(version.split('.')) > 3 else version

        ctx = create_default_context()

        ctx.check_hostname = False
        ctx.verify_mode    = CERT_NONE
        ctx.set_ciphers('RSA')

        _req = HTTPSConnection('codeload.github.com', context=ctx)
        _req.request('GET', '/feetbots/tooltils/zip/refs/tags/{}'.format(
                     'v' + verOverride), body=None,
                     headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:10.0) " + 
                              "Gecko/20100101 Firefox/10.0"})

        with open(_bm.baseDir + f'temp{_bm.split}files.zip', 'wb+') as _f:
            _f.write(_req.getresponse().read())
        
        with ZipFile(_bm.baseDir + f'temp{_bm.split}files.zip') as _f:
            _f.extractall(_bm.baseDir + f'temp{_bm.split}files')
        
        with open(_bm.baseDir + f'temp{_bm.split}files{_bm.split}tooltils-{verOverride}{_bm.split}LICENSE') as _f, \
             open(_bm.baseDir + f'temp{_bm.split}files{_bm.split}tooltils-{verOverride}{_bm.split}README.md') as _f2:
            license, long_description = _f.read(), _f2.read()

        _editCache('info', {"licenseContent": license, 
                            "readmeContent": long_description})
    except Exception:
        pass
    finally:
        try:
            _bm.remove(_bm.baseDir + f'temp{_bm.split}files.zip')
            _bm.rmtree(_bm.baseDir + f'temp{_bm.split}files')
        except Exception:
            pass

        _req.close()
else:
    license          = _loadCache('info')['licenseContent']
    long_description = _loadCache('info')['readmeContent']

if not license and not long_description:
    _editCache('info', {"licenseContent": 0, "readmeContent": 0})

def _getLines():
    def getFiles(dir: str) -> list:
        fileList: list = []

        for i in _bm.listdir(location + dir):
            fileList.append(location + ('' if not dir else dir + _bm.split) + i)
        
        return fileList

    lines:  int = 0
    files: list = getFiles('') + getFiles('requests')

    for i in files:
        for x in ('README.md', 'API.md', 'CHANGELOG.md', 'LICENSE', '.DS_Store',
                  '__pycache__', '.git'):
            if x in i:
                files.remove(i)

    for i in files:
        try:
            with open(i) as _f:
                lines += len(_f.readlines())
        except (IsADirectoryError, UnicodeDecodeError, PermissionError):
            # PermissionError catches exceptions that are raised when we try to open a directory
            continue

    return lines

license:          str = str(license) if type(license) is str else None
"""The content of the currently used license"""
long_description: str = str(long_description) if type(long_description) is str else None
"""The long description of tooltils"""
lines:            int = int(_getLines())
"""The amount of lines of code in this tooltils installation"""

for i in ['_getLines', '_cache', '_config', '_check', 'create_default_context', 
          'CERT_NONE', 'ctx', 'HTTPSConnection', 'ZipFile', '_req', '_data', 
          '_f', '_f2', 'i']:
    try:
        del locals()[i]
    except KeyError:
        continue
