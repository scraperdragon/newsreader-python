import json
import requests

def getter(path_fragment, page=1, **kwargs):
    kwargs['output'] = 'json'
    json_args = {arg: json.dumps(kwargs[arg]) for arg in kwargs}
    print json_args
    r = requests.get ("https://newsreader.scraperwiki.com/{}/page/{}".format(path_fragment, page), params = json_args)
    try:
        return r.json()
    except Exception:
        print r.url, r
        print r.content
        raise

def nice_get(*args, **kwargs):
    x = getter(*args, **kwargs)
    print json.dumps(x, indent=2)

print nice_get("SynerscopeQuery", uris=['<http://dbpedia.org/resource/David_Beckham>'])
print nice_get("EntitiesThatAreActorsQuery", page=2)
#print nice_get("GetEventDetailsByActorUri", uris=['<http://dbpedia.org/resource/David_Beckham>'])

