from telethon import TelegramClient,events,Button,types,functions,sync,functions,types
from flask import Flask 
from flask import Flask, request
import asyncio,json
api_id = 15278307
api_hash = "e2cb1c09f6899dcf30f7cac503495d90"
app = Flask(__name__)

@app.route("/",methods=['GET'])
def ids():
    new = int(request.args.get('new'))
    user = str(request.args.get('user'))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient(f'session_name', api_id, api_hash)
    client.start()
    async def main(new,user):
      if int(new) == 0:
          result = await client(functions.stories.GetPeerStoriesRequest(peer=user))
          user_id= ((str(result).split("(peer=PeerUser(user_id=")[1]).split("),")[0])
          if result.stories.stories == []:
              return {"Total":"stories not found"}
          else:
              i = 0
              r = []
              for story in result.stories.stories:
                  if story:
                      if hasattr(story.media, 'document'):
                          media = "video"
                          id_file = story.media.document.id 
                          story_id = story.id
                          ext = story.media.document.mime_type.split('/')[1]
                          filename = f"stories/{user_id}_{story_id}.{ext}"
                          if filename:pass
                          else:downloaded = await client.download_media(story.media.document, file=filename)
                      elif hasattr(story.media, 'photo'):
                          media = "photo"
                          story_id = story.id
                          id_file = story.media.photo.id
                          filename = f"stories/{user_id}_{story_id}.jpg"
                          if filename:pass
                          else:downloaded = await client.download_media(story.media.document, file=filename)
                      id_story = story.id
                      date = story.date
                      i+=1
                      re = {
                      "media": media,
                      "id_story": id_story,
                      "filename": filename,
                      "date": date
                      }
                      r.append(re)
              ve = {
              "Total": str(i),
              "User": str(user),
              "stories": r
              }
              return ve
      elif int(new) == 1:
          limit = int(request.args.get('limit'))
          result = await client(functions.stories.GetPinnedStoriesRequest(
          peer=user,
          offset_id=limit,
          limit=limit))
          if result.stories == []:
              return {"Total":"stories not found"}
          else:
              i = 0
              r = []
              for story in result.stories:
                  if story:
                      if hasattr(story.media, 'document'):
                          media = "video"
                          id_file = story.media.document.id 
                          story_id = story.id
                          print(result)
                          ext = story.media.document.mime_type.split('/')[1]
                          filename = f"stories/{user_id}_{story_id}.{ext}"
                          if filename:pass
                          else:downloaded = await client.download_media(story.media.document, file=filename)
                      elif hasattr(story.media, 'photo'):
                          media = "photo"
                          story_id = story.id
                           
                          id_file = story.media.photo.id
                          filename = f"stories/{user_id}_{story_id}.jpg"
                          if filename:pass
                          else:downloaded = await client.download_media(story.media.document, file=filename)
                      id_story = story.id
                      date = story.date
                      i+=1
                      re = {
                      "media": media,
                      "id_story": id_story,
                      "id_file": id_file,
                      "date": date
                      }
                      r.append(re)
              ve = {
              "Total": str(i),
              "User": str(user),
              "stories": r
              }
              return ve
    with client:
      result = client.loop.run_until_complete(main(new,user))
      return result
      
app.run(host='0.0.0.0', port=8080)