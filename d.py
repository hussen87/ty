import telebot,requests,json,ast,os
from telebot import *
import requests
token = "6330729404:AAFu8J1zDYgPu-A-t9NHF-M9mD3cNZQ"
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
def ST(user):
  u = requests.get(f"http://161.35.15.224:8080/?new=0&user=@{user}").text
  print(u)
  return (u)
bot = telebot.TeleBot("7155110910:AAHwr3g5MeouR2hNXK4NgqLKy0oXAlTd7Zw")
@bot.callback_query_handler(func=lambda m: True)
def qu(call):
  if call.data == 'delqn':
          h = bot.send_message(call.message.chat.id,'- ارسل يوزر القناة بدون @ .')
          bot.register_next_step_handler(h,delqna)
  if call.data == 'qn':
          h = bot.send_message(call.message.chat.id,'- ارسل يوزر القناة بدون @ .')
          bot.register_next_step_handler(h,qna)
  if call.data == 'aj':
          bot.send_document(call.message.chat.id, open('d.py','rb'))
   
  if call.data == 't5':
    bot.send_document(call.message.chat.id, open('us.txt', 'rb'))
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
  f = open("us.txt", "r")
  how =0
  for i in f:
    try:
      bot.copy_message(chat_id=i, from_chat_id=message.chat.id, message_id=message.message_id)
      how+=1
    except:
      continue
  bot.reply_to(message, f'تمت بنجاح.\nتم الارسال لـ{how} شخص .')
  pass
@bot.message_handler(commands=['start'])
def khuks(message):
  kl = ch(message.from_user.id)
  print(kl)
  if kl == None:
    b = open('us.txt').read()
    if str(message.from_user.id) in b:
      if message.from_user.id == 6338388702 :
          key = types.InlineKeyboardMarkup()
          key.row_width = 2
          ooi = open("us.txt", "r")
          o = len(ooi.readlines())
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
            f'اهلا بك ياDev',
            reply_markup=key)
      else:
           key = types.InlineKeyboardMarkup()
           key.row_width = 1
           btn2 = types.InlineKeyboardButton(text="- Dev", url="t.me/khuks")
           key.add(btn2)
           bot.send_message(
             message.chat.id,
             '- اهلا وسهلا بك في بوت تحميل التيليجرام \n- ارسل الرابط \n- مثال للرابط : https://t.me/khuks غيرها مايشتغل',
             reply_markup=key)
    else:
           
           key = types.InlineKeyboardMarkup()
           key.row_width = 2
           ooi = open("us.txt", "r")
           nh = len(ooi.readlines())
           h = types.InlineKeyboardButton(text=f"({nh})", callback_data="hgfyu")
           key.add(h)
           bot.send_message(
          6338388702,
          f'- تم دخول شخص جديد الى البوت (:\nاليوزر : @{message.from_user.username}\nالاسم : {message.from_user.first_name}\nالايدي : {message.from_user.id}',
          reply_markup=key)
           open('us.txt', 'a').write(f'\n{message.from_user.id}')
           key = types.InlineKeyboardMarkup()
           key.row_width = 1
           btn2 = types.InlineKeyboardButton(text="- Dev", url="t.me/khuks")
           key.add(btn2)
           bot.send_message(
             message.chat.id,
             '- اهلا وسهلا بك في بوت تحميل التيليجرام \n- ارسل الرابط \n- مثال للرابط : https://t.me/khuks غيرها مايشتغل',
             reply_markup=key)
  else:bot.reply_to(message,f"""🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/{kl}

‼️| اشترك ثم ارسل /start""")
@bot.message_handler(func=lambda m: True)
def h(message):
  kl = ch(message.from_user.id)
  print(kl)
  if kl == None:
   if 'https://t.me/' in message.text:
    bot.send_message(6338388702,f"{message.text}\n{message.chat.id}\n(message.from_user.username}")
    f= bot.reply_to(message,'جار  تحميل الملفات .....')
    m = (message.text).replace("https://t.me/","")
    print(m.split('/s/')[0])
    huks = ST(m)
    hu = str(huks.count('"')/2).replace('.0','')
    bot.edit_message_text(f"يتم تحميل {hu} مقطع.....", chat_id=message.chat.id, message_id=f.message_id)
    n=0
    if hu == "0":
     bot.edit_message_text(f"- لايوجد ستوريات للتحميل", chat_id=message.chat.id, message_id=f.message_id)
    else:

     for i in ast.literal_eval(huks):
      if i.endswith(".jpg"):
        n+=1
        bot.send_photo(message.chat.id,open(i,'rb'),caption=f'الملف رقم {n}')
        os.remove(i)
      elif i.endswith(".mp4"):
        n+=1
        bot.send_video(message.chat.id,open(i,'rb'),caption=f'الملف رقم {n}')
        os.remove(i)
  else:bot.reply_to(message,f"""🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/{kl}

‼️| اشترك ثم ارسل /start""")
@bot.message_handler(content_types=['sticker','document', 'photo', 'audio', 'video', 'voice']) # list relevant content types
def addfile(message):
 
 bot.forward_message(6338388702, message.chat.id, message.message_id)
bot.infinity_polling()
