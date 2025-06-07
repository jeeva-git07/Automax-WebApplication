def user_listing_path(instance,filename):
    return "user_{0}/filters/{1}".format(instance.seller.user.id,filename)