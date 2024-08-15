import telebot, requests, os, sys ,json
from datetime import datetime
from bs4 import BeautifulSoup
token = "6330729404:AAFu8J1zDYgPu-A-t9NHF-M9mD3cNZQMpuA"
def lang(la,type):
 if type == '@':
  if la == 'ar':return '- رجاءا ارسل بدون @'
  if la == 'en' or 'ru':return '- please send the username without @'
 if type == 'unkn':
  if la == 'ar':return '- لم افهم الامر'
  if la == 'en' or 'ru':return '- i don`t understand'
 if type =='id':
  if la == 'ar':return 'ايدي'
  if la == 'en':return 'id'
  if la == 'ru':return 'id'
 if type == 'fg':
  if la == 'ar':return 'متابعهم'
  if la == 'en':return 'following'
  if la == 'ru':return 'Он следует за ними'
 if type == 'fs':
  if la == 'ar': return 'متابعين'
  if la == 'en': return 'followers'
  if la =='ru':return 'Последователи'
 if type == 'date':
  if la == 'ar':return 'الانشاء'
  if la == 'en' :return 'date'
  if la == 'ru':return 'Время строительства'
 if type =='lnc':
  if la == 'ar':return 'اخر تغيير للاسم'
  if la == 'en':return 'Last name change'
  if la == 'ru':return 'Фамилия изменена'
 if type == 'name':
  if la == 'ar':return 'الاسم'
  if la == 'en':return 'name'
  if la == 'ru':return 'имя'
 if type == 'con':
  if la == 'ar':return 'الدولة'
  if la == 'en':return 'country'
  if la == 'ru':return 'Страна'
 if type == 'wait':
  if la == 'ar' : return 'انتظر ....'
  if la == 'en' : return 'wait ...'
  if la == 'ru' : return 'Подожди ....'
 if type == 'prop':
  if la == 'ar':return '-توجد مشاكل في البحث .'
  if la == 'ru': return '-Есть проблемы с поиском.'
  if la == 'en': return '-There are problems with the search.'
 if type == 'ترحيب':
  if la == 'ru':return 'Добро пожаловать в бот информации об аккаунте TikTok'
  elif la == 'ar':return 'اهلا بك في بوت معلومات حساب تيك توك'
  elif la == 'en':return 'Welcome to the TikTok account information bot'
 elif 'اجباري:' in type:
  kl = type.split(':')[1]
  if la == 'en':
   return f"""🚸| Sorry dear
🔰| You must subscribe to the bot channel to be able to use it

- https://t.me/{kl}

‼️| Subscribe and send /start"""
  elif la == 'ar':
    
    return f"""🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/{kl}

    ‼️| اشترك ثم ارسل /start"""
  elif la == 'ru':
   return f"""🚸| Прости, дорогая
🔰| Чтобы иметь возможность использовать его, вам необходимо подписаться на канал бота

- https://t.me/{kl} 

‼️ Подпишитесь и отправьте /start"""

def ch(user_id): 
   b=0
   f = open("ch.txt", "r")
   for khuks1 in f:
    kuks = str(khuks1).split(':')[0]
    x = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{kuks}&user_id={user_id}")
    if any(["member" in x.text, "administrator" in x.text, "creator" in x.text]):
        pass
    else:
     return str(khuks1).split(":")[1]
def khuksflag(co):
 return co.replace("Q","🇶").replace("I","🇮").replace("A","🇦").replace('B','🇧').replace('C','🇨').replace('D','🇩').replace('E','🇪').replace('F','🇫').replace('G','🇬').replace('H','🇭').replace('J','🇯').replace('K','🇰').replace('L','🇱').replace('M','🇲').replace('N','🇳').replace('O','🇴').replace('P','🇵').replace('R','🇷').replace('S','🇸').replace('T','🇹').replace('U','🇺').replace('V','🇻').replace('W','🇼').replace('X','🇽').replace('Y','🇾').replace('Z','🇿') 
def tiktok_timestamp(f):           
  binary = '{0:b}'.format(int(f))
  print(binary)
  i = 0
  bits = ""
  while i < 31:
    bits += binary[i]
    i += 1
  timestamp = int(bits, 2)
  dt_object = datetime.fromtimestamp(timestamp)
  return dt_object
