"""General installation information"""


class _bm:
    from logging import basicConfig, DEBUG, INFO, WARN, ERROR, CRITICAL
    from os.path import exists, abspath
    from os import listdir, mkdir
    from json import load, dumps
    from typing import Union

    from ._logs import create, enable, disable, close

    class LoggingLevel:
        pass

    lines:  int = 0
    files: list = listdir('./') + ['tooltils/' + i for i in listdir('./tooltils')] + \
                  ['tooltils/requests/' + i for i in listdir('./tooltils/requests')] + \
                  ['tooltils/sys/' + i for i in listdir('./tooltils/sys')]

    for i in ('API.md', 'CHANGELOG.md', 'LICENSE'):
        files.remove(i)

    for i in files:
        if i == '.DS_Store' or i == '__pycache__':
            files.remove(i)
            continue

        try:
            with open(i) as _f:
                lines += len(_f.readlines())
        except (IsADirectoryError, UnicodeDecodeError):
            pass
    
    with open('LICENSE') as _f:
        lt: str = _f.read()
    
    with open('README.md') as _f:
        ld: str = _f.read()
    
    defaultCache: dict = {
        "errors": {},
        "global": {
            # "configMethodValues": {}
        },
        "info": {},
        "main": {},
        "requests": {
            "verifiableTimesChecked": 0,
            "verifiableNetworkList": {},
            "connectedTimesChecked": 0,
            "connectedNetworkList": {}
        },
        "sys.info": {},
        "sys": {}
    }

    defaultConfig: dict = {
        "errors": {},
        "global": {
            # "config": {
            #     "runConfigMethodAlways": False,
            #     "checkMethodForSafety": True
            # } 
        },
        "info": {},
        "main": {},
        "requests": {
            # "defaultVerificationMethod": True,
            "verifiableCachingCheck": 50,
            "connectedCachingCheck": 50,
            "verifiableCaching": False,
            "connectedCaching": False
        },
        "sys.info": {},
        "sys": {}
    }


    # actualConfig: dict = defaultConfig
    openCache  = None
    openConfig = None


def _create(name: str):
    with open('storage/' + name + '.json', 'a+') as _f:
        if name == 'cache':
            _f.write(_bm.dumps(_bm.defaultCache, indent=4))
        else:
            _f.write(_bm.dumps(_bm.defaultConfig, indent=4))

    return open('storage/' + name + '.json', 'r+')

if _bm.exists('storage'):
    if not _bm.exists('storage/cache.json'):
        _bm.openCache = _create('cache')
    if not _bm.exists('storage/config.json'):
        _bm.openConfig = _create('config')
else:
    _bm.mkdir('storage')

    _bm.openCache  = _create('cache')
    _bm.openConfig = _create('config')

def _getCache():
    if _bm.openCache is None:
        _bm.openCache = open('storage/cache.json', 'r+')

    return _bm.openCache

def _loadCache(module: str='') -> dict:
    _f = _getCache()
    data: dict = _bm.load(_f)
    _f.seek(0)

    if module == '':
        return data
    else:
        return data[module]

def _editCache(module: str, option: dict, subclass: str='') -> None:
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

def _getConfig():
    if _bm.openConfig is None:
        _bm.openConfig = open('storage/config.json', 'r+')

    return _bm.openConfig

def _loadConfig(module: str='') -> dict:
    _f = _getConfig()
    data: dict = _bm.load(_f)
    _f.seek(0)

    if module == '':
        return data
    else:
        return data[module]

def _editConfig(module: str, option: dict, subclass: str='') -> None:
    _f = _getConfig()
    data: dict = _bm.load(_f)

    if subclass:
        data[module][subclass].update(option)
    else:
        data[module].update(option)

    _f.seek(0)
    _f.truncate()
    _f.write(_bm.dumps(data, indent=4))
    _f.seek(0)

def clearCache(module: str=None) -> None:
    """Clear the file cache of tooltils or a specific module within"""

    module: str = str(module).lower()
    _f          = _getCache()

    if module == 'none':
        wdata: str = _bm.defaultCache
    else:
        wdata: dict = _bm.load(_f)

        try:
            wdata.update(_bm.defaultCache[module])
        except KeyError:
            raise FileNotFoundError('Cache module not found')
        
    _f.seek(0)
    _f.truncate(0)
    _f.write(_bm.dumps(wdata, indent=4))
    _f.seek(0)

def clearConfig(module: str=None) -> None:
    """Revert the config of tooltils or a specific module within"""

    module: str = str(module).lower()
    _f          = _getConfig()

    if module == 'none':
        wdata: str = _bm.defaultConfig
    else:
        wdata: dict = _bm.load(_f)

        try:
            wdata.update(_bm.defaultConfig[module])
        except KeyError:
            raise FileNotFoundError('Config module not found')
        
    _f.seek(0)
    _f.truncate(0)
    _f.write(_bm.dumps(wdata, indent=4))
    _f.seek(0)

