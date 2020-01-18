#!/usr/bin/env python

# This file is part of ci_hsc_gen2.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__all__ = ["makeButler", "REPO_ROOT"]

import os

from lsst.utils import getPackageDir
from lsst.daf.butler import Butler, ButlerConfig

REPO_ROOT = os.path.join(getPackageDir("ci_hsc_gen2"), "DATA")
SEARCH_PATHS = [os.path.join(getPackageDir("ci_hsc_gen2"), "gen3config"), ]


def makeButler(config=None, root=REPO_ROOT, collection="raw/hsc"):
    if config is None:
        config = REPO_ROOT
    butlerConfig = ButlerConfig(config, searchPaths=SEARCH_PATHS)
    # Force the configuration directory to refer to the ci_hsc root
    butlerConfig.configDir = root
    return Butler(butlerConfig, run=collection)