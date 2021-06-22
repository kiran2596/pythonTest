import requests
import json

def display_post(post,comments):
    list2 =[]
    for i in range(3):
        mydic={}
        mydic['id']= post[i]['id']
        mydic['title']= post[i]['title']
        list1 = []
        cmt = ""
        
        for j in range(2):
            cmt=comments[j]['body']
            list1.append(cmt)  
            if post[i]['id']==comments[j]['postId']:
                mydic['comment']=list1 
            else :
                mydic['comment']=""   
        list2.append(mydic)

    jsondata = json.dumps(list2, indent = 4)
    return jsondata    
        
api_post= 'https://my-json-server.typicode.com/typicode/demo/posts'
api_comment =  'https://my-json-server.typicode.com/typicode/demo/comments'

responce_post = requests.get(api_post)
responce_comments = requests.get(api_comment)

post = json.dumps(responce_post.json())
comment = json.dumps(responce_comments.json())

postdata= json.loads(post)
commentdata=json.loads(comment)
print(display_post(postdata,commentdata))
