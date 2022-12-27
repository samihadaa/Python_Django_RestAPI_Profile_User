# Python_Django_RestAPI_Profile_User
#Developping my first Profile RestAPI in order to handle the registration of new users in the system : Validating data, Listing existing profiles so users can find other users, also you can view, update your own profile(permissions)
#At first i created a virtual environment in order to isolate my project from other python environements in the system
#Then i created my own project which is "profiles" and the application profiles_api with the commands startapp and startproject from manage.py
#I create my custom "UserProfileModel" to overwrite the django default user model. For that i imported the "AbstractBaseUser" and "BaseUserManager" then maked USERNAME_FIELD = 'email'.
#In the settings.py i configured my new user model : AUTH_USER_MODEL = 'profiles_api.UserProfile'
#I create migrations files to match my models with the Database : he commandes "Makemigrations" and "Migrate"
#Finally i created my "superuser" account with the command "createsuperuser"
#Creation of my API for managing profiles :
#At first i created my serializer "UserProfileSerializer" with the fields : "id","email","name","password",
#iI used the create function to add a new user account
#I create my model Viewset "UserProfileViewSet" using the serializer and the queryset
#Adding the router for the "UserProfileViewSet"
#After testing the "creating profile" function, i added the permissions.py file to restrict access for authenticated users using the class "BasePermission" 
# Adding authentification and permissions to the "UserProfileViewSet" using the class "TokenAuthentication"
#I added the fonctionnality filter to my "UserProfileViewSet" from the rest_framework module "filters": searching by 'name' and 'email'
#After i finished the "UserProfileViewSet", i created the "feed_API" with the new model "ProfileFeedItem" then the serializer "ProfileFeedItemSerializer" then "UserProfileFeedViewSet"
