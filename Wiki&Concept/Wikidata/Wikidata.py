from qwikidata.entity import WikidataItem, WikidataLexeme, WikidataProperty
from qwikidata.linked_data_interface import get_entity_dict_from_api
# from qwikidata.sparql import

# create an item
Q = "Q2"
q_dict = get_entity_dict_from_api(Q)
q = WikidataItem(q_dict)

# Get claims
claims = q.get_truthy_claim_groups()
p31_claim_groups = claims["P31"]
# Print the first item in the p31 group
print(p31_claim_groups[0].mainsnak.datavalue.value['id'])
