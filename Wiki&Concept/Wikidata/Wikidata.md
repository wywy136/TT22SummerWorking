# Wikidata

## Resources

Tools for Wikidata

- qwikidata: https://qwikidata.readthedocs.io/en/stable/index.html
- Wikidata: https://wikidata.readthedocs.io/en/stable/

## Structure

Each item is represented by a unique ID, starts from Q, e.g., Q2

Item could be linked to other items

- Comparing items ...
  - [said to be the same as (P460)](https://www.wikidata.org/wiki/Property:P460)
  - [different from (P1889)](https://www.wikidata.org/wiki/Property:P1889) - (different from, but sometimes confused with ...)
- Item is part of ...
  - [part of (P361)](https://www.wikidata.org/wiki/Property:P361) - (section of .../ contained within .../ pieces of ...)
  - [instance of (P31)](https://www.wikidata.org/wiki/Property:P31) - (is an example of ...)
  - [subclass of (P279)](https://www.wikidata.org/wiki/Property:P279) - (is a subset of ...)
  - [facet of (P1269)](https://www.wikidata.org/wiki/Property:P1269) - (aspect of .../ subitem of .../ a broader perspective on the same topic is offered by ...)
  - [has quality (P1552)](https://www.wikidata.org/wiki/Property:P1552) - (has characteristic .../ defining feature .../ inherent property ...)
- Item contains ...
  - [has part or parts (P527)](https://www.wikidata.org/wiki/Property:P527) - (contains ...)
  - [has part(s) of the class (P2670)](https://www.wikidata.org/wiki/Property:P2670) (has parts that are instances of .../ some parts form subclass of ...)
- Lots of other properties, in "Statements" section of each entity pages, could be get as follows:

To get statements from an entity

```python
Q = "Q2"
q_dict = get_entity_dict_from_api(Q)
q = WikidataItem(q_dict)
claim_groups = q.get_truthy_claim_groups()
# P31: instance of
p31_claim_groups = claims["P31"]
ist_id = p31_claim_groups[0].mainsnak.datavalue.value['id']
```