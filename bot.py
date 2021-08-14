# @mrjeluxe ©️ coshgyn
#jlbots
import os
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from googletrans import Translator
TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", 12345))

API_HASH = os.environ.get("API_HASH", "")
app = Client(
        "Gtt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )

@app.on_message(filters.private & filters.command(['start']))
async def start(client, message):
	await message.reply_text(text =f"Salam **{message.from_user.first_name }** 🙋 \n\n __Mən tərcüməçi botam 🙆 \n Mən istənilən sözü/cümləni/paraqrafı sənin seçdiyin dilə çevirə bilirəm 🙇 \n İndi mənə tərcümə etmək istədiyin mesajı göndər🙂__ \n **/help yazaraq daha ətraflı məlumat alın.**",reply_to_message_id = message.message_id ,parse_mode="markdown", reply_markup=InlineKeyboardMarkup([ [                    InlineKeyboardButton("Etiraf Botumuz 🤖" ,url="https://t.me/EtirafStoryBot?start") ],               [InlineKeyboardButton("Abunə ol🧐", url="https://t.me/EtirafStory") ],               [InlineKeyboardButton("Sahibim👨🏻‍💻", url="https://t.me/MenZroyam") ]  ]  ) )

@app.on_message(filters.private & filters.command(['help']))
async def help(client, message):
	await message.reply_text(text =f"Salam **{message.from_user.first_name }** 🙋 \n\n **Mən tərcüməçi botam 🙆 \n Sizin işinizi dahada asanlaşdırmaq üçün yaradılmışam. 🙇 \n Mənə tərcümə etmək istədiyin mesajı göndər və tərcümə etmək istədiyin dili seç. **",reply_to_message_id = message.message_id ,parse_mode="markdown", reply_markup=InlineKeyboardMarkup([    [InlineKeyboardButton("Məlumatℹ", url="https://telegra.ph/AZ-Translate-08-13-2") ], [InlineKeyboardButton("Sahibim👨🏻‍💻", url="https://t.me/MenZroyam") ]  ]  ) )
                                  
	
@app.on_message(filters.private & filters.text  )
async def echo(client, message):
	
 
 keybord1= InlineKeyboardMarkup( [
        [ 
            InlineKeyboardButton("Afrikanca", callback_data='af'),
             InlineKeyboardButton("Albanca", callback_data='sq'),
            InlineKeyboardButton("Amharca",callback_data ='am'),
        ],
        [   InlineKeyboardButton("Ərəbcə", callback_data='ar'),
        InlineKeyboardButton("Ermənicə", callback_data='hy'),      
        InlineKeyboardButton("Azərbaycanca",callback_data = 'az'),        
        ],
        [InlineKeyboardButton("Baskca",callback_data ="eu"),
        	 InlineKeyboardButton("Belarusca",callback_data ="be"),       	
	InlineKeyboardButton("Benqalca",callback_data="bn")],
	
	[InlineKeyboardButton("Bosnakca",callback_data = "bs"),
	InlineKeyboardButton("Bulqarca",callback_data ="bg"),
	InlineKeyboardButton("Katalanca",callback_data = "ca")
	],
	[ 
	InlineKeyboardButton("Korsikaca",callback_data ="co"),
	InlineKeyboardButton("Xorvatca",callback_data = "hr"),
	InlineKeyboardButton("Çexcə", callback_data = "cs"),
	],
	[ InlineKeyboardButton("Danimarkaca",callback_data = "da"),
	InlineKeyboardButton("Hollandca",callback_data = "nl"),
	InlineKeyboardButton("Esperantoca",callback_data = "eo"),	 
	],
	[InlineKeyboardButton(" Növbəti⏩",callback_data = "page2")
	]
	] )
	
 await  message.reply_text("Dili seç 👇",reply_to_message_id = message.message_id, reply_markup = keybord1) 


@app.on_callback_query()
async def translate_text(bot,update):
  keybord6 =  InlineKeyboardMarkup([
       [InlineKeyboardButton("Taylandca",callback_data = "th"),
       InlineKeyboardButton("Türkcə",callback_data = "tr"),
       InlineKeyboardButton("Türkməncə",callback_data ="tk")     
       ],
       [InlineKeyboardButton("Ukranca",callback_data = "uk"),
       InlineKeyboardButton("Urduca",callback_data = "ur"),
       InlineKeyboardButton("Uyğurca",callback_data ="ug")
       
       ],
       [InlineKeyboardButton("Özbəkcə",callback_data = "uz"),
       InlineKeyboardButton("Vyetnamca",callback_data ="vi"),
       InlineKeyboardButton("Uelscə",callback_data = "cy")
       
       ],
       [InlineKeyboardButton("Xosaca",callback_data = "xh"),
       InlineKeyboardButton("Yidişcə",callback_data = "yi"),
       InlineKeyboardButton("Yorubaca",callback_data = "yo")],
       [InlineKeyboardButton("⏪Geri",callback_data = "page5")
       
       ]
 ])
  
  keybord5 = InlineKeyboardMarkup([
         [InlineKeyboardButton("Şotlandca",callback_data = "gd"),
         InlineKeyboardButton("Serbcə",callback_data = "sr"),
         InlineKeyboardButton("Sesotoca",callback_data = "st")
         ],
         [InlineKeyboardButton("Sonaca",callback_data ="sn"),
         InlineKeyboardButton("Sindicə",callback_data ="sd"),
         InlineKeyboardButton("Sinhalca",callback_data = "si")
         ],
         [InlineKeyboardButton("Slovakca",callback_data = "sk"),
         InlineKeyboardButton("Slovencə",callback_data = "sl"),
         InlineKeyboardButton("Somalicə",callback_data = "so")
         ],
         [InlineKeyboardButton("Ispanca",callback_data = "es"),
         InlineKeyboardButton("Sundanese",callback_data ="su"),
         InlineKeyboardButton("Suahilicə",callback_data ="sw")
         ],
         [InlineKeyboardButton("İsveçcə",callback_data = "sv"),
         InlineKeyboardButton("Filippincə",callback_data ='tl'),
         InlineKeyboardButton("Tacikcə",callback_data = "tg")
         ],
         [InlineKeyboardButton("Tamilcə",callback_data = "ta"),
         InlineKeyboardButton("Tatarca",callback_data = "tt"),
         InlineKeyboardButton("Teluquca",callback_data = "te")
         ],
         [InlineKeyboardButton("⏪Geri",callback_data = "page4"),
         InlineKeyboardButton("Növbəti⏩",callback_data = "page6")
         ]  ])
   
 
  keybord4 = InlineKeyboardMarkup([
          [InlineKeyboardButton("Malayyaca",callback_data = "ml"),
          InlineKeyboardButton("Maltaca",callback_data = "mt"),
          InlineKeyboardButton("Maoricə",callback_data = "mi")
          ],
          [InlineKeyboardButton("Marathicə",callback_data = "mr"),
          InlineKeyboardButton("Monqolca",callback_data = "mn"),
          InlineKeyboardButton("Myanmaca",callback_data = "my")
          ],
          [InlineKeyboardButton("Nepalca",callback_data ="ne"),
          InlineKeyboardButton("Norveçcə",callback_data = "no"),
          InlineKeyboardButton("Nyanja(Chichewa)",callback_data = "ny")
          ],
          [InlineKeyboardButton("Odia",callback_data = "or"),
          InlineKeyboardButton("Puştuca",callback_data = "ps"),
          InlineKeyboardButton("Farsca",callback_data = "fa"),
          ],
          [InlineKeyboardButton("Polyakca",callback_data = "pl"),
          InlineKeyboardButton("Portuqalca",callback_data = "pt"),
          InlineKeyboardButton("Pəncabca",callback_data = "pa"),
          ],
          [InlineKeyboardButton("Romanca",callback_data = "ro"),
          InlineKeyboardButton("Rusca",callback_data = "ru"),
          InlineKeyboardButton("Samoaca",callback_data= "sm"),
          ],
          [InlineKeyboardButton("⏪Geri",callback_data = "page3"),
          InlineKeyboardButton("Növbəti⏩",callback_data = "page5")
          ]
          
 
 
 
 ])
  
  
  keybord3 = InlineKeyboardMarkup([
                [ InlineKeyboardButton("Italyanca",callback_data = "it"),
                InlineKeyboardButton("Yaponca",callback_data = "ja"),
                InlineKeyboardButton("Yavaca",callback_data = "jv")
                ],
                [InlineKeyboardButton("Kannadaca",callback_data = "kn"),
                InlineKeyboardButton("Qazaxca",callback_data = "kk"),
                InlineKeyboardButton("Khmer",callback_data = "km")
                ],
                [InlineKeyboardButton("Kinyarvandaca",callback_data = "rw"),
                InlineKeyboardButton("Koreaca",callback_data ="ko"),
                InlineKeyboardButton("Kürdcə",callback_data = "ku")
                ],
                [ InlineKeyboardButton("Qırğızca",callback_data ="ky"),
                InlineKeyboardButton("Lao'ca",callback_data = "lo"),
                InlineKeyboardButton("Latınca",callback_data = "la")
                ],
                [InlineKeyboardButton("Latışca",callback_data = "lv"),
                InlineKeyboardButton('Litvanca',callback_data ="lt"),
                InlineKeyboardButton("Luksenburqca",callback_data = "lb")
                ],
                [InlineKeyboardButton("Makedonca",callback_data = "mk"),
                InlineKeyboardButton("Malagasicə",callback_data ="mg"),
                InlineKeyboardButton("Malayca",callback_data ="ms")
                ],
                [InlineKeyboardButton("⏪Geri",callback_data = "page2"),
                InlineKeyboardButton(" Növbət⏩",callback_data = "page4")
                ]
              
 
 ])
  
  
  keybord1= InlineKeyboardMarkup( [
        [ 
            InlineKeyboardButton("Afrikanca", callback_data='af'),
             InlineKeyboardButton("Albanca", callback_data='sq'),
            InlineKeyboardButton("Amarikcə",callback_data ='am'),
        ],
        [   InlineKeyboardButton("Ərəbcə", callback_data='ar'),
        InlineKeyboardButton("Ermənicə", callback_data='hy'),      
        InlineKeyboardButton("Azərbaycanca",callback_data = 'az'),        
        ],
        [InlineKeyboardButton("Baskca",callback_data ="eu"),
        	 InlineKeyboardButton("Belarusca",callback_data ="be"),       	
	InlineKeyboardButton("Benqalca",callback_data="bn")],
	
	[InlineKeyboardButton("Bosniyaca",callback_data = "bs"),
	InlineKeyboardButton("Bolqarca",callback_data ="bg"),
	InlineKeyboardButton("Katalanca",callback_data = "ca")
	],
	[ 
	InlineKeyboardButton("Korsikanca",callback_data ="co"),
	InlineKeyboardButton("Xorvatca",callback_data = "hr"),
	InlineKeyboardButton("Çexcə", callback_data = "cs"),
	],
	[ InlineKeyboardButton("Danimarkca",callback_data = "da"),
	InlineKeyboardButton("Hollandca",callback_data = "nl"),
	InlineKeyboardButton("Esperantoca",callback_data = "eo"),	 
	],
	[InlineKeyboardButton(" Növbəti⏩",callback_data = "page2")
	]
	] )
  
  
  keybord2= InlineKeyboardMarkup([
           [InlineKeyboardButton("Ingiliscə",callback_data = "en"),
           InlineKeyboardButton("Estonca",callback_data = "et"),
           InlineKeyboardButton("Fincə(Finlandca)",callback_data = "fi")
           ],
           [InlineKeyboardButton("Fransızca",callback_data = "fr"),
           InlineKeyboardButton("Frizcə",callback_data = "fy"),
           InlineKeyboardButton("Qalisianca",callback_data = "gl")
           ],
           [InlineKeyboardButton("Gürcücə",callback_data = "ka"),
           InlineKeyboardButton("Almanca",callback_data = "de"),
           InlineKeyboardButton("Yunanca",callback_data = "el")
           ],
           [InlineKeyboardButton("Gujarati",callback_data = "gu"),
           InlineKeyboardButton("Haiticə",callback_data = "ht"),
           InlineKeyboardButton("Hausaca",callback_data ="ha")
           ],
           [InlineKeyboardButton("Hindcə",callback_data = "hi"),
           InlineKeyboardButton("Macarca",callback_data = "hu"),
           InlineKeyboardButton("Islandca",callback_data = "is")
           ],
           [InlineKeyboardButton("Igbo",callback_data = "ig"),
           InlineKeyboardButton("Indoneziyaca",callback_data = "id"),
           InlineKeyboardButton("Irlandca",callback_data = "ga")
           ],
           [InlineKeyboardButton("⏪Geri",callback_data = "page1"),
           InlineKeyboardButton(" Növbəti⏩",callback_data = "page3"),
           ]
            ])
						
  
  
  
  tr_text = update.message.reply_to_message.text
  cb_data = update.data
  if cb_data== "page2":
  	await update.message.edit("Dili seç 👇",reply_markup = keybord2)
  elif cb_data == "page1":
  	await update.message.edit("Dili seç 👇",reply_markup =keybord1)
  elif cb_data =="page3":
  	await update.message.edit("Dili seç 👇",reply_markup =keybord3)
  elif cb_data == "page4":
  	await update.message.edit("Dili seç 👇",reply_markup =keybord4)
  elif cb_data =="page5":
  	await update.message.edit("Dili seç 👇",reply_markup =keybord5)
  elif cb_data =="page6":
  	await update.message.edit("Dili seç 👇",reply_markup =keybord6)
  else :
       translator = Translator()  
       translation = translator.translate(tr_text,dest=cb_data) 
       await update.message.edit(translation.text)

				 
app.run()