from telebot import *
id = 6338388702
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def khuks(message):
  kl = ch(message.from_user.id)
  lan = open("lang.txt").read()
  if kl == None:
      
      bb = open("ban.txt", "r")
      b = open('user.txt').read()
      bo = open('ban.txt').read()
      if str(message.from_user.id) in b:
        if message.from_user.id == 6338388702 :
          key = types.InlineKeyboardMarkup()
          key.row_width = 2
          ooi = open("user.txt", "r")
          o = len(ooi.readlines())
          oi = len(bb.readlines())
          bt = types.InlineKeyboardButton(text=f"- ارسال القنوات الاجبارية .",callback_data='aj')
          btn = types.InlineKeyboardButton(text=f"- مسح قناة اجباري .",callback_data='delqn')
          bn1 = types.InlineKeyboardButton(text=f"- تفعيل قناة اجباري",callback_data='qn')
          h = types.InlineKeyboardButton(text=f"({o})", callback_data="hgfyu")
          btnn = types.InlineKeyboardButton(text="- Dev", url="t.me/khuks")
          btn1 = types.InlineKeyboardButton(text="- اذاعة .",
                                            callback_data="send")
          btn2 = types.InlineKeyboardButton(text="- ارسل التخزين .",
                                            callback_data="t5")
          key.add(btn1,bn1,bt,btn, btn2, h, btnn)
          bot.reply_to(
            message,
            f'اهلا بك ياDev \nعدد المحظورين : {oi}\nلحظر شخص ارسل حظر + الايدي',
            reply_markup=key)
        elif str(message.from_user.id) in bo:

          bot.reply_to(message, 'تم حظرك من البوت راسل Dev لفكه @khuks')

        else:
          if str(message.from_user.id) in lan:
           l = (lan.split(f'{message.from_user.id}:')[1]).split('\n')[0]
           key = types.InlineKeyboardMarkup()
           key.row_width = 1
           btn2 = types.InlineKeyboardButton(text="- Dev", url="t.me/khuks")
           key.add(btn2)
           bot.send_message(
             message.chat.id,
             lang(l,'ترحيب'),
             reply_markup=key)
          else:
           key = types.InlineKeyboardMarkup()
           key.row_width = 3
           btn2 = types.InlineKeyboardButton(text="- русский (🇷🇺)",callback_data="ru")
           btn1 = types.InlineKeyboardButton(text="- English (🇺🇸)",callback_data="en")
           btn3 = types.InlineKeyboardButton(text="- عربي (🇮🇶)",callback_data="ar")
           key.add(btn2,btn1,btn3)
           bot.send_message(
             message.chat.id,
             'Пожалуйста, выберите язык\nPlease choose a language\nارجوك اختر لغة 👇🏿',
             reply_markup=key)
      else:
        key = types.InlineKeyboardMarkup()
        key.row_width = 2
        ooi = open("user.txt", "r")
        nh = len(ooi.readlines())
        h = types.InlineKeyboardButton(text=f"({nh})", callback_data="hgfyu")
        key.add(h)
        bot.send_message(
          6338388702,
          f'- تم دخول شخص جديد الى البوت (:\nاليوزر : @{message.from_user.username}\nالاسم : {message.from_user.first_name}\nالايدي : {message.from_user.id}',
          reply_markup=key)
        open('user.txt', 'a').write(f'\n{message.from_user.id}')
        key = types.InlineKeyboardMarkup()
        key.row_width = 3
        btn2 = types.InlineKeyboardButton(text="- русский (🇷🇺)",callback_data="ru")
        btn1 = types.InlineKeyboardButton(text="- English (🇺🇸)",callback_data="en")
        btn3 = types.InlineKeyboardButton(text="- عربي (🇮🇶)",callback_data="ar")
        key.add(btn2,btn1,btn3)
        bot.send_message(
             message.chat.id,
             'Пожалуйста, выберите язык\nPlease choose a language\nارجوك اختر لغة 👇🏿',
             reply_markup=key)
  else:
    if str(message.from_user.id) in lan:
     l = (lan.split(f'{message.from_user.id}:')[1]).split('\n')[0]
     g = lang(l,f'اجباري:{kl}')
     bot.reply_to(message,g)
    else:
           key = types.InlineKeyboardMarkup()
           key.row_width = 3
           btn2 = types.InlineKeyboardButton(text="- русский (🇷🇺)",callback_data="ru")
           btn1 = types.InlineKeyboardButton(text="- English (🇺🇸)",callback_data="en")
           btn3 = types.InlineKeyboardButton(text="- عربي (🇮🇶)",callback_data="ar")
           key.add(btn2,btn1,btn3)
           bot.send_message(
             message.chat.id,
             'Пожалуйста, выберите язык\nPlease choose a language\nارجوك اختر لغة 👇🏿',
             reply_markup=key)
