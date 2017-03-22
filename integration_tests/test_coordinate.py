import renderapi
import pytest
import tempfile
import os
import logging
import sys
import json
import numpy as np
from test_data import render_host, render_port, \
    client_script_location, tilespec_file, tform_file


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
#
logger.addHandler(ch)


@pytest.fixture(scope='module')
def render():
    render_test_parameters={
            'host':render_host,
            'port':8080,
            'owner':'test_coordinate',
            'project':'test_coordinate_project',
            'client_scripts':client_script_location
    }
    return renderapi.render.connect(**render_test_parameters)

@pytest.fixture(scope='module')
def teststack_tilespec():
    render_test_parameters={
            'host':render_host,
            'port':8080,
            'owner':'test_coordinate',
            'project':'test_coordinate_project',
            'client_scripts':client_script_location
    }
    render=renderapi.render.connect(**render_test_parameters)
    ts_json = json.load(open(tilespec_file,'r'))
    tform_json = json.load(open(tform_file,'r'))

    tilespecs = [renderapi.tilespec.TileSpec(json=ts) for ts in ts_json]
    tforms = [renderapi.transform.load_transform_json(td) for td in tform_json]

    stack = 'test_coordinate_stack'
    r=render.run(renderapi.stack.create_stack,stack,force_resolution=True)
    render.run(renderapi.client.import_tilespecs,stack,tilespecs,
    sharedTransforms=tforms)
    r=render.run(renderapi.stack.set_stack_state,stack,'COMPLETE')
    yield (stack,tilespecs[0])
    render.run(renderapi.stack.delete_stack,stack)

def test_world_to_local_coordinates(render,teststack_tilespec):
    logger.debug('test not implemented yet')
    assert(False)

def test_local_to_world_coordinates(render,teststack_tilespec):
    logger.debug('test not implemented yet')
    assert(False)

def test_world_to_local_coordinates_batch(render,teststack_tilespec):
    logger.debug('test not implemented yet')
    assert(False)

def test_local_to_world_coordinates_batch(render,teststack_tilespec):
    logger.debug('test not implemented yet')
    assert(False)

def old_world_to_local_coordinates_array(render,teststack_tilespec):
    logger.debug('test not implemented yet')
    assert(False)

def test_world_to_local_coordinates_array(render,teststack_tilespec):
    logger.debug('test not implemented yet')
    assert(False)

def old_local_to_world_coordinates_array(render,teststack_tilespec):
    logger.debug('test not implemented yet')
    assert(False)

def local_to_world_coordinates_array(render,teststack_tilespec):
    logger.debug('test not implemented yet')
    assert(False)

def world_to_local_coordinates_clientside():
    logger.debug('test not implemented yet')
    assert(False)

def local_to_world_coordinates_clientside():
    logger.debug('test not implemented yet')
    assert(False)