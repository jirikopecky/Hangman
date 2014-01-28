#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import wx
import gui
import random
import keyboard

class MainWindow(gui.MainWindow):
    def __init__(self, parent=None):
        gui.MainWindow.__init__(self, parent)
        self.Center()

        self.Words = ("black", "blue", "white", "red", "green", "yellow", "purple", "pink", "gray", "orange")
        self.Word = ""

        self._ClearStats()

        self.StartNewGame()
                
    def StartNewGame(self):
        self.Word = self._GetRandomWord()
        self.HiddenWord = self._GetHiddenWord(self.Word)
        
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
        if self.Word != self.HiddenWord:
            self._StatsRecordLoose()

        self.StartNewGame()

    def LoadButtonClicked( self, event ):
        dialog = wx.FileDialog(self, "Open new words file", wildcard = "Hangman files (*.hgm)|*.hgm", style= wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        self.Words = []
        with open(dialog.GetPath()) as f:
            for line in f.readlines():
                self.Words.append(line.strip())
        
        self._ClearStats()
        self.StartNewGame()
        
    def HandleKeyPressed(self, key):
        if key == "Ctrl+N":
            self.StartNewGame()
        elif key == "Ctrl+O":
            self.LoadButtonClicked(None)
        elif key == "Ctrl+X":
            self.Close()
        elif len(key) == 1 and key.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self._HandleCharLetter(key.upper())

    def _GetRandomWord(self):
        word = random.choice(self.Words).upper()
        while word==self.Word:
            word = random.choice(self.Words).upper()

        return word

    def _HandleCharLetter(self, letter):
        self._DisableButtonByLetter(letter)

        if letter in self.Word:
            self._ShowChars(letter)
            
            if self.HiddenWord == self.Word:
                self._StatsRecordWin()
                self.m_word.SetForegroundColour('GREEN')
                self._DisableButtons()
        else:
            self.Lives -= 1
            self.m_gauge_lives.SetValue(self.Lives)
            
            if self.Lives == 0:
                self._StatsRecordLoose()
                self.m_word.SetValue(self.Word)
                self.HiddenWord = self.Word
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

    def _GetHiddenWord(self, word):
        hidden = ""

        for i in range(0, len(word)):
            if word[i] == " ":
                hidden += " "
            else:
                hidden += "*"

        return hidden

    def _ClearStats(self):
        self.StatGames = 0
        self.StatWins = 0
        self.StatLoses = 0
        
        self._RefreshStats()
        
    def _StatsRecordWin(self):
        self.StatGames += 1
        self.StatWins += 1
        self._RefreshStats()

    def _StatsRecordLoose(self):
        self.StatGames += 1
        self.StatLoses += 1
        self._RefreshStats()

    def _RefreshStats(self):
        self.m_gamesPlayed.SetLabel(str(self.StatGames))
        self.m_gamesWon.SetLabel(str(self.StatWins))
        self.m_gamesLost.SetLabel(str(self.StatLoses))

        if self.StatGames > 0:
            self.m_successPercent.SetLabel(str( int(100.0 * self.StatWins / self.StatGames) ))
        else:
            self.m_successPercent.SetLabel('0')

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
        self.SetCallFilterEvent(True)
        return True

    def FilterEvent(self, evt):
        if evt.GetEventType() == wx.wxEVT_KEY_DOWN:
            #print keyboard.GetKeyPress(evt)
            self.frame.HandleKeyPressed(keyboard.GetKeyPress(evt))
        else:
            evt.Skip()

def main():
    app = App(0)
    app.MainLoop()
 
if __name__ == '__main__':
    main()