@bot.message_handler(regexp='المحظورين')
def f(message):
  bot.reply_to(message, open('ban.txt').read())


@bot.callback_query_handler(func=lambda m: True)
def qu(call):
  if call.data == "en":
   if str(call.from_user.id) in open("lang.txt").read():
    j= (open("lang.txt").read())
    J = (open("lang.txt").read()).split(f'{call.from_user.id}:')[1]
    Jj = J.split('\n')[0]
    print(str(call.from_user.id)+Jj)
    HU=(j.replace(f'{call.from_user.id}:{Jj}',f'{call.from_user.id}:en'))
    print(HU)
    open('lang.txt','w').write(HU)
    bot.reply_to(call.message,'The language has been changed to English\n- send /start')
   else:
    open('lang.txt', 'a').write(f'\n{call.from_user.id}:en')
    bot.send_message(call.message.chat.id,'English language was selected\n- send /start')
  if call.data == "ar":
   if str(call.from_user.id) in open("lang.txt").read():
    j= (open("lang.txt").read())
    J = (open("lang.txt").read()).split(f'{call.from_user.id}:')[1]
    Jj = J.split('\n')[0]
    print(str(call.from_user.id)+Jj)
    HU=(j.replace(f'{call.from_user.id}:{Jj}',f'{call.from_user.id}:ar'))
    print(HU)
    open('lang.txt','w').write(HU)
    bot.reply_to(call.message,'تم تغيير اللغة الى العربية .\n- ارسل /start')
   else:
    open('lang.txt', 'a').write(f'\n{call.from_user.id}:ar')
    bot.send_message(call.message.chat.id,'- تم اختيار اللغة العربية .\n- ارسل /start')
    
  if call.data == "ru":
   if str(call.from_user.id) in open("lang.txt").read():
    j= (open("lang.txt").read())
    J = (open("lang.txt").read()).split(f'{call.from_user.id}:')[1]
    Jj = J.split('\n')[0]
    print(str(call.from_user.id)+Jj)
    HU=(j.replace(f'{call.from_user.id}:{Jj}',f'{call.from_user.id}:ru'))
    print(HU)
    open('lang.txt','w').write(HU)
    bot.reply_to(call.message,'Перешел на русский язык\n- /start')
   else:
    open('lang.txt', 'a').write(f'\n{call.from_user.id}:ru')
    bot.send_message(call.message.chat.id,'Был выбран русский язык.\n- /start')
  if call.data == 'delqn':
          h = bot.send_message(call.message.chat.id,'- ارسل يوزر القناة بدون @ .')
          bot.register_next_step_handler(h,delqna)
  if call.data == 'qn':
          h = bot.send_message(call.message.chat.id,'- ارسل يوزر القناة بدون @ .')
          bot.register_next_step_handler(h,qna)
  if call.data == 'aj':
          bot.send_document(call.message.chat.id, open('info.py','rb'))
   
  if call.data == 't5':
    bot.send_document(call.message.chat.id, open(('user.txt'), 'rb'))
  if call.data == "send":
    g = bot.send_message(call.message.chat.id, '- ارسل الرسالة للأذاعة .')
    bot.register_next_step_handler(g, khuks)

def delqna(message):
 f = open("ch.txt", "r").read()
 HU=(f.replace(f'\n{message.text}',''))
 open('ch.txt','w').write(HU)
 bot.reply_to(message,f'تم حذف القناة {message.text} بنجاح .')
def qna(message):
 open('ch.txt','a').write(f'{message.text}')
 bot.reply_to(message,f'تم اضافة القناة {message.text} بنجاح .')
def khuks(message):
  f = open("user.txt", "r")
  how =0
  for i in f:
    try:
      bot.copy_message(chat_id=i, from_chat_id=message.chat.id, message_id=message.message_id)
      how+=1
    except:
      continue
  bot.reply_to(message, f'تمت بنجاح.\nتم الارسال لـ{how} شخص .')
  pass

