from config import *

from decouple import config

import datetime
import pytz

app: FastAPI = Config().app


@app.post('/time')
def get_time(request: Request, area: GlobalArea):
    if not request.headers.get('AuthDistaste') == config('AUTH_PASSWORD', cast=str):
        return {
            'success': False,
            'body': 'Invalid auth password'
        }

    u: datetime.datetime = datetime.datetime.utcnow()
    u = u.replace(tzinfo=pytz.utc)

    try:
        info: datetime.datetime = u.astimezone(pytz.timezone(area.region))

        return {
            'success': True,
            'body': {
                'hora': info.hour,
                'minuto': info.minute,
                'segundo': info.second,
                'dia': info.day,
                'mês': info.month,
                'ano': info.year
            }
        }

    except Exception as e:
        return {
            'success': False,
            'body': f'Invalid input: {e}'
        }
