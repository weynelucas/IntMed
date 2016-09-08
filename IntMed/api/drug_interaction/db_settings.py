DB_SETTINGS = {
    'HOST': 'bolt://localhost/browser/',
    'USER': 'neo4j',
    'PASSWORD': 'password',
}

NODE_LABELS = ["DRUG"]
RELATIONSHIP_TYPES = ["MILD_INTERACTION", "MODERATE_INTERACTION", "NOTHING_EXPECTED", "SEVERE_INTERACTION", "UNKNOWN_SEVERITY_INTERACTION"]
PROPERTY_KEYS = {
    'NODE': ["name", "drugAction"],
    'RELATIONSHIP': ["evidence", "action", "explanation"]
}
