from woocommerce import API
import traceback

wcapi = API(
    url="https://staging3.trexnex.com",

    consumer_key="ck_b3ecde7ddff3bc6c12b72de465c97f18d0618bda",
    consumer_secret="cs_0da51cba71ebc7c805dc053bc67fab27144e1156",
    version="wc/v3",
    timeout=60
)
exportedFile = open("exported.csv", 'r').read().splitlines()
categoryFile = open("livecat.txt", 'r').read().splitlines()

nestedDict={}
for val in categoryFile:
    try:
        categoryId = val.split(",")[0]
        slug = val.split(",")[1]
        if slug in nestedDict:
            cats=nestedDict[slug]
            a_dictionary = {"id": categoryId}
            cats.append(a_dictionary)
            nestedDict[slug]=cats
        else:
            cats=[]
            a_dictionary = {"id": categoryId}
            cats.append(a_dictionary)
            nestedDict[slug]=cats
        
    except:
        traceback.print_exc()



exportedDic = {}
for val in exportedFile:
    productId = val.split(",")[0]
    slug = val.split(",")[1]
    exportedDic[slug] = productId
##
for slug, categoryId in nestedDict.items():
##    print("slug: "+slug, "category:"+str(categoryId))
    try:
        productId = exportedDic[slug]
        data = {
            "categories": nestedDict[slug]
            

        }
        print(str(data)+" id:"+productId+"\n\n\n")
        print(wcapi.put("products/" + productId, data).json())

    except:
        traceback.print_exc()

