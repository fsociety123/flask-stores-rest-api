from werkzeug.security import safe_str_cmp
from models.user_model import UserModel

'''#Creating user objects
users= [User(1, "xyz", 'doYourThing')]

#Creating a dictionary which maps each user to it's object
username_mapping= {u.username: u for u in users}

#Creating a dictionary which maps each userid to it's object
userid_mapping= {u.id: u for u in users}'''

#Authenticate based on username and password
def authenticate(username, password):

    #Get the object for the username
    user= UserModel.get_user_username(username)
    
    #If the username and the password of that user are valid 
    if user and safe_str_cmp(user.password, password):
        return user

    return None

def identity(payload):

    #Get the user object based on the id
    user_id= payload["identity"]

    '''#Return the user object if the userid exists else None
    return userid_mapping.get(user_id, None)'''

    user= UserModel.get_user_id(user_id)

    return user

