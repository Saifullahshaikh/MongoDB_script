import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Create or access a database
mydb = client["mydatabase"]

# Create a collection
user_profiles = mydb["user_profiles"]
# Define a user profile
user_profile_1 = {
    "username": "saif",
    "email": "saif@example.com",
    "date_of_birth": "2000-01-01",
    "interests": ["coding", "reading", "music"]
}
user_profile_2 = {
    "username": "john",
    "email": "john@example.com",
    "date_of_birth": "1990-01-01",
    "interests": ["cooking", "reading", "music"]
}
user_profile_3 = {
    "username": "mike",
    "email": "mike@example.com",
    "date_of_birth": "2005-01-01",
    "interests": ["traveling", "reading", "sports"]
}

# Insert the user profile into the collection
user_profiles.insert_one(user_profile_1)
user_profiles.insert_one(user_profile_2)
user_profiles.insert_one(user_profile_3)

def get_user_profiles_by_interest(interest):
    # Query MongoDB to find user profiles with the given interest
    query = {"interests": interest}
    result = user_profiles.find(query)
    
    # Return the matched user profiles
    return list(result)

# Example usage
interest = "reading"
matched_profiles = get_user_profiles_by_interest(interest)
for profile in matched_profiles:
    print(profile)