class logger():
    """Create a logging instance for tooltils modules only"""

    def enable(self) -> None:
        _bm.enable(self._logger, self.enabled, self.closed)

    def disable(self) -> None:
        _bm.disable(self._logger, self.enabled, self.closed)
    
    def close(self) -> None:
        _bm.close(self._logger, self.closed)

    @property
    def module(self) -> str:
        """What module the logging is enabled for"""

        return self._module
    
    @module.setter
    def module(self, value):
        raise AttributeError('Module property cannot be changed')

    @property
    def level(self) -> _bm.Union[str, int, _bm.LoggingLevel]:
        """What level of logging is being used"""

        return self._level
    
    @level.setter
    def level(self, value):
        raise AttributeError('Level property cannot be changed')
    
    @property
    def level2(self) -> _bm.Union[str, int, _bm.LoggingLevel]:
        """What max level of logging is being used"""

        return self._level2
    
    @level2.setter
    def level2(self, value):
        raise AttributeError('Level2 property cannot be changed')

    @property
    def enabled(self) -> bool:
        """Whether the logger is enabled"""

        return self._enabled
    
    @enabled.setter
    def enabled(self, value):
        raise AttributeError('Enabled property cannot be changed')

    @property
    def closed(self) -> bool:
        """Whether the logger has been closed"""

        return self._closed
    
    @closed.setter
    def closed(self, value):
        raise AttributeError('Closed property cannot be changed')
    
    def enable(self) -> None:
        """Enable the logger instance"""

        self._enabled = not _bm.enable(self._logger, self.enabled, self.closed)
    
    def disable(self) -> None:
        """Disable the logger instance"""

        self._enabled = bool(_bm.disable(self._logger, self.enabled, self.closed))
    
    def close(self) -> None:
        """Close the logger instance"""
        
        self._disabled = True
        self._closed   = not _bm.close(self._logger, self.closed)

    def __init__(self, 
                 module: str='ALL', 
                 level: _bm.Union[str, int, _bm.LoggingLevel]='ALL',
                 level2: _bm.Union[str, int, _bm.LoggingLevel]='ALL'
                 ) -> None:
        if type(module) is str: module = module.upper()
        if type(level) is str: level = level.upper()
        if type(level2) is str: level2 = level2.upper()
        
        if type(module) is not str:
            raise TypeError('Module must be a valid \'str\' instance')
        elif module not in ('', 'ALL', 'MAIN', 'REQUESTS', 'SYS'):
            raise ValueError('Unknown module \'{}\''.format(module))
        else:
            self._module: str = module

            if module == '' or module == 'ALL' or module == 'MAIN':
                self._module: str = 'tooltils'
            else:
                self._module: str = 'tooltils.' + module.lower()
        for i in (('level', level), ('level2', level2)):
            if not isinstance(i[1], (str, int, _bm.DEBUG, _bm.INFO, _bm.WARN,
                                     _bm.ERROR, _bm.CRITICAL)):
                raise TypeError(f'{i[0]} must be a valid \'str\', \'int\' or \'logging\' level instance')
            elif i[1] not in ('ALL', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL', 10, 20, 30, 40, 50):
                raise ValueError('Invalid level \'{}\''.format(i[1]))
            else:
                if i[0] == 'level':
                    if level == 'ALL':
                        self._level = _bm.DEBUG
                    else:
                        self._level = level
                else:
                    if level2 == 'ALL':
                        self._level2 = _bm.CRITICAL
                    else:
                        self._level2 = level2

        self._logger  = _bm.create(self._module, self._level, self._level2)
        self._closed  = False
        self._enabled = True

        _bm.basicConfig(format=
                        '[%(asctime)s] [{}/%(levelname)s]: %(message)s'.format(self._module),
                        datefmt='%I:%M:%S')

    def __str__(self) -> str:
        module: str = 'ALL' if not self.module else self.module.upper()
        state:  str = 'on' if self.enabled else 'off'

        return f'<Logger instance: [{state}] -> [{module}]>'

author:      str = str('feetbots')
"""The creator of tooltils (is and always will be feetbots)"""
version:     str = str('1.5.0')
"""The current installation version"""
released:    str = str(' /11/2023')
"""Release date of the current version"""
lines:       int = int(_bm.lines)
"""How many lines of code in this version"""
license:     str = str(_bm.lt)
"""The content of the currently used license"""
location:    str = str('/' + '/'.join(_bm.abspath('info.py').split('/')[1:-1]) + '/')
"""The path of the current installation of tooltils"""
description: str = str('A lightweight python utility package built on the standard library')
"""The short description of tooltils"""
long_description: str = str(_bm.ld)
"""The long description of tooltils (README.md)"""
