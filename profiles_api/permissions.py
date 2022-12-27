from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit his own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: 
            return True
        else:
            return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update his own status"""
    def has_object_permission(self, request, view, obj):
        """Check the User is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS: 
            return True
        else:
            return obj.user_profile.id == request.user.id