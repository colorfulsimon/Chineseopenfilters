# __init__.py
# 
# GUI for OpenFilters.
# 
# Copyright (c) 2001,2002,2004-2007 Stephane Larouche.
# 
# This file is part of OpenFilters.
# 
# OpenFilters is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# OpenFilters is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA



import wx

# Compatibility aliases for wxPython Phoenix file dialog flags.
if not hasattr(wx, "OPEN"):
	wx.OPEN = wx.FD_OPEN
if not hasattr(wx, "SAVE"):
	wx.SAVE = wx.FD_SAVE
if not hasattr(wx, "OVERWRITE_PROMPT"):
	wx.OVERWRITE_PROMPT = wx.FD_OVERWRITE_PROMPT
if not hasattr(wx, "CHANGE_DIR"):
	wx.CHANGE_DIR = wx.FD_CHANGE_DIR

# wxPython Phoenix is stricter about invalid sizer flags than the legacy
# wx used by upstream OpenFilters. During migration we disable the runtime
# consistency assertions to keep dialogs usable.
try:
	wx.SizerFlags.DisableConsistencyChecks()
except AttributeError:
	pass

from . import GUI_calculate
from . import GUI_color
from . import GUI_filter_grid
from . import GUI_filter_properties
from . import GUI_layer_dialogs
from . import GUI_layer_grid
from . import GUI_main_window
from . import GUI_materials
from . import GUI_optimization
from . import GUI_plot
from . import GUI_preproduction
from . import GUI_stack
from . import GUI_target_grid
from . import GUI_targets
from . import GUI_validators



########################################################################
#                                                                      #
# Filters_GUI                                                          #
#                                                                      #
########################################################################
class Filters_GUI(wx.App):
	"""Graphical user interface for OpenFilters"""
	
	
	######################################################################
	#                                                                    #
	# OnInit                                                             #
	#                                                                    #
	######################################################################
	def OnInit(self):
		"""Initialize the graphical user interface
		
		This method is automatically called when the instance is
		initialized. It takes no arguments and returns a boolean value
		indicating if it the application was successfully initialized."""
		
		main_window = GUI_main_window.main_window(None)
		self.SetTopWindow(main_window)
		
		return True
		
