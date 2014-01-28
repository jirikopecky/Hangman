# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hangman", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,400 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_word = wx.TextCtrl( self, wx.ID_ANY, u"HANGMAN", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.m_word.SetFont( wx.Font( 36, 74, 90, 92, False, "Consolas" ) )
		
		bSizer1.Add( self.m_word, 0, wx.ALL|wx.EXPAND, 5 )
		
		buttonsSizer = wx.GridSizer( 4, 7, 0, 0 )
		
		self.m_btn_Key0 = wx.Button( self, wx.ID_ANY, u"A", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key0, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key1 = wx.Button( self, wx.ID_ANY, u"B", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key2 = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key3 = wx.Button( self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key3, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_btn_Key4 = wx.Button( self, wx.ID_ANY, u"E", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key4, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key5 = wx.Button( self, wx.ID_ANY, u"F", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key5, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key6 = wx.Button( self, wx.ID_ANY, u"G", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key6, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key7 = wx.Button( self, wx.ID_ANY, u"H", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key7, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key8 = wx.Button( self, wx.ID_ANY, u"I", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key8, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key9 = wx.Button( self, wx.ID_ANY, u"J", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key9, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key10 = wx.Button( self, wx.ID_ANY, u"K", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key10, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key11 = wx.Button( self, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key11, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key12 = wx.Button( self, wx.ID_ANY, u"M", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key12, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key13 = wx.Button( self, wx.ID_ANY, u"N", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key13, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key14 = wx.Button( self, wx.ID_ANY, u"O", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key14, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key15 = wx.Button( self, wx.ID_ANY, u"P", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key15, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key16 = wx.Button( self, wx.ID_ANY, u"Q", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key16, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key17 = wx.Button( self, wx.ID_ANY, u"R", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key17, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key18 = wx.Button( self, wx.ID_ANY, u"S", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key18, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key19 = wx.Button( self, wx.ID_ANY, u"T", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key19, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key20 = wx.Button( self, wx.ID_ANY, u"U", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key20, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		buttonsSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_btn_Key21 = wx.Button( self, wx.ID_ANY, u"V", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key21, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key22 = wx.Button( self, wx.ID_ANY, u"W", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key22, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key23 = wx.Button( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key23, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key24 = wx.Button( self, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key24, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Key25 = wx.Button( self, wx.ID_ANY, u"Z", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.m_btn_Key25, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		buttonsSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( buttonsSizer, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Lives" ), wx.VERTICAL )
		
		self.m_gauge_lives = wx.Gauge( self, wx.ID_ANY, 6, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_lives.SetValue( 6 ) 
		sbSizer1.Add( self.m_gauge_lives, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer1, 0, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Statistics" ), wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Games played:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_gamesPlayed = wx.StaticText( self, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_gamesPlayed.Wrap( -1 )
		bSizer2.Add( self.m_gamesPlayed, 0, wx.ALL, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Games won", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_gamesWon = wx.StaticText( self, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_gamesWon.Wrap( -1 )
		bSizer2.Add( self.m_gamesWon, 0, wx.ALL, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Games lost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_gamesLost = wx.StaticText( self, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_gamesLost.Wrap( -1 )
		bSizer2.Add( self.m_gamesLost, 0, wx.ALL, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Succes percentage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_successPercent = wx.StaticText( self, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.Size( 25,-1 ), wx.ALIGN_RIGHT )
		self.m_successPercent.Wrap( -1 )
		bSizer2.Add( self.m_successPercent, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer2.Add( self.m_staticText9, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		sbSizer2.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_btn_newGame = wx.Button( self, wx.ID_ANY, u"New Game", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_btn_newGame, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_Load = wx.Button( self, wx.ID_ANY, u"Load Words", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_btn_Load, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer3, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CHAR, self.OnChar )
		self.m_btn_Key0.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key1.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key2.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key3.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key4.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key5.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key6.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key7.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key8.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key9.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key10.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key11.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key12.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key13.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key14.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key15.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key16.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key17.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key18.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key19.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key20.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key21.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key22.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key23.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key24.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_Key25.Bind( wx.EVT_BUTTON, self.LetterButtonClicked )
		self.m_btn_newGame.Bind( wx.EVT_BUTTON, self.NewGameButtonClicked )
		self.m_btn_Load.Bind( wx.EVT_BUTTON, self.LoadButtonClicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnChar( self, event ):
		event.Skip()
	
	def LetterButtonClicked( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def NewGameButtonClicked( self, event ):
		event.Skip()
	
	def LoadButtonClicked( self, event ):
		event.Skip()
	

