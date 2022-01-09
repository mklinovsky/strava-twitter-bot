import requests
import datetime
import store
import math

stored_access_data = store.get_access_data()
strava_settings = store.get_strava_settings()

def refresh_access_token():
    global stored_access_data

    params = {
        'client_id': strava_settings['client_id'], 
        'client_secret': strava_settings['client_secret'], 
        'grant_type': 'refresh_token', 
        'refresh_token': stored_access_data['refresh_token']
    }
    access_data = requests.post(strava_settings['api_url'] + 'oauth/token', params=params).json()
    stored_access_data = access_data
    store.save_access_data(access_data)

def has_access():
    expires_at = stored_access_data['expires_at']
    date = datetime.datetime.fromtimestamp(expires_at)
    now = datetime.datetime.today()
    
    return date > now

def check_access():
    if (not has_access()):
        refresh_access_token()

def get(url):
    check_access()

    access_token = stored_access_data['access_token']
    headers={'Authorization': f'Bearer {access_token}'}

    return requests.get(strava_settings['api_url'] + url, headers=headers).json()

def get_stats():
    athlete_id = strava_settings['athlete_id']
    return get(f'athletes/{athlete_id}/stats')

def get_stats_text(stats):
    time = get_time(stats['elapsed_time'])

    distance = f"🏃 {round(stats['distance'] / 1000, 2)} km\n"
    elevation = f"⛰ {math.floor(stats['elevation_gain'])} m\n"
    elapsed = f"🕒 {time}\n"
    count = f"🖐 {stats['count']} runs"

    return f'{distance}{elevation}{elapsed}{count}'

def get_avg_week_distance(stats):
    distance = round(stats['distance'] / 1000 / 4, 2)
    return f'🏃 {distance} km'

def get_time(minutes):
    if (minutes < 60):
        return f'{minutes}m'

    if (minutes == 60):
        return '1h'

    h = minutes // 60
    m = minutes % 60
    return f'{h}h {m}m'

def get_stats_message():
    stats = get_stats()
    recent_stats = stats['recent_run_totals']
    
    recent_stats_text = get_stats_text(recent_stats)
    ytd_stats_text = get_stats_text(stats['ytd_run_totals'])
    avg_week_distance = get_avg_week_distance(recent_stats)

    return f'Avg week:\n{avg_week_distance}\n\nLast 4 weeks:\n{recent_stats_text}\n\nThis year:\n{ytd_stats_text}'
