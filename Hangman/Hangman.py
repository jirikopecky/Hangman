#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import wx
import gui
import random

class MainWindow(gui.MainWindow):
    def __init__(self, parent=None):
        gui.MainWindow.__init__(self, parent)
        self.Center()

        self.Words = ("black", "blue", "white", "red", "green", "yellow", "purple", "pink", "gray", "orange")

        self.StartNewGame()

        self.SetFocus()
                
    def StartNewGame(self):
        self.Word = random.choice(self.Words).upper()
        self.HiddenWord = self._GetHiddenWord()
        
        self.Lives = 6
        self.m_word.SetValue(self.HiddenWord)
        self.m_gauge_lives.SetRange(self.Lives)
        self.m_gauge_lives.SetValue(self.Lives)

        self._EnableButtons()
        self.m_word.SetForegroundColour('BLACK')
        
    def LetterButtonClicked( self, event ):
        button = event.GetEventObject()
        letter = button.Label
        
        self._HandleCharLetter(letter)
    
    def NewGameButtonClicked( self, event ):
        self.StartNewGame()

    def LoadButtonClicked( self, event ):
        dialog = wx.FileDialog(self, "Open new words file", wildcard = "Hangman files (*.hgm)|*.hgm", style= wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        self.Words = []
        with open(dialog.GetFilename()) as f:
            for line in f.readlines():
                self.Words.append(line.strip())
        
        self.StartNewGame()

    def OnChar(self, event):
        keycode = event.GetUnicodeKey()

        if keycode != wx.WXK_NONE:
            if keycode == wx.WXK_CONTROL_N:
                self.StartNewGame()
                return
            elif keycode == wx.WXK_CONTROL_O:
                self.LoadButtonClicked(None)
                return
            elif keycode == wx.WXK_CONTROL_X:
                self.Close()
                return

            char = chr(keycode).upper()
            self._HandleCharLetter(char)

    def _HandleCharLetter(self, letter):
        self._DisableButtonByLetter(letter)

        if letter in self.Word:
            self._ShowChars(letter)
            
            if self.HiddenWord == self.Word:
                self.m_word.SetForegroundColour('GREEN')
                self._DisableButtons()
        else:
            self.Lives -= 1
            self.m_gauge_lives.SetValue(self.Lives)
            
            if self.Lives == 0:
                self.m_word.SetValue(self.Word)
                self.m_word.SetForegroundColour('RED')
                self.m_word.Refresh()
                self._DisableButtons()

    def _ShowChars(self, char):
        newWord = ""

        for i in range(0, len(self.Word)):
            if self.Word[i] == char:
                newWord = newWord + self.Word[i]
            else:
                newWord = newWord + self.HiddenWord[i]

        self.HiddenWord = newWord
        self.m_word.SetValue(self.HiddenWord)

    def _GetHiddenWord(self):
        hidden = ""

        for i in range(0, len(self.Word)):
            if self.Word[i] == " ":
                hidden += " "
            else:
                hidden += "*"

        return hidden

    def _DisableButtonByLetter(self, letter):
        letter = letter.upper()

        if letter=="A":
            self.m_btn_Key0.Disable()
        elif letter=="B":
            self.m_btn_Key1.Disable()
        elif letter=="C":
            self.m_btn_Key2.Disable()
        elif letter=="D":
            self.m_btn_Key3.Disable()
        elif letter=="E":
            self.m_btn_Key4.Disable()
        elif letter=="F":
            self.m_btn_Key5.Disable()
        elif letter=="G":
            self.m_btn_Key6.Disable()
        elif letter=="H":
            self.m_btn_Key7.Disable()
        elif letter=="I":
            self.m_btn_Key8.Disable()
        elif letter=="J":
            self.m_btn_Key9.Disable()
        elif letter=="K":
            self.m_btn_Key10.Disable()
        elif letter=="L":
            self.m_btn_Key11.Disable()
        elif letter=="M":
            self.m_btn_Key12.Disable()
        elif letter=="N":
            self.m_btn_Key13.Disable()
        elif letter=="O":
            self.m_btn_Key14.Disable()
        elif letter=="P":
            self.m_btn_Key15.Disable()
        elif letter=="Q":
            self.m_btn_Key16.Disable()
        elif letter=="R":
            self.m_btn_Key17.Disable()
        elif letter=="S":
            self.m_btn_Key18.Disable()
        elif letter=="T":
            self.m_btn_Key19.Disable()
        elif letter=="U":
            self.m_btn_Key20.Disable()
        elif letter=="V":
            self.m_btn_Key21.Disable()
        elif letter=="W":
            self.m_btn_Key22.Disable()
        elif letter=="X":
            self.m_btn_Key23.Disable()
        elif letter=="Y":
            self.m_btn_Key24.Disable()
        elif letter=="Z":
            self.m_btn_Key25.Disable()

    def _DisableButtons(self):
        self.m_btn_Key0.Disable()
        self.m_btn_Key1.Disable()
        self.m_btn_Key2.Disable()
        self.m_btn_Key3.Disable()
        self.m_btn_Key4.Disable()
        self.m_btn_Key5.Disable()
        self.m_btn_Key6.Disable()
        self.m_btn_Key7.Disable()
        self.m_btn_Key8.Disable()
        self.m_btn_Key9.Disable()
        self.m_btn_Key10.Disable()
        self.m_btn_Key11.Disable()
        self.m_btn_Key12.Disable()
        self.m_btn_Key13.Disable()
        self.m_btn_Key14.Disable()
        self.m_btn_Key15.Disable()
        self.m_btn_Key16.Disable()
        self.m_btn_Key17.Disable()
        self.m_btn_Key18.Disable()
        self.m_btn_Key19.Disable()
        self.m_btn_Key20.Disable()
        self.m_btn_Key21.Disable()
        self.m_btn_Key22.Disable()
        self.m_btn_Key23.Disable()
        self.m_btn_Key24.Disable()
        self.m_btn_Key25.Disable()

    def _EnableButtons(self):
        self.m_btn_Key0.Enable()
        self.m_btn_Key1.Enable()
        self.m_btn_Key2.Enable()
        self.m_btn_Key3.Enable()
        self.m_btn_Key4.Enable()
        self.m_btn_Key5.Enable()
        self.m_btn_Key6.Enable()
        self.m_btn_Key7.Enable()
        self.m_btn_Key8.Enable()
        self.m_btn_Key9.Enable()
        self.m_btn_Key10.Enable()
        self.m_btn_Key11.Enable()
        self.m_btn_Key12.Enable()
        self.m_btn_Key13.Enable()
        self.m_btn_Key14.Enable()
        self.m_btn_Key15.Enable()
        self.m_btn_Key16.Enable()
        self.m_btn_Key17.Enable()
        self.m_btn_Key18.Enable()
        self.m_btn_Key19.Enable()
        self.m_btn_Key20.Enable()
        self.m_btn_Key21.Enable()
        self.m_btn_Key22.Enable()
        self.m_btn_Key23.Enable()
        self.m_btn_Key24.Enable()
        self.m_btn_Key25.Enable()

class App(wx.App):
    def OnInit(self):
        self.frame = MainWindow()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = App(0)
    app.MainLoop()
 
if __name__ == '__main__':
    main()
