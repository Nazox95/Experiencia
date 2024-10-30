#Remember change value for height in
window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 300,
	"height" : 25*14+16, #<---Here

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 300,
			"height" : 25*14+16, #<---And here

			"children" :

	#Now Add in the end 
				#exp
				{
					"name" : "expplus_on_of",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 319, #Put your value

					"text" : uiScriptLocale.OPTION_EXPERIENCE,
				},
				{
					"name" : "experience_on_of_button",
					"type" : "button",

					"x" : LINE_DATA_X,
					"y" : 319, #Same value from expplus_on_of

					"text" : uiScriptLocale.OPTION_EXPERIENCE2,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