@bot.message_handler(regexp='حظر')
def f(message):
  if message.from_user.id == 6338388702 or message.from_user.id == 5543149965:
    id = message.text.replace('حظر ', '')
    open('ban.txt', 'a').write(f'\n{id}')
    bot.reply_to(message, f'تم حظر {id} بنجاح')
  else:
    bot.reply_to(message, 'انت لست Dev')


@bot.message_handler(func=lambda m: True)
def h(message):
 lan = open("lang.txt").read()
 if '@' in message.text:
  if str(message.from_user.id) in lan:
   l = (lan.split(f'{message.from_user.id}:')[1]).split('\n')[0]
   bot.reply_to(message,lang(l,'@'))
  else:
   bot.reply_to(message,'- please send /start')
 else:
  if str(message.from_user.id) in lan:
   kl = ch(message.from_user.id)
   if kl == None:
       l = (lan.split(f'{message.from_user.id}:')[1]).split('\n')[0]
       b = open('ban.txt').read()
 
       if str(message.from_user.id) in b:
         bot.reply_to(message, 'تم حظرك من البوت راسل Dev لفكه @khuks')
       else:
 
         bot.reply_to(message, lang(l,'wait'))
         user = message.text
         h = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
         rt = requests.get(f"https://www.tiktok.com/@{user}", headers=h)
         server_log = str(rt.text)
         def reg():
            try:
             soup = BeautifulSoup(server_log, 'html.parser')
             
             
             script_tag = soup.find('script', {'id': '__UNIVERSAL_DATA_FOR_REHYDRATION__'})
             script_text = script_tag.text.strip()
             data = json.loads(script_text)["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
 
             hh = data["stats"]["followingCount"]
             time = data["user"]["nickNameModifyTime"]
             cd = datetime.fromtimestamp(int(time))
             r=data["user"]["region"]
             se =data["user"]["nickname"]
             id = data["user"]["id"]
             fs = data["stats"]["followerCount"]
     
            
             return f'{r};{cd};{hh};{fs};{se};{id}'
            except Exception as e:
             print(e)
             return ("nothing")
         h = reg()
         
         if h=='nothing':bot.reply_to(message,lang(l,'prop'))
         else:
          print(h)
       
          fg=h.split(';')[2]
          co =h.split(';')[0]
          cd =h.split(';')[1]
          c = khuksflag(co)
          fs = h.split(';')[3]
          name =h.split(';')[4]
          id = h.split(';')[5]
          date = tiktok_timestamp(id)
          msg = f"- {lang(l,'con')} ({c} - {co})•\n- {lang(l,'date')} ({date})•\n- {lang(l,'id')} ({id})•\n- {lang(l,'lnc')} ({cd})•\n- {lang(l,'fg')} ({fg})•\n- {lang(l,'fs')} ({fs})•\n- {lang(l,'name')} ({name})• "
          bot.send_message(message.chat.id,
                            f'''- Done sir .
 - By : @khuks (Iraqi) Ch : @iHuks . 
 {msg}''',
                            reply_to_message_id=message.message_id)
 
         
   else:
     if str(message.from_user.id) in lan:
      l = (lan.split(f'{message.from_user.id}:')[1]).split('\n')[0]
      g = lang(l,f'اجباري:{kl}')
      bot.reply_to(message,g)
     else:
            key = types.InlineKeyboardMarkup()
            key.row_width = 3
            btn2 = types.InlineKeyboardButton(text="- русский (🇷🇺)",callback_data="ru")
            btn1 = types.InlineKeyboardButton(text="- English (🇺🇸)",callback_data="en")
            btn3 = types.InlineKeyboardButton(text="- عربي (🇮🇶)",callback_data="ar")
            key.add(btn2,btn1,btn3)
            bot.send_message(
              message.chat.id,
              'Пожалуйста, выберите язык\nPlease choose a language\nارجوك اختر لغة 👇🏿',
              reply_markup=key)
  else:bot.send_message(message.chat.id,'''- ارسل /start لغرض التحديث ❤️
- Send /start for update 
- Отправить /start для обновления .''')

@bot.message_handler(content_types=['document', 'photo', 'audio', 'video', 'voice']) # list relevant content types
def addfile(message):
 
 bot.forward_message(id, message.chat.id, message.message_id)
bot.infinity_polling()
