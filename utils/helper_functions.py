def get_entity_name(entity):
    entity = str(entity)

    # Ontology classes
    if "#" in entity:
        return entity.split("#")[-1]

    # AIFB entities
    if "view" in entity:
        parts = entity.rstrip("/").split("/")
        return f"{parts[-3]}({parts[-1]})"

    # Keep external URLs unchanged
    return entity


def get_predicate_name(predicate):
    predicate = str(predicate)

    # Standard RDF/OWL/SWRC predicates
    if "#" in predicate:
        return predicate.split("#")[-1]

    # Leave uncommon predicates unchanged
    return predicate


def print_triple(subject, predicate, obj):
    """
    Print one RDF triple in a human-readable format.
    """

    print(f"Subject   : {get_entity_name(subject)}")
    print(f"Predicate : {get_predicate_name(predicate)}")

    if str(obj).startswith("http"):
        print(f"Object    : {get_entity_name(obj)}")
    else:
        print(f"Object    : {obj}")

    print("-" * 80)