#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <https://github.com/calamares> ===
#
#   Copyright 2014-2015, Philip Müller <philm@manjaro.org>
#   Copyright 2015-2017, Teo Mrnjavac <teo@kde.org>
#   Copyright 2017, Alf Gaida <agaida@siduction.org>
#   Copyright 2017, Adriaan de Groot <groot@kde.org>
#   Copyright 2017, Gabriel Craciunescu <crazy@frugalware.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import libcalamares
import os

def system_addons(rmp,config):
    '''
        Create link to resolv.conf
    '''
    if config['flash']:
        # install Flash by epic
        calamares.utils.target_env_call(['epic','-u','install','/usr/share/zero-lliurex-flash/flash.epi'])

    analytics_path = "{rootmountpoint}/etc/lliurex-analytics/".format(rootmountpoint=rmp)
    os.system("mkdir -p {ap}".format(ap=analytics_path))
    if config['statistics']:
        # Enable Statistics
        with open(os.path.join(analytics_path,"status"),"w") as fd:
            fd.write('yes\n')
    else:
        with open(os.path.join(analytics_path,"status"),"w") as fd:
            fd.write('no\n')


    return None

def run():
    """
    Create ubiquity modifications
    :return:
    """
    root_mount_point = libcalamares.globalstorage.value("rootMountPoint")
    config = libcalamares.globalstorage.value('systemaddons')
    return system_addons(root_mount_point,config)