RELATIONSHIP_RETURN_ALIAS =  "RETURN DISTINCT type(r) as type, r.evidence as evidence, r.action as action, r.explanation as explanation, startNode(r).name as startNode, endNode(r).name as endNode"
OTHER_APPEND = ", n.name as other"

ALL_DRUGS = "MATCH (d:DRUG) RETURN d.name as name, d.drugAction as action"
INTERACTIONS_PER_DRUG = "MATCH (:DRUG {name:{name}})-[r]-(n:DRUG) " + RELATIONSHIP_RETURN_ALIAS + OTHER_APPEND
MULTIPLE_DRUGS_INTERACTIONS = "MATCH (d:DRUG) WHERE d.name IN {names} WITH COLLECT(d) as ds MATCH (x)-[r]-(y) WHERE x in ds AND y in ds " + RELATIONSHIP_RETURN_ALIAS
