#Add
import net

#Add in Class OptionDialog(ui.ScriptWindow): in def __Initialize(self):
	def __Initialize(self):
		self.titleBar = 0
		self.nameColorModeButtonList = []
    [..]
    #EXP
		self.expplus_btn = None

#Now  in 	def __Load_BindObject(self): add
	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.nameColorModeButtonList.append(GetObject("name_color_normal"))
			[..]
			#EXP
			self.expplus_btn = GetObject("experience_on_of_button")

#Now in 	def __Load(self): add

	def __Load(self):
		[..]
		self.nameColorModeButtonList[0].SAFE_SetEvent(self.__OnClickNameColorModeNormalButton)
		self.nameColorModeButtonList[1].SAFE_SetEvent(self.__OnClickNameColorModeEmpireButton)
		[..]
		#EXP
		self.expplus_btn.SAFE_SetEvent(self.__OnClickExpPlusButton)

#add in the end
	def __OnClickExpPlusButton(self):
			net.SendChatPacket("/exp_text")
	
