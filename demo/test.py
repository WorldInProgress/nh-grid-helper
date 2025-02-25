import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from gridHelper import NHGridHelper as gridHelper

DIR_RESOURCE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'testRes'))
DIR_GRID_INFO_RESOURCE = os.path.abspath(os.path.join(DIR_RESOURCE, 'gridInfo.json'))
DIR_DEM_RESOURCE = os.path.abspath(os.path.join(DIR_RESOURCE, 'Digital Terrain Model.tif'))

helper = gridHelper(DIR_GRID_INFO_RESOURCE, DIR_DEM_RESOURCE)
helper.export(DIR_RESOURCE)