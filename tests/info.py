import sys

if sys.platform.startswith('win'):
    split: str = '\\'
else:
    split: str = '/'

sys.path.append(split.join(__file__.split(split)[:-2]) + split)

import tooltils


i = tooltils.info
s = tooltils.sys.info

print('\n'.join([f'tooltils.info.{k}: {v}' for k, v in {"author": i.author, "author_email": i.author_email,
                                                        "maintainer": i.maintainer, "maintainer_email": i.maintainer_email,
                                                        "version": i.version, "released": i.released,
                                                        "description": i.description, "long_description": i.long_description,
                                                        "license": i.license, "classifiers": i.classifiers,
                                                        "homepage": i.homepage, "homepage_issues": i.homepage_issues,
                                                        "location": i.location, "lines": i.lines}.items()]))
print('\n\n')

print('\n'.join([f'tooltils.sys.info.{k}: {v}' for k, v in {"macOS_releases": s.macOS_releases, "python_version": s.python_version,
                                                            "name": s.name, "bitsize": s.bitsize, "interpereter": s.interpreter,
                                                            "platform": s.platform, "detailed_platform": s.detailed_platform,
                                                            "cpu": s.cpu, "arch": s.arch, "platform_version": s.platform_version,
                                                            "model": s.model, "cores": s.cores, "ram": s.ram, "manufacturer": s.manufacturer,
                                                            "serial_number": s.serial_number, "boot_drive": s.boot_drive}.items()]))
print('\n\n')
