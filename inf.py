import telebot, requests, os, sys 
from datetime import datetime
from bs4 import BeautifulSoup
token = "5894588181:AAFl7Qi-OctrJPg86D0-HN-FgdI0brUTXbs"
def ch(user_id):
   b=0
   f = open("ch.txt", "r")
   for huks in f:
    x = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{huks}&user_id={user_id}")
    
    if any(["member" in x.text, "administrator" in x.text, "creator" in x.text]):
        pass
    else:
     return None
def huksflag(co):
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

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def huks(message):

  kl = ch(message.from_user.id)
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
          btnn = types.InlineKeyboardButton(text="- المطور", url="t.me/itsnathaile")
          btn1 = types.InlineKeyboardButton(text="- اذاعة .",
                                            callback_data="send")
          btn2 = types.InlineKeyboardButton(text="- ارسل التخزين .",
                                            callback_data="t5")
          key.add(btn1,bn1,bt,btn, btn2, h, btnn)
          bot.reply_to(
            message,
            f'اهلا بك ياالمطور \nعدد المحظورين : {oi}\nلحظر شخص ارسل حظر + الايدي',
            reply_markup=key)
        elif str(message.from_user.id) in bo:

          bot.reply_to(message, 'تم حظرك من البوت راسل المطور لفكه @itsnathaile - @i_m_q')

        else:

          key = types.InlineKeyboardMarkup()
          key.row_width = 1
          btn2 = types.InlineKeyboardButton(text="- المطور", url="t.me/itsnathaile")
          key.add(btn2)
          bot.send_message(
            message.chat.id,
            'تم نقل البوت الى هنا @Tiktokinfor_bot',
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
        key.row_width = 1
        btn2 = types.InlineKeyboardButton(text="- المطور", url="t.me/itsnathaile")
        key.add(btn2)

        bot.send_message(
          message.chat.id,
          'تم نقل البوت الى هنا @Tiktokinfor_bot',
          reply_markup=key)
  else:bot.reply_to(message,f'''🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/{kl}

    ‼️| اشترك ثم ارسل /start''')
@bot.message_handler(regexp='المحظورين')
def f(message):
  bot.reply_to(message, open('ban.txt').read())


@bot.callback_query_handler(func=lambda m: True)
def qu(call):
  if call.data == 'delqn':
          h = bot.send_message(call.message.chat.id,'- ارسل يوزر القناة بدون @ .')
          bot.register_next_step_handler(h,delqna)
  if call.data == 'qn':
          h = bot.send_message(call.message.chat.id,'- ارسل يوزر القناة بدون @ .')
          bot.register_next_step_handler(h,qna)
  if call.data == 'aj':
          bot.send_document(call.message.chat.id, open('info.py','rb'))
   
  if call.data == 't5':
    bot.send_document(call.message.chat.id, open('user.txt'), 'rb')
  if call.data == "send":
    g = bot.send_message(call.message.chat.id, '- ارسل الرسالة للأذاعة .')
    bot.register_next_step_handler(g, huks)

def delqna(message):
 f = open("ch.txt", "r").read()
 HU=(f.replace(f'\n{message.text}',''))
 open('ch.txt','w').write(HU)
 bot.reply_to(message,f'تم حذف القناة {message.text} بنجاح .')
def qna(message):
 open('ch.txt','a').write(f'{message.text}')
 bot.reply_to(message,f'تم اضافة القناة {message.text} بنجاح .')
def huks(message):
  f = open("user.txt", "r")
  how =0
  for i in f:
    try:
      bot.copy_message(chat_id=i, from_chat_id=message.chat.id, message_id=message.message_id)
      how+=1
    except:
      continue
  bot.reply_to(message, f'تمت بنجاح.\nتم الارسال لـ{how} كواد .')
  pass

@bot.message_handler(regexp='حظر')
def f(message):
  if message.from_user.id == 6338388702 or message.from_user.id == 5543149965:
    id = message.text.replace('حظر ', '')
    open('ban.txt', 'a').write(f'\n{id}')
    bot.reply_to(message, f'تم حظر {id} بنجاح')
  else:
    bot.reply_to(message, 'انت لست المطور')


@bot.message_handler(func=lambda m: True)
def h(message):
  kl = ch(message.from_user.id)
  if kl == None:
      b = open('ban.txt').read()

      if str(message.from_user.id) in b:
        bot.reply_to(message, 'تم حظرك من البوت راسل المطور لفكه @itsnathaile')
      else:

        bot.reply_to(message, 'تم نقل البوت الى هنا @Tiktokinfor_bot')
        user = message.text
        h = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
        rt = requests.get(f"https://www.tiktok.com/@{user}", headers=h)
        server_log = str(rt.text)
        def reg():
           try:
            soup = BeautifulSoup(server_log, 'html.parser')
            script = soup.find(id='SIGI_STATE').contents
            
            data = str(script).split('},"UserModule":{"users":')[1]
            huks=(data.replace("']",""))
            hh = data.split('"followingCount":')[1].split(',')[0]
            time = data.split('"nickNameModifyTime":')[1].split(',')[0]
            cd = datetime.fromtimestamp(int(time))
            r=(huks.split('"region":"')[1].split('"')[0])
            se =data.split(',"nickname":"')[1].split('",')[0]
            id = data.split('"id":"')[1].split('",')[0]
            fs = data.split('"followerCount":')[1].split(',')[0]
            return f'{r};{cd};{hh};{fs};{se};{id}'
           except Exception as e:
            print(e)
            return ("nothing")
        h=reg()
        if h=='nothing':pass
         #bot.reply_to(message,'-توجد مشاكل في البحث .')
        else:
         fg=h.split(';')[2]
         co =h.split(';')[0]
         cd =h.split(';')[1]
         c = huksflag(co)
         fs = h.split(';')[3]
         name =h.split(';')[4]
         id = h.split(';')[5]
         date = tiktok_timestamp(id)
         #bot.send_message(message.chat.id,        
  else:bot.reply_to(message,f'''🚸| عذرا عزيزي
    🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
    
- https://t.me/{kl}

    ‼️| اشترك ثم ارسل /start''')

bot.infinity_polling()
