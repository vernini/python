# --coding : utf-8 --

'''
========================================================================
INSTRUCTIONS::
========================================================================

Moti Pulse


========================================================================
---->  Import Modules  <----
========================================================================
'''
import os

import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import pymel.core as pm

import common.yaml as yaml

import common.pyside_util as pyside_util


'''
========================================================================
---->  Global Variables  <----
========================================================================
'''
TOOLS_PATH = os.path.dirname( __file__ )

WINDOW_TITLE = 'Save Preset'
WINDOW_VERSION = 1.5
WINDOW_NAME = 'save_preset'

UI_FILE_PATH = os.path.join( TOOLS_PATH, 'save_preset.ui')
UI_OBJECT, BASE_CLASS = pyside_util.get_pyside_class( UI_FILE_PATH )

'''
========================================================================
---->  Create/Connect UI Functionality  <----
========================================================================
'''
class Save_Preset(BASE_CLASS,UI_OBJECT):
    def __init__(self, parent=pyside_util.get_maya_window(),*args):
        super(Save_Preset,self).__init__(parent,QtCore.Qt.Tool)
        self.setupUi(self)
        self.setObjectName(WINDOW_NAME)
        self.setWindowTitle('{0} {1}'.format(WINDOW_TITLE, str(WINDOW_VERSION)))

        self.btb_save.accepted.connect(self.save_preset_preview)
        self.show()


    def save_preset_preview(self):

        brute_force=int(QtGui.QLineEdit.text(self.line_dmc_subdivs))
        light_cache=int(QtGui.QLineEdit.text(self.line_subdivs))
        min_subdivs=int(QtGui.QLineEdit.text(self.line_dmcMinSubdivs))
        max_subdivs=int(QtGui.QLineEdit.text(self.line_dmcMaxSubdivs))
        dmcthreshold=float(QtGui.QLineEdit.text(self.line_dmcThreshold))
        dmcs_threshold=float(QtGui.QLineEdit.text(self.line_dmcs_adaptiveThreshold))
        dmcs_minsamples=int(QtGui.QLineEdit.text(self.line_dmcs_adaptiveMinSamples))

        preset = {
                    'brute_force' : brute_force,
                    'light_cache' : light_cache,
                    'min_subdivs' : min_subdivs,
                    'max_subdivs' : max_subdivs,
                    'dmcthreshold' : dmcthreshold,
                    'dmcs_threshold' : dmcs_threshold,
                    'dmcs_minsamples' : dmcs_minsamples,
                    }

        save_name = QtGui.QLineEdit.text(self.line_save_preset_name)
        stream = file('X:/GBK/Post/Episode/trailer/data/yaml/'+save_name+'.yaml','w')
        yaml.dump(preset,stream,default_flow_style=False)

'''
========================================================================
---->  Show .ui File  <----
========================================================================
'''

def show_ui():
    if pm.window(WINDOW_NAME,exists=True,q=True):
        pm.deleteUI(WINDOW_NAME)

    Save_Preset()

