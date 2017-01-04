# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:12:40 2016

@author: Mads
"""

# This is a script that gets twitter posts from a list of users

import twitter


from twitter.twitter_utils import enf_type
from twitter import Status
#import io, json
import codecs

    
api = twitter.Api(consumer_key='1rlrE1gW9e9o6pee7GT6agG6E',
                      consumer_secret='HPntWOwsDYnCtZFqp1CymOohrJrJvKWHZMl34iWASGJM37Dg6q',
                      access_token_key='801488457663184896-WIA3vErvaAXLbQzYZ4iXfwP7zZQZa6u',
                      access_token_secret='oN81rr5qkEfFcmHivpFW9e7d8wtSOGHhtVBv5medO1OXf')
               

def GetUserTimeline(self, user_id, screen_name, count, since_id, max_id , include_rts, trim_user, exclude_replies):
        
        url = '%s/statuses/user_timeline.json' % (self.base_url)
        parameters = {}

        if user_id:
            parameters['user_id'] = enf_type('user_id', int, user_id)
        elif screen_name:
            parameters['screen_name'] = screen_name
        if since_id:
            parameters['since_id'] = enf_type('since_id', int, since_id)
        if max_id:
            parameters['max_id'] = enf_type('max_id', int, max_id)
        if count:
            parameters['count'] = enf_type('count', int, count)

        parameters['include_rts'] = enf_type('include_rts', bool, include_rts)
        parameters['trim_user'] = enf_type('trim_user', bool, trim_user)
        parameters['exclude_replies'] = enf_type('exclude_replies', bool, exclude_replies)

        resp = self._RequestUrl(url, 'GET', data=parameters)
        data = self._ParseAndCheckTwitter(resp.content.decode('utf-8'))

        return [Status.NewFromJsonDict(x) for x in data]
           
output = GetUserTimeline(api,
                        user_id=1704527995,
                        screen_name='Alternativet',
                        count = 50,
                        since_id = None,
                        max_id= 611642862283919360,
                        include_rts = True,
                        trim_user = True,
                        exclude_replies = True)


with codecs.open("alt_twitterfile.csv", "w", "utf-8" ) as f:
    for o in output:
        f.write(o.text + "\n")