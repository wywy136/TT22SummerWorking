# ConceptNet

## Resources

Build and run conceptnet locally: https://pypi.org/project/ConceptNet/#description

ConceptNet info: https://github.com/commonsense/conceptnet5/wiki

## Access

Use `requests` libraries to access ConceptNet.

```python
>>> import requests
>>> obj = requests.get('http://api.conceptnet.io/c/en/example').json()
>>> obj.keys()
dict_keys(['view', '@context', '@id', 'edges'])
```

## Structure

The nodes of ConceptNet are words and phrases of natural language. Each node has a URI within ConceptNet that starts with `/c/` and a language code, such as `/c/en/example`.

Overview

```json
{
  "@context": [
    "http://api.conceptnet.io/ld/conceptnet5.7/context.ld.json"
  ],
  "@id": "/c/en/example",
  "edges": [...],
  "view": {
    "@id": "/c/en/example?offset=0&limit=20",
    "firstPage": "/c/en/example?offset=0&limit=20",
    "nextPage": "/c/en/example?offset=20&limit=20",
    "paginatedProperty": "edges"
  }
}
```

Edge

```json
{
  "@id": "/a/[/r/UsedFor/,/c/en/example/,/c/en/explain/]",
  "dataset": "/d/conceptnet/4/en",
  "end": {
    "@id": "/c/en/explain",
    "label": "explain something",
    "language": "en",
    "term": "/c/en/explain"
  },
  "license": "cc:by-sa/4.0",
  "rel": {
    "@id": "/r/UsedFor",
    "label": "UsedFor"
  },
  "sources": [
    {
      "@id": "/and/[/s/activity/omcs/omcs1_possibly_free_text/,/s/contributor/omcs/pavlos/]",
      "activity": "/s/activity/omcs/omcs1_possibly_free_text",
      "contributor": "/s/contributor/omcs/pavlos"
    }
  ],
  "start": {
    "@id": "/c/en/example",
    "label": "an example",
    "language": "en",
    "term": "/c/en/example"
  },
  "surfaceText": "You can use [[an example]] to [[explain something]]",
  "weight": 1.0,
  "@context": [
    "http://api.conceptnet.io/ld/conceptnet5.5/context.ld.json",
    "http://api.conceptnet.io/ld/conceptnet5.5/pagination.ld.json"
  ]
}
```

