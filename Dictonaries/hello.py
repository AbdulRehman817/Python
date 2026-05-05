chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"};
# print(chai_types["Masala"])
# print(chai_types.get("Masala"))
# chai_types["Green"]="Fresh"
# print(chai_types)

# for chai in chai_types:
#     print(chai,chai_types[chai])
# THEY BOTH DO THE SAME THING 
# for key,values in chai_types.items():
#     print(key,values)
# del chai_types["Ginger"];
# print(chai_types)


tea_shop={
    "chai":{"Masala":"Spicy","Ginger":"Zesty"},
    "Tea":{"Green":"Mild","Black":"Strong"}
}
# print(tea_shop)
print(tea_shop["chai"])