"""Tests for cement2.ext.ext_daemon."""

import os
from nose.tools import with_setup, ok_, eq_, raises
from nose import SkipTest

from cement2.core import handler, backend, log, hook
from cement2 import test_helper as _t

def import_daemon():
    from cement2.ext import ext_daemon
    hook.register()(ext_daemon.cement_post_setup_hook)
    hook.register()(ext_daemon.cement_pre_run_hook)
        
def test_daemon():
    defaults = backend.defaults('myapp')    
    app = _t.prep('myapp')
    import_daemon()
    
    app.argv = ['--daemon']
    app.setup()    
    app.config.set('daemon', 'pid_file', None)
    