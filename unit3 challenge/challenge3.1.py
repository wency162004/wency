def lineraSearchProduct(productList, targetproduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetproduct:
      indices.append(index)
  return indices

products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
result = lineraSearchProduct(products, target)
print(result)