# Primary storage keyed by a unique ID
npcs = {
    1: {"name": "Alice", "area": "town"},
    2: {"name": "Bob", "area": "town"},
    3: {"name": "Guard", "area": "castle"}
}

# Secondary index for areas:
from collections import defaultdict
npcs_by_area = defaultdict(list)
for npc_id, npc_obj in npcs.items():
    npcs_by_area[npc_obj["area"]].append(npc_obj)

print("\nnpcs")
print(npcs)
print("\nnpcs_by_area")
print(npcs_by_area)
print("\n npc_obj")
print(npc_obj)