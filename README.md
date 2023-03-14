# django-channels-tutorial   
Basic setup of how to use Django channels to build a chat box application.

https://www.honeybadger.io/blog/django-channels-websockets-chat/


#   comunication from server to client

- group_name=chatbot

- channel_name = chatbot

```python
from channels.layers import get_channel_layer
channel_layer = get_channel_layer()

def function(){
    async_to_sync(channel_layer.group_send)(
        'chatbox',
        {
            'type': 'chatbox_message',
            'message': 'message to send'

        }
    )
  }  
```
With default Backend

```python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': "channels.layers.InMemoryChannelLayer"
        }
    }
```

With Celery task and Redis Backend

```python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("127.0.0.1", 6379)],
            },
        }
    }
    
```


